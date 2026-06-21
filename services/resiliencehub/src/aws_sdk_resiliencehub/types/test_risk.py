"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestRisk``."""

from typing import Literal, TypeAlias, cast

TestRisk: TypeAlias = Literal[
    "Small",
    "Medium",
    "High",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestRisk) -> str:
    return value


def deserialize_json(data: str) -> TestRisk:
    return cast(TestRisk, data)
