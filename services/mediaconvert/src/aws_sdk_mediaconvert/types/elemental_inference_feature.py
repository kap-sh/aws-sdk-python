"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Elemental Inference feature."""
ElementalInferenceFeature: TypeAlias = Literal["SMART_CROP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SMART_CROP",))


def serialize_json(value: ElementalInferenceFeature) -> str:
    return value


def deserialize_json(data: str) -> ElementalInferenceFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ElementalInferenceFeature value: {data!r}")
    return cast(ElementalInferenceFeature, data)
