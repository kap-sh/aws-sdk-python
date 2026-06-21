"""Generated from Smithy shape ``com.amazonaws.ssmsap#AllocationType``."""

from typing import Literal, TypeAlias, cast

AllocationType: TypeAlias = Literal[
    "VPC_SUBNET",
    "ELASTIC_IP",
    "OVERLAY",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllocationType) -> str:
    return value


def deserialize_json(data: str) -> AllocationType:
    return cast(AllocationType, data)
