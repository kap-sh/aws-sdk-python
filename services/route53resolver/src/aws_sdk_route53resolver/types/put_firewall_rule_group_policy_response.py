"""Generated from Smithy shape ``com.amazonaws.route53resolver#PutFirewallRuleGroupPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.boolean


class PutFirewallRuleGroupPolicyResponse(TypedDict, closed=True):
    return_value: "aws_sdk_route53resolver.types.boolean.Boolean"
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFirewallRuleGroupPolicyResponse) -> dict:
    out: dict = {}
    out["ReturnValue"] = value.get("return_value", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFirewallRuleGroupPolicyResponse:
    out: PutFirewallRuleGroupPolicyResponse = {}  # type: ignore[typeddict-item]
    if "ReturnValue" in data:
        out["return_value"] = data["ReturnValue"]
    else:
        out["return_value"] = False
    return out
