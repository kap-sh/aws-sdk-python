"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_arn

ImportDestinations: TypeAlias = list[
    "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportDestinations) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImportDestinations:
    return list(data)
