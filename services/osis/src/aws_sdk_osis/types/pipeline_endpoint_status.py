"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_osis.errors import DeserializationError

PipelineEndpointStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "CREATE_FAILED",
    "DELETING",
    "REVOKING",
    "REVOKED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "CREATE_FAILED",
        "DELETING",
        "REVOKING",
        "REVOKED",
    )
)


def serialize_json(value: PipelineEndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> PipelineEndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineEndpointStatus value: {data!r}")
    return cast(PipelineEndpointStatus, data)
