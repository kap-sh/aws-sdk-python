"""Generated from Smithy shape ``com.amazonaws.glue#SourceControlAuthStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

SourceControlAuthStrategy: TypeAlias = Literal[
    "PERSONAL_ACCESS_TOKEN",
    "AWS_SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSONAL_ACCESS_TOKEN",
        "AWS_SECRETS_MANAGER",
    )
)


def serialize_aws_json_1_1(value: SourceControlAuthStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceControlAuthStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceControlAuthStrategy value: {data!r}")
    return cast(SourceControlAuthStrategy, data)
