"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestType``."""

from typing import Literal, TypeAlias, cast

TestType: TypeAlias = Literal[
    "Software",
    "Hardware",
    "AZ",
    "Region",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestType) -> str:
    return value


def deserialize_json(data: str) -> TestType:
    return cast(TestType, data)
