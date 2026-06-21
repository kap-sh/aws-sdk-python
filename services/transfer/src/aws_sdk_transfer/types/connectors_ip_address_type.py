"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorsIpAddressType``."""

from typing import Literal, TypeAlias, cast

ConnectorsIpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorsIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorsIpAddressType:
    return cast(ConnectorsIpAddressType, data)
