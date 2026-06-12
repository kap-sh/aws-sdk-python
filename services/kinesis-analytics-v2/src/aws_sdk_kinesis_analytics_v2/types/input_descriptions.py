"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.input_description

InputDescriptions: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.input_description.InputDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDescriptions) -> list:
    import aws_sdk_kinesis_analytics_v2.types.input_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.input_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputDescriptions:
    import aws_sdk_kinesis_analytics_v2.types.input_description

    out: InputDescriptions = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.input_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
