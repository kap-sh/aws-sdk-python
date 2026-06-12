"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnvironmentVariableType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

EnvironmentVariableType: TypeAlias = Literal[
    "PLAINTEXT",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PLAINTEXT",
        "SECRETS_MANAGER",
    )
)


def serialize_aws_json_1_1(value: EnvironmentVariableType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentVariableType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentVariableType value: {data!r}")
    return cast(EnvironmentVariableType, data)
