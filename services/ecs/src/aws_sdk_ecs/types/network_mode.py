"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkMode``."""

from typing import Literal, TypeAlias, cast

NetworkMode: TypeAlias = Literal[
    "bridge",
    "host",
    "awsvpc",
    "none",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkMode:
    return cast(NetworkMode, data)
