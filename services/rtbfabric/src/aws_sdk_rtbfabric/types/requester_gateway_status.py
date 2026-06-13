"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RequesterGatewayStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

RequesterGatewayStatus: TypeAlias = Literal[
    "PENDING_CREATION",
    "ACTIVE",
    "PENDING_DELETION",
    "DELETED",
    "ERROR",
    "PENDING_UPDATE",
    "ISOLATED",
    "PENDING_ISOLATION",
    "PENDING_RESTORATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_CREATION",
        "ACTIVE",
        "PENDING_DELETION",
        "DELETED",
        "ERROR",
        "PENDING_UPDATE",
        "ISOLATED",
        "PENDING_ISOLATION",
        "PENDING_RESTORATION",
    )
)


def serialize_json(value: RequesterGatewayStatus) -> str:
    return value


def deserialize_json(data: str) -> RequesterGatewayStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequesterGatewayStatus value: {data!r}")
    return cast(RequesterGatewayStatus, data)
