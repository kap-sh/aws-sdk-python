"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExecutionRoleIdentityConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ExecutionRoleIdentityConfig: TypeAlias = Literal[
    "USER_PROFILE_NAME",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_PROFILE_NAME",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ExecutionRoleIdentityConfig) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionRoleIdentityConfig:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExecutionRoleIdentityConfig value: {data!r}"
        )
    return cast(ExecutionRoleIdentityConfig, data)
