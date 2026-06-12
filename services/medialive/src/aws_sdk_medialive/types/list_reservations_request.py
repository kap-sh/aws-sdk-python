"""Generated from Smithy shape ``com.amazonaws.medialive#ListReservationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListReservationsRequest(TypedDict):
    channel_class: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE'"""
    codec: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', 'LINK', or 'AV1'"""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    maximum_bitrate: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'"""
    maximum_framerate: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'"""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    resolution: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'"""
    resource_type: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'"""
    special_feature: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'"""
    video_quality: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReservationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReservationsRequest:
    out: ListReservationsRequest = {}  # type: ignore[typeddict-item]
    return out
