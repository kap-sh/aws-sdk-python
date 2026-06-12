"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

SourceAuthType: TypeAlias = Literal[
    "OAUTH",
    "CODECONNECTIONS",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OAUTH",
        "CODECONNECTIONS",
        "SECRETS_MANAGER",
    )
)


def serialize_aws_json_1_1(value: SourceAuthType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceAuthType value: {data!r}")
    return cast(SourceAuthType, data)
