"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OutboundCrossClusterSearchConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

OutboundCrossClusterSearchConnectionStatusCode: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "VALIDATING",
    "VALIDATION_FAILED",
    "PROVISIONING",
    "ACTIVE",
    "REJECTED",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_ACCEPTANCE",
        "VALIDATING",
        "VALIDATION_FAILED",
        "PROVISIONING",
        "ACTIVE",
        "REJECTED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: OutboundCrossClusterSearchConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> OutboundCrossClusterSearchConnectionStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OutboundCrossClusterSearchConnectionStatusCode value: {data!r}"
        )
    return cast(OutboundCrossClusterSearchConnectionStatusCode, data)
