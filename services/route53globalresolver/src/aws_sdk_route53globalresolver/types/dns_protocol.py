"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DnsProtocol``."""

from typing import Literal, TypeAlias, cast

DnsProtocol: TypeAlias = Literal[
    "DO53",
    "DOH",
    "DOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DnsProtocol) -> str:
    return value


def deserialize_json(data: str) -> DnsProtocol:
    return cast(DnsProtocol, data)
