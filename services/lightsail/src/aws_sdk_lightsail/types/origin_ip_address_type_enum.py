"""Generated from Smithy shape ``com.amazonaws.lightsail#OriginIpAddressTypeEnum``."""

from typing import Literal, TypeAlias, cast

OriginIpAddressTypeEnum: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dualstack",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OriginIpAddressTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginIpAddressTypeEnum:
    return cast(OriginIpAddressTypeEnum, data)
