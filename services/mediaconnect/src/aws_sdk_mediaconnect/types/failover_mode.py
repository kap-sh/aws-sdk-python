"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverMode``."""

from typing import Literal, TypeAlias, cast

FailoverMode: TypeAlias = Literal[
    "MERGE",
    "FAILOVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailoverMode) -> str:
    return value


def deserialize_json(data: str) -> FailoverMode:
    return cast(FailoverMode, data)
