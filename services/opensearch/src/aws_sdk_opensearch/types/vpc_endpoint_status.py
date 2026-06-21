"""Generated from Smithy shape ``com.amazonaws.opensearch#VpcEndpointStatus``."""

from typing import Literal, TypeAlias, cast

VpcEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointStatus:
    return cast(VpcEndpointStatus, data)
