"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GlobalResolverIpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

GlobalResolverIpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUAL_STACK",
    )
)


def serialize_json(value: GlobalResolverIpAddressType) -> str:
    return value


def deserialize_json(data: str) -> GlobalResolverIpAddressType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalResolverIpAddressType value: {data!r}"
        )
    return cast(GlobalResolverIpAddressType, data)
