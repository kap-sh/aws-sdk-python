"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#TargetStore``."""

from typing import Literal, TypeAlias, cast

TargetStore: TypeAlias = Literal[
    "OnlineStore",
    "OfflineStore",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStore) -> str:
    return value


def deserialize_json(data: str) -> TargetStore:
    return cast(TargetStore, data)
