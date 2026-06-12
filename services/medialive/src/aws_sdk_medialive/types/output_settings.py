"""Generated from Smithy shape ``com.amazonaws.medialive#OutputSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.archive_output_settings
    import aws_sdk_medialive.types.cmaf_ingest_output_settings
    import aws_sdk_medialive.types.frame_capture_output_settings
    import aws_sdk_medialive.types.hls_output_settings
    import aws_sdk_medialive.types.media_connect_router_output_settings
    import aws_sdk_medialive.types.media_package_output_settings
    import aws_sdk_medialive.types.ms_smooth_output_settings
    import aws_sdk_medialive.types.multiplex_output_settings
    import aws_sdk_medialive.types.rtmp_output_settings
    import aws_sdk_medialive.types.srt_output_settings
    import aws_sdk_medialive.types.udp_output_settings


class OutputSettings(TypedDict):
    archive_output_settings: NotRequired[
        "aws_sdk_medialive.types.archive_output_settings.ArchiveOutputSettings"
    ]
    frame_capture_output_settings: NotRequired[
        "aws_sdk_medialive.types.frame_capture_output_settings.FrameCaptureOutputSettings"
    ]
    hls_output_settings: NotRequired[
        "aws_sdk_medialive.types.hls_output_settings.HlsOutputSettings"
    ]
    media_package_output_settings: NotRequired[
        "aws_sdk_medialive.types.media_package_output_settings.MediaPackageOutputSettings"
    ]
    ms_smooth_output_settings: NotRequired[
        "aws_sdk_medialive.types.ms_smooth_output_settings.MsSmoothOutputSettings"
    ]
    multiplex_output_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_output_settings.MultiplexOutputSettings"
    ]
    rtmp_output_settings: NotRequired[
        "aws_sdk_medialive.types.rtmp_output_settings.RtmpOutputSettings"
    ]
    udp_output_settings: NotRequired[
        "aws_sdk_medialive.types.udp_output_settings.UdpOutputSettings"
    ]
    cmaf_ingest_output_settings: NotRequired[
        "aws_sdk_medialive.types.cmaf_ingest_output_settings.CmafIngestOutputSettings"
    ]
    srt_output_settings: NotRequired[
        "aws_sdk_medialive.types.srt_output_settings.SrtOutputSettings"
    ]
    media_connect_router_output_settings: NotRequired[
        "aws_sdk_medialive.types.media_connect_router_output_settings.MediaConnectRouterOutputSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OutputSettings) -> dict:
    out: dict = {}
    if "archive_output_settings" in value:
        import aws_sdk_medialive.types.archive_output_settings

        out["archiveOutputSettings"] = (
            aws_sdk_medialive.types.archive_output_settings.serialize_json(
                value["archive_output_settings"]
            )
        )
    if "frame_capture_output_settings" in value:
        import aws_sdk_medialive.types.frame_capture_output_settings

        out["frameCaptureOutputSettings"] = (
            aws_sdk_medialive.types.frame_capture_output_settings.serialize_json(
                value["frame_capture_output_settings"]
            )
        )
    if "hls_output_settings" in value:
        import aws_sdk_medialive.types.hls_output_settings

        out["hlsOutputSettings"] = (
            aws_sdk_medialive.types.hls_output_settings.serialize_json(
                value["hls_output_settings"]
            )
        )
    if "media_package_output_settings" in value:
        import aws_sdk_medialive.types.media_package_output_settings

        out["mediaPackageOutputSettings"] = (
            aws_sdk_medialive.types.media_package_output_settings.serialize_json(
                value["media_package_output_settings"]
            )
        )
    if "ms_smooth_output_settings" in value:
        import aws_sdk_medialive.types.ms_smooth_output_settings

        out["msSmoothOutputSettings"] = (
            aws_sdk_medialive.types.ms_smooth_output_settings.serialize_json(
                value["ms_smooth_output_settings"]
            )
        )
    if "multiplex_output_settings" in value:
        import aws_sdk_medialive.types.multiplex_output_settings

        out["multiplexOutputSettings"] = (
            aws_sdk_medialive.types.multiplex_output_settings.serialize_json(
                value["multiplex_output_settings"]
            )
        )
    if "rtmp_output_settings" in value:
        import aws_sdk_medialive.types.rtmp_output_settings

        out["rtmpOutputSettings"] = (
            aws_sdk_medialive.types.rtmp_output_settings.serialize_json(
                value["rtmp_output_settings"]
            )
        )
    if "udp_output_settings" in value:
        import aws_sdk_medialive.types.udp_output_settings

        out["udpOutputSettings"] = (
            aws_sdk_medialive.types.udp_output_settings.serialize_json(
                value["udp_output_settings"]
            )
        )
    if "cmaf_ingest_output_settings" in value:
        import aws_sdk_medialive.types.cmaf_ingest_output_settings

        out["cmafIngestOutputSettings"] = (
            aws_sdk_medialive.types.cmaf_ingest_output_settings.serialize_json(
                value["cmaf_ingest_output_settings"]
            )
        )
    if "srt_output_settings" in value:
        import aws_sdk_medialive.types.srt_output_settings

        out["srtOutputSettings"] = (
            aws_sdk_medialive.types.srt_output_settings.serialize_json(
                value["srt_output_settings"]
            )
        )
    if "media_connect_router_output_settings" in value:
        import aws_sdk_medialive.types.media_connect_router_output_settings

        out["mediaConnectRouterOutputSettings"] = (
            aws_sdk_medialive.types.media_connect_router_output_settings.serialize_json(
                value["media_connect_router_output_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputSettings:
    out: OutputSettings = {}  # type: ignore[typeddict-item]
    if "archiveOutputSettings" in data:
        import aws_sdk_medialive.types.archive_output_settings

        out["archive_output_settings"] = (
            aws_sdk_medialive.types.archive_output_settings.deserialize_json(
                data["archiveOutputSettings"]
            )
        )
    if "frameCaptureOutputSettings" in data:
        import aws_sdk_medialive.types.frame_capture_output_settings

        out["frame_capture_output_settings"] = (
            aws_sdk_medialive.types.frame_capture_output_settings.deserialize_json(
                data["frameCaptureOutputSettings"]
            )
        )
    if "hlsOutputSettings" in data:
        import aws_sdk_medialive.types.hls_output_settings

        out["hls_output_settings"] = (
            aws_sdk_medialive.types.hls_output_settings.deserialize_json(
                data["hlsOutputSettings"]
            )
        )
    if "mediaPackageOutputSettings" in data:
        import aws_sdk_medialive.types.media_package_output_settings

        out["media_package_output_settings"] = (
            aws_sdk_medialive.types.media_package_output_settings.deserialize_json(
                data["mediaPackageOutputSettings"]
            )
        )
    if "msSmoothOutputSettings" in data:
        import aws_sdk_medialive.types.ms_smooth_output_settings

        out["ms_smooth_output_settings"] = (
            aws_sdk_medialive.types.ms_smooth_output_settings.deserialize_json(
                data["msSmoothOutputSettings"]
            )
        )
    if "multiplexOutputSettings" in data:
        import aws_sdk_medialive.types.multiplex_output_settings

        out["multiplex_output_settings"] = (
            aws_sdk_medialive.types.multiplex_output_settings.deserialize_json(
                data["multiplexOutputSettings"]
            )
        )
    if "rtmpOutputSettings" in data:
        import aws_sdk_medialive.types.rtmp_output_settings

        out["rtmp_output_settings"] = (
            aws_sdk_medialive.types.rtmp_output_settings.deserialize_json(
                data["rtmpOutputSettings"]
            )
        )
    if "udpOutputSettings" in data:
        import aws_sdk_medialive.types.udp_output_settings

        out["udp_output_settings"] = (
            aws_sdk_medialive.types.udp_output_settings.deserialize_json(
                data["udpOutputSettings"]
            )
        )
    if "cmafIngestOutputSettings" in data:
        import aws_sdk_medialive.types.cmaf_ingest_output_settings

        out["cmaf_ingest_output_settings"] = (
            aws_sdk_medialive.types.cmaf_ingest_output_settings.deserialize_json(
                data["cmafIngestOutputSettings"]
            )
        )
    if "srtOutputSettings" in data:
        import aws_sdk_medialive.types.srt_output_settings

        out["srt_output_settings"] = (
            aws_sdk_medialive.types.srt_output_settings.deserialize_json(
                data["srtOutputSettings"]
            )
        )
    if "mediaConnectRouterOutputSettings" in data:
        import aws_sdk_medialive.types.media_connect_router_output_settings

        out["media_connect_router_output_settings"] = (
            aws_sdk_medialive.types.media_connect_router_output_settings.deserialize_json(
                data["mediaConnectRouterOutputSettings"]
            )
        )
    return out
