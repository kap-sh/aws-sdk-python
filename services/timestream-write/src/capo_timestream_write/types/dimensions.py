"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_write.types.dimension

Dimensions: TypeAlias = list["capo_timestream_write.types.dimension.Dimension"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimensions) -> list:
    import capo_timestream_write.types.dimension

    out: list = []
    for item in value:
        out.append(capo_timestream_write.types.dimension.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Dimensions:
    import capo_timestream_write.types.dimension

    out: Dimensions = []
    for item in data:
        out.append(capo_timestream_write.types.dimension.deserialize_aws_json_1_0(item))
    return out
