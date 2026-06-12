"""Generated from Smithy shape ``com.amazonaws.guardduty#IpSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "DEACTIVATING",
        "ERROR",
        "DELETE_PENDING",
        "DELETED",
    )
)


def serialize_json(value: IpSetStatus) -> str:
    return value


def deserialize_json(data: str) -> IpSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpSetStatus value: {data!r}")
    return cast(IpSetStatus, data)
