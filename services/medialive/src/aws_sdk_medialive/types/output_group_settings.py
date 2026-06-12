"""Generated from Smithy shape ``com.amazonaws.medialive#OutputGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.archive_group_settings
    import aws_sdk_medialive.types.cmaf_ingest_group_settings
    import aws_sdk_medialive.types.frame_capture_group_settings
    import aws_sdk_medialive.types.hls_group_settings
    import aws_sdk_medialive.types.media_connect_router_group_settings
    import aws_sdk_medialive.types.media_package_group_settings
    import aws_sdk_medialive.types.ms_smooth_group_settings
    import aws_sdk_medialive.types.multiplex_group_settings
    import aws_sdk_medialive.types.rtmp_group_settings
    import aws_sdk_medialive.types.srt_group_settings
    import aws_sdk_medialive.types.udp_group_settings


class OutputGroupSettings(TypedDict):
    archive_group_settings: NotRequired[
        "aws_sdk_medialive.types.archive_group_settings.ArchiveGroupSettings"
    ]
    frame_capture_group_settings: NotRequired[
        "aws_sdk_medialive.types.frame_capture_group_settings.FrameCaptureGroupSettings"
    ]
    hls_group_settings: NotRequired[
        "aws_sdk_medialive.types.hls_group_settings.HlsGroupSettings"
    ]
    media_package_group_settings: NotRequired[
        "aws_sdk_medialive.types.media_package_group_settings.MediaPackageGroupSettings"
    ]
    ms_smooth_group_settings: NotRequired[
        "aws_sdk_medialive.types.ms_smooth_group_settings.MsSmoothGroupSettings"
    ]
    multiplex_group_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_group_settings.MultiplexGroupSettings"
    ]
    rtmp_group_settings: NotRequired[
        "aws_sdk_medialive.types.rtmp_group_settings.RtmpGroupSettings"
    ]
    udp_group_settings: NotRequired[
        "aws_sdk_medialive.types.udp_group_settings.UdpGroupSettings"
    ]
    cmaf_ingest_group_settings: NotRequired[
        "aws_sdk_medialive.types.cmaf_ingest_group_settings.CmafIngestGroupSettings"
    ]
    srt_group_settings: NotRequired[
        "aws_sdk_medialive.types.srt_group_settings.SrtGroupSettings"
    ]
    media_connect_router_group_settings: NotRequired[
        "aws_sdk_medialive.types.media_connect_router_group_settings.MediaConnectRouterGroupSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroupSettings) -> dict:
    out: dict = {}
    if "archive_group_settings" in value:
        import aws_sdk_medialive.types.archive_group_settings

        out["archiveGroupSettings"] = (
            aws_sdk_medialive.types.archive_group_settings.serialize_json(
                value["archive_group_settings"]
            )
        )
    if "frame_capture_group_settings" in value:
        import aws_sdk_medialive.types.frame_capture_group_settings

        out["frameCaptureGroupSettings"] = (
            aws_sdk_medialive.types.frame_capture_group_settings.serialize_json(
                value["frame_capture_group_settings"]
            )
        )
    if "hls_group_settings" in value:
        import aws_sdk_medialive.types.hls_group_settings

        out["hlsGroupSettings"] = (
            aws_sdk_medialive.types.hls_group_settings.serialize_json(
                value["hls_group_settings"]
            )
        )
    if "media_package_group_settings" in value:
        import aws_sdk_medialive.types.media_package_group_settings

        out["mediaPackageGroupSettings"] = (
            aws_sdk_medialive.types.media_package_group_settings.serialize_json(
                value["media_package_group_settings"]
            )
        )
    if "ms_smooth_group_settings" in value:
        import aws_sdk_medialive.types.ms_smooth_group_settings

        out["msSmoothGroupSettings"] = (
            aws_sdk_medialive.types.ms_smooth_group_settings.serialize_json(
                value["ms_smooth_group_settings"]
            )
        )
    if "multiplex_group_settings" in value:
        import aws_sdk_medialive.types.multiplex_group_settings

        out["multiplexGroupSettings"] = (
            aws_sdk_medialive.types.multiplex_group_settings.serialize_json(
                value["multiplex_group_settings"]
            )
        )
    if "rtmp_group_settings" in value:
        import aws_sdk_medialive.types.rtmp_group_settings

        out["rtmpGroupSettings"] = (
            aws_sdk_medialive.types.rtmp_group_settings.serialize_json(
                value["rtmp_group_settings"]
            )
        )
    if "udp_group_settings" in value:
        import aws_sdk_medialive.types.udp_group_settings

        out["udpGroupSettings"] = (
            aws_sdk_medialive.types.udp_group_settings.serialize_json(
                value["udp_group_settings"]
            )
        )
    if "cmaf_ingest_group_settings" in value:
        import aws_sdk_medialive.types.cmaf_ingest_group_settings

        out["cmafIngestGroupSettings"] = (
            aws_sdk_medialive.types.cmaf_ingest_group_settings.serialize_json(
                value["cmaf_ingest_group_settings"]
            )
        )
    if "srt_group_settings" in value:
        import aws_sdk_medialive.types.srt_group_settings

        out["srtGroupSettings"] = (
            aws_sdk_medialive.types.srt_group_settings.serialize_json(
                value["srt_group_settings"]
            )
        )
    if "media_connect_router_group_settings" in value:
        import aws_sdk_medialive.types.media_connect_router_group_settings

        out["mediaConnectRouterGroupSettings"] = (
            aws_sdk_medialive.types.media_connect_router_group_settings.serialize_json(
                value["media_connect_router_group_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputGroupSettings:
    out: OutputGroupSettings = {}  # type: ignore[typeddict-item]
    if "archiveGroupSettings" in data:
        import aws_sdk_medialive.types.archive_group_settings

        out["archive_group_settings"] = (
            aws_sdk_medialive.types.archive_group_settings.deserialize_json(
                data["archiveGroupSettings"]
            )
        )
    if "frameCaptureGroupSettings" in data:
        import aws_sdk_medialive.types.frame_capture_group_settings

        out["frame_capture_group_settings"] = (
            aws_sdk_medialive.types.frame_capture_group_settings.deserialize_json(
                data["frameCaptureGroupSettings"]
            )
        )
    if "hlsGroupSettings" in data:
        import aws_sdk_medialive.types.hls_group_settings

        out["hls_group_settings"] = (
            aws_sdk_medialive.types.hls_group_settings.deserialize_json(
                data["hlsGroupSettings"]
            )
        )
    if "mediaPackageGroupSettings" in data:
        import aws_sdk_medialive.types.media_package_group_settings

        out["media_package_group_settings"] = (
            aws_sdk_medialive.types.media_package_group_settings.deserialize_json(
                data["mediaPackageGroupSettings"]
            )
        )
    if "msSmoothGroupSettings" in data:
        import aws_sdk_medialive.types.ms_smooth_group_settings

        out["ms_smooth_group_settings"] = (
            aws_sdk_medialive.types.ms_smooth_group_settings.deserialize_json(
                data["msSmoothGroupSettings"]
            )
        )
    if "multiplexGroupSettings" in data:
        import aws_sdk_medialive.types.multiplex_group_settings

        out["multiplex_group_settings"] = (
            aws_sdk_medialive.types.multiplex_group_settings.deserialize_json(
                data["multiplexGroupSettings"]
            )
        )
    if "rtmpGroupSettings" in data:
        import aws_sdk_medialive.types.rtmp_group_settings

        out["rtmp_group_settings"] = (
            aws_sdk_medialive.types.rtmp_group_settings.deserialize_json(
                data["rtmpGroupSettings"]
            )
        )
    if "udpGroupSettings" in data:
        import aws_sdk_medialive.types.udp_group_settings

        out["udp_group_settings"] = (
            aws_sdk_medialive.types.udp_group_settings.deserialize_json(
                data["udpGroupSettings"]
            )
        )
    if "cmafIngestGroupSettings" in data:
        import aws_sdk_medialive.types.cmaf_ingest_group_settings

        out["cmaf_ingest_group_settings"] = (
            aws_sdk_medialive.types.cmaf_ingest_group_settings.deserialize_json(
                data["cmafIngestGroupSettings"]
            )
        )
    if "srtGroupSettings" in data:
        import aws_sdk_medialive.types.srt_group_settings

        out["srt_group_settings"] = (
            aws_sdk_medialive.types.srt_group_settings.deserialize_json(
                data["srtGroupSettings"]
            )
        )
    if "mediaConnectRouterGroupSettings" in data:
        import aws_sdk_medialive.types.media_connect_router_group_settings

        out["media_connect_router_group_settings"] = (
            aws_sdk_medialive.types.media_connect_router_group_settings.deserialize_json(
                data["mediaConnectRouterGroupSettings"]
            )
        )
    return out
