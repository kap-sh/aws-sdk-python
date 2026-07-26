"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#Outputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.output

Outputs: TypeAlias = list["capo_kinesis_analytics.types.output.Output"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Outputs) -> list:
    import capo_kinesis_analytics.types.output

    out: list = []
    for item in value:
        out.append(capo_kinesis_analytics.types.output.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Outputs:
    import capo_kinesis_analytics.types.output

    out: Outputs = []
    for item in data:
        out.append(capo_kinesis_analytics.types.output.deserialize_aws_json_1_1(item))
    return out
