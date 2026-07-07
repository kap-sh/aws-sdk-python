"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MxfXavcProfileSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max2147483647
    import aws_sdk_mediaconvert.types.mxf_xavc_duration_mode


class MxfXavcProfileSettings(TypedDict, closed=True):
    duration_mode: NotRequired[
        "aws_sdk_mediaconvert.types.mxf_xavc_duration_mode.MxfXavcDurationMode"
    ]
    """To create an output that complies with the XAVC file format guidelines for interoperability, keep the default value, Drop frames for compliance. To include all frames from your input in this output, keep the default setting, Allow any duration. The number of frames that MediaConvert excludes when you set this to Drop frames for compliance depends on the output frame rate and duration."""
    max_anc_data_size: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify a value for this setting only for outputs that you set up with one of these two XAVC profiles: XAVC HD Intra CBG or XAVC 4K Intra CBG. Specify the amount of space in each frame that the service reserves for ancillary data, such as teletext captions. The default value for this setting is 1492 bytes per frame. This should be sufficient to prevent overflow unless you have multiple pages of teletext captions data. If you have a large amount of teletext data, specify a larger number."""


# --- restJson1 ser/de ---
def serialize_json(value: MxfXavcProfileSettings) -> dict:
    out: dict = {}
    if "duration_mode" in value:
        import aws_sdk_mediaconvert.types.mxf_xavc_duration_mode

        out["durationMode"] = (
            aws_sdk_mediaconvert.types.mxf_xavc_duration_mode.serialize_json(
                value["duration_mode"]
            )
        )
    if "max_anc_data_size" in value:
        out["maxAncDataSize"] = value["max_anc_data_size"]
    return out


def deserialize_json(data: dict) -> MxfXavcProfileSettings:
    out: MxfXavcProfileSettings = {}  # type: ignore[typeddict-item]
    if "durationMode" in data:
        import aws_sdk_mediaconvert.types.mxf_xavc_duration_mode

        out["duration_mode"] = (
            aws_sdk_mediaconvert.types.mxf_xavc_duration_mode.deserialize_json(
                data["durationMode"]
            )
        )
    if "maxAncDataSize" in data:
        out["max_anc_data_size"] = data["maxAncDataSize"]
    return out
