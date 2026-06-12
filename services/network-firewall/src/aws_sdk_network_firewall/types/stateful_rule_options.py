"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.rule_order


class StatefulRuleOptions(TypedDict):
    rule_order: NotRequired["aws_sdk_network_firewall.types.rule_order.RuleOrder"]
    """<p>Indicates how to manage the order of the rule evaluation for the rule group. <code>DEFAULT_ACTION_ORDER</code> is the default behavior. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see <a href=\"https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html\">Evaluation order for stateful rules</a> in the <i>Network Firewall Developer Guide</i>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleOptions) -> dict:
    out: dict = {}
    if "rule_order" in value:
        import aws_sdk_network_firewall.types.rule_order

        out["RuleOrder"] = (
            aws_sdk_network_firewall.types.rule_order.serialize_aws_json_1_0(
                value["rule_order"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulRuleOptions:
    out: StatefulRuleOptions = {}  # type: ignore[typeddict-item]
    if "RuleOrder" in data:
        import aws_sdk_network_firewall.types.rule_order

        out["rule_order"] = (
            aws_sdk_network_firewall.types.rule_order.deserialize_aws_json_1_0(
                data["RuleOrder"]
            )
        )
    return out
