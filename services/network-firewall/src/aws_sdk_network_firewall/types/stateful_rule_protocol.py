"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

StatefulRuleProtocol: TypeAlias = Literal[
    "IP",
    "TCP",
    "UDP",
    "ICMP",
    "HTTP",
    "FTP",
    "TLS",
    "SMB",
    "DNS",
    "DCERPC",
    "SSH",
    "SMTP",
    "IMAP",
    "MSN",
    "KRB5",
    "IKEV2",
    "TFTP",
    "NTP",
    "DHCP",
    "HTTP2",
    "QUIC",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IP",
        "TCP",
        "UDP",
        "ICMP",
        "HTTP",
        "FTP",
        "TLS",
        "SMB",
        "DNS",
        "DCERPC",
        "SSH",
        "SMTP",
        "IMAP",
        "MSN",
        "KRB5",
        "IKEV2",
        "TFTP",
        "NTP",
        "DHCP",
        "HTTP2",
        "QUIC",
    )
)


def serialize_aws_json_1_0(value: StatefulRuleProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatefulRuleProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatefulRuleProtocol value: {data!r}")
    return cast(StatefulRuleProtocol, data)
