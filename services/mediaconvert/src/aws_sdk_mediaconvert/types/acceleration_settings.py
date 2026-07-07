"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AccelerationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.acceleration_mode


class AccelerationSettings(TypedDict, closed=True):
    mode: NotRequired["aws_sdk_mediaconvert.types.acceleration_mode.AccelerationMode"]
    """Specify the conditions when the service will run your job with accelerated transcoding."""


# --- restJson1 ser/de ---
def serialize_json(value: AccelerationSettings) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_mediaconvert.types.acceleration_mode

        out["mode"] = aws_sdk_mediaconvert.types.acceleration_mode.serialize_json(
            value["mode"]
        )
    return out


def deserialize_json(data: dict) -> AccelerationSettings:
    out: AccelerationSettings = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_mediaconvert.types.acceleration_mode

        out["mode"] = aws_sdk_mediaconvert.types.acceleration_mode.deserialize_json(
            data["mode"]
        )
    return out
