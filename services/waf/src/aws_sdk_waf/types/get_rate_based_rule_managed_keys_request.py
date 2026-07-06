"""Generated from Smithy shape ``com.amazonaws.waf#GetRateBasedRuleManagedKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.next_marker
    import aws_sdk_waf.types.resource_id


class GetRateBasedRuleManagedKeysRequest(TypedDict, closed=True):
    rule_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>RuleId</code> of the <a>RateBasedRule</a> for which you want to get a list of <code>ManagedKeys</code>. <code>RuleId</code> is returned by <a>CreateRateBasedRule</a> and by <a>ListRateBasedRules</a>.</p>"""
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>A null value and not currently used. Do not include this in your request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedRuleManagedKeysRequest) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedRuleManagedKeysRequest:
    out: GetRateBasedRuleManagedKeysRequest = {}  # type: ignore[typeddict-item]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError(
            "GetRateBasedRuleManagedKeysRequest.rule_id required"
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
