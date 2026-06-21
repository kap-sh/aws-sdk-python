"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DnsSecValidationType``."""

from typing import Literal, TypeAlias, cast

DnsSecValidationType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DnsSecValidationType) -> str:
    return value


def deserialize_json(data: str) -> DnsSecValidationType:
    return cast(DnsSecValidationType, data)
