"""Generated from Smithy shape ``com.amazonaws.wafregional#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.next_marker
    import aws_sdk_waf_regional.types.rule_summaries


class ListRulesResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>Rules</code> than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>Rules</code>, submit another <code>ListRules</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    rules: NotRequired["aws_sdk_waf_regional.types.rule_summaries.RuleSummaries"]
    """<p>An array of <a>RuleSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "rules" in value:
        import aws_sdk_waf_regional.types.rule_summaries

        out["Rules"] = aws_sdk_waf_regional.types.rule_summaries.serialize_aws_json_1_1(
            value["rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "Rules" in data:
        import aws_sdk_waf_regional.types.rule_summaries

        out["rules"] = (
            aws_sdk_waf_regional.types.rule_summaries.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    return out
