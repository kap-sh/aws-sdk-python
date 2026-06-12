"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseFilterPostTemporalSharpening``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you set Noise reducer to Temporal, the bandwidth and sharpness of your output is reduced. You can optionally use Post temporal sharpening to apply sharpening to the edges of your output. Note that Post temporal sharpening will also make the bandwidth reduction from the Noise reducer smaller. The default behavior, Auto, allows the transcoder to determine whether to apply sharpening, depending on your input type and quality. When you set Post temporal sharpening to Enabled, specify how much sharpening is applied using Post temporal sharpening strength. Set Post temporal sharpening to Disabled to not apply sharpening."""
NoiseFilterPostTemporalSharpening: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "AUTO",
    )
)


def serialize_json(value: NoiseFilterPostTemporalSharpening) -> str:
    return value


def deserialize_json(data: str) -> NoiseFilterPostTemporalSharpening:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NoiseFilterPostTemporalSharpening value: {data!r}"
        )
    return cast(NoiseFilterPostTemporalSharpening, data)
