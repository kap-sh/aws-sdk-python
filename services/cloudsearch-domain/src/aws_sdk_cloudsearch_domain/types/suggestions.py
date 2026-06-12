"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Suggestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.suggestion_match

Suggestions: TypeAlias = list[
    "aws_sdk_cloudsearch_domain.types.suggestion_match.SuggestionMatch"
]


# --- restJson1 ser/de ---
def serialize_json(value: Suggestions) -> list:
    import aws_sdk_cloudsearch_domain.types.suggestion_match

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudsearch_domain.types.suggestion_match.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Suggestions:
    import aws_sdk_cloudsearch_domain.types.suggestion_match

    out: Suggestions = []
    for item in data:
        out.append(
            aws_sdk_cloudsearch_domain.types.suggestion_match.deserialize_json(item)
        )
    return out
