"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallBlockResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

FirewallBlockResponse: TypeAlias = Literal[
    "NODATA",
    "NXDOMAIN",
    "OVERRIDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NODATA",
        "NXDOMAIN",
        "OVERRIDE",
    )
)


def serialize_json(value: FirewallBlockResponse) -> str:
    return value


def deserialize_json(data: str) -> FirewallBlockResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallBlockResponse value: {data!r}")
    return cast(FirewallBlockResponse, data)
