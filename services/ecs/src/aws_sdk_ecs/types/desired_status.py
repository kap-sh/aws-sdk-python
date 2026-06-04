"""Generated from Smithy shape ``com.amazonaws.ecs#DesiredStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DesiredStatus: TypeAlias = Literal[
    "RUNNING",
    "PENDING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "PENDING",
        "STOPPED",
    )
)


def serialize_aws_json_1_1(value: DesiredStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DesiredStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DesiredStatus value: {data!r}")
    return cast(DesiredStatus, data)
