"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.input_update

InputUpdates: TypeAlias = list["capo_kinesis_analytics.types.input_update.InputUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputUpdates) -> list:
    import capo_kinesis_analytics.types.input_update

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics.types.input_update.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputUpdates:
    import capo_kinesis_analytics.types.input_update

    out: InputUpdates = []
    for item in data:
        out.append(
            capo_kinesis_analytics.types.input_update.deserialize_aws_json_1_1(item)
        )
    return out
