"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRuleEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Effect of a network traffic rule.</p>"""
NetworkTrafficRuleEffect: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_json(value: NetworkTrafficRuleEffect) -> str:
    return value


def deserialize_json(data: str) -> NetworkTrafficRuleEffect:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkTrafficRuleEffect value: {data!r}")
    return cast(NetworkTrafficRuleEffect, data)
