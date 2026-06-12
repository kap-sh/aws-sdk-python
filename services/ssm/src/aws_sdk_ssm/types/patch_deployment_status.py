"""Generated from Smithy shape ``com.amazonaws.ssm#PatchDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchDeploymentStatus: TypeAlias = Literal[
    "APPROVED",
    "PENDING_APPROVAL",
    "EXPLICIT_APPROVED",
    "EXPLICIT_REJECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "PENDING_APPROVAL",
        "EXPLICIT_APPROVED",
        "EXPLICIT_REJECTED",
    )
)


def serialize_aws_json_1_1(value: PatchDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchDeploymentStatus value: {data!r}")
    return cast(PatchDeploymentStatus, data)
