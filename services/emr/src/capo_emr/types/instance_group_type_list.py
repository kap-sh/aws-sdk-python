"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance_group_type

InstanceGroupTypeList: TypeAlias = list[
    "capo_emr.types.instance_group_type.InstanceGroupType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupTypeList) -> list:
    import capo_emr.types.instance_group_type

    out: list = []
    for item in value:
        out.append(capo_emr.types.instance_group_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGroupTypeList:
    import capo_emr.types.instance_group_type

    out: InstanceGroupTypeList = []
    for item in data:
        out.append(capo_emr.types.instance_group_type.deserialize_aws_json_1_1(item))
    return out
