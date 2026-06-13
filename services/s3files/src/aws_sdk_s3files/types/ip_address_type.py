"""Generated from Smithy shape ``com.amazonaws.s3files#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3files.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "IPV4_ONLY",
    "IPV6_ONLY",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4_ONLY",
        "IPV6_ONLY",
        "DUAL_STACK",
    )
)


def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
