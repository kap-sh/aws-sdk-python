"""Generated from Smithy shape ``com.amazonaws.kendra#UserGroupResolutionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

UserGroupResolutionMode: TypeAlias = Literal[
    "AWS_SSO",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_SSO",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: UserGroupResolutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserGroupResolutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserGroupResolutionMode value: {data!r}")
    return cast(UserGroupResolutionMode, data)
