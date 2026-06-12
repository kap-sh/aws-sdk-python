"""Generated from Smithy shape ``com.amazonaws.athena#QueryResultType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

QueryResultType: TypeAlias = Literal[
    "DATA_MANIFEST",
    "DATA_ROWS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_MANIFEST",
        "DATA_ROWS",
    )
)


def serialize_aws_json_1_1(value: QueryResultType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryResultType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryResultType value: {data!r}")
    return cast(QueryResultType, data)
