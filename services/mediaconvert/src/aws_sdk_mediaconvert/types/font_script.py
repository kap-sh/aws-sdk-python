"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FontScript``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Provide the font script, using an ISO 15924 script code, if the LanguageCode is not sufficient for determining the script type. Where LanguageCode or CustomLanguageCode is sufficient, use \"AUTOMATIC\" or leave unset."""
FontScript: TypeAlias = Literal[
    "AUTOMATIC",
    "HANS",
    "HANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "HANS",
        "HANT",
    )
)


def serialize_json(value: FontScript) -> str:
    return value


def deserialize_json(data: str) -> FontScript:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FontScript value: {data!r}")
    return cast(FontScript, data)
