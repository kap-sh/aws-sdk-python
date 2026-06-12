"""Generated from Smithy shape ``com.amazonaws.opensearch#InboundConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

InboundConnectionStatusCode: TypeAlias = Literal[
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


def serialize_json(value: InboundConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> InboundConnectionStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InboundConnectionStatusCode value: {data!r}"
        )
    return cast(InboundConnectionStatusCode, data)
