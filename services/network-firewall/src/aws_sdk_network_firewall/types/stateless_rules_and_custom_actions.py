"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatelessRulesAndCustomActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.custom_actions
    import aws_sdk_network_firewall.types.stateless_rules


class StatelessRulesAndCustomActions(TypedDict, closed=True):
    stateless_rules: "aws_sdk_network_firewall.types.stateless_rules.StatelessRules"
    """<p>Defines the set of stateless rules for use in a stateless rule group. </p>"""
    custom_actions: NotRequired[
        "aws_sdk_network_firewall.types.custom_actions.CustomActions"
    ]
    """<p>Defines an array of individual custom action definitions that are available for use by the stateless rules in this <code>StatelessRulesAndCustomActions</code> specification. You name each custom action that you define, and then you can use it by name in your <a>StatelessRule</a> <a>RuleDefinition</a> <code>Actions</code> specification.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatelessRulesAndCustomActions) -> dict:
    out: dict = {}
    import aws_sdk_network_firewall.types.stateless_rules

    out["StatelessRules"] = (
        aws_sdk_network_firewall.types.stateless_rules.serialize_aws_json_1_0(
            value["stateless_rules"]
        )
    )
    if "custom_actions" in value:
        import aws_sdk_network_firewall.types.custom_actions

        out["CustomActions"] = (
            aws_sdk_network_firewall.types.custom_actions.serialize_aws_json_1_0(
                value["custom_actions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatelessRulesAndCustomActions:
    out: StatelessRulesAndCustomActions = {}  # type: ignore[typeddict-item]
    if "StatelessRules" in data:
        import aws_sdk_network_firewall.types.stateless_rules

        out["stateless_rules"] = (
            aws_sdk_network_firewall.types.stateless_rules.deserialize_aws_json_1_0(
                data["StatelessRules"]
            )
        )
    else:
        raise DeserializationError(
            "StatelessRulesAndCustomActions.stateless_rules required"
        )
    if "CustomActions" in data:
        import aws_sdk_network_firewall.types.custom_actions

        out["custom_actions"] = (
            aws_sdk_network_firewall.types.custom_actions.deserialize_aws_json_1_0(
                data["CustomActions"]
            )
        )
    return out
