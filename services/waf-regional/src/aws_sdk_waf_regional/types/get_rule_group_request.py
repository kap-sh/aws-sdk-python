"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_id


class GetRuleGroupRequest(TypedDict, closed=True):
    rule_group_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RuleGroupId</code> of the <a>RuleGroup</a> that you want to get. <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRuleGroupRequest) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRuleGroupRequest:
    out: GetRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("GetRuleGroupRequest.rule_group_id required")
    return out
