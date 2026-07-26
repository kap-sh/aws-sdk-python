"""Generated from Smithy shape ``com.amazonaws.emr#InstanceStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.instance_state

InstanceStateList: TypeAlias = list["capo_emr.types.instance_state.InstanceState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStateList) -> list:
    import capo_emr.types.instance_state

    out: list = []
    for item in value:
        out.append(capo_emr.types.instance_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceStateList:
    import capo_emr.types.instance_state

    out: InstanceStateList = []
    for item in data:
        out.append(capo_emr.types.instance_state.deserialize_aws_json_1_1(item))
    return out
