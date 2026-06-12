"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265FlickerAdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable this setting to have the encoder reduce I-frame pop. I-frame pop appears as a visual flicker that can arise when the encoder saves bits by copying some macroblocks many times from frame to frame, and then refreshes them at the I-frame. When you enable this setting, the encoder updates these macroblocks slightly more often to smooth out the flicker. This setting is disabled by default. Related setting: In addition to enabling this setting, you must also set adaptiveQuantization to a value other than Off."""
H265FlickerAdaptiveQuantization: TypeAlias = Literal[
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


def serialize_json(value: H265FlickerAdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H265FlickerAdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265FlickerAdaptiveQuantization value: {data!r}"
        )
    return cast(H265FlickerAdaptiveQuantization, data)
