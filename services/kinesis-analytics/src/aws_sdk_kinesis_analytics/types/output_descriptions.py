"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#OutputDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.output_description

OutputDescriptions: TypeAlias = list[
    "aws_sdk_kinesis_analytics.types.output_description.OutputDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputDescriptions) -> list:
    import aws_sdk_kinesis_analytics.types.output_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics.types.output_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OutputDescriptions:
    import aws_sdk_kinesis_analytics.types.output_description

    out: OutputDescriptions = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics.types.output_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
