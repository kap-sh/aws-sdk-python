"""Generated from Smithy shape ``com.amazonaws.launchwizard#WorkloadDeploymentPatternStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_launch_wizard.errors import DeserializationError

WorkloadDeploymentPatternStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DISABLED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
        "DISABLED",
        "DELETED",
    )
)


def serialize_json(value: WorkloadDeploymentPatternStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkloadDeploymentPatternStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkloadDeploymentPatternStatus value: {data!r}"
        )
    return cast(WorkloadDeploymentPatternStatus, data)
