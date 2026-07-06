"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallRuleGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn


class GetFirewallRuleGroupPolicyRequest(TypedDict, closed=True):
    arn: "aws_sdk_route53resolver.types.arn.Arn"
    """<p>The ARN (Amazon Resource Name) for the rule group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallRuleGroupPolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallRuleGroupPolicyRequest:
    out: GetFirewallRuleGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetFirewallRuleGroupPolicyRequest.arn required")
    return out
