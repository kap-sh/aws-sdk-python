"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SuggestionMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.long
    import aws_sdk_cloudsearch_domain.types.string


class SuggestionMatch(TypedDict, closed=True):
    suggestion: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The string that matches the query string specified in the <code>SuggestRequest</code>. </p>"""
    score: "aws_sdk_cloudsearch_domain.types.long.Long"
    """<p>The relevance score of a suggested match.</p>"""
    id: NotRequired["aws_sdk_cloudsearch_domain.types.string.String"]
    """<p>The document ID of the suggested document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestionMatch) -> dict:
    out: dict = {}
    if "suggestion" in value:
        out["suggestion"] = value["suggestion"]
    out["score"] = value.get("score", 0)
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> SuggestionMatch:
    out: SuggestionMatch = {}  # type: ignore[typeddict-item]
    if "suggestion" in data:
        out["suggestion"] = data["suggestion"]
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    if "id" in data:
        out["id"] = data["id"]
    return out
