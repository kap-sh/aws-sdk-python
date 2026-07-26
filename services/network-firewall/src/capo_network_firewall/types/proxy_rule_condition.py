"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.condition_key
    import capo_network_firewall.types.condition_operator
    import capo_network_firewall.types.proxy_condition_value_list


class ProxyRuleCondition(TypedDict, closed=True):
    condition_operator: NotRequired[
        "capo_network_firewall.types.condition_operator.ConditionOperator"
    ]
    """<p>Defines how to perform a match.</p>"""
    condition_key: NotRequired["capo_network_firewall.types.condition_key.ConditionKey"]
    """<p>Defines what is to be matched.</p>"""
    condition_values: NotRequired[
        "capo_network_firewall.types.proxy_condition_value_list.ProxyConditionValueList"
    ]
    """<p>Specifes the exact value that needs to be matched against.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleCondition) -> dict:
    out: dict = {}
    if "condition_operator" in value:
        out["ConditionOperator"] = value["condition_operator"]
    if "condition_key" in value:
        out["ConditionKey"] = value["condition_key"]
    if "condition_values" in value:
        import capo_network_firewall.types.proxy_condition_value_list

        out["ConditionValues"] = (
            capo_network_firewall.types.proxy_condition_value_list.serialize_aws_json_1_0(
                value["condition_values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRuleCondition:
    out: ProxyRuleCondition = {}  # type: ignore[typeddict-item]
    if "ConditionOperator" in data:
        out["condition_operator"] = data["ConditionOperator"]
    if "ConditionKey" in data:
        out["condition_key"] = data["ConditionKey"]
    if "ConditionValues" in data:
        import capo_network_firewall.types.proxy_condition_value_list

        out["condition_values"] = (
            capo_network_firewall.types.proxy_condition_value_list.deserialize_aws_json_1_0(
                data["ConditionValues"]
            )
        )
    return out
