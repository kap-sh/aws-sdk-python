"""Generated from Smithy shape ``com.amazonaws.transfer#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

IpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "DUALSTACK",
    )
)


def serialize_aws_json_1_1(value: IpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
