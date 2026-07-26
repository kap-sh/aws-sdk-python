"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatelessRuleGroupReferencesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class FirewallPolicyStatelessRuleGroupReferencesDetails(TypedDict, closed=True):
    priority: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The order in which to run the stateless rule group.</p>"""
    resource_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the stateless rule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatelessRuleGroupReferencesDetails) -> dict:
    out: dict = {}
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> FirewallPolicyStatelessRuleGroupReferencesDetails:
    out: FirewallPolicyStatelessRuleGroupReferencesDetails = {}  # type: ignore[typeddict-item]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
