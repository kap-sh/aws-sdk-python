"""Generated from Smithy shape ``com.amazonaws.lightsail#HttpEndpoint``."""

from typing import Literal, TypeAlias, cast

HttpEndpoint: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpoint) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HttpEndpoint:
    return cast(HttpEndpoint, data)
