"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store

EventDataStores: TypeAlias = list[
    "aws_sdk_cloudtrail.types.event_data_store.EventDataStore"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDataStores) -> list:
    import aws_sdk_cloudtrail.types.event_data_store

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.event_data_store.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventDataStores:
    import aws_sdk_cloudtrail.types.event_data_store

    out: EventDataStores = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.event_data_store.deserialize_aws_json_1_1(item)
        )
    return out
