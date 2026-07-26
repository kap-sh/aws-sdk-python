"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Suggestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.suggestion_match

Suggestions: TypeAlias = list[
    "capo_cloudsearch_domain.types.suggestion_match.SuggestionMatch"
]


# --- restJson1 ser/de ---
def serialize_json(value: Suggestions) -> list:
    import capo_cloudsearch_domain.types.suggestion_match

    out: list = []
    for item in value:
        out.append(capo_cloudsearch_domain.types.suggestion_match.serialize_json(item))
    return out


def deserialize_json(data: list) -> Suggestions:
    import capo_cloudsearch_domain.types.suggestion_match

    out: Suggestions = []
    for item in data:
        out.append(
            capo_cloudsearch_domain.types.suggestion_match.deserialize_json(item)
        )
    return out
