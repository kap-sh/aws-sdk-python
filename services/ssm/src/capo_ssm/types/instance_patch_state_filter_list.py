"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_patch_state_filter

InstancePatchStateFilterList: TypeAlias = list[
    "capo_ssm.types.instance_patch_state_filter.InstancePatchStateFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateFilterList) -> list:
    import capo_ssm.types.instance_patch_state_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.instance_patch_state_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePatchStateFilterList:
    import capo_ssm.types.instance_patch_state_filter

    out: InstancePatchStateFilterList = []
    for item in data:
        out.append(
            capo_ssm.types.instance_patch_state_filter.deserialize_aws_json_1_1(item)
        )
    return out
