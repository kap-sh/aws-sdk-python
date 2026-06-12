"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_edge.errors import DeserializationError

DeploymentStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAIL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAIL",
    )
)


def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
