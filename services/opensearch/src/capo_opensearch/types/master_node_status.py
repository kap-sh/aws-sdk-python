"""Generated from Smithy shape ``com.amazonaws.opensearch#MasterNodeStatus``."""

from typing import Literal, TypeAlias, cast

MasterNodeStatus: TypeAlias = Literal[
    "Available",
    "UnAvailable",
]


# --- restJson1 ser/de ---
def serialize_json(value: MasterNodeStatus) -> str:
    return value


def deserialize_json(data: str) -> MasterNodeStatus:
    return cast(MasterNodeStatus, data)
