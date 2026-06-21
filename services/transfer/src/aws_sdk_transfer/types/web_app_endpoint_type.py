"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppEndpointType``."""

from typing import Literal, TypeAlias, cast

WebAppEndpointType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAppEndpointType:
    return cast(WebAppEndpointType, data)
