"""Generated from Smithy shape ``com.amazonaws.waf#MatchFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf.errors import DeserializationError

MatchFieldType: TypeAlias = Literal[
    "URI",
    "QUERY_STRING",
    "HEADER",
    "METHOD",
    "BODY",
    "SINGLE_QUERY_ARG",
    "ALL_QUERY_ARGS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "URI",
        "QUERY_STRING",
        "HEADER",
        "METHOD",
        "BODY",
        "SINGLE_QUERY_ARG",
        "ALL_QUERY_ARGS",
    )
)


def serialize_aws_json_1_1(value: MatchFieldType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MatchFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchFieldType value: {data!r}")
    return cast(MatchFieldType, data)
