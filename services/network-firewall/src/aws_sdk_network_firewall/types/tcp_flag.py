"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TCPFlag``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

TCPFlag: TypeAlias = Literal[
    "FIN",
    "SYN",
    "RST",
    "PSH",
    "ACK",
    "URG",
    "ECE",
    "CWR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIN",
        "SYN",
        "RST",
        "PSH",
        "ACK",
        "URG",
        "ECE",
        "CWR",
    )
)


def serialize_aws_json_1_0(value: TCPFlag) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TCPFlag:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TCPFlag value: {data!r}")
    return cast(TCPFlag, data)
