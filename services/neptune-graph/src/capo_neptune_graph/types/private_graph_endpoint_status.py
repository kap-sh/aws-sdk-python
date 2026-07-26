"""Generated from Smithy shape ``com.amazonaws.neptunegraph#PrivateGraphEndpointStatus``."""

from typing import Literal, TypeAlias, cast

PrivateGraphEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateGraphEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateGraphEndpointStatus:
    return cast(PrivateGraphEndpointStatus, data)
