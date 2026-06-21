"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExecutionRoleIdentityConfig``."""

from typing import Literal, TypeAlias, cast

ExecutionRoleIdentityConfig: TypeAlias = Literal[
    "USER_PROFILE_NAME",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionRoleIdentityConfig) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionRoleIdentityConfig:
    return cast(ExecutionRoleIdentityConfig, data)
