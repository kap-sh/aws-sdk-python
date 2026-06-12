"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IdentifiedType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

IdentifiedType: TypeAlias = Literal[
    "STATELESS_RULE_FORWARDING_ASYMMETRICALLY",
    "STATELESS_RULE_CONTAINS_TCP_FLAGS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATELESS_RULE_FORWARDING_ASYMMETRICALLY",
        "STATELESS_RULE_CONTAINS_TCP_FLAGS",
    )
)


def serialize_aws_json_1_0(value: IdentifiedType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdentifiedType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentifiedType value: {data!r}")
    return cast(IdentifiedType, data)
