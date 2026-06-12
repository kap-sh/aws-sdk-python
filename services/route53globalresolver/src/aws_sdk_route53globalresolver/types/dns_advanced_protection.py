"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DnsAdvancedProtection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

DnsAdvancedProtection: TypeAlias = Literal[
    "DGA",
    "DNS_TUNNELING",
    "DICTIONARY_DGA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DGA",
        "DNS_TUNNELING",
        "DICTIONARY_DGA",
    )
)


def serialize_json(value: DnsAdvancedProtection) -> str:
    return value


def deserialize_json(data: str) -> DnsAdvancedProtection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DnsAdvancedProtection value: {data!r}")
    return cast(DnsAdvancedProtection, data)
