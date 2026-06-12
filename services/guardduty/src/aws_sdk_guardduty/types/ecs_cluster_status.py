"""Generated from Smithy shape ``com.amazonaws.guardduty#EcsClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

EcsClusterStatus: TypeAlias = Literal[
    "ACTIVE",
    "PROVISIONING",
    "DEPROVISIONING",
    "FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PROVISIONING",
        "DEPROVISIONING",
        "FAILED",
        "INACTIVE",
    )
)


def serialize_json(value: EcsClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> EcsClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EcsClusterStatus value: {data!r}")
    return cast(EcsClusterStatus, data)
