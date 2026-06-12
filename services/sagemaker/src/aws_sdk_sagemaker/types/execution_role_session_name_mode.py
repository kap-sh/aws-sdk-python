"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExecutionRoleSessionNameMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ExecutionRoleSessionNameMode: TypeAlias = Literal[
    "STATIC",
    "USER_IDENTITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "USER_IDENTITY",
    )
)


def serialize_aws_json_1_1(value: ExecutionRoleSessionNameMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionRoleSessionNameMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExecutionRoleSessionNameMode value: {data!r}"
        )
    return cast(ExecutionRoleSessionNameMode, data)
