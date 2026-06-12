"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

LogType: TypeAlias = Literal[
    "ALERT",
    "FLOW",
    "TLS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALERT",
        "FLOW",
        "TLS",
    )
)


def serialize_aws_json_1_0(value: LogType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
