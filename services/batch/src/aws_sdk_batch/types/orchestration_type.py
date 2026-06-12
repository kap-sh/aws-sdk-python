"""Generated from Smithy shape ``com.amazonaws.batch#OrchestrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

OrchestrationType: TypeAlias = Literal[
    "ECS",
    "EKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ECS",
        "EKS",
    )
)


def serialize_json(value: OrchestrationType) -> str:
    return value


def deserialize_json(data: str) -> OrchestrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrchestrationType value: {data!r}")
    return cast(OrchestrationType, data)
