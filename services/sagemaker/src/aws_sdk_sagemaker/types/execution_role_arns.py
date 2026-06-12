"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExecutionRoleArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.role_arn

ExecutionRoleArns: TypeAlias = list["aws_sdk_sagemaker.types.role_arn.RoleArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionRoleArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExecutionRoleArns:
    return list(data)
