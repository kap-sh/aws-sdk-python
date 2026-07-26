"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetModality``."""

from typing import Literal, TypeAlias, cast

TestSetModality: TypeAlias = Literal[
    "Text",
    "Audio",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestSetModality) -> str:
    return value


def deserialize_json(data: str) -> TestSetModality:
    return cast(TestSetModality, data)
