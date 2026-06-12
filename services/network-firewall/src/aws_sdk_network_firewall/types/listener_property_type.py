"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerPropertyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

ListenerPropertyType: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP",
        "HTTPS",
    )
)


def serialize_aws_json_1_0(value: ListenerPropertyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListenerPropertyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListenerPropertyType value: {data!r}")
    return cast(ListenerPropertyType, data)
