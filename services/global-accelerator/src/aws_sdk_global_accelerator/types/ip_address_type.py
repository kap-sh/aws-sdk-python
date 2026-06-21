"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpAddressType``."""

from typing import Literal, TypeAlias, cast

IpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUAL_STACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
