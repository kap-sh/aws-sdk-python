"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamDimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.timestream_dimension

TimestreamDimensionList: TypeAlias = list[
    "capo_iot.types.timestream_dimension.TimestreamDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamDimensionList) -> list:
    import capo_iot.types.timestream_dimension

    out: list = []
    for item in value:
        out.append(capo_iot.types.timestream_dimension.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimestreamDimensionList:
    import capo_iot.types.timestream_dimension

    out: TimestreamDimensionList = []
    for item in data:
        out.append(capo_iot.types.timestream_dimension.deserialize_json(item))
    return out
