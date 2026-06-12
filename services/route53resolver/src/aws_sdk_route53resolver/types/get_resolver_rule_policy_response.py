"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverRulePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_rule_policy


class GetResolverRulePolicyResponse(TypedDict):
    resolver_rule_policy: NotRequired[
        "aws_sdk_route53resolver.types.resolver_rule_policy.ResolverRulePolicy"
    ]
    """<p>The Resolver rule policy for the rule that you specified in a <code>GetResolverRulePolicy</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverRulePolicyResponse) -> dict:
    out: dict = {}
    if "resolver_rule_policy" in value:
        out["ResolverRulePolicy"] = value["resolver_rule_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverRulePolicyResponse:
    out: GetResolverRulePolicyResponse = {}  # type: ignore[typeddict-item]
    if "ResolverRulePolicy" in data:
        out["resolver_rule_policy"] = data["ResolverRulePolicy"]
    return out
