"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsSegmentationStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Segmentation Style"""
M2tsSegmentationStyle: TypeAlias = Literal[
    "MAINTAIN_CADENCE",
    "RESET_CADENCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAINTAIN_CADENCE",
        "RESET_CADENCE",
    )
)


def serialize_json(value: M2tsSegmentationStyle) -> str:
    return value


def deserialize_json(data: str) -> M2tsSegmentationStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsSegmentationStyle value: {data!r}")
    return cast(M2tsSegmentationStyle, data)
