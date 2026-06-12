"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

QuerySuggestionsStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: QuerySuggestionsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuerySuggestionsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QuerySuggestionsStatus value: {data!r}")
    return cast(QuerySuggestionsStatus, data)
