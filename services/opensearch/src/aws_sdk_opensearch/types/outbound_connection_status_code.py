"""Generated from Smithy shape ``com.amazonaws.opensearch#OutboundConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

OutboundConnectionStatusCode: TypeAlias = Literal[
    "VALIDATING",
    "VALIDATION_FAILED",
    "PENDING_ACCEPTANCE",
    "APPROVED",
    "PROVISIONING",
    "ACTIVE",
    "REJECTING",
    "REJECTED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATING",
        "VALIDATION_FAILED",
        "PENDING_ACCEPTANCE",
        "APPROVED",
        "PROVISIONING",
        "ACTIVE",
        "REJECTING",
        "REJECTED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: OutboundConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> OutboundConnectionStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OutboundConnectionStatusCode value: {data!r}"
        )
    return cast(OutboundConnectionStatusCode, data)
