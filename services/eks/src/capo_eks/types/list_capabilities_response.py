"""Generated from Smithy shape ``com.amazonaws.eks#ListCapabilitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.capability_summary_list
    import capo_eks.types.string


class ListCapabilitiesResponse(TypedDict, closed=True):
    capabilities: NotRequired[
        "capo_eks.types.capability_summary_list.CapabilitySummaryList"
    ]
    """<p>A list of capability summary objects, each containing basic information about a capability including its name, ARN, type, status, version, and timestamps.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListCapabilities</code> request. When the results of a <code>ListCapabilities</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapabilitiesResponse) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import capo_eks.types.capability_summary_list

        out["capabilities"] = capo_eks.types.capability_summary_list.serialize_json(
            value["capabilities"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCapabilitiesResponse:
    out: ListCapabilitiesResponse = {}  # type: ignore[typeddict-item]
    if "capabilities" in data:
        import capo_eks.types.capability_summary_list

        out["capabilities"] = capo_eks.types.capability_summary_list.deserialize_json(
            data["capabilities"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
