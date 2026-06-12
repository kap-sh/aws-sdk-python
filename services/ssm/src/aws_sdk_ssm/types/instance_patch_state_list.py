"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_patch_state

InstancePatchStateList: TypeAlias = list[
    "aws_sdk_ssm.types.instance_patch_state.InstancePatchState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateList) -> list:
    import aws_sdk_ssm.types.instance_patch_state

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.instance_patch_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePatchStateList:
    import aws_sdk_ssm.types.instance_patch_state

    out: InstancePatchStateList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.instance_patch_state.deserialize_aws_json_1_1(item)
        )
    return out
