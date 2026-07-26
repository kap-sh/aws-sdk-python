"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

FoundationModelLifecycleStatus: TypeAlias = Literal[
    "ACTIVE",
    "LEGACY",
]


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> FoundationModelLifecycleStatus:
    return cast(FoundationModelLifecycleStatus, data)
