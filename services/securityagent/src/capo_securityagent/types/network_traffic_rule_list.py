"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.network_traffic_rule

NetworkTrafficRuleList: TypeAlias = list[
    "capo_securityagent.types.network_traffic_rule.NetworkTrafficRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTrafficRuleList) -> list:
    import capo_securityagent.types.network_traffic_rule

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.network_traffic_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkTrafficRuleList:
    import capo_securityagent.types.network_traffic_rule

    out: NetworkTrafficRuleList = []
    for item in data:
        out.append(capo_securityagent.types.network_traffic_rule.deserialize_json(item))
    return out
