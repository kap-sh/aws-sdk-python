"""Generated from Smithy shape ``com.amazonaws.quicksight#MemberType``."""

from typing import Literal, TypeAlias, cast

MemberType: TypeAlias = Literal[
    "DASHBOARD",
    "ANALYSIS",
    "DATASET",
    "DATASOURCE",
    "TOPIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: MemberType) -> str:
    return value


def deserialize_json(data: str) -> MemberType:
    return cast(MemberType, data)
