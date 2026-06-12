"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#Inputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.input

Inputs: TypeAlias = list["aws_sdk_kinesis_analytics.types.input.Input"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Inputs) -> list:
    import aws_sdk_kinesis_analytics.types.input

    out: list = []
    for item in value:
        out.append(aws_sdk_kinesis_analytics.types.input.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Inputs:
    import aws_sdk_kinesis_analytics.types.input

    out: Inputs = []
    for item in data:
        out.append(aws_sdk_kinesis_analytics.types.input.deserialize_aws_json_1_1(item))
    return out
