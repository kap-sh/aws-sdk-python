"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppEndpointPolicy``."""

from typing import Literal, TypeAlias, cast

WebAppEndpointPolicy: TypeAlias = Literal[
    "FIPS",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppEndpointPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAppEndpointPolicy:
    return cast(WebAppEndpointPolicy, data)
