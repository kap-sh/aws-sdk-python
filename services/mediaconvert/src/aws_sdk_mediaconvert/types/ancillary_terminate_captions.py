"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AncillaryTerminateCaptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""By default, the service terminates any unterminated captions at the end of each input. If you want the caption to continue onto your next input, disable this setting."""
AncillaryTerminateCaptions: TypeAlias = Literal[
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


def serialize_json(value: AncillaryTerminateCaptions) -> str:
    return value


def deserialize_json(data: str) -> AncillaryTerminateCaptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AncillaryTerminateCaptions value: {data!r}"
        )
    return cast(AncillaryTerminateCaptions, data)
