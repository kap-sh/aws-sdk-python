"""Generated from Smithy shape ``com.amazonaws.sagemaker#AssumableRoleArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.role_arn

AssumableRoleArns: TypeAlias = list["capo_sagemaker.types.role_arn.RoleArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssumableRoleArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssumableRoleArns:
    return list(data)
