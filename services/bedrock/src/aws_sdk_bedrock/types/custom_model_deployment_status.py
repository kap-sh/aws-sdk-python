"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

CustomModelDeploymentStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Active",
        "Failed",
    )
)


def serialize_json(value: CustomModelDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomModelDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomModelDeploymentStatus value: {data!r}"
        )
    return cast(CustomModelDeploymentStatus, data)
