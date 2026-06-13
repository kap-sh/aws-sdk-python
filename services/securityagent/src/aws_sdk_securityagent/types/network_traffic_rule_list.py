"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.network_traffic_rule

NetworkTrafficRuleList: TypeAlias = list[
    "aws_sdk_securityagent.types.network_traffic_rule.NetworkTrafficRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTrafficRuleList) -> list:
    import aws_sdk_securityagent.types.network_traffic_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.network_traffic_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkTrafficRuleList:
    import aws_sdk_securityagent.types.network_traffic_rule

    out: NetworkTrafficRuleList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.network_traffic_rule.deserialize_json(item)
        )
    return out
