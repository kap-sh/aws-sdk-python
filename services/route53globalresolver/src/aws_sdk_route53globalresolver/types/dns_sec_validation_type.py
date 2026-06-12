"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DnsSecValidationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

DnsSecValidationType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DnsSecValidationType) -> str:
    return value


def deserialize_json(data: str) -> DnsSecValidationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DnsSecValidationType value: {data!r}")
    return cast(DnsSecValidationType, data)
