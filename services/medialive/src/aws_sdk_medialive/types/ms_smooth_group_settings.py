"""Generated from Smithy shape ``com.amazonaws.medialive#MsSmoothGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.__integer_min0_max10000
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_loss_action_for_ms_smooth_out
    import aws_sdk_medialive.types.output_location_ref
    import aws_sdk_medialive.types.smooth_group_audio_only_timecode_control
    import aws_sdk_medialive.types.smooth_group_certificate_mode
    import aws_sdk_medialive.types.smooth_group_event_id_mode
    import aws_sdk_medialive.types.smooth_group_event_stop_behavior
    import aws_sdk_medialive.types.smooth_group_segmentation_mode
    import aws_sdk_medialive.types.smooth_group_sparse_track_type
    import aws_sdk_medialive.types.smooth_group_stream_manifest_behavior
    import aws_sdk_medialive.types.smooth_group_timestamp_offset_mode


class MsSmoothGroupSettings(TypedDict, closed=True):
    acquisition_point_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID to include in each message in the sparse track. Ignored if sparseTrackType is NONE."""
    audio_only_timecode_control: NotRequired[
        "aws_sdk_medialive.types.smooth_group_audio_only_timecode_control.SmoothGroupAudioOnlyTimecodeControl"
    ]
    """If set to passthrough for an audio-only MS Smooth output, the fragment absolute time will be set to the current timecode. This option does not write timecodes to the audio elementary stream."""
    certificate_mode: NotRequired[
        "aws_sdk_medialive.types.smooth_group_certificate_mode.SmoothGroupCertificateMode"
    ]
    """If set to verifyAuthenticity, verify the https certificate chain to a trusted Certificate Authority (CA). This will cause https outputs to self-signed certificates to fail."""
    connection_retry_interval: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """Number of seconds to wait before retrying connection to the IIS server if the connection is lost. Content will be cached during this time and the cache will be be delivered to the IIS server once the connection is re-established."""
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    r"""Smooth Streaming publish point on an IIS server. Elemental Live acts as a \"Push\" encoder to IIS."""
    event_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """MS Smooth event ID to be sent to the IIS server. Should only be specified if eventIdMode is set to useConfigured."""
    event_id_mode: NotRequired[
        "aws_sdk_medialive.types.smooth_group_event_id_mode.SmoothGroupEventIdMode"
    ]
    r"""Specifies whether or not to send an event ID to the IIS server. If no event ID is sent and the same Live Event is used without changing the publishing point, clients might see cached video from the previous run. Options: - \"useConfigured\" - use the value provided in eventId - \"useTimestamp\" - generate and send an event ID based on the current timestamp - \"noEventId\" - do not send an event ID to the IIS server."""
    event_stop_behavior: NotRequired[
        "aws_sdk_medialive.types.smooth_group_event_stop_behavior.SmoothGroupEventStopBehavior"
    ]
    """When set to sendEos, send EOS signal to IIS server when stopping the event"""
    filecache_duration: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """Size in seconds of file cache for streaming outputs."""
    fragment_length: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """Length of mp4 fragments to generate (in seconds). Fragment length must be compatible with GOP size and framerate."""
    input_loss_action: NotRequired[
        "aws_sdk_medialive.types.input_loss_action_for_ms_smooth_out.InputLossActionForMsSmoothOut"
    ]
    """Parameter that control output group behavior on input loss."""
    num_retries: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """Number of retry attempts."""
    restart_delay: NotRequired["aws_sdk_medialive.types.__integer_min0.__integerMin0"]
    """Number of seconds before initiating a restart due to output failure, due to exhausting the numRetries on one segment, or exceeding filecacheDuration."""
    segmentation_mode: NotRequired[
        "aws_sdk_medialive.types.smooth_group_segmentation_mode.SmoothGroupSegmentationMode"
    ]
    """useInputSegmentation has been deprecated. The configured segment size is always used."""
    send_delay_ms: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """Number of milliseconds to delay the output from the second pipeline."""
    sparse_track_type: NotRequired[
        "aws_sdk_medialive.types.smooth_group_sparse_track_type.SmoothGroupSparseTrackType"
    ]
    """Identifies the type of data to place in the sparse track: - SCTE35: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame to start a new segment. - SCTE35_WITHOUT_SEGMENTATION: Insert SCTE-35 messages from the source content. With each message, insert an IDR frame but don't start a new segment. - NONE: Don't generate a sparse track for any outputs in this output group."""
    stream_manifest_behavior: NotRequired[
        "aws_sdk_medialive.types.smooth_group_stream_manifest_behavior.SmoothGroupStreamManifestBehavior"
    ]
    """When set to send, send stream manifest so publishing point doesn't start until all streams start."""
    timestamp_offset: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Timestamp offset for the event. Only used if timestampOffsetMode is set to useConfiguredOffset."""
    timestamp_offset_mode: NotRequired[
        "aws_sdk_medialive.types.smooth_group_timestamp_offset_mode.SmoothGroupTimestampOffsetMode"
    ]
    """Type of timestamp date offset to use. - useEventStartDate: Use the date the event was started as the offset - useConfiguredOffset: Use an explicitly configured date as the offset"""


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothGroupSettings) -> dict:
    out: dict = {}
    if "acquisition_point_id" in value:
        out["acquisitionPointId"] = value["acquisition_point_id"]
    if "audio_only_timecode_control" in value:
        import aws_sdk_medialive.types.smooth_group_audio_only_timecode_control

        out["audioOnlyTimecodeControl"] = (
            aws_sdk_medialive.types.smooth_group_audio_only_timecode_control.serialize_json(
                value["audio_only_timecode_control"]
            )
        )
    if "certificate_mode" in value:
        import aws_sdk_medialive.types.smooth_group_certificate_mode

        out["certificateMode"] = (
            aws_sdk_medialive.types.smooth_group_certificate_mode.serialize_json(
                value["certificate_mode"]
            )
        )
    if "connection_retry_interval" in value:
        out["connectionRetryInterval"] = value["connection_retry_interval"]
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_id_mode" in value:
        import aws_sdk_medialive.types.smooth_group_event_id_mode

        out["eventIdMode"] = (
            aws_sdk_medialive.types.smooth_group_event_id_mode.serialize_json(
                value["event_id_mode"]
            )
        )
    if "event_stop_behavior" in value:
        import aws_sdk_medialive.types.smooth_group_event_stop_behavior

        out["eventStopBehavior"] = (
            aws_sdk_medialive.types.smooth_group_event_stop_behavior.serialize_json(
                value["event_stop_behavior"]
            )
        )
    if "filecache_duration" in value:
        out["filecacheDuration"] = value["filecache_duration"]
    if "fragment_length" in value:
        out["fragmentLength"] = value["fragment_length"]
    if "input_loss_action" in value:
        import aws_sdk_medialive.types.input_loss_action_for_ms_smooth_out

        out["inputLossAction"] = (
            aws_sdk_medialive.types.input_loss_action_for_ms_smooth_out.serialize_json(
                value["input_loss_action"]
            )
        )
    if "num_retries" in value:
        out["numRetries"] = value["num_retries"]
    if "restart_delay" in value:
        out["restartDelay"] = value["restart_delay"]
    if "segmentation_mode" in value:
        import aws_sdk_medialive.types.smooth_group_segmentation_mode

        out["segmentationMode"] = (
            aws_sdk_medialive.types.smooth_group_segmentation_mode.serialize_json(
                value["segmentation_mode"]
            )
        )
    if "send_delay_ms" in value:
        out["sendDelayMs"] = value["send_delay_ms"]
    if "sparse_track_type" in value:
        import aws_sdk_medialive.types.smooth_group_sparse_track_type

        out["sparseTrackType"] = (
            aws_sdk_medialive.types.smooth_group_sparse_track_type.serialize_json(
                value["sparse_track_type"]
            )
        )
    if "stream_manifest_behavior" in value:
        import aws_sdk_medialive.types.smooth_group_stream_manifest_behavior

        out["streamManifestBehavior"] = (
            aws_sdk_medialive.types.smooth_group_stream_manifest_behavior.serialize_json(
                value["stream_manifest_behavior"]
            )
        )
    if "timestamp_offset" in value:
        out["timestampOffset"] = value["timestamp_offset"]
    if "timestamp_offset_mode" in value:
        import aws_sdk_medialive.types.smooth_group_timestamp_offset_mode

        out["timestampOffsetMode"] = (
            aws_sdk_medialive.types.smooth_group_timestamp_offset_mode.serialize_json(
                value["timestamp_offset_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> MsSmoothGroupSettings:
    out: MsSmoothGroupSettings = {}  # type: ignore[typeddict-item]
    if "acquisitionPointId" in data:
        out["acquisition_point_id"] = data["acquisitionPointId"]
    if "audioOnlyTimecodeControl" in data:
        import aws_sdk_medialive.types.smooth_group_audio_only_timecode_control

        out["audio_only_timecode_control"] = (
            aws_sdk_medialive.types.smooth_group_audio_only_timecode_control.deserialize_json(
                data["audioOnlyTimecodeControl"]
            )
        )
    if "certificateMode" in data:
        import aws_sdk_medialive.types.smooth_group_certificate_mode

        out["certificate_mode"] = (
            aws_sdk_medialive.types.smooth_group_certificate_mode.deserialize_json(
                data["certificateMode"]
            )
        )
    if "connectionRetryInterval" in data:
        out["connection_retry_interval"] = data["connectionRetryInterval"]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventIdMode" in data:
        import aws_sdk_medialive.types.smooth_group_event_id_mode

        out["event_id_mode"] = (
            aws_sdk_medialive.types.smooth_group_event_id_mode.deserialize_json(
                data["eventIdMode"]
            )
        )
    if "eventStopBehavior" in data:
        import aws_sdk_medialive.types.smooth_group_event_stop_behavior

        out["event_stop_behavior"] = (
            aws_sdk_medialive.types.smooth_group_event_stop_behavior.deserialize_json(
                data["eventStopBehavior"]
            )
        )
    if "filecacheDuration" in data:
        out["filecache_duration"] = data["filecacheDuration"]
    if "fragmentLength" in data:
        out["fragment_length"] = data["fragmentLength"]
    if "inputLossAction" in data:
        import aws_sdk_medialive.types.input_loss_action_for_ms_smooth_out

        out["input_loss_action"] = (
            aws_sdk_medialive.types.input_loss_action_for_ms_smooth_out.deserialize_json(
                data["inputLossAction"]
            )
        )
    if "numRetries" in data:
        out["num_retries"] = data["numRetries"]
    if "restartDelay" in data:
        out["restart_delay"] = data["restartDelay"]
    if "segmentationMode" in data:
        import aws_sdk_medialive.types.smooth_group_segmentation_mode

        out["segmentation_mode"] = (
            aws_sdk_medialive.types.smooth_group_segmentation_mode.deserialize_json(
                data["segmentationMode"]
            )
        )
    if "sendDelayMs" in data:
        out["send_delay_ms"] = data["sendDelayMs"]
    if "sparseTrackType" in data:
        import aws_sdk_medialive.types.smooth_group_sparse_track_type

        out["sparse_track_type"] = (
            aws_sdk_medialive.types.smooth_group_sparse_track_type.deserialize_json(
                data["sparseTrackType"]
            )
        )
    if "streamManifestBehavior" in data:
        import aws_sdk_medialive.types.smooth_group_stream_manifest_behavior

        out["stream_manifest_behavior"] = (
            aws_sdk_medialive.types.smooth_group_stream_manifest_behavior.deserialize_json(
                data["streamManifestBehavior"]
            )
        )
    if "timestampOffset" in data:
        out["timestamp_offset"] = data["timestampOffset"]
    if "timestampOffsetMode" in data:
        import aws_sdk_medialive.types.smooth_group_timestamp_offset_mode

        out["timestamp_offset_mode"] = (
            aws_sdk_medialive.types.smooth_group_timestamp_offset_mode.deserialize_json(
                data["timestampOffsetMode"]
            )
        )
    return out
