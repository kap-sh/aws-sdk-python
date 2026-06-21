"""Generated from Smithy shape ``com.amazonaws.lightsail#IpAddressType``."""

from typing import Literal, TypeAlias, cast

IpAddressType: TypeAlias = Literal[
    "dualstack",
    "ipv4",
    "ipv6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
