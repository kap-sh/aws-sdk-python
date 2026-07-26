"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseScenarioType``."""

from typing import Literal, TypeAlias, cast

TestCaseScenarioType: TypeAlias = Literal[
    "Advanced",
    "Basic",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseScenarioType) -> str:
    return value


def deserialize_json(data: str) -> TestCaseScenarioType:
    return cast(TestCaseScenarioType, data)
