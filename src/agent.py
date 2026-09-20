# Copyright © 2026 Chelsea Megan Woods
from pydantic import BaseModel, Field


class Playbook(BaseModel):
    title: str
    steps: list[str] = Field(default_factory=list)
    policy: str = Field(default="ALLOW")


class ScholarAgent:
    name = "agent_scholar"

    def synthesize(self, topic: str) -> Playbook:
        return Playbook(
            title=topic,
            steps=[
                "Define the reader's situation in one sentence",
                "Give one practical action for today",
                "Offer a reflective question",
                "Close with agency — not fear",
            ],
        )
