"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SuggestModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.long
    import capo_cloudsearch_domain.types.string
    import capo_cloudsearch_domain.types.suggestions


class SuggestModel(TypedDict, closed=True):
    query: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The query string specified in the suggest request.</p>"""
    found: "capo_cloudsearch_domain.types.long.Long"
    """<p>The number of documents that were found to match the query string.</p>"""
    suggestions: NotRequired["capo_cloudsearch_domain.types.suggestions.Suggestions"]
    """<p>The documents that match the query string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestModel) -> dict:
    out: dict = {}
    if "query" in value:
        out["query"] = value["query"]
    out["found"] = value.get("found", 0)
    if "suggestions" in value:
        import capo_cloudsearch_domain.types.suggestions

        out["suggestions"] = capo_cloudsearch_domain.types.suggestions.serialize_json(
            value["suggestions"]
        )
    return out


def deserialize_json(data: dict) -> SuggestModel:
    out: SuggestModel = {}  # type: ignore[typeddict-item]
    if "query" in data:
        out["query"] = data["query"]
    if "found" in data:
        out["found"] = data["found"]
    else:
        out["found"] = 0
    if "suggestions" in data:
        import capo_cloudsearch_domain.types.suggestions

        out["suggestions"] = capo_cloudsearch_domain.types.suggestions.deserialize_json(
            data["suggestions"]
        )
    return out
