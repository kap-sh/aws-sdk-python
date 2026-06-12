"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionDestinationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.burnin_destination_settings
    import aws_sdk_mediaconvert.types.caption_destination_type
    import aws_sdk_mediaconvert.types.dvb_sub_destination_settings
    import aws_sdk_mediaconvert.types.embedded_destination_settings
    import aws_sdk_mediaconvert.types.imsc_destination_settings
    import aws_sdk_mediaconvert.types.scc_destination_settings
    import aws_sdk_mediaconvert.types.srt_destination_settings
    import aws_sdk_mediaconvert.types.teletext_destination_settings
    import aws_sdk_mediaconvert.types.ttml_destination_settings
    import aws_sdk_mediaconvert.types.webvtt_destination_settings


class CaptionDestinationSettings(TypedDict):
    burnin_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.burnin_destination_settings.BurninDestinationSettings"
    ]
    """Burn-in is a captions delivery method, rather than a captions format. Burn-in writes the captions directly on your video frames, replacing pixels of video content with the captions. Set up burn-in captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/burn-in-output-captions.html."""
    destination_type: NotRequired[
        "aws_sdk_mediaconvert.types.caption_destination_type.CaptionDestinationType"
    ]
    """Specify the format for this set of captions on this output. The default format is embedded without SCTE-20. Note that your choice of video output container constrains your choice of output captions format. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/captions-support-tables.html. If you are using SCTE-20 and you want to create an output that complies with the SCTE-43 spec, choose SCTE-20 plus embedded. To create a non-compliant output where the embedded captions come first, choose Embedded plus SCTE-20."""
    dvb_sub_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.dvb_sub_destination_settings.DvbSubDestinationSettings"
    ]
    """Settings related to DVB-Sub captions. Set up DVB-Sub captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/dvb-sub-output-captions.html."""
    embedded_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.embedded_destination_settings.EmbeddedDestinationSettings"
    ]
    """Settings related to CEA/EIA-608 and CEA/EIA-708 (also called embedded or ancillary) captions. Set up embedded captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/embedded-output-captions.html."""
    imsc_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.imsc_destination_settings.ImscDestinationSettings"
    ]
    """Settings related to IMSC captions. IMSC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html."""
    scc_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.scc_destination_settings.SccDestinationSettings"
    ]
    """Settings related to SCC captions. SCC is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/scc-srt-output-captions.html."""
    srt_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.srt_destination_settings.SrtDestinationSettings"
    ]
    """Settings related to SRT captions. SRT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video."""
    teletext_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.teletext_destination_settings.TeletextDestinationSettings"
    ]
    """Settings related to teletext captions. Set up teletext captions in the same output as your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/teletext-output-captions.html."""
    ttml_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.ttml_destination_settings.TtmlDestinationSettings"
    ]
    """Settings related to TTML captions. TTML is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html."""
    webvtt_destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.webvtt_destination_settings.WebvttDestinationSettings"
    ]
    """Settings related to WebVTT captions. WebVTT is a sidecar format that holds captions in a file that is separate from the video container. Set up sidecar captions in the same output group, but different output from your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/ttml-and-webvtt-output-captions.html."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionDestinationSettings) -> dict:
    out: dict = {}
    if "burnin_destination_settings" in value:
        import aws_sdk_mediaconvert.types.burnin_destination_settings

        out["burninDestinationSettings"] = (
            aws_sdk_mediaconvert.types.burnin_destination_settings.serialize_json(
                value["burnin_destination_settings"]
            )
        )
    if "destination_type" in value:
        import aws_sdk_mediaconvert.types.caption_destination_type

        out["destinationType"] = (
            aws_sdk_mediaconvert.types.caption_destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "dvb_sub_destination_settings" in value:
        import aws_sdk_mediaconvert.types.dvb_sub_destination_settings

        out["dvbSubDestinationSettings"] = (
            aws_sdk_mediaconvert.types.dvb_sub_destination_settings.serialize_json(
                value["dvb_sub_destination_settings"]
            )
        )
    if "embedded_destination_settings" in value:
        import aws_sdk_mediaconvert.types.embedded_destination_settings

        out["embeddedDestinationSettings"] = (
            aws_sdk_mediaconvert.types.embedded_destination_settings.serialize_json(
                value["embedded_destination_settings"]
            )
        )
    if "imsc_destination_settings" in value:
        import aws_sdk_mediaconvert.types.imsc_destination_settings

        out["imscDestinationSettings"] = (
            aws_sdk_mediaconvert.types.imsc_destination_settings.serialize_json(
                value["imsc_destination_settings"]
            )
        )
    if "scc_destination_settings" in value:
        import aws_sdk_mediaconvert.types.scc_destination_settings

        out["sccDestinationSettings"] = (
            aws_sdk_mediaconvert.types.scc_destination_settings.serialize_json(
                value["scc_destination_settings"]
            )
        )
    if "srt_destination_settings" in value:
        import aws_sdk_mediaconvert.types.srt_destination_settings

        out["srtDestinationSettings"] = (
            aws_sdk_mediaconvert.types.srt_destination_settings.serialize_json(
                value["srt_destination_settings"]
            )
        )
    if "teletext_destination_settings" in value:
        import aws_sdk_mediaconvert.types.teletext_destination_settings

        out["teletextDestinationSettings"] = (
            aws_sdk_mediaconvert.types.teletext_destination_settings.serialize_json(
                value["teletext_destination_settings"]
            )
        )
    if "ttml_destination_settings" in value:
        import aws_sdk_mediaconvert.types.ttml_destination_settings

        out["ttmlDestinationSettings"] = (
            aws_sdk_mediaconvert.types.ttml_destination_settings.serialize_json(
                value["ttml_destination_settings"]
            )
        )
    if "webvtt_destination_settings" in value:
        import aws_sdk_mediaconvert.types.webvtt_destination_settings

        out["webvttDestinationSettings"] = (
            aws_sdk_mediaconvert.types.webvtt_destination_settings.serialize_json(
                value["webvtt_destination_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionDestinationSettings:
    out: CaptionDestinationSettings = {}  # type: ignore[typeddict-item]
    if "burninDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.burnin_destination_settings

        out["burnin_destination_settings"] = (
            aws_sdk_mediaconvert.types.burnin_destination_settings.deserialize_json(
                data["burninDestinationSettings"]
            )
        )
    if "destinationType" in data:
        import aws_sdk_mediaconvert.types.caption_destination_type

        out["destination_type"] = (
            aws_sdk_mediaconvert.types.caption_destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if "dvbSubDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.dvb_sub_destination_settings

        out["dvb_sub_destination_settings"] = (
            aws_sdk_mediaconvert.types.dvb_sub_destination_settings.deserialize_json(
                data["dvbSubDestinationSettings"]
            )
        )
    if "embeddedDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.embedded_destination_settings

        out["embedded_destination_settings"] = (
            aws_sdk_mediaconvert.types.embedded_destination_settings.deserialize_json(
                data["embeddedDestinationSettings"]
            )
        )
    if "imscDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.imsc_destination_settings

        out["imsc_destination_settings"] = (
            aws_sdk_mediaconvert.types.imsc_destination_settings.deserialize_json(
                data["imscDestinationSettings"]
            )
        )
    if "sccDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.scc_destination_settings

        out["scc_destination_settings"] = (
            aws_sdk_mediaconvert.types.scc_destination_settings.deserialize_json(
                data["sccDestinationSettings"]
            )
        )
    if "srtDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.srt_destination_settings

        out["srt_destination_settings"] = (
            aws_sdk_mediaconvert.types.srt_destination_settings.deserialize_json(
                data["srtDestinationSettings"]
            )
        )
    if "teletextDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.teletext_destination_settings

        out["teletext_destination_settings"] = (
            aws_sdk_mediaconvert.types.teletext_destination_settings.deserialize_json(
                data["teletextDestinationSettings"]
            )
        )
    if "ttmlDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.ttml_destination_settings

        out["ttml_destination_settings"] = (
            aws_sdk_mediaconvert.types.ttml_destination_settings.deserialize_json(
                data["ttmlDestinationSettings"]
            )
        )
    if "webvttDestinationSettings" in data:
        import aws_sdk_mediaconvert.types.webvtt_destination_settings

        out["webvtt_destination_settings"] = (
            aws_sdk_mediaconvert.types.webvtt_destination_settings.deserialize_json(
                data["webvttDestinationSettings"]
            )
        )
    return out
