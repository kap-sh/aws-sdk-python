"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsLaunchType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

EcsLaunchType: TypeAlias = Literal[
    "FARGATE",
    "EC2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FARGATE",
        "EC2",
    )
)


def serialize_json(value: EcsLaunchType) -> str:
    return value


def deserialize_json(data: str) -> EcsLaunchType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EcsLaunchType value: {data!r}")
    return cast(EcsLaunchType, data)
