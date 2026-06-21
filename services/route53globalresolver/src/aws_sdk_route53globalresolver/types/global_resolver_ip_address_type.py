"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GlobalResolverIpAddressType``."""

from typing import Literal, TypeAlias, cast

GlobalResolverIpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalResolverIpAddressType) -> str:
    return value


def deserialize_json(data: str) -> GlobalResolverIpAddressType:
    return cast(GlobalResolverIpAddressType, data)
