"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InAppStreamNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.in_app_stream_name

InAppStreamNames: TypeAlias = list[
    "aws_sdk_kinesis_analytics.types.in_app_stream_name.InAppStreamName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InAppStreamNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InAppStreamNames:
    return list(data)
