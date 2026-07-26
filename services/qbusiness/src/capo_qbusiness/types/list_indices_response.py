"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListIndicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.indices
    import capo_qbusiness.types.next_token


class ListIndicesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token that you can use in the subsequent request to retrieve the next set of indexes.</p>"""
    indices: NotRequired["capo_qbusiness.types.indices.Indices"]
    """<p>An array of information on the items in one or more indexes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndicesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "indices" in value:
        import capo_qbusiness.types.indices

        out["indices"] = capo_qbusiness.types.indices.serialize_json(value["indices"])
    return out


def deserialize_json(data: dict) -> ListIndicesResponse:
    out: ListIndicesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "indices" in data:
        import capo_qbusiness.types.indices

        out["indices"] = capo_qbusiness.types.indices.deserialize_json(data["indices"])
    return out
