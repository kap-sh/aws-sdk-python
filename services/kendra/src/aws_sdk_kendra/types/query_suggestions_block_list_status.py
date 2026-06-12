"""Generated from Smithy shape ``com.amazonaws.kendra#QuerySuggestionsBlockListStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

QuerySuggestionsBlockListStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "UPDATING",
    "ACTIVE_BUT_UPDATE_FAILED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "DELETING",
        "UPDATING",
        "ACTIVE_BUT_UPDATE_FAILED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: QuerySuggestionsBlockListStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QuerySuggestionsBlockListStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown QuerySuggestionsBlockListStatus value: {data!r}"
        )
    return cast(QuerySuggestionsBlockListStatus, data)
