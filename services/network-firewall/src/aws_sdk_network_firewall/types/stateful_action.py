"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

StatefulAction: TypeAlias = Literal[
    "PASS",
    "DROP",
    "ALERT",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "DROP",
        "ALERT",
        "REJECT",
    )
)


def serialize_aws_json_1_0(value: StatefulAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatefulAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatefulAction value: {data!r}")
    return cast(StatefulAction, data)
