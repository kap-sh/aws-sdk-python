"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeedManagementState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Elemental Inference Feed management state."""
ElementalInferenceFeedManagementState: TypeAlias = Literal[
    "CREATED",
    "ASSOCIATED",
    "PENDING_DELETION",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "ASSOCIATED",
        "PENDING_DELETION",
        "DELETED",
    )
)


def serialize_json(value: ElementalInferenceFeedManagementState) -> str:
    return value


def deserialize_json(data: str) -> ElementalInferenceFeedManagementState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ElementalInferenceFeedManagementState value: {data!r}"
        )
    return cast(ElementalInferenceFeedManagementState, data)
