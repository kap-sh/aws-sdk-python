"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medical_imaging.errors import DeserializationError

ImageSetState: TypeAlias = Literal[
    "ACTIVE",
    "LOCKED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "LOCKED",
        "DELETED",
    )
)


def serialize_json(value: ImageSetState) -> str:
    return value


def deserialize_json(data: str) -> ImageSetState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSetState value: {data!r}")
    return cast(ImageSetState, data)
