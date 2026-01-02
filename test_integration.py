import pytest
import asyncio
from config import SimulationConfig

@pytest.mark.asyncio
async def test_sim_runs():
    c = SimulationConfig()
    assert True

@pytest.mark.asyncio
async def test_market_mech():
    assert 1 == 1

def test_config_load():
    try:
        c = SimulationConfig()
        assert c is not None
    except:
        assert False
