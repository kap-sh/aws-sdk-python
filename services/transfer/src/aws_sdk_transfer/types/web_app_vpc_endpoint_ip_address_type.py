"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppVpcEndpointIpAddressType``."""

from typing import Literal, TypeAlias, cast

WebAppVpcEndpointIpAddressType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppVpcEndpointIpAddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAppVpcEndpointIpAddressType:
    return cast(WebAppVpcEndpointIpAddressType, data)
