"""Generated from Smithy shape ``com.amazonaws.pcs#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pcs.types.instance_config

InstanceList: TypeAlias = list["capo_pcs.types.instance_config.InstanceConfig"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceList) -> list:
    import capo_pcs.types.instance_config

    out: list = []
    for item in value:
        out.append(capo_pcs.types.instance_config.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InstanceList:
    import capo_pcs.types.instance_config

    out: InstanceList = []
    for item in data:
        out.append(capo_pcs.types.instance_config.deserialize_aws_json_1_0(item))
    return out
