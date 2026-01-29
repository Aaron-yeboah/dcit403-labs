from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio
import random
from datetime import datetime


class SenseEnvironmentBehaviour(CyclicBehaviour):
    async def run(self):
        disaster_types = ["Flood", "Fire", "Earthquake"]
        severity_levels = ["Low", "Medium", "High"]

        disaster = random.choice(disaster_types)
        severity = random.choice(severity_levels)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        event = {
            "time": timestamp,
            "disaster": disaster,
            "severity": severity
        }

        log_message = (
            f"[{timestamp}] Detected {disaster} | Severity: {severity}"
        )

        print(log_message)

        # save event to log file
        with open("event_log.txt", "a") as log:
            log.write(log_message + "\n")

        await asyncio.sleep(6)


class SensorAgent(Agent):
    async def setup(self):
        print(f"[{self.jid}] SensorAgent started")
        self.add_behaviour(SenseEnvironmentBehaviour())


async def main():
    jid = "sensor@localhost"
    password = "password123"

    agent = SensorAgent(jid, password)
    await agent.start()

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())

