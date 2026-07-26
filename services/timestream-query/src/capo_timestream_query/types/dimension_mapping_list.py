"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DimensionMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.dimension_mapping

DimensionMappingList: TypeAlias = list[
    "capo_timestream_query.types.dimension_mapping.DimensionMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionMappingList) -> list:
    import capo_timestream_query.types.dimension_mapping

    out: list = []
    for item in value:
        out.append(
            capo_timestream_query.types.dimension_mapping.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DimensionMappingList:
    import capo_timestream_query.types.dimension_mapping

    out: DimensionMappingList = []
    for item in data:
        out.append(
            capo_timestream_query.types.dimension_mapping.deserialize_aws_json_1_0(item)
        )
    return out
