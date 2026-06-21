"""Generated from Smithy shape ``com.amazonaws.transfer#EndpointType``."""

from typing import Literal, TypeAlias, cast

EndpointType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
    "VPC_ENDPOINT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointType:
    return cast(EndpointType, data)
