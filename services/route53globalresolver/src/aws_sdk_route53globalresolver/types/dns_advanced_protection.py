"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DnsAdvancedProtection``."""

from typing import Literal, TypeAlias, cast

DnsAdvancedProtection: TypeAlias = Literal[
    "DGA",
    "DNS_TUNNELING",
    "DICTIONARY_DGA",
]


# --- restJson1 ser/de ---
def serialize_json(value: DnsAdvancedProtection) -> str:
    return value


def deserialize_json(data: str) -> DnsAdvancedProtection:
    return cast(DnsAdvancedProtection, data)
