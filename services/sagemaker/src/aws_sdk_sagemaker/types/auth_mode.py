"""Generated from Smithy shape ``com.amazonaws.sagemaker#AuthMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AuthMode: TypeAlias = Literal[
    "SSO",
    "IAM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSO",
        "IAM",
    )
)


def serialize_aws_json_1_1(value: AuthMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthMode value: {data!r}")
    return cast(AuthMode, data)
