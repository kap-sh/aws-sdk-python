"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DnsProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

DnsProtocol: TypeAlias = Literal[
    "DO53",
    "DOH",
    "DOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DO53",
        "DOH",
        "DOT",
    )
)


def serialize_json(value: DnsProtocol) -> str:
    return value


def deserialize_json(data: str) -> DnsProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DnsProtocol value: {data!r}")
    return cast(DnsProtocol, data)
