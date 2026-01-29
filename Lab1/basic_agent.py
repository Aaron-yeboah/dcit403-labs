from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio


class HelloBehaviour(CyclicBehaviour):
    async def run(self):
        print(f"[{self.agent.jid}] Agent is running...")
        await asyncio.sleep(5)


class BasicAgent(Agent):
    async def setup(self):
        print(f"[{self.jid}] Agent started")
        self.add_behaviour(HelloBehaviour())


async def main():
    jid = "testagent@localhost"
    password = "password123"

    agent = BasicAgent(jid, password)
    await agent.start(auto_register=True)

    # keep agent alive
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
