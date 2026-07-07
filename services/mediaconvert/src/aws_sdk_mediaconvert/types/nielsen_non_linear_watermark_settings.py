"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NielsenNonLinearWatermarkSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max65534
    import aws_sdk_mediaconvert.types.__string_min1_max20
    import aws_sdk_mediaconvert.types.__string_min1_max50
    import aws_sdk_mediaconvert.types.__string_pattern0x_a_fa_f0908190908
    import aws_sdk_mediaconvert.types.__string_pattern_https
    import aws_sdk_mediaconvert.types.__string_pattern_s3
    import aws_sdk_mediaconvert.types.nielsen_active_watermark_process_type
    import aws_sdk_mediaconvert.types.nielsen_source_watermark_status_type
    import aws_sdk_mediaconvert.types.nielsen_unique_tic_per_audio_track_type


class NielsenNonLinearWatermarkSettings(TypedDict, closed=True):
    active_watermark_process: NotRequired[
        "aws_sdk_mediaconvert.types.nielsen_active_watermark_process_type.NielsenActiveWatermarkProcessType"
    ]
    """Choose the type of Nielsen watermarks that you want in your outputs. When you choose NAES 2 and NW, you must provide a value for the setting SID. When you choose CBET, you must provide a value for the setting CSID. When you choose NAES 2, NW, and CBET, you must provide values for both of these settings."""
    adi_filename: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Optional. Use this setting when you want the service to include an ADI file in the Nielsen metadata .zip file. To provide an ADI file, store it in Amazon S3 and provide a URL to it here. The URL should be in the following format: S3://bucket/path/ADI-file. For more information about the metadata .zip file, see the setting Metadata destination."""
    asset_id: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min1_max20.__stringMin1Max20"
    ]
    """Use the asset ID that you provide to Nielsen to uniquely identify this asset. Required for all Nielsen non-linear watermarking."""
    asset_name: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min1_max50.__stringMin1Max50"
    ]
    """Use the asset name that you provide to Nielsen for this asset. Required for all Nielsen non-linear watermarking."""
    cbet_source_id: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern0x_a_fa_f0908190908.__stringPattern0xAFaF0908190908"
    ]
    """Use the CSID that Nielsen provides to you. This CBET source ID should be unique to your Nielsen account but common to all of your output assets that have CBET watermarking. Required when you choose a value for the setting Watermark types that includes CBET."""
    episode_id: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min1_max20.__stringMin1Max20"
    ]
    """Optional. If this asset uses an episode ID with Nielsen, provide it here."""
    metadata_destination: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_s3.__stringPatternS3"
    ]
    """Specify the Amazon S3 location where you want MediaConvert to save your Nielsen non-linear metadata .zip file. This Amazon S3 bucket must be in the same Region as the one where you do your MediaConvert transcoding. If you want to include an ADI file in this .zip file, use the setting ADI file to specify it. MediaConvert delivers the Nielsen metadata .zip files only to your metadata destination Amazon S3 bucket. It doesn't deliver the .zip files to Nielsen. You are responsible for delivering the metadata .zip files to Nielsen."""
    source_id: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max65534.__integerMin0Max65534"
    ]
    """Use the SID that Nielsen provides to you. This source ID should be unique to your Nielsen account but common to all of your output assets. Required for all Nielsen non-linear watermarking. This ID should be unique to your Nielsen account but common to all of your output assets. Required for all Nielsen non-linear watermarking."""
    source_watermark_status: NotRequired[
        "aws_sdk_mediaconvert.types.nielsen_source_watermark_status_type.NielsenSourceWatermarkStatusType"
    ]
    """Required. Specify whether your source content already contains Nielsen non-linear watermarks. When you set this value to Watermarked, the service fails the job. Nielsen requires that you add non-linear watermarking to only clean content that doesn't already have non-linear Nielsen watermarks."""
    tic_server_url: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_https.__stringPatternHttps"
    ]
    """Specify the endpoint for the TIC server that you have deployed and configured in the AWS Cloud. Required for all Nielsen non-linear watermarking. MediaConvert can't connect directly to a TIC server. Instead, you must use API Gateway to provide a RESTful interface between MediaConvert and a TIC server that you deploy in your AWS account. For more information on deploying a TIC server in your AWS account and the required API Gateway, contact Nielsen support."""
    unique_tic_per_audio_track: NotRequired[
        "aws_sdk_mediaconvert.types.nielsen_unique_tic_per_audio_track_type.NielsenUniqueTicPerAudioTrackType"
    ]
    """To create assets that have the same TIC values in each audio track, keep the default value Share TICs. To create assets that have unique TIC values for each audio track, choose Use unique TICs."""


# --- restJson1 ser/de ---
def serialize_json(value: NielsenNonLinearWatermarkSettings) -> dict:
    out: dict = {}
    if "active_watermark_process" in value:
        import aws_sdk_mediaconvert.types.nielsen_active_watermark_process_type

        out["activeWatermarkProcess"] = (
            aws_sdk_mediaconvert.types.nielsen_active_watermark_process_type.serialize_json(
                value["active_watermark_process"]
            )
        )
    if "adi_filename" in value:
        out["adiFilename"] = value["adi_filename"]
    if "asset_id" in value:
        out["assetId"] = value["asset_id"]
    if "asset_name" in value:
        out["assetName"] = value["asset_name"]
    if "cbet_source_id" in value:
        out["cbetSourceId"] = value["cbet_source_id"]
    if "episode_id" in value:
        out["episodeId"] = value["episode_id"]
    if "metadata_destination" in value:
        out["metadataDestination"] = value["metadata_destination"]
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "source_watermark_status" in value:
        import aws_sdk_mediaconvert.types.nielsen_source_watermark_status_type

        out["sourceWatermarkStatus"] = (
            aws_sdk_mediaconvert.types.nielsen_source_watermark_status_type.serialize_json(
                value["source_watermark_status"]
            )
        )
    if "tic_server_url" in value:
        out["ticServerUrl"] = value["tic_server_url"]
    if "unique_tic_per_audio_track" in value:
        import aws_sdk_mediaconvert.types.nielsen_unique_tic_per_audio_track_type

        out["uniqueTicPerAudioTrack"] = (
            aws_sdk_mediaconvert.types.nielsen_unique_tic_per_audio_track_type.serialize_json(
                value["unique_tic_per_audio_track"]
            )
        )
    return out


def deserialize_json(data: dict) -> NielsenNonLinearWatermarkSettings:
    out: NielsenNonLinearWatermarkSettings = {}  # type: ignore[typeddict-item]
    if "activeWatermarkProcess" in data:
        import aws_sdk_mediaconvert.types.nielsen_active_watermark_process_type

        out["active_watermark_process"] = (
            aws_sdk_mediaconvert.types.nielsen_active_watermark_process_type.deserialize_json(
                data["activeWatermarkProcess"]
            )
        )
    if "adiFilename" in data:
        out["adi_filename"] = data["adiFilename"]
    if "assetId" in data:
        out["asset_id"] = data["assetId"]
    if "assetName" in data:
        out["asset_name"] = data["assetName"]
    if "cbetSourceId" in data:
        out["cbet_source_id"] = data["cbetSourceId"]
    if "episodeId" in data:
        out["episode_id"] = data["episodeId"]
    if "metadataDestination" in data:
        out["metadata_destination"] = data["metadataDestination"]
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "sourceWatermarkStatus" in data:
        import aws_sdk_mediaconvert.types.nielsen_source_watermark_status_type

        out["source_watermark_status"] = (
            aws_sdk_mediaconvert.types.nielsen_source_watermark_status_type.deserialize_json(
                data["sourceWatermarkStatus"]
            )
        )
    if "ticServerUrl" in data:
        out["tic_server_url"] = data["ticServerUrl"]
    if "uniqueTicPerAudioTrack" in data:
        import aws_sdk_mediaconvert.types.nielsen_unique_tic_per_audio_track_type

        out["unique_tic_per_audio_track"] = (
            aws_sdk_mediaconvert.types.nielsen_unique_tic_per_audio_track_type.deserialize_json(
                data["uniqueTicPerAudioTrack"]
            )
        )
    return out
