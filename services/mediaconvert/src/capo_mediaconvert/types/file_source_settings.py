"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FileSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import capo_mediaconvert.types.__string_min14_pattern_s3_scc_scc_ttml_ttml_dfxp_dfxp_stl_stl_srt_srt_xml_xml_smi_smi_vtt_vtt_webvtt_webvtt_https_scc_scc_ttml_ttml_dfxp_dfxp_stl_stl_srt_srt_xml_xml_smi_smi_vtt_vtt_webvtt_webvtt
    import capo_mediaconvert.types.caption_source_byte_rate_limit
    import capo_mediaconvert.types.caption_source_convert_paint_on_to_pop_on
    import capo_mediaconvert.types.caption_source_framerate
    import capo_mediaconvert.types.caption_source_upconvert_stl_to_teletext
    import capo_mediaconvert.types.file_source_convert608_to708
    import capo_mediaconvert.types.file_source_time_delta_units


class FileSourceSettings(TypedDict, closed=True):
    byte_rate_limit: NotRequired[
        "capo_mediaconvert.types.caption_source_byte_rate_limit.CaptionSourceByteRateLimit"
    ]
    """Choose whether to limit the byte rate at which your SCC input captions are inserted into your output. To not limit the caption rate: We recommend that you keep the default value, Disabled. MediaConvert inserts captions in your output according to the byte rates listed in the EIA-608 specification, typically 2 or 3 caption bytes per frame depending on your output frame rate. To limit your output caption rate: Choose Enabled. Choose this option if your downstream systems require a maximum of 2 caption bytes per frame. Note that this setting has no effect when your output frame rate is 30 or 60."""
    convert608_to708: NotRequired[
        "capo_mediaconvert.types.file_source_convert608_to708.FileSourceConvert608To708"
    ]
    """Specify whether this set of input captions appears in your outputs in both 608 and 708 format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the 608 data through using the 608 compatibility bytes fields of the 708 wrapper, and it also translates the 608 data into 708."""
    convert_paint_to_pop: NotRequired[
        "capo_mediaconvert.types.caption_source_convert_paint_on_to_pop_on.CaptionSourceConvertPaintOnToPopOn"
    ]
    """Choose the presentation style of your input SCC captions. To use the same presentation style as your input: Keep the default value, Disabled. To convert paint-on captions to pop-on: Choose Enabled. We also recommend that you choose Enabled if you notice additional repeated lines in your output captions."""
    framerate: NotRequired[
        "capo_mediaconvert.types.caption_source_framerate.CaptionSourceFramerate"
    ]
    """Ignore this setting unless your input captions format is SCC. To have the service compensate for differing frame rates between your input captions and input video, specify the frame rate of the captions file. Specify this value as a fraction. For example, you might specify 24 / 1 for 24 fps, 25 / 1 for 25 fps, 24000 / 1001 for 23.976 fps, or 30000 / 1001 for 29.97 fps."""
    source_file: NotRequired[
        "capo_mediaconvert.types.__string_min14_pattern_s3_scc_scc_ttml_ttml_dfxp_dfxp_stl_stl_srt_srt_xml_xml_smi_smi_vtt_vtt_webvtt_webvtt_https_scc_scc_ttml_ttml_dfxp_dfxp_stl_stl_srt_srt_xml_xml_smi_smi_vtt_vtt_webvtt_webvtt.__stringMin14PatternS3SccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTTHttpsSccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTT"
    ]
    """External caption file used for loading captions. Accepted file extensions are 'scc', 'ttml', 'dfxp', 'stl', 'srt', 'xml', 'smi', 'webvtt', and 'vtt'."""
    time_delta: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Optional. Use this setting when you need to adjust the sync between your sidecar captions and your video. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/time-delta-use-cases.html. Enter a positive or negative number to modify the times in the captions file. For example, type 15 to add 15 seconds to all the times in the captions file. Type -5 to subtract 5 seconds from the times in the captions file. You can optionally specify your time delta in milliseconds instead of seconds. When you do so, set the related setting, Time delta units to Milliseconds. Note that, when you specify a time delta for timecode-based caption sources, such as SCC and STL, and your time delta isn't a multiple of the input frame rate, MediaConvert snaps the captions to the nearest frame. For example, when your input video frame rate is 25 fps and you specify 1010ms for time delta, MediaConvert delays your captions by 1000 ms."""
    time_delta_units: NotRequired[
        "capo_mediaconvert.types.file_source_time_delta_units.FileSourceTimeDeltaUnits"
    ]
    """When you use the setting Time delta to adjust the sync between your sidecar captions and your video, use this setting to specify the units for the delta that you specify. When you don't specify a value for Time delta units, MediaConvert uses seconds by default."""
    upconvert_stl_to_teletext: NotRequired[
        "capo_mediaconvert.types.caption_source_upconvert_stl_to_teletext.CaptionSourceUpconvertSTLToTeletext"
    ]
    """Specify whether this set of input captions appears in your outputs in both STL and Teletext format. If you choose Upconvert, MediaConvert includes the captions data in two ways: it passes the STL data through using the Teletext compatibility bytes fields of the Teletext wrapper, and it also translates the STL data into Teletext."""


# --- restJson1 ser/de ---
def serialize_json(value: FileSourceSettings) -> dict:
    out: dict = {}
    if "byte_rate_limit" in value:
        import capo_mediaconvert.types.caption_source_byte_rate_limit

        out["byteRateLimit"] = (
            capo_mediaconvert.types.caption_source_byte_rate_limit.serialize_json(
                value["byte_rate_limit"]
            )
        )
    if "convert608_to708" in value:
        import capo_mediaconvert.types.file_source_convert608_to708

        out["convert608To708"] = (
            capo_mediaconvert.types.file_source_convert608_to708.serialize_json(
                value["convert608_to708"]
            )
        )
    if "convert_paint_to_pop" in value:
        import capo_mediaconvert.types.caption_source_convert_paint_on_to_pop_on

        out["convertPaintToPop"] = (
            capo_mediaconvert.types.caption_source_convert_paint_on_to_pop_on.serialize_json(
                value["convert_paint_to_pop"]
            )
        )
    if "framerate" in value:
        import capo_mediaconvert.types.caption_source_framerate

        out["framerate"] = (
            capo_mediaconvert.types.caption_source_framerate.serialize_json(
                value["framerate"]
            )
        )
    if "source_file" in value:
        out["sourceFile"] = value["source_file"]
    if "time_delta" in value:
        out["timeDelta"] = value["time_delta"]
    if "time_delta_units" in value:
        import capo_mediaconvert.types.file_source_time_delta_units

        out["timeDeltaUnits"] = (
            capo_mediaconvert.types.file_source_time_delta_units.serialize_json(
                value["time_delta_units"]
            )
        )
    if "upconvert_stl_to_teletext" in value:
        import capo_mediaconvert.types.caption_source_upconvert_stl_to_teletext

        out["upconvertSTLToTeletext"] = (
            capo_mediaconvert.types.caption_source_upconvert_stl_to_teletext.serialize_json(
                value["upconvert_stl_to_teletext"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileSourceSettings:
    out: FileSourceSettings = {}  # type: ignore[typeddict-item]
    if "byteRateLimit" in data:
        import capo_mediaconvert.types.caption_source_byte_rate_limit

        out["byte_rate_limit"] = (
            capo_mediaconvert.types.caption_source_byte_rate_limit.deserialize_json(
                data["byteRateLimit"]
            )
        )
    if "convert608To708" in data:
        import capo_mediaconvert.types.file_source_convert608_to708

        out["convert608_to708"] = (
            capo_mediaconvert.types.file_source_convert608_to708.deserialize_json(
                data["convert608To708"]
            )
        )
    if "convertPaintToPop" in data:
        import capo_mediaconvert.types.caption_source_convert_paint_on_to_pop_on

        out["convert_paint_to_pop"] = (
            capo_mediaconvert.types.caption_source_convert_paint_on_to_pop_on.deserialize_json(
                data["convertPaintToPop"]
            )
        )
    if "framerate" in data:
        import capo_mediaconvert.types.caption_source_framerate

        out["framerate"] = (
            capo_mediaconvert.types.caption_source_framerate.deserialize_json(
                data["framerate"]
            )
        )
    if "sourceFile" in data:
        out["source_file"] = data["sourceFile"]
    if "timeDelta" in data:
        out["time_delta"] = data["timeDelta"]
    if "timeDeltaUnits" in data:
        import capo_mediaconvert.types.file_source_time_delta_units

        out["time_delta_units"] = (
            capo_mediaconvert.types.file_source_time_delta_units.deserialize_json(
                data["timeDeltaUnits"]
            )
        )
    if "upconvertSTLToTeletext" in data:
        import capo_mediaconvert.types.caption_source_upconvert_stl_to_teletext

        out["upconvert_stl_to_teletext"] = (
            capo_mediaconvert.types.caption_source_upconvert_stl_to_teletext.deserialize_json(
                data["upconvertSTLToTeletext"]
            )
        )
    return out
