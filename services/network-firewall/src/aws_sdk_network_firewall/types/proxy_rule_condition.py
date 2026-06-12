"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.condition_key
    import aws_sdk_network_firewall.types.condition_operator
    import aws_sdk_network_firewall.types.proxy_condition_value_list


class ProxyRuleCondition(TypedDict):
    condition_operator: NotRequired[
        "aws_sdk_network_firewall.types.condition_operator.ConditionOperator"
    ]
    """<p>Defines how to perform a match.</p>"""
    condition_key: NotRequired[
        "aws_sdk_network_firewall.types.condition_key.ConditionKey"
    ]
    """<p>Defines what is to be matched.</p>"""
    condition_values: NotRequired[
        "aws_sdk_network_firewall.types.proxy_condition_value_list.ProxyConditionValueList"
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
        import aws_sdk_network_firewall.types.proxy_condition_value_list

        out["ConditionValues"] = (
            aws_sdk_network_firewall.types.proxy_condition_value_list.serialize_aws_json_1_0(
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
        import aws_sdk_network_firewall.types.proxy_condition_value_list

        out["condition_values"] = (
            aws_sdk_network_firewall.types.proxy_condition_value_list.deserialize_aws_json_1_0(
                data["ConditionValues"]
            )
        )
    return out
