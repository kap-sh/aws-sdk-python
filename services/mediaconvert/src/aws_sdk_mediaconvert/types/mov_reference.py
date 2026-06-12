"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovReference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Always keep the default value (SELF_CONTAINED) for this setting."""
MovReference: TypeAlias = Literal[
    "SELF_CONTAINED",
    "EXTERNAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF_CONTAINED",
        "EXTERNAL",
    )
)


def serialize_json(value: MovReference) -> str:
    return value


def deserialize_json(data: str) -> MovReference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MovReference value: {data!r}")
    return cast(MovReference, data)
