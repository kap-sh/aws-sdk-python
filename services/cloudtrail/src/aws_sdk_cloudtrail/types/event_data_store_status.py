"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStoreStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

EventDataStoreStatus: TypeAlias = Literal[
    "CREATED",
    "ENABLED",
    "PENDING_DELETION",
    "STARTING_INGESTION",
    "STOPPING_INGESTION",
    "STOPPED_INGESTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "ENABLED",
        "PENDING_DELETION",
        "STARTING_INGESTION",
        "STOPPING_INGESTION",
        "STOPPED_INGESTION",
    )
)


def serialize_aws_json_1_1(value: EventDataStoreStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventDataStoreStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventDataStoreStatus value: {data!r}")
    return cast(EventDataStoreStatus, data)
