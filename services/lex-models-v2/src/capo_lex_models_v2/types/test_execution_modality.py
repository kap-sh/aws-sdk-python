"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionModality``."""

from typing import Literal, TypeAlias, cast

TestExecutionModality: TypeAlias = Literal[
    "Text",
    "Audio",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionModality) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionModality:
    return cast(TestExecutionModality, data)
