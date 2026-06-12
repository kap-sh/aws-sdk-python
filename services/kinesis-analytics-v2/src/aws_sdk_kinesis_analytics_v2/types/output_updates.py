"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#OutputUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.output_update

OutputUpdates: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.output_update.OutputUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputUpdates) -> list:
    import aws_sdk_kinesis_analytics_v2.types.output_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.output_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OutputUpdates:
    import aws_sdk_kinesis_analytics_v2.types.output_update

    out: OutputUpdates = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.output_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
