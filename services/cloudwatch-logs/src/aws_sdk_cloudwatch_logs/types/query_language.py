"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

QueryLanguage: TypeAlias = Literal[
    "CWLI",
    "SQL",
    "PPL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CWLI",
        "SQL",
        "PPL",
    )
)


def serialize_aws_json_1_1(value: QueryLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryLanguage value: {data!r}")
    return cast(QueryLanguage, data)
