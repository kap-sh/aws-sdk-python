"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EmbeddedTerminateCaptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting."""
EmbeddedTerminateCaptions: TypeAlias = Literal[
    "END_OF_INPUT",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "END_OF_INPUT",
        "DISABLED",
    )
)


def serialize_json(value: EmbeddedTerminateCaptions) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedTerminateCaptions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmbeddedTerminateCaptions value: {data!r}")
    return cast(EmbeddedTerminateCaptions, data)
