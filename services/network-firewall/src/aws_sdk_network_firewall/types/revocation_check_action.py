"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RevocationCheckAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

RevocationCheckAction: TypeAlias = Literal[
    "PASS",
    "DROP",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "DROP",
        "REJECT",
    )
)


def serialize_aws_json_1_0(value: RevocationCheckAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RevocationCheckAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RevocationCheckAction value: {data!r}")
    return cast(RevocationCheckAction, data)
