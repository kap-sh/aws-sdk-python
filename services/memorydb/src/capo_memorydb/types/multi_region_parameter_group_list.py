"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.multi_region_parameter_group

MultiRegionParameterGroupList: TypeAlias = list[
    "capo_memorydb.types.multi_region_parameter_group.MultiRegionParameterGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionParameterGroupList) -> list:
    import capo_memorydb.types.multi_region_parameter_group

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.multi_region_parameter_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MultiRegionParameterGroupList:
    import capo_memorydb.types.multi_region_parameter_group

    out: MultiRegionParameterGroupList = []
    for item in data:
        out.append(
            capo_memorydb.types.multi_region_parameter_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
