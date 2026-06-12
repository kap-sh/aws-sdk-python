"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ContainerSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.cmfc_settings
    import aws_sdk_mediaconvert.types.container_type
    import aws_sdk_mediaconvert.types.f4v_settings
    import aws_sdk_mediaconvert.types.m2ts_settings
    import aws_sdk_mediaconvert.types.m3u8_settings
    import aws_sdk_mediaconvert.types.mov_settings
    import aws_sdk_mediaconvert.types.mp4_settings
    import aws_sdk_mediaconvert.types.mpd_settings
    import aws_sdk_mediaconvert.types.mxf_settings


class ContainerSettings(TypedDict):
    cmfc_settings: NotRequired["aws_sdk_mediaconvert.types.cmfc_settings.CmfcSettings"]
    """These settings relate to the fragmented MP4 container for the segments in your CMAF outputs."""
    container: NotRequired["aws_sdk_mediaconvert.types.container_type.ContainerType"]
    """Container for this output. Some containers require a container settings object. If not specified, the default object will be created."""
    f4v_settings: NotRequired["aws_sdk_mediaconvert.types.f4v_settings.F4vSettings"]
    """Settings for F4v container"""
    m2ts_settings: NotRequired["aws_sdk_mediaconvert.types.m2ts_settings.M2tsSettings"]
    """MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset."""
    m3u8_settings: NotRequired["aws_sdk_mediaconvert.types.m3u8_settings.M3u8Settings"]
    """These settings relate to the MPEG-2 transport stream (MPEG2-TS) container for the MPEG2-TS segments in your HLS outputs."""
    mov_settings: NotRequired["aws_sdk_mediaconvert.types.mov_settings.MovSettings"]
    """These settings relate to your QuickTime MOV output container."""
    mp4_settings: NotRequired["aws_sdk_mediaconvert.types.mp4_settings.Mp4Settings"]
    """These settings relate to your MP4 output container. You can create audio only outputs with this container. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/supported-codecs-containers-audio-only.html#output-codecs-and-containers-supported-for-audio-only."""
    mpd_settings: NotRequired["aws_sdk_mediaconvert.types.mpd_settings.MpdSettings"]
    """These settings relate to the fragmented MP4 container for the segments in your DASH outputs."""
    mxf_settings: NotRequired["aws_sdk_mediaconvert.types.mxf_settings.MxfSettings"]
    """These settings relate to your MXF output container."""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerSettings) -> dict:
    out: dict = {}
    if "cmfc_settings" in value:
        import aws_sdk_mediaconvert.types.cmfc_settings

        out["cmfcSettings"] = aws_sdk_mediaconvert.types.cmfc_settings.serialize_json(
            value["cmfc_settings"]
        )
    if "container" in value:
        import aws_sdk_mediaconvert.types.container_type

        out["container"] = aws_sdk_mediaconvert.types.container_type.serialize_json(
            value["container"]
        )
    if "f4v_settings" in value:
        import aws_sdk_mediaconvert.types.f4v_settings

        out["f4vSettings"] = aws_sdk_mediaconvert.types.f4v_settings.serialize_json(
            value["f4v_settings"]
        )
    if "m2ts_settings" in value:
        import aws_sdk_mediaconvert.types.m2ts_settings

        out["m2tsSettings"] = aws_sdk_mediaconvert.types.m2ts_settings.serialize_json(
            value["m2ts_settings"]
        )
    if "m3u8_settings" in value:
        import aws_sdk_mediaconvert.types.m3u8_settings

        out["m3u8Settings"] = aws_sdk_mediaconvert.types.m3u8_settings.serialize_json(
            value["m3u8_settings"]
        )
    if "mov_settings" in value:
        import aws_sdk_mediaconvert.types.mov_settings

        out["movSettings"] = aws_sdk_mediaconvert.types.mov_settings.serialize_json(
            value["mov_settings"]
        )
    if "mp4_settings" in value:
        import aws_sdk_mediaconvert.types.mp4_settings

        out["mp4Settings"] = aws_sdk_mediaconvert.types.mp4_settings.serialize_json(
            value["mp4_settings"]
        )
    if "mpd_settings" in value:
        import aws_sdk_mediaconvert.types.mpd_settings

        out["mpdSettings"] = aws_sdk_mediaconvert.types.mpd_settings.serialize_json(
            value["mpd_settings"]
        )
    if "mxf_settings" in value:
        import aws_sdk_mediaconvert.types.mxf_settings

        out["mxfSettings"] = aws_sdk_mediaconvert.types.mxf_settings.serialize_json(
            value["mxf_settings"]
        )
    return out


def deserialize_json(data: dict) -> ContainerSettings:
    out: ContainerSettings = {}  # type: ignore[typeddict-item]
    if "cmfcSettings" in data:
        import aws_sdk_mediaconvert.types.cmfc_settings

        out["cmfc_settings"] = (
            aws_sdk_mediaconvert.types.cmfc_settings.deserialize_json(
                data["cmfcSettings"]
            )
        )
    if "container" in data:
        import aws_sdk_mediaconvert.types.container_type

        out["container"] = aws_sdk_mediaconvert.types.container_type.deserialize_json(
            data["container"]
        )
    if "f4vSettings" in data:
        import aws_sdk_mediaconvert.types.f4v_settings

        out["f4v_settings"] = aws_sdk_mediaconvert.types.f4v_settings.deserialize_json(
            data["f4vSettings"]
        )
    if "m2tsSettings" in data:
        import aws_sdk_mediaconvert.types.m2ts_settings

        out["m2ts_settings"] = (
            aws_sdk_mediaconvert.types.m2ts_settings.deserialize_json(
                data["m2tsSettings"]
            )
        )
    if "m3u8Settings" in data:
        import aws_sdk_mediaconvert.types.m3u8_settings

        out["m3u8_settings"] = (
            aws_sdk_mediaconvert.types.m3u8_settings.deserialize_json(
                data["m3u8Settings"]
            )
        )
    if "movSettings" in data:
        import aws_sdk_mediaconvert.types.mov_settings

        out["mov_settings"] = aws_sdk_mediaconvert.types.mov_settings.deserialize_json(
            data["movSettings"]
        )
    if "mp4Settings" in data:
        import aws_sdk_mediaconvert.types.mp4_settings

        out["mp4_settings"] = aws_sdk_mediaconvert.types.mp4_settings.deserialize_json(
            data["mp4Settings"]
        )
    if "mpdSettings" in data:
        import aws_sdk_mediaconvert.types.mpd_settings

        out["mpd_settings"] = aws_sdk_mediaconvert.types.mpd_settings.deserialize_json(
            data["mpdSettings"]
        )
    if "mxfSettings" in data:
        import aws_sdk_mediaconvert.types.mxf_settings

        out["mxf_settings"] = aws_sdk_mediaconvert.types.mxf_settings.deserialize_json(
            data["mxfSettings"]
        )
    return out
