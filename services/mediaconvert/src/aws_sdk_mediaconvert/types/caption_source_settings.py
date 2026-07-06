"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.ancillary_source_settings
    import aws_sdk_mediaconvert.types.caption_source_type
    import aws_sdk_mediaconvert.types.dvb_sub_source_settings
    import aws_sdk_mediaconvert.types.embedded_source_settings
    import aws_sdk_mediaconvert.types.file_source_settings
    import aws_sdk_mediaconvert.types.teletext_source_settings
    import aws_sdk_mediaconvert.types.track_source_settings
    import aws_sdk_mediaconvert.types.webvtt_hls_source_settings


class CaptionSourceSettings(TypedDict, closed=True):
    ancillary_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.ancillary_source_settings.AncillarySourceSettings"
    ]
    """Settings for ancillary captions source."""
    dvb_sub_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.dvb_sub_source_settings.DvbSubSourceSettings"
    ]
    """DVB Sub Source Settings"""
    embedded_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.embedded_source_settings.EmbeddedSourceSettings"
    ]
    """Settings for embedded captions Source"""
    file_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.file_source_settings.FileSourceSettings"
    ]
    """If your input captions are SCC, SMI, SRT, STL, TTML, WebVTT, or IMSC 1.1 in an xml file, specify the URI of the input caption source file. If your caption source is IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings."""
    source_type: NotRequired[
        "aws_sdk_mediaconvert.types.caption_source_type.CaptionSourceType"
    ]
    """Use Source to identify the format of your input captions. The service cannot auto-detect caption format."""
    teletext_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.teletext_source_settings.TeletextSourceSettings"
    ]
    """Settings specific to Teletext caption sources, including Page number."""
    track_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.track_source_settings.TrackSourceSettings"
    ]
    """Settings specific to caption sources that are specified by track number. Currently, this is only IMSC captions in an IMF package. If your caption source is IMSC 1.1 in a separate xml file, use FileSourceSettings instead of TrackSourceSettings."""
    webvtt_hls_source_settings: NotRequired[
        "aws_sdk_mediaconvert.types.webvtt_hls_source_settings.WebvttHlsSourceSettings"
    ]
    """Settings specific to WebVTT sources in HLS alternative rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique subtitle track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the specified properties, the job fails. If there is only one subtitle track in the rendition group, the settings can be left empty and the default subtitle track will be chosen. If your caption source is a sidecar file, use FileSourceSettings instead of WebvttHlsSourceSettings."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSourceSettings) -> dict:
    out: dict = {}
    if "ancillary_source_settings" in value:
        import aws_sdk_mediaconvert.types.ancillary_source_settings

        out["ancillarySourceSettings"] = (
            aws_sdk_mediaconvert.types.ancillary_source_settings.serialize_json(
                value["ancillary_source_settings"]
            )
        )
    if "dvb_sub_source_settings" in value:
        import aws_sdk_mediaconvert.types.dvb_sub_source_settings

        out["dvbSubSourceSettings"] = (
            aws_sdk_mediaconvert.types.dvb_sub_source_settings.serialize_json(
                value["dvb_sub_source_settings"]
            )
        )
    if "embedded_source_settings" in value:
        import aws_sdk_mediaconvert.types.embedded_source_settings

        out["embeddedSourceSettings"] = (
            aws_sdk_mediaconvert.types.embedded_source_settings.serialize_json(
                value["embedded_source_settings"]
            )
        )
    if "file_source_settings" in value:
        import aws_sdk_mediaconvert.types.file_source_settings

        out["fileSourceSettings"] = (
            aws_sdk_mediaconvert.types.file_source_settings.serialize_json(
                value["file_source_settings"]
            )
        )
    if "source_type" in value:
        import aws_sdk_mediaconvert.types.caption_source_type

        out["sourceType"] = (
            aws_sdk_mediaconvert.types.caption_source_type.serialize_json(
                value["source_type"]
            )
        )
    if "teletext_source_settings" in value:
        import aws_sdk_mediaconvert.types.teletext_source_settings

        out["teletextSourceSettings"] = (
            aws_sdk_mediaconvert.types.teletext_source_settings.serialize_json(
                value["teletext_source_settings"]
            )
        )
    if "track_source_settings" in value:
        import aws_sdk_mediaconvert.types.track_source_settings

        out["trackSourceSettings"] = (
            aws_sdk_mediaconvert.types.track_source_settings.serialize_json(
                value["track_source_settings"]
            )
        )
    if "webvtt_hls_source_settings" in value:
        import aws_sdk_mediaconvert.types.webvtt_hls_source_settings

        out["webvttHlsSourceSettings"] = (
            aws_sdk_mediaconvert.types.webvtt_hls_source_settings.serialize_json(
                value["webvtt_hls_source_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionSourceSettings:
    out: CaptionSourceSettings = {}  # type: ignore[typeddict-item]
    if "ancillarySourceSettings" in data:
        import aws_sdk_mediaconvert.types.ancillary_source_settings

        out["ancillary_source_settings"] = (
            aws_sdk_mediaconvert.types.ancillary_source_settings.deserialize_json(
                data["ancillarySourceSettings"]
            )
        )
    if "dvbSubSourceSettings" in data:
        import aws_sdk_mediaconvert.types.dvb_sub_source_settings

        out["dvb_sub_source_settings"] = (
            aws_sdk_mediaconvert.types.dvb_sub_source_settings.deserialize_json(
                data["dvbSubSourceSettings"]
            )
        )
    if "embeddedSourceSettings" in data:
        import aws_sdk_mediaconvert.types.embedded_source_settings

        out["embedded_source_settings"] = (
            aws_sdk_mediaconvert.types.embedded_source_settings.deserialize_json(
                data["embeddedSourceSettings"]
            )
        )
    if "fileSourceSettings" in data:
        import aws_sdk_mediaconvert.types.file_source_settings

        out["file_source_settings"] = (
            aws_sdk_mediaconvert.types.file_source_settings.deserialize_json(
                data["fileSourceSettings"]
            )
        )
    if "sourceType" in data:
        import aws_sdk_mediaconvert.types.caption_source_type

        out["source_type"] = (
            aws_sdk_mediaconvert.types.caption_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    if "teletextSourceSettings" in data:
        import aws_sdk_mediaconvert.types.teletext_source_settings

        out["teletext_source_settings"] = (
            aws_sdk_mediaconvert.types.teletext_source_settings.deserialize_json(
                data["teletextSourceSettings"]
            )
        )
    if "trackSourceSettings" in data:
        import aws_sdk_mediaconvert.types.track_source_settings

        out["track_source_settings"] = (
            aws_sdk_mediaconvert.types.track_source_settings.deserialize_json(
                data["trackSourceSettings"]
            )
        )
    if "webvttHlsSourceSettings" in data:
        import aws_sdk_mediaconvert.types.webvtt_hls_source_settings

        out["webvtt_hls_source_settings"] = (
            aws_sdk_mediaconvert.types.webvtt_hls_source_settings.deserialize_json(
                data["webvttHlsSourceSettings"]
            )
        )
    return out
