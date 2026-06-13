"""Generated from Smithy shape ``com.amazonaws.securityagent#NetworkTrafficRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of network traffic rule.</p>"""
NetworkTrafficRuleType: TypeAlias = Literal["URL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("URL",))


def serialize_json(value: NetworkTrafficRuleType) -> str:
    return value


def deserialize_json(data: str) -> NetworkTrafficRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkTrafficRuleType value: {data!r}")
    return cast(NetworkTrafficRuleType, data)
