"""Generated from Smithy shape ``com.amazonaws.emr#InstanceTypeConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance_type_config

InstanceTypeConfigList: TypeAlias = list[
    "capo_emr.types.instance_type_config.InstanceTypeConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceTypeConfigList) -> list:
    import capo_emr.types.instance_type_config

    out: list = []
    for item in value:
        out.append(capo_emr.types.instance_type_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceTypeConfigList:
    import capo_emr.types.instance_type_config

    out: InstanceTypeConfigList = []
    for item in data:
        out.append(capo_emr.types.instance_type_config.deserialize_aws_json_1_1(item))
    return out
