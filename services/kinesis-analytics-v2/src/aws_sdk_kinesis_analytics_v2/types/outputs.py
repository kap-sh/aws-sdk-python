"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#Outputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.output

Outputs: TypeAlias = list["aws_sdk_kinesis_analytics_v2.types.output.Output"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Outputs) -> list:
    import aws_sdk_kinesis_analytics_v2.types.output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.output.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Outputs:
    import aws_sdk_kinesis_analytics_v2.types.output

    out: Outputs = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.output.deserialize_aws_json_1_1(item)
        )
    return out
