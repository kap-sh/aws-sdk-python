"""Generated from Smithy shape ``com.amazonaws.wafregional#ListRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.next_marker
    import capo_waf_regional.types.pagination_limit


class ListRulesRequest(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf_regional.types.next_marker.NextMarker"]
    """<p>If you specify a value for <code>Limit</code> and you have more <code>Rules</code> than the value of <code>Limit</code>, AWS WAF returns a <code>NextMarker</code> value in the response that allows you to list another group of <code>Rules</code>. For the second and subsequent <code>ListRules</code> requests, specify the value of <code>NextMarker</code> from the previous response to get information about another batch of <code>Rules</code>.</p>"""
    limit: "capo_waf_regional.types.pagination_limit.PaginationLimit"
    """<p>Specifies the number of <code>Rules</code> that you want AWS WAF to return for this request. If you have more <code>Rules</code> than the number that you specify for <code>Limit</code>, the response includes a <code>NextMarker</code> value that you can use to get another batch of <code>Rules</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesRequest) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Limit"] = value.get("limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesRequest:
    out: ListRulesRequest = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    return out
