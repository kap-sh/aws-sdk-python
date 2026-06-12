"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallRuleGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class GetFirewallRuleGroupRequest(TypedDict):
    firewall_rule_group_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule group. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallRuleGroupRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallRuleGroupRequest:
    out: GetFirewallRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupId" in data:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    else:
        raise DeserializationError(
            "GetFirewallRuleGroupRequest.firewall_rule_group_id required"
        )
    return out
