"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlansRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.max_results
    import aws_sdk_arc_region_switch.types.next_token


class ListPlansRequest(TypedDict):
    max_results: NotRequired["aws_sdk_arc_region_switch.types.max_results.MaxResults"]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired["aws_sdk_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlansRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlansRequest:
    out: ListPlansRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
