"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.network_traffic_rule_effect
    import aws_sdk_securityagent.types.network_traffic_rule_type


class NetworkTrafficRule(TypedDict, closed=True):
    effect: NotRequired[
        "aws_sdk_securityagent.types.network_traffic_rule_effect.NetworkTrafficRuleEffect"
    ]
    """<p>The effect of the rule. Valid values are ALLOW and DENY.</p>"""
    pattern: NotRequired["str"]
    """<p>The URL pattern to match for the rule.</p>"""
    network_traffic_rule_type: NotRequired[
        "aws_sdk_securityagent.types.network_traffic_rule_type.NetworkTrafficRuleType"
    ]
    """<p>The type of the network traffic rule. Currently, only URL is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTrafficRule) -> dict:
    out: dict = {}
    if "effect" in value:
        import aws_sdk_securityagent.types.network_traffic_rule_effect

        out["effect"] = (
            aws_sdk_securityagent.types.network_traffic_rule_effect.serialize_json(
                value["effect"]
            )
        )
    if "pattern" in value:
        out["pattern"] = value["pattern"]
    if "network_traffic_rule_type" in value:
        import aws_sdk_securityagent.types.network_traffic_rule_type

        out["networkTrafficRuleType"] = (
            aws_sdk_securityagent.types.network_traffic_rule_type.serialize_json(
                value["network_traffic_rule_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkTrafficRule:
    out: NetworkTrafficRule = {}  # type: ignore[typeddict-item]
    if "effect" in data:
        import aws_sdk_securityagent.types.network_traffic_rule_effect

        out["effect"] = (
            aws_sdk_securityagent.types.network_traffic_rule_effect.deserialize_json(
                data["effect"]
            )
        )
    if "pattern" in data:
        out["pattern"] = data["pattern"]
    if "networkTrafficRuleType" in data:
        import aws_sdk_securityagent.types.network_traffic_rule_type

        out["network_traffic_rule_type"] = (
            aws_sdk_securityagent.types.network_traffic_rule_type.deserialize_json(
                data["networkTrafficRuleType"]
            )
        )
    return out
