"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListKeywordsForDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.keywords
    import capo_auditmanager.types.token


class ListKeywordsForDataSourceResponse(TypedDict, closed=True):
    keywords: NotRequired["capo_auditmanager.types.keywords.Keywords"]
    """<p>The list of keywords for the control mapping source.</p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeywordsForDataSourceResponse) -> dict:
    out: dict = {}
    if "keywords" in value:
        import capo_auditmanager.types.keywords

        out["keywords"] = capo_auditmanager.types.keywords.serialize_json(
            value["keywords"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKeywordsForDataSourceResponse:
    out: ListKeywordsForDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "keywords" in data:
        import capo_auditmanager.types.keywords

        out["keywords"] = capo_auditmanager.types.keywords.deserialize_json(
            data["keywords"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
