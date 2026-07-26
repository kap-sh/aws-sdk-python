"""Generated from Smithy shape ``com.amazonaws.quicksight#NetworkInterfaceStatus``."""

from typing import Literal, TypeAlias, cast

NetworkInterfaceStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATION_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
    "DELETION_FAILED",
    "DELETION_SCHEDULED",
    "ATTACHMENT_FAILED_ROLLBACK_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceStatus) -> str:
    return value


def deserialize_json(data: str) -> NetworkInterfaceStatus:
    return cast(NetworkInterfaceStatus, data)
