"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ResponderGatewayStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

ResponderGatewayStatus: TypeAlias = Literal[
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


def serialize_json(value: ResponderGatewayStatus) -> str:
    return value


def deserialize_json(data: str) -> ResponderGatewayStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponderGatewayStatus value: {data!r}")
    return cast(ResponderGatewayStatus, data)
