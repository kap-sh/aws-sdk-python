"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MeasureValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.measure_value

MeasureValues: TypeAlias = list[
    "aws_sdk_timestream_write.types.measure_value.MeasureValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MeasureValues) -> list:
    import aws_sdk_timestream_write.types.measure_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_write.types.measure_value.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MeasureValues:
    import aws_sdk_timestream_write.types.measure_value

    out: MeasureValues = []
    for item in data:
        out.append(
            aws_sdk_timestream_write.types.measure_value.deserialize_aws_json_1_0(item)
        )
    return out
