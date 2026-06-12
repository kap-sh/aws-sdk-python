"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallStatefulRuleGroupOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.network_firewall_override_action


class NetworkFirewallStatefulRuleGroupOverride(TypedDict):
    action: NotRequired[
        "aws_sdk_fms.types.network_firewall_override_action.NetworkFirewallOverrideAction"
    ]
    """<p>The action that changes the rule group from <code>DROP</code> to <code>ALERT</code>. This only applies to managed rule groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallStatefulRuleGroupOverride) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_fms.types.network_firewall_override_action

        out["Action"] = (
            aws_sdk_fms.types.network_firewall_override_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallStatefulRuleGroupOverride:
    out: NetworkFirewallStatefulRuleGroupOverride = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_fms.types.network_firewall_override_action

        out["action"] = (
            aws_sdk_fms.types.network_firewall_override_action.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    return out
