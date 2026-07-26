"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIngestionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.ingestions
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListIngestionsResponse(TypedDict, closed=True):
    ingestions: NotRequired["capo_quicksight.types.ingestions.Ingestions"]
    """<p>A list of the ingestions.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestionsResponse) -> dict:
    out: dict = {}
    if "ingestions" in value:
        import capo_quicksight.types.ingestions

        out["Ingestions"] = capo_quicksight.types.ingestions.serialize_json(
            value["ingestions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListIngestionsResponse:
    out: ListIngestionsResponse = {}  # type: ignore[typeddict-item]
    if "Ingestions" in data:
        import capo_quicksight.types.ingestions

        out["ingestions"] = capo_quicksight.types.ingestions.deserialize_json(
            data["Ingestions"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
