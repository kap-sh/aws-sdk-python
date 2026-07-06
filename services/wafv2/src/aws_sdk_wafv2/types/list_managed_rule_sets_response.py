"""Generated from Smithy shape ``com.amazonaws.wafv2#ListManagedRuleSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.managed_rule_set_summaries
    import aws_sdk_wafv2.types.next_marker


class ListManagedRuleSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    managed_rule_sets: NotRequired[
        "aws_sdk_wafv2.types.managed_rule_set_summaries.ManagedRuleSetSummaries"
    ]
    """<p>Your managed rule sets. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListManagedRuleSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "managed_rule_sets" in value:
        import aws_sdk_wafv2.types.managed_rule_set_summaries

        out["ManagedRuleSets"] = (
            aws_sdk_wafv2.types.managed_rule_set_summaries.serialize_aws_json_1_1(
                value["managed_rule_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListManagedRuleSetsResponse:
    out: ListManagedRuleSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "ManagedRuleSets" in data:
        import aws_sdk_wafv2.types.managed_rule_set_summaries

        out["managed_rule_sets"] = (
            aws_sdk_wafv2.types.managed_rule_set_summaries.deserialize_aws_json_1_1(
                data["ManagedRuleSets"]
            )
        )
    return out
