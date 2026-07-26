"""Generated from Smithy shape ``com.amazonaws.finspace#KxNodeStatus``."""

from typing import Literal, TypeAlias, cast

KxNodeStatus: TypeAlias = Literal[
    "RUNNING",
    "PROVISIONING",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxNodeStatus) -> str:
    return value


def deserialize_json(data: str) -> KxNodeStatus:
    return cast(KxNodeStatus, data)
