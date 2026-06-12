"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#DeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_edge.errors import DeserializationError

DeploymentType: TypeAlias = Literal["Model",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Model",))


def serialize_json(value: DeploymentType) -> str:
    return value


def deserialize_json(data: str) -> DeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentType value: {data!r}")
    return cast(DeploymentType, data)
