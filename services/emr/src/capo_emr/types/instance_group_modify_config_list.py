"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupModifyConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance_group_modify_config

InstanceGroupModifyConfigList: TypeAlias = list[
    "capo_emr.types.instance_group_modify_config.InstanceGroupModifyConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupModifyConfigList) -> list:
    import capo_emr.types.instance_group_modify_config

    out: list = []
    for item in value:
        out.append(
            capo_emr.types.instance_group_modify_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGroupModifyConfigList:
    import capo_emr.types.instance_group_modify_config

    out: InstanceGroupModifyConfigList = []
    for item in data:
        out.append(
            capo_emr.types.instance_group_modify_config.deserialize_aws_json_1_1(item)
        )
    return out
