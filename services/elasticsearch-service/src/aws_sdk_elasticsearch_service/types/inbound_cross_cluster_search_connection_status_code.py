"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#InboundCrossClusterSearchConnectionStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

InboundCrossClusterSearchConnectionStatusCode: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "APPROVED",
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
        "REJECTING",
        "REJECTED",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: InboundCrossClusterSearchConnectionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> InboundCrossClusterSearchConnectionStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InboundCrossClusterSearchConnectionStatusCode value: {data!r}"
        )
    return cast(InboundCrossClusterSearchConnectionStatusCode, data)
