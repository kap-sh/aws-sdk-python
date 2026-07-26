"""Generated from Smithy shape ``com.amazonaws.memorydb#ParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.parameter_group

ParameterGroupList: TypeAlias = list[
    "capo_memorydb.types.parameter_group.ParameterGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterGroupList) -> list:
    import capo_memorydb.types.parameter_group

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.parameter_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterGroupList:
    import capo_memorydb.types.parameter_group

    out: ParameterGroupList = []
    for item in data:
        out.append(capo_memorydb.types.parameter_group.deserialize_aws_json_1_1(item))
    return out
