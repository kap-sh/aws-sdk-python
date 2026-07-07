"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.mov_clap_atom
    import aws_sdk_mediaconvert.types.mov_cslg_atom
    import aws_sdk_mediaconvert.types.mov_mpeg2_four_cc_control
    import aws_sdk_mediaconvert.types.mov_padding_control
    import aws_sdk_mediaconvert.types.mov_reference


class MovSettings(TypedDict, closed=True):
    clap_atom: NotRequired["aws_sdk_mediaconvert.types.mov_clap_atom.MovClapAtom"]
    """When enabled, include 'clap' atom if appropriate for the video output settings."""
    cslg_atom: NotRequired["aws_sdk_mediaconvert.types.mov_cslg_atom.MovCslgAtom"]
    """When enabled, file composition times will start at zero, composition times in the 'ctts' (composition time to sample) box for B-frames will be negative, and a 'cslg' (composition shift least greatest) box will be included per 14496-1 amendment 1. This improves compatibility with Apple players and tools."""
    mpeg2_four_cc_control: NotRequired[
        "aws_sdk_mediaconvert.types.mov_mpeg2_four_cc_control.MovMpeg2FourCCControl"
    ]
    """When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2."""
    padding_control: NotRequired[
        "aws_sdk_mediaconvert.types.mov_padding_control.MovPaddingControl"
    ]
    """Unless you need Omneon compatibility: Keep the default value, None. To make this output compatible with Omneon: Choose Omneon. When you do, MediaConvert increases the length of the 'elst' edit list atom. Note that this might cause file rejections when a recipient of the output file doesn't expect this extra padding."""
    reference: NotRequired["aws_sdk_mediaconvert.types.mov_reference.MovReference"]
    """Always keep the default value (SELF_CONTAINED) for this setting."""


# --- restJson1 ser/de ---
def serialize_json(value: MovSettings) -> dict:
    out: dict = {}
    if "clap_atom" in value:
        import aws_sdk_mediaconvert.types.mov_clap_atom

        out["clapAtom"] = aws_sdk_mediaconvert.types.mov_clap_atom.serialize_json(
            value["clap_atom"]
        )
    if "cslg_atom" in value:
        import aws_sdk_mediaconvert.types.mov_cslg_atom

        out["cslgAtom"] = aws_sdk_mediaconvert.types.mov_cslg_atom.serialize_json(
            value["cslg_atom"]
        )
    if "mpeg2_four_cc_control" in value:
        import aws_sdk_mediaconvert.types.mov_mpeg2_four_cc_control

        out["mpeg2FourCCControl"] = (
            aws_sdk_mediaconvert.types.mov_mpeg2_four_cc_control.serialize_json(
                value["mpeg2_four_cc_control"]
            )
        )
    if "padding_control" in value:
        import aws_sdk_mediaconvert.types.mov_padding_control

        out["paddingControl"] = (
            aws_sdk_mediaconvert.types.mov_padding_control.serialize_json(
                value["padding_control"]
            )
        )
    if "reference" in value:
        import aws_sdk_mediaconvert.types.mov_reference

        out["reference"] = aws_sdk_mediaconvert.types.mov_reference.serialize_json(
            value["reference"]
        )
    return out


def deserialize_json(data: dict) -> MovSettings:
    out: MovSettings = {}  # type: ignore[typeddict-item]
    if "clapAtom" in data:
        import aws_sdk_mediaconvert.types.mov_clap_atom

        out["clap_atom"] = aws_sdk_mediaconvert.types.mov_clap_atom.deserialize_json(
            data["clapAtom"]
        )
    if "cslgAtom" in data:
        import aws_sdk_mediaconvert.types.mov_cslg_atom

        out["cslg_atom"] = aws_sdk_mediaconvert.types.mov_cslg_atom.deserialize_json(
            data["cslgAtom"]
        )
    if "mpeg2FourCCControl" in data:
        import aws_sdk_mediaconvert.types.mov_mpeg2_four_cc_control

        out["mpeg2_four_cc_control"] = (
            aws_sdk_mediaconvert.types.mov_mpeg2_four_cc_control.deserialize_json(
                data["mpeg2FourCCControl"]
            )
        )
    if "paddingControl" in data:
        import aws_sdk_mediaconvert.types.mov_padding_control

        out["padding_control"] = (
            aws_sdk_mediaconvert.types.mov_padding_control.deserialize_json(
                data["paddingControl"]
            )
        )
    if "reference" in data:
        import aws_sdk_mediaconvert.types.mov_reference

        out["reference"] = aws_sdk_mediaconvert.types.mov_reference.deserialize_json(
            data["reference"]
        )
    return out
