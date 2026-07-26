"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpAddressFamily``."""

from typing import Literal, TypeAlias, cast

IpAddressFamily: TypeAlias = Literal[
    "IPv4",
    "IPv6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressFamily) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressFamily:
    return cast(IpAddressFamily, data)
