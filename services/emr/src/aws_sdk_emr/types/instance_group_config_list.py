"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_group_config

InstanceGroupConfigList: TypeAlias = list[
    "aws_sdk_emr.types.instance_group_config.InstanceGroupConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupConfigList) -> list:
    import aws_sdk_emr.types.instance_group_config

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.instance_group_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceGroupConfigList:
    import aws_sdk_emr.types.instance_group_config

    out: InstanceGroupConfigList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.instance_group_config.deserialize_aws_json_1_1(item)
        )
    return out
