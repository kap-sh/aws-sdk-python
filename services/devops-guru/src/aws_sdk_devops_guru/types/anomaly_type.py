"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

AnomalyType: TypeAlias = Literal[
    "CAUSAL",
    "CONTEXTUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAUSAL",
        "CONTEXTUAL",
    )
)


def serialize_json(value: AnomalyType) -> str:
    return value


def deserialize_json(data: str) -> AnomalyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyType value: {data!r}")
    return cast(AnomalyType, data)
