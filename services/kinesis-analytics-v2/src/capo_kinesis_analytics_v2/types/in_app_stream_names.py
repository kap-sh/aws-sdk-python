"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InAppStreamNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.in_app_stream_name

InAppStreamNames: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.in_app_stream_name.InAppStreamName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InAppStreamNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InAppStreamNames:
    return list(data)
