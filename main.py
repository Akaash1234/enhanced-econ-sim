import asyncio
from config import SimulationConfig
from simulation import Simulation

async def main():
    print("starting main...")
    c = SimulationConfig()
    s = Simulation(c)
    await s.run_simulation(10)
    print("done")

if __name__ == "__main__":
    asyncio.run(main())
