"""Generated from Smithy shape ``com.amazonaws.ecs#ApplicationProtocol``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ApplicationProtocol: TypeAlias = Literal[
    "http",
    "http2",
    "grpc",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "http",
        "http2",
        "grpc",
    )
)


def serialize_aws_json_1_1(value: ApplicationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationProtocol value: {data!r}")
    return cast(ApplicationProtocol, data)
