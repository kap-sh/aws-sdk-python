"""Generated from Smithy shape ``com.amazonaws.ecs#ApplicationProtocol``."""

from typing import Literal, TypeAlias, cast

ApplicationProtocol: TypeAlias = Literal[
    "http",
    "http2",
    "grpc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationProtocol:
    return cast(ApplicationProtocol, data)
