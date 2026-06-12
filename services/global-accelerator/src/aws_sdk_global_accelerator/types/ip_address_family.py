"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpAddressFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

IpAddressFamily: TypeAlias = Literal[
    "IPv4",
    "IPv6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPv4",
        "IPv6",
    )
)


def serialize_aws_json_1_1(value: IpAddressFamily) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressFamily:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressFamily value: {data!r}")
    return cast(IpAddressFamily, data)
