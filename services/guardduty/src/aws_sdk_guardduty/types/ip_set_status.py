"""Generated from Smithy shape ``com.amazonaws.guardduty#IpSetStatus``."""

from typing import Literal, TypeAlias, cast

IpSetStatus: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVATING",
    "ACTIVE",
    "DEACTIVATING",
    "ERROR",
    "DELETE_PENDING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpSetStatus) -> str:
    return value


def deserialize_json(data: str) -> IpSetStatus:
    return cast(IpSetStatus, data)
