"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamDimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.timestream_dimension

TimestreamDimensionList: TypeAlias = list[
    "aws_sdk_iot.types.timestream_dimension.TimestreamDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamDimensionList) -> list:
    import aws_sdk_iot.types.timestream_dimension

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.timestream_dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimestreamDimensionList:
    import aws_sdk_iot.types.timestream_dimension

    out: TimestreamDimensionList = []
    for item in data:
        out.append(aws_sdk_iot.types.timestream_dimension.deserialize_json(item))
    return out
