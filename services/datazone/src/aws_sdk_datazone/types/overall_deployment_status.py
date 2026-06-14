"""Generated from Smithy shape ``com.amazonaws.datazone#OverallDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

OverallDeploymentStatus: TypeAlias = Literal[
    "PENDING_DEPLOYMENT",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED_VALIDATION",
    "FAILED_DEPLOYMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_DEPLOYMENT",
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED_VALIDATION",
        "FAILED_DEPLOYMENT",
    )
)


def serialize_json(value: OverallDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> OverallDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OverallDeploymentStatus value: {data!r}")
    return cast(OverallDeploymentStatus, data)
