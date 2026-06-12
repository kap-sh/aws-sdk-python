"""Generated from Smithy shape ``com.amazonaws.codebuild#AuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

AuthType: TypeAlias = Literal[
    "OAUTH",
    "BASIC_AUTH",
    "PERSONAL_ACCESS_TOKEN",
    "CODECONNECTIONS",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OAUTH",
        "BASIC_AUTH",
        "PERSONAL_ACCESS_TOKEN",
        "CODECONNECTIONS",
        "SECRETS_MANAGER",
    )
)


def serialize_aws_json_1_1(value: AuthType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthType value: {data!r}")
    return cast(AuthType, data)
