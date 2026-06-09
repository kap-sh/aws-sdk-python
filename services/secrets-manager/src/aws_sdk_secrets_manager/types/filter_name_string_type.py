"""Generated from Smithy shape ``com.amazonaws.secretsmanager#FilterNameStringType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_secrets_manager.errors import DeserializationError

FilterNameStringType: TypeAlias = Literal[
    "description",
    "name",
    "tag-key",
    "tag-value",
    "primary-region",
    "owning-service",
    "all",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "description",
        "name",
        "tag-key",
        "tag-value",
        "primary-region",
        "owning-service",
        "all",
    )
)


def serialize_aws_json_1_1(value: FilterNameStringType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterNameStringType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterNameStringType value: {data!r}")
    return cast(FilterNameStringType, data)
