"""Generated from Smithy shape ``com.amazonaws.kendra#SuggestionType``."""

from typing import Literal, TypeAlias, cast

SuggestionType: TypeAlias = Literal[
    "QUERY",
    "DOCUMENT_ATTRIBUTES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuggestionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SuggestionType:
    return cast(SuggestionType, data)
