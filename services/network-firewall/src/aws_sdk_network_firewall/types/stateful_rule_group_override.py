"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleGroupOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.override_action


class StatefulRuleGroupOverride(TypedDict, closed=True):
    action: NotRequired["aws_sdk_network_firewall.types.override_action.OverrideAction"]
    """<p>The action that changes the rule group from <code>DROP</code> to <code>ALERT</code>. This only applies to managed rule groups.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleGroupOverride) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_network_firewall.types.override_action

        out["Action"] = (
            aws_sdk_network_firewall.types.override_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulRuleGroupOverride:
    out: StatefulRuleGroupOverride = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_network_firewall.types.override_action

        out["action"] = (
            aws_sdk_network_firewall.types.override_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    return out
