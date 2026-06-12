"""Generated from Smithy shape ``com.amazonaws.kendra#QueryResultFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

QueryResultFormat: TypeAlias = Literal[
    "TABLE",
    "TEXT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TABLE",
        "TEXT",
    )
)


def serialize_aws_json_1_1(value: QueryResultFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryResultFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryResultFormat value: {data!r}")
    return cast(QueryResultFormat, data)
