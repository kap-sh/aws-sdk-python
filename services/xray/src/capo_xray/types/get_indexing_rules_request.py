"""Generated from Smithy shape ``com.amazonaws.xray#GetIndexingRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string


class GetIndexingRulesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexingRulesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetIndexingRulesRequest:
    out: GetIndexingRulesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
