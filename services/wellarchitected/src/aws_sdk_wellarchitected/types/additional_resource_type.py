"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AdditionalResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

AdditionalResourceType: TypeAlias = Literal[
    "HELPFUL_RESOURCE",
    "IMPROVEMENT_PLAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HELPFUL_RESOURCE",
        "IMPROVEMENT_PLAN",
    )
)


def serialize_json(value: AdditionalResourceType) -> str:
    return value


def deserialize_json(data: str) -> AdditionalResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdditionalResourceType value: {data!r}")
    return cast(AdditionalResourceType, data)
