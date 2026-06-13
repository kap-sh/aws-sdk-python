"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

CustomModelDeploymentUpdateStatus: TypeAlias = Literal[
    "Updating",
    "UpdateCompleted",
    "UpdateFailed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Updating",
        "UpdateCompleted",
        "UpdateFailed",
    )
)


def serialize_json(value: CustomModelDeploymentUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomModelDeploymentUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomModelDeploymentUpdateStatus value: {data!r}"
        )
    return cast(CustomModelDeploymentUpdateStatus, data)
