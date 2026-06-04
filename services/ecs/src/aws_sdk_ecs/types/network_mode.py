"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkMode``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

NetworkMode: TypeAlias = Literal[
    "bridge",
    "host",
    "awsvpc",
    "none",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "bridge",
        "host",
        "awsvpc",
        "none",
    )
)


def serialize_aws_json_1_1(value: NetworkMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkMode value: {data!r}")
    return cast(NetworkMode, data)
