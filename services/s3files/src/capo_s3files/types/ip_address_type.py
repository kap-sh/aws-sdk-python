"""Generated from Smithy shape ``com.amazonaws.s3files#IpAddressType``."""

from typing import Literal, TypeAlias, cast

IpAddressType: TypeAlias = Literal[
    "IPV4_ONLY",
    "IPV6_ONLY",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
