"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DimensionMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.dimension_mapping

DimensionMappings: TypeAlias = list[
    "aws_sdk_timestream_write.types.dimension_mapping.DimensionMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionMappings) -> list:
    import aws_sdk_timestream_write.types.dimension_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_write.types.dimension_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DimensionMappings:
    import aws_sdk_timestream_write.types.dimension_mapping

    out: DimensionMappings = []
    for item in data:
        out.append(
            aws_sdk_timestream_write.types.dimension_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
