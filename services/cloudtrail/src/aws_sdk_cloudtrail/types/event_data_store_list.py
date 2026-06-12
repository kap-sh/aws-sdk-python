"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStoreList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn

EventDataStoreList: TypeAlias = list[
    "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDataStoreList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EventDataStoreList:
    return list(data)
