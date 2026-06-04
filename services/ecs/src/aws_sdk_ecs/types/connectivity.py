"""Generated from Smithy shape ``com.amazonaws.ecs#Connectivity``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

Connectivity: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "DISCONNECTED",
    )
)


def serialize_aws_json_1_1(value: Connectivity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Connectivity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Connectivity value: {data!r}")
    return cast(Connectivity, data)
