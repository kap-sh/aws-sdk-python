"""Generated from Smithy shape ``com.amazonaws.xray#GetRetrievedTracesGraphRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.retrieval_token
    import aws_sdk_xray.types.string


class GetRetrievedTracesGraphRequest(TypedDict):
    retrieval_token: "aws_sdk_xray.types.retrieval_token.RetrievalToken"
    """<p> Retrieval token. </p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
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
