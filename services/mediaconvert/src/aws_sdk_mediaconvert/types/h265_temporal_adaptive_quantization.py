"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265TemporalAdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Keep the default value, Enabled, to adjust quantization within each frame based on temporal variation of content complexity. When you enable this feature, the encoder uses fewer bits on areas of the frame that aren't moving and uses more bits on complex objects with sharp edges that move a lot. For example, this feature improves the readability of text tickers on newscasts and scoreboards on sports matches. Enabling this feature will almost always improve your video quality. Note, though, that this feature doesn't take into account where the viewer's attention is likely to be. If viewers are likely to be focusing their attention on a part of the screen that doesn't have moving objects with sharp edges, such as sports athletes' faces, you might choose to disable this feature. Related setting: When you enable temporal quantization, adjust the strength of the filter with the setting Adaptive quantization."""
H265TemporalAdaptiveQuantization: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H265TemporalAdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H265TemporalAdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265TemporalAdaptiveQuantization value: {data!r}"
        )
    return cast(H265TemporalAdaptiveQuantization, data)
