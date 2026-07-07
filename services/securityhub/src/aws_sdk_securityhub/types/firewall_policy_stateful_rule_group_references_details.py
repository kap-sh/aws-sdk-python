"""Generated from Smithy shape ``com.amazonaws.securityhub#FirewallPolicyStatefulRuleGroupReferencesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class FirewallPolicyStatefulRuleGroupReferencesDetails(TypedDict, closed=True):
    resource_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the stateful rule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FirewallPolicyStatefulRuleGroupReferencesDetails) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> FirewallPolicyStatefulRuleGroupReferencesDetails:
    out: FirewallPolicyStatefulRuleGroupReferencesDetails = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
