"""Generated from Smithy shape ``com.amazonaws.sagemaker#LifecycleConfigArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.studio_lifecycle_config_arn

LifecycleConfigArns: TypeAlias = list[
    "capo_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleConfigArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LifecycleConfigArns:
    return list(data)
