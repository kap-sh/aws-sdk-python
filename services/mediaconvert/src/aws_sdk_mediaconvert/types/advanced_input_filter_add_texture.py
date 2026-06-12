"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AdvancedInputFilterAddTexture``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Add texture and detail to areas of your input video content that were lost after applying the Advanced input filter. To adaptively add texture and reduce softness: Choose Enabled. To not add any texture: Keep the default value, Disabled. We recommend that you choose Disabled for input video content that doesn't have texture, including screen recordings, computer graphics, or cartoons."""
AdvancedInputFilterAddTexture: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AdvancedInputFilterAddTexture) -> str:
    return value


def deserialize_json(data: str) -> AdvancedInputFilterAddTexture:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdvancedInputFilterAddTexture value: {data!r}"
        )
    return cast(AdvancedInputFilterAddTexture, data)
