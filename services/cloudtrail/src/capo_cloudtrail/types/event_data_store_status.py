"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStoreStatus``."""

from typing import Literal, TypeAlias, cast

EventDataStoreStatus: TypeAlias = Literal[
    "CREATED",
    "ENABLED",
    "PENDING_DELETION",
    "STARTING_INGESTION",
    "STOPPING_INGESTION",
    "STOPPED_INGESTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDataStoreStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventDataStoreStatus:
    return cast(EventDataStoreStatus, data)
