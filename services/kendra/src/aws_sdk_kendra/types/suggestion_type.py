"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

SuggestionType: TypeAlias = Literal[
    "QUERY",
    "DOCUMENT_ATTRIBUTES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUERY",
        "DOCUMENT_ATTRIBUTES",
    )
)


def serialize_aws_json_1_1(value: SuggestionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuggestionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SuggestionType value: {data!r}")
    return cast(SuggestionType, data)
