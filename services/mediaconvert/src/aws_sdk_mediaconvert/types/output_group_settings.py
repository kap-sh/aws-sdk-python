"""Generated from Smithy shape ``com.amazonaws.mediaconvert#OutputGroupSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_frame_metric_type
    import aws_sdk_mediaconvert.types.cmaf_group_settings
    import aws_sdk_mediaconvert.types.dash_iso_group_settings
    import aws_sdk_mediaconvert.types.file_group_settings
    import aws_sdk_mediaconvert.types.hls_group_settings
    import aws_sdk_mediaconvert.types.ms_smooth_group_settings
    import aws_sdk_mediaconvert.types.output_group_type


class OutputGroupSettings(TypedDict):
    cmaf_group_settings: NotRequired[
        "aws_sdk_mediaconvert.types.cmaf_group_settings.CmafGroupSettings"
    ]
    """Settings related to your CMAF output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html."""
    dash_iso_group_settings: NotRequired[
        "aws_sdk_mediaconvert.types.dash_iso_group_settings.DashIsoGroupSettings"
    ]
    """Settings related to your DASH output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html."""
    file_group_settings: NotRequired[
        "aws_sdk_mediaconvert.types.file_group_settings.FileGroupSettings"
    ]
    """Settings related to your File output group. MediaConvert uses this group of settings to generate a single standalone file, rather than a streaming package."""
    hls_group_settings: NotRequired[
        "aws_sdk_mediaconvert.types.hls_group_settings.HlsGroupSettings"
    ]
    """Settings related to your HLS output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html."""
    ms_smooth_group_settings: NotRequired[
        "aws_sdk_mediaconvert.types.ms_smooth_group_settings.MsSmoothGroupSettings"
    ]
    """Settings related to your Microsoft Smooth Streaming output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html."""
    per_frame_metrics: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_frame_metric_type.__listOfFrameMetricType"
    ]
    """Optionally choose one or more per frame metric reports to generate along with your output. You can use these metrics to analyze your video output according to one or more commonly used image quality metrics. You can specify per frame metrics for output groups or for individual outputs. When you do, MediaConvert writes a CSV (Comma-Separated Values) file to your S3 output destination, named after the output name and metric type. For example: videofile_PSNR.csv Jobs that generate per frame metrics will take longer to complete, depending on the resolution and complexity of your output. For example, some 4K jobs might take up to twice as long to complete. Note that when analyzing the video quality of your output, or when comparing the video quality of multiple different outputs, we generally also recommend a detailed visual review in a controlled environment. You can choose from the following per frame metrics: * PSNR: Peak Signal-to-Noise Ratio * SSIM: Structural Similarity Index Measure * MS_SSIM: Multi-Scale Similarity Index Measure * PSNR_HVS: Peak Signal-to-Noise Ratio, Human Visual System * VMAF: Video Multi-Method Assessment Fusion * QVBR: Quality-Defined Variable Bitrate. This option is only available when your output uses the QVBR rate control mode. * SHOT_CHANGE: Shot Changes"""
    type: NotRequired["aws_sdk_mediaconvert.types.output_group_type.OutputGroupType"]
    """Type of output group (File group, Apple HLS, DASH ISO, Microsoft Smooth Streaming, CMAF)"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputGroupSettings) -> dict:
    out: dict = {}
    if "cmaf_group_settings" in value:
        import aws_sdk_mediaconvert.types.cmaf_group_settings

        out["cmafGroupSettings"] = (
            aws_sdk_mediaconvert.types.cmaf_group_settings.serialize_json(
                value["cmaf_group_settings"]
            )
        )
    if "dash_iso_group_settings" in value:
        import aws_sdk_mediaconvert.types.dash_iso_group_settings

        out["dashIsoGroupSettings"] = (
            aws_sdk_mediaconvert.types.dash_iso_group_settings.serialize_json(
                value["dash_iso_group_settings"]
            )
        )
    if "file_group_settings" in value:
        import aws_sdk_mediaconvert.types.file_group_settings

        out["fileGroupSettings"] = (
            aws_sdk_mediaconvert.types.file_group_settings.serialize_json(
                value["file_group_settings"]
            )
        )
    if "hls_group_settings" in value:
        import aws_sdk_mediaconvert.types.hls_group_settings

        out["hlsGroupSettings"] = (
            aws_sdk_mediaconvert.types.hls_group_settings.serialize_json(
                value["hls_group_settings"]
            )
        )
    if "ms_smooth_group_settings" in value:
        import aws_sdk_mediaconvert.types.ms_smooth_group_settings

        out["msSmoothGroupSettings"] = (
            aws_sdk_mediaconvert.types.ms_smooth_group_settings.serialize_json(
                value["ms_smooth_group_settings"]
            )
        )
    if "per_frame_metrics" in value:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["perFrameMetrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.serialize_json(
                value["per_frame_metrics"]
            )
        )
    if "type" in value:
        import aws_sdk_mediaconvert.types.output_group_type

        out["type"] = aws_sdk_mediaconvert.types.output_group_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> OutputGroupSettings:
    out: OutputGroupSettings = {}  # type: ignore[typeddict-item]
    if "cmafGroupSettings" in data:
        import aws_sdk_mediaconvert.types.cmaf_group_settings

        out["cmaf_group_settings"] = (
            aws_sdk_mediaconvert.types.cmaf_group_settings.deserialize_json(
                data["cmafGroupSettings"]
            )
        )
    if "dashIsoGroupSettings" in data:
        import aws_sdk_mediaconvert.types.dash_iso_group_settings

        out["dash_iso_group_settings"] = (
            aws_sdk_mediaconvert.types.dash_iso_group_settings.deserialize_json(
                data["dashIsoGroupSettings"]
            )
        )
    if "fileGroupSettings" in data:
        import aws_sdk_mediaconvert.types.file_group_settings

        out["file_group_settings"] = (
            aws_sdk_mediaconvert.types.file_group_settings.deserialize_json(
                data["fileGroupSettings"]
            )
        )
    if "hlsGroupSettings" in data:
        import aws_sdk_mediaconvert.types.hls_group_settings

        out["hls_group_settings"] = (
            aws_sdk_mediaconvert.types.hls_group_settings.deserialize_json(
                data["hlsGroupSettings"]
            )
        )
    if "msSmoothGroupSettings" in data:
        import aws_sdk_mediaconvert.types.ms_smooth_group_settings

        out["ms_smooth_group_settings"] = (
            aws_sdk_mediaconvert.types.ms_smooth_group_settings.deserialize_json(
                data["msSmoothGroupSettings"]
            )
        )
    if "perFrameMetrics" in data:
        import aws_sdk_mediaconvert.types.__list_of_frame_metric_type

        out["per_frame_metrics"] = (
            aws_sdk_mediaconvert.types.__list_of_frame_metric_type.deserialize_json(
                data["perFrameMetrics"]
            )
        )
    if "type" in data:
        import aws_sdk_mediaconvert.types.output_group_type

        out["type"] = aws_sdk_mediaconvert.types.output_group_type.deserialize_json(
            data["type"]
        )
    return out
