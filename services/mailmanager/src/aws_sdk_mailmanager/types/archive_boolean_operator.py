"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ArchiveBooleanOperator: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IS_TRUE",
        "IS_FALSE",
    )
)


def serialize_aws_json_1_0(value: ArchiveBooleanOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveBooleanOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArchiveBooleanOperator value: {data!r}")
    return cast(ArchiveBooleanOperator, data)
