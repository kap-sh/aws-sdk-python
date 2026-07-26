"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsLaunchType``."""

from typing import Literal, TypeAlias, cast

EcsLaunchType: TypeAlias = Literal[
    "FARGATE",
    "EC2",
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsLaunchType) -> str:
    return value


def deserialize_json(data: str) -> EcsLaunchType:
    return cast(EcsLaunchType, data)
