"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionApiMode``."""

from typing import Literal, TypeAlias, cast

TestExecutionApiMode: TypeAlias = Literal[
    "Streaming",
    "NonStreaming",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionApiMode) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionApiMode:
    return cast(TestExecutionApiMode, data)
