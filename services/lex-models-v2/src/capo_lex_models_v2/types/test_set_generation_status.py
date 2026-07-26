"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetGenerationStatus``."""

from typing import Literal, TypeAlias, cast

TestSetGenerationStatus: TypeAlias = Literal[
    "Generating",
    "Ready",
    "Failed",
    "Pending",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> TestSetGenerationStatus:
    return cast(TestSetGenerationStatus, data)
