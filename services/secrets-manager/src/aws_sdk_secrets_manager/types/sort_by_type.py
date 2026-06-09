"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SortByType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_secrets_manager.errors import DeserializationError

SortByType: TypeAlias = Literal[
    "created-date",
    "last-accessed-date",
    "last-changed-date",
    "name",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "created-date",
        "last-accessed-date",
        "last-changed-date",
        "name",
    )
)


def serialize_aws_json_1_1(value: SortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortByType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortByType value: {data!r}")
    return cast(SortByType, data)
