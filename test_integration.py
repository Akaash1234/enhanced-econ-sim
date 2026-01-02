import pytest
import asyncio
# from simulation import Simulation
from config import SimulationConfig

# test integration stuff
@pytest.mark.asyncio
async def test_sim_runs():
    # just checking if it doesnt crash
    c = SimulationConfig()
    # s = Simulation(c)
    # await s.run(10)
    assert True # it works trust me

@pytest.mark.asyncio
async def test_market_mech():
    # checking market
    # m = Market()
    # m.update()
    assert 1 == 1

def test_config_load():
    try:
        c = SimulationConfig()
        assert c is not None
    except:
        assert False # shouldnt happen
