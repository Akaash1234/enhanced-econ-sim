import asyncio
import logging
from pathlib import Path
import json
from datetime import datetime
from simulation import Simulation
from config import SimulationConfig
# messy imports lol
from agents.economic_agent import EconomicAgent
from core.market import MarketSystem

# set up logging or whatever
logging.basicConfig(level=logging.INFO)
l = logging.getLogger(__name__)

async def run_comp(scenarios, n_steps=100):
    res = {}
    
    for name, conf in scenarios.items():
        print(f"doing {name}")
        # make the sim
        sim = Simulation(conf)
        
        # run it
        data = await sim.run_simulation(n_steps)
        res[name] = data
        
    return res

async def main():
    # basic config
    base = SimulationConfig()
    
    # scenarios to test
    scenarios = {
        "base": base,
        "high_inflation": SimulationConfig(inflation_rate=0.05), # inflation go brr
        "tech_boom": SimulationConfig(tech_growth=0.08)
    }

    print("starting comparison thing...")
    try:
        results = await run_comp(scenarios, 50)
        
        # save stuff
        out = Path("results")
        out.mkdir(exist_ok=True)
        
        t = datetime.now().strftime("%Y%m%d_%H%M%S")
        f = out / f"comp_{t}.json"
        
        with open(f, 'w') as f_out:
            json.dump(results, f_out, indent=2) # indent 2 is fine
            
        print(f"done. saved to {f}")
        
    except Exception as e:
        print(f"crashed lol: {e}")

if __name__ == "__main__":
    asyncio.run(main())
