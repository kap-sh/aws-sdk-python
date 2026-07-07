"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Deinterlacer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.deinterlace_algorithm
    import aws_sdk_mediaconvert.types.deinterlacer_control
    import aws_sdk_mediaconvert.types.deinterlacer_mode


class Deinterlacer(TypedDict, closed=True):
    algorithm: NotRequired[
        "aws_sdk_mediaconvert.types.deinterlace_algorithm.DeinterlaceAlgorithm"
    ]
    """Only applies when you set Deinterlace mode to Deinterlace or Adaptive. Interpolate produces sharper pictures, while blend produces smoother motion. If your source file includes a ticker, such as a scrolling headline at the bottom of the frame: Choose Interpolate ticker or Blend ticker. To apply field doubling: Choose Linear interpolation. Note that Linear interpolation may introduce video artifacts into your output."""
    control: NotRequired[
        "aws_sdk_mediaconvert.types.deinterlacer_control.DeinterlacerControl"
    ]
    """- When set to NORMAL (default), the deinterlacer does not convert frames that are tagged in metadata as progressive. It will only convert those that are tagged as some other type. - When set to FORCE_ALL_FRAMES, the deinterlacer converts every frame to progressive - even those that are already tagged as progressive. Turn Force mode on only if there is a good chance that the metadata has tagged frames as progressive when they are not progressive. Do not turn on otherwise; processing frames that are already progressive into progressive will probably result in lower quality video."""
    mode: NotRequired["aws_sdk_mediaconvert.types.deinterlacer_mode.DeinterlacerMode"]
    """Use Deinterlacer to choose how the service will do deinterlacing. Default is Deinterlace. - Deinterlace converts interlaced to progressive. - Inverse telecine converts Hard Telecine 29.97i to progressive 23.976p. - Adaptive auto-detects and converts to progressive."""


# --- restJson1 ser/de ---
def serialize_json(value: Deinterlacer) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import aws_sdk_mediaconvert.types.deinterlace_algorithm

        out["algorithm"] = (
            aws_sdk_mediaconvert.types.deinterlace_algorithm.serialize_json(
                value["algorithm"]
            )
        )
    if "control" in value:
        import aws_sdk_mediaconvert.types.deinterlacer_control

        out["control"] = aws_sdk_mediaconvert.types.deinterlacer_control.serialize_json(
            value["control"]
        )
    if "mode" in value:
        import aws_sdk_mediaconvert.types.deinterlacer_mode

        out["mode"] = aws_sdk_mediaconvert.types.deinterlacer_mode.serialize_json(
            value["mode"]
        )
    return out


def deserialize_json(data: dict) -> Deinterlacer:
    out: Deinterlacer = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import aws_sdk_mediaconvert.types.deinterlace_algorithm

        out["algorithm"] = (
            aws_sdk_mediaconvert.types.deinterlace_algorithm.deserialize_json(
                data["algorithm"]
            )
        )
    if "control" in data:
        import aws_sdk_mediaconvert.types.deinterlacer_control

        out["control"] = (
            aws_sdk_mediaconvert.types.deinterlacer_control.deserialize_json(
                data["control"]
            )
        )
    if "mode" in data:
        import aws_sdk_mediaconvert.types.deinterlacer_mode

        out["mode"] = aws_sdk_mediaconvert.types.deinterlacer_mode.deserialize_json(
            data["mode"]
        )
    return out
