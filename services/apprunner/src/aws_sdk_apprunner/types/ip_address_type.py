"""Generated from Smithy shape ``com.amazonaws.apprunner#IpAddressType``."""

from typing import Literal, TypeAlias, cast

IpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUAL_STACK",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IpAddressType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
