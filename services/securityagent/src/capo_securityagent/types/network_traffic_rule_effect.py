"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRuleEffect``."""

from typing import Literal, TypeAlias, cast

"""<p>Effect of a network traffic rule.</p>"""
NetworkTrafficRuleEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTrafficRuleEffect) -> str:
    return value


def deserialize_json(data: str) -> NetworkTrafficRuleEffect:
    return cast(NetworkTrafficRuleEffect, data)
