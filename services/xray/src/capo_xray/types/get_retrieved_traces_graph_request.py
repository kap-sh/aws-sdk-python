"""Generated from Smithy shape ``com.amazonaws.xray#GetRetrievedTracesGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.retrieval_token
    import capo_xray.types.string


class GetRetrievedTracesGraphRequest(TypedDict, closed=True):
    retrieval_token: "capo_xray.types.retrieval_token.RetrievalToken"
    """<p> Retrieval token. </p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetrievedTracesGraphRequest) -> dict:
    out: dict = {}
    out["RetrievalToken"] = value["retrieval_token"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetRetrievedTracesGraphRequest:
    out: GetRetrievedTracesGraphRequest = {}  # type: ignore[typeddict-item]
    if "RetrievalToken" in data:
        out["retrieval_token"] = data["RetrievalToken"]
    else:
        raise DeserializationError(
            "GetRetrievedTracesGraphRequest.retrieval_token required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
