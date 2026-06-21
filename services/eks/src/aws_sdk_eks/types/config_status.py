"""Generated from Smithy shape ``com.amazonaws.eks#configStatus``."""

from typing import Literal, TypeAlias, cast

configStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: configStatus) -> str:
    return value


def deserialize_json(data: str) -> configStatus:
    return cast(configStatus, data)
