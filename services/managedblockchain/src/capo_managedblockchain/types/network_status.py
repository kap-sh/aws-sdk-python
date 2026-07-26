"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkStatus``."""

from typing import Literal, TypeAlias, cast

NetworkStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATE_FAILED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkStatus) -> str:
    return value


def deserialize_json(data: str) -> NetworkStatus:
    return cast(NetworkStatus, data)
