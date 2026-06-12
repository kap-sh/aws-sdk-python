"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_patch_state_filter_value

InstancePatchStateFilterValues: TypeAlias = list[
    "aws_sdk_ssm.types.instance_patch_state_filter_value.InstancePatchStateFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstancePatchStateFilterValues:
    return list(data)
