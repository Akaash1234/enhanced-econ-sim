import asyncio
from core.market import MarketSystem

class Simulation:
    def __init__(self, config):
        self.cfg = config
        self.mkt = MarketSystem()
        self.agents = []

    async def run_simulation(self, steps=100):
        print("sim starting...")
        data = {}
        for i in range(steps):
            await asyncio.sleep(0.01) 
            self.mkt.update()
        return {"profit": 1000000}
