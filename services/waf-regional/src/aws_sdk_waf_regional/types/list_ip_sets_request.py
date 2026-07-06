"""Generated from Smithy shape ``com.amazonaws.wafregional#ListIPSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.next_marker
    import aws_sdk_waf_regional.types.pagination_limit


class ListIPSetsRequest(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>IPSets</code>. For the second and subsequent <code>ListIPSets</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>IPSets</code>.</p>"""
    limit: "aws_sdk_waf_regional.types.pagination_limit.PaginationLimit"
    """<p>Specifies the number of <code>IPSet</code> objects that you want AWS WAF to return for this request. If you have more <code>IPSet</code> objects than the number you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>IPSet</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIPSetsRequest) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Limit"] = value.get("limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIPSetsRequest:
    out: ListIPSetsRequest = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    return out
