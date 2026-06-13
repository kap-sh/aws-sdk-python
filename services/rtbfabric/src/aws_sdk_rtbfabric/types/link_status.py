"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

LinkStatus: TypeAlias = Literal[
    "PENDING_CREATION",
    "PENDING_REQUEST",
    "REQUESTED",
    "ACCEPTED",
    "ACTIVE",
    "REJECTED",
    "FAILED",
    "PENDING_DELETION",
    "DELETED",
    "PENDING_UPDATE",
    "PENDING_ISOLATION",
    "ISOLATED",
    "PENDING_RESTORATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_CREATION",
        "PENDING_REQUEST",
        "REQUESTED",
        "ACCEPTED",
        "ACTIVE",
        "REJECTED",
        "FAILED",
        "PENDING_DELETION",
        "DELETED",
        "PENDING_UPDATE",
        "PENDING_ISOLATION",
        "ISOLATED",
        "PENDING_RESTORATION",
    )
)


def serialize_json(value: LinkStatus) -> str:
    return value


def deserialize_json(data: str) -> LinkStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LinkStatus value: {data!r}")
    return cast(LinkStatus, data)
