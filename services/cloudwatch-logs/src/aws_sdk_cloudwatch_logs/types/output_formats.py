"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OutputFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.output_format

OutputFormats: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.output_format.OutputFormat"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputFormats) -> list:
    import aws_sdk_cloudwatch_logs.types.output_format

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.output_format.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OutputFormats:
    import aws_sdk_cloudwatch_logs.types.output_format

    out: OutputFormats = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.output_format.deserialize_aws_json_1_1(item)
        )
    return out
