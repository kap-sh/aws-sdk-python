"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TargetResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

TargetResourceType: TypeAlias = Literal[
    "ASSET",
    "COMPUTATION_MODEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSET",
        "COMPUTATION_MODEL",
    )
)


def serialize_json(value: TargetResourceType) -> str:
    return value


def deserialize_json(data: str) -> TargetResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetResourceType value: {data!r}")
    return cast(TargetResourceType, data)
