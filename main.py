from fastapi import FastAPI

from models import TokenTask, CfClearanceTask
from solvers.token_solver import solve_token
from solvers.cf_clearance_solver import solve_cf_clearance

app = FastAPI()


@app.post("/solve/token")
async def token_solver(task: TokenTask):
    return await solve_token(task)


@app.post("/solve/cf_clearance")
async def cf_solver(task: CfClearanceTask):
    return await solve_cf_clearance(task)
