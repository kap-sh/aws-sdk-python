"""Generated from Smithy shape ``com.amazonaws.medialive#RtmpGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.__integer_min30
    import aws_sdk_medialive.types.__list_of_rtmp_ad_markers
    import aws_sdk_medialive.types.authentication_scheme
    import aws_sdk_medialive.types.include_filler_nal_units
    import aws_sdk_medialive.types.input_loss_action_for_rtmp_out
    import aws_sdk_medialive.types.rtmp_cache_full_behavior
    import aws_sdk_medialive.types.rtmp_caption_data


class RtmpGroupSettings(TypedDict, closed=True):
    ad_markers: NotRequired[
        "aws_sdk_medialive.types.__list_of_rtmp_ad_markers.__listOfRtmpAdMarkers"
    ]
    """Choose the ad marker type for this output group. MediaLive will create a message based on the content of each SCTE-35 message, format it for that marker type, and insert it in the datastream."""
    authentication_scheme: NotRequired[
        "aws_sdk_medialive.types.authentication_scheme.AuthenticationScheme"
    ]
    """Authentication scheme to use when connecting with CDN"""
    cache_full_behavior: NotRequired[
        "aws_sdk_medialive.types.rtmp_cache_full_behavior.RtmpCacheFullBehavior"
    ]
    """Controls behavior when content cache fills up. If remote origin server stalls the RTMP connection and does not accept content fast enough the 'Media Cache' will fill up. When the cache reaches the duration specified by cacheLength the cache will stop accepting new content. If set to disconnectImmediately, the RTMP output will force a disconnect. Clear the media cache, and reconnect after restartDelay seconds. If set to waitForServer, the RTMP output will wait up to 5 minutes to allow the origin server to begin accepting data again."""
    cache_length: NotRequired["aws_sdk_medialive.types.__integer_min30.__integerMin30"]
    """Cache length, in seconds, is used to calculate buffer size."""
    caption_data: NotRequired[
        "aws_sdk_medialive.types.rtmp_caption_data.RtmpCaptionData"
    ]
    """Controls the types of data that passes to onCaptionInfo outputs. If set to 'all' then 608 and 708 carried DTVCC data will be passed. If set to 'field1AndField2608' then DTVCC data will be stripped out, but 608 data from both fields will be passed. If set to 'field1608' then only the data carried in 608 from field 1 video will be passed."""
    input_loss_action: NotRequired[
        "aws_sdk_medialive.types.input_loss_action_for_rtmp_out.InputLossActionForRtmpOut"
    ]
    """Controls the behavior of this RTMP group if input becomes unavailable. - emitOutput: Emit a slate until input returns. - pauseOutput: Stop transmitting data until input returns. This does not close the underlying RTMP connection."""
    restart_delay: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """If a streaming output fails, number of seconds to wait until a restart is initiated. A value of 0 means never restart."""
    include_filler_nal_units: NotRequired[
        "aws_sdk_medialive.types.include_filler_nal_units.IncludeFillerNalUnits"
    ]
    """Applies only when the rate control mode (in the codec settings) is CBR (constant bit rate). Controls whether the RTMP output stream is padded (with FILL NAL units) in order to achieve a constant bit rate that is truly constant. When there is no padding, the bandwidth varies (up to the bitrate value in the codec settings). We recommend that you choose Auto."""


# --- restJson1 ser/de ---
def serialize_json(value: RtmpGroupSettings) -> dict:
    out: dict = {}
    if "ad_markers" in value:
        import aws_sdk_medialive.types.__list_of_rtmp_ad_markers

        out["adMarkers"] = (
            aws_sdk_medialive.types.__list_of_rtmp_ad_markers.serialize_json(
                value["ad_markers"]
            )
        )
    if "authentication_scheme" in value:
        import aws_sdk_medialive.types.authentication_scheme

        out["authenticationScheme"] = (
            aws_sdk_medialive.types.authentication_scheme.serialize_json(
                value["authentication_scheme"]
            )
        )
    if "cache_full_behavior" in value:
        import aws_sdk_medialive.types.rtmp_cache_full_behavior

        out["cacheFullBehavior"] = (
            aws_sdk_medialive.types.rtmp_cache_full_behavior.serialize_json(
                value["cache_full_behavior"]
            )
        )
    if "cache_length" in value:
        out["cacheLength"] = value["cache_length"]
    if "caption_data" in value:
        import aws_sdk_medialive.types.rtmp_caption_data

        out["captionData"] = aws_sdk_medialive.types.rtmp_caption_data.serialize_json(
            value["caption_data"]
        )
    if "input_loss_action" in value:
        import aws_sdk_medialive.types.input_loss_action_for_rtmp_out

        out["inputLossAction"] = (
            aws_sdk_medialive.types.input_loss_action_for_rtmp_out.serialize_json(
                value["input_loss_action"]
            )
        )
    if "restart_delay" in value:
        out["restartDelay"] = value["restart_delay"]
    if "include_filler_nal_units" in value:
        import aws_sdk_medialive.types.include_filler_nal_units

        out["includeFillerNalUnits"] = (
            aws_sdk_medialive.types.include_filler_nal_units.serialize_json(
                value["include_filler_nal_units"]
            )
        )
    return out


def deserialize_json(data: dict) -> RtmpGroupSettings:
    out: RtmpGroupSettings = {}  # type: ignore[typeddict-item]
    if "adMarkers" in data:
        import aws_sdk_medialive.types.__list_of_rtmp_ad_markers

        out["ad_markers"] = (
            aws_sdk_medialive.types.__list_of_rtmp_ad_markers.deserialize_json(
                data["adMarkers"]
            )
        )
    if "authenticationScheme" in data:
        import aws_sdk_medialive.types.authentication_scheme

        out["authentication_scheme"] = (
            aws_sdk_medialive.types.authentication_scheme.deserialize_json(
                data["authenticationScheme"]
            )
        )
    if "cacheFullBehavior" in data:
        import aws_sdk_medialive.types.rtmp_cache_full_behavior

        out["cache_full_behavior"] = (
            aws_sdk_medialive.types.rtmp_cache_full_behavior.deserialize_json(
                data["cacheFullBehavior"]
            )
        )
    if "cacheLength" in data:
        out["cache_length"] = data["cacheLength"]
    if "captionData" in data:
        import aws_sdk_medialive.types.rtmp_caption_data

        out["caption_data"] = (
            aws_sdk_medialive.types.rtmp_caption_data.deserialize_json(
                data["captionData"]
            )
        )
    if "inputLossAction" in data:
        import aws_sdk_medialive.types.input_loss_action_for_rtmp_out

        out["input_loss_action"] = (
            aws_sdk_medialive.types.input_loss_action_for_rtmp_out.deserialize_json(
                data["inputLossAction"]
            )
        )
    if "restartDelay" in data:
        out["restart_delay"] = data["restartDelay"]
    if "includeFillerNalUnits" in data:
        import aws_sdk_medialive.types.include_filler_nal_units

        out["include_filler_nal_units"] = (
            aws_sdk_medialive.types.include_filler_nal_units.deserialize_json(
                data["includeFillerNalUnits"]
            )
        )
    return out
