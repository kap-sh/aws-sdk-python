"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterType``."""

from typing import Literal, TypeAlias, cast

KxClusterType: TypeAlias = Literal[
    "HDB",
    "RDB",
    "GATEWAY",
    "GP",
    "TICKERPLANT",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxClusterType) -> str:
    return value


def deserialize_json(data: str) -> KxClusterType:
    return cast(KxClusterType, data)
