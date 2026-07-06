"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationResourceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel_class
    import aws_sdk_medialive.types.reservation_codec
    import aws_sdk_medialive.types.reservation_maximum_bitrate
    import aws_sdk_medialive.types.reservation_maximum_framerate
    import aws_sdk_medialive.types.reservation_resolution
    import aws_sdk_medialive.types.reservation_resource_type
    import aws_sdk_medialive.types.reservation_special_feature
    import aws_sdk_medialive.types.reservation_video_quality


class ReservationResourceSpecification(TypedDict, closed=True):
    channel_class: NotRequired["aws_sdk_medialive.types.channel_class.ChannelClass"]
    """Channel class, e.g. 'STANDARD'"""
    codec: NotRequired["aws_sdk_medialive.types.reservation_codec.ReservationCodec"]
    """Codec, e.g. 'AVC'"""
    maximum_bitrate: NotRequired[
        "aws_sdk_medialive.types.reservation_maximum_bitrate.ReservationMaximumBitrate"
    ]
    """Maximum bitrate, e.g. 'MAX_20_MBPS'"""
    maximum_framerate: NotRequired[
        "aws_sdk_medialive.types.reservation_maximum_framerate.ReservationMaximumFramerate"
    ]
    """Maximum framerate, e.g. 'MAX_30_FPS' (Outputs only)"""
    resolution: NotRequired[
        "aws_sdk_medialive.types.reservation_resolution.ReservationResolution"
    ]
    """Resolution, e.g. 'HD'"""
    resource_type: NotRequired[
        "aws_sdk_medialive.types.reservation_resource_type.ReservationResourceType"
    ]
    """Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'"""
    special_feature: NotRequired[
        "aws_sdk_medialive.types.reservation_special_feature.ReservationSpecialFeature"
    ]
    """Special feature, e.g. 'AUDIO_NORMALIZATION' (Channels only)"""
    video_quality: NotRequired[
        "aws_sdk_medialive.types.reservation_video_quality.ReservationVideoQuality"
    ]
    """Video quality, e.g. 'STANDARD' (Outputs only)"""


# --- restJson1 ser/de ---
def serialize_json(value: ReservationResourceSpecification) -> dict:
    out: dict = {}
    if "channel_class" in value:
        import aws_sdk_medialive.types.channel_class

        out["channelClass"] = aws_sdk_medialive.types.channel_class.serialize_json(
            value["channel_class"]
        )
    if "codec" in value:
        import aws_sdk_medialive.types.reservation_codec

        out["codec"] = aws_sdk_medialive.types.reservation_codec.serialize_json(
            value["codec"]
        )
    if "maximum_bitrate" in value:
        import aws_sdk_medialive.types.reservation_maximum_bitrate

        out["maximumBitrate"] = (
            aws_sdk_medialive.types.reservation_maximum_bitrate.serialize_json(
                value["maximum_bitrate"]
            )
        )
    if "maximum_framerate" in value:
        import aws_sdk_medialive.types.reservation_maximum_framerate

        out["maximumFramerate"] = (
            aws_sdk_medialive.types.reservation_maximum_framerate.serialize_json(
                value["maximum_framerate"]
            )
        )
    if "resolution" in value:
        import aws_sdk_medialive.types.reservation_resolution

        out["resolution"] = (
            aws_sdk_medialive.types.reservation_resolution.serialize_json(
                value["resolution"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_medialive.types.reservation_resource_type

        out["resourceType"] = (
            aws_sdk_medialive.types.reservation_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "special_feature" in value:
        import aws_sdk_medialive.types.reservation_special_feature

        out["specialFeature"] = (
            aws_sdk_medialive.types.reservation_special_feature.serialize_json(
                value["special_feature"]
            )
        )
    if "video_quality" in value:
        import aws_sdk_medialive.types.reservation_video_quality

        out["videoQuality"] = (
            aws_sdk_medialive.types.reservation_video_quality.serialize_json(
                value["video_quality"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReservationResourceSpecification:
    out: ReservationResourceSpecification = {}  # type: ignore[typeddict-item]
    if "channelClass" in data:
        import aws_sdk_medialive.types.channel_class

        out["channel_class"] = aws_sdk_medialive.types.channel_class.deserialize_json(
            data["channelClass"]
        )
    if "codec" in data:
        import aws_sdk_medialive.types.reservation_codec

        out["codec"] = aws_sdk_medialive.types.reservation_codec.deserialize_json(
            data["codec"]
        )
    if "maximumBitrate" in data:
        import aws_sdk_medialive.types.reservation_maximum_bitrate

        out["maximum_bitrate"] = (
            aws_sdk_medialive.types.reservation_maximum_bitrate.deserialize_json(
                data["maximumBitrate"]
            )
        )
    if "maximumFramerate" in data:
        import aws_sdk_medialive.types.reservation_maximum_framerate

        out["maximum_framerate"] = (
            aws_sdk_medialive.types.reservation_maximum_framerate.deserialize_json(
                data["maximumFramerate"]
            )
        )
    if "resolution" in data:
        import aws_sdk_medialive.types.reservation_resolution

        out["resolution"] = (
            aws_sdk_medialive.types.reservation_resolution.deserialize_json(
                data["resolution"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_medialive.types.reservation_resource_type

        out["resource_type"] = (
            aws_sdk_medialive.types.reservation_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    if "specialFeature" in data:
        import aws_sdk_medialive.types.reservation_special_feature

        out["special_feature"] = (
            aws_sdk_medialive.types.reservation_special_feature.deserialize_json(
                data["specialFeature"]
            )
        )
    if "videoQuality" in data:
        import aws_sdk_medialive.types.reservation_video_quality

        out["video_quality"] = (
            aws_sdk_medialive.types.reservation_video_quality.deserialize_json(
                data["videoQuality"]
            )
        )
    return out
