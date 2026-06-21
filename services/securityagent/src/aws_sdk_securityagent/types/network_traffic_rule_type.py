"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRuleType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of network traffic rule.</p>"""
NetworkTrafficRuleType: TypeAlias = Literal["URL",]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTrafficRuleType) -> str:
    return value


def deserialize_json(data: str) -> NetworkTrafficRuleType:
    return cast(NetworkTrafficRuleType, data)
