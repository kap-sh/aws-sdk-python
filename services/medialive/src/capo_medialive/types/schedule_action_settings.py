"""Generated from Smithy shape ``com.amazonaws.medialive#ScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.hls_id3_segment_tagging_schedule_action_settings
    import capo_medialive.types.hls_timed_metadata_schedule_action_settings
    import capo_medialive.types.id3_segment_tagging_schedule_action_settings
    import capo_medialive.types.input_prepare_schedule_action_settings
    import capo_medialive.types.input_switch_schedule_action_settings
    import capo_medialive.types.motion_graphics_activate_schedule_action_settings
    import capo_medialive.types.motion_graphics_deactivate_schedule_action_settings
    import capo_medialive.types.pause_state_schedule_action_settings
    import capo_medialive.types.scte35_input_schedule_action_settings
    import capo_medialive.types.scte35_return_to_network_schedule_action_settings
    import capo_medialive.types.scte35_splice_insert_schedule_action_settings
    import capo_medialive.types.scte35_time_signal_schedule_action_settings
    import capo_medialive.types.static_image_activate_schedule_action_settings
    import capo_medialive.types.static_image_deactivate_schedule_action_settings
    import capo_medialive.types.static_image_output_activate_schedule_action_settings
    import capo_medialive.types.static_image_output_deactivate_schedule_action_settings
    import capo_medialive.types.timed_metadata_schedule_action_settings


class ScheduleActionSettings(TypedDict, closed=True):
    hls_id3_segment_tagging_settings: NotRequired[
        "capo_medialive.types.hls_id3_segment_tagging_schedule_action_settings.HlsId3SegmentTaggingScheduleActionSettings"
    ]
    """Action to insert ID3 metadata in every segment, in HLS output groups"""
    hls_timed_metadata_settings: NotRequired[
        "capo_medialive.types.hls_timed_metadata_schedule_action_settings.HlsTimedMetadataScheduleActionSettings"
    ]
    """Action to insert ID3 metadata once, in HLS output groups"""
    input_prepare_settings: NotRequired[
        "capo_medialive.types.input_prepare_schedule_action_settings.InputPrepareScheduleActionSettings"
    ]
    """Action to prepare an input for a future immediate input switch"""
    input_switch_settings: NotRequired[
        "capo_medialive.types.input_switch_schedule_action_settings.InputSwitchScheduleActionSettings"
    ]
    """Action to switch the input"""
    motion_graphics_image_activate_settings: NotRequired[
        "capo_medialive.types.motion_graphics_activate_schedule_action_settings.MotionGraphicsActivateScheduleActionSettings"
    ]
    """Action to activate a motion graphics image overlay"""
    motion_graphics_image_deactivate_settings: NotRequired[
        "capo_medialive.types.motion_graphics_deactivate_schedule_action_settings.MotionGraphicsDeactivateScheduleActionSettings"
    ]
    """Action to deactivate a motion graphics image overlay"""
    pause_state_settings: NotRequired[
        "capo_medialive.types.pause_state_schedule_action_settings.PauseStateScheduleActionSettings"
    ]
    """Action to pause or unpause one or both channel pipelines"""
    scte35_input_settings: NotRequired[
        "capo_medialive.types.scte35_input_schedule_action_settings.Scte35InputScheduleActionSettings"
    ]
    """Action to specify scte35 input"""
    scte35_return_to_network_settings: NotRequired[
        "capo_medialive.types.scte35_return_to_network_schedule_action_settings.Scte35ReturnToNetworkScheduleActionSettings"
    ]
    """Action to insert SCTE-35 return_to_network message"""
    scte35_splice_insert_settings: NotRequired[
        "capo_medialive.types.scte35_splice_insert_schedule_action_settings.Scte35SpliceInsertScheduleActionSettings"
    ]
    """Action to insert SCTE-35 splice_insert message"""
    scte35_time_signal_settings: NotRequired[
        "capo_medialive.types.scte35_time_signal_schedule_action_settings.Scte35TimeSignalScheduleActionSettings"
    ]
    """Action to insert SCTE-35 time_signal message"""
    static_image_activate_settings: NotRequired[
        "capo_medialive.types.static_image_activate_schedule_action_settings.StaticImageActivateScheduleActionSettings"
    ]
    """Action to activate a static image overlay"""
    static_image_deactivate_settings: NotRequired[
        "capo_medialive.types.static_image_deactivate_schedule_action_settings.StaticImageDeactivateScheduleActionSettings"
    ]
    """Action to deactivate a static image overlay"""
    static_image_output_activate_settings: NotRequired[
        "capo_medialive.types.static_image_output_activate_schedule_action_settings.StaticImageOutputActivateScheduleActionSettings"
    ]
    """Action to activate a static image overlay in one or more specified outputs"""
    static_image_output_deactivate_settings: NotRequired[
        "capo_medialive.types.static_image_output_deactivate_schedule_action_settings.StaticImageOutputDeactivateScheduleActionSettings"
    ]
    """Action to deactivate a static image overlay in one or more specified outputs"""
    id3_segment_tagging_settings: NotRequired[
        "capo_medialive.types.id3_segment_tagging_schedule_action_settings.Id3SegmentTaggingScheduleActionSettings"
    ]
    """Action to insert ID3 metadata in every segment, in applicable output groups"""
    timed_metadata_settings: NotRequired[
        "capo_medialive.types.timed_metadata_schedule_action_settings.TimedMetadataScheduleActionSettings"
    ]
    """Action to insert ID3 metadata once, in applicable output groups"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionSettings) -> dict:
    out: dict = {}
    if "hls_id3_segment_tagging_settings" in value:
        import capo_medialive.types.hls_id3_segment_tagging_schedule_action_settings

        out["hlsId3SegmentTaggingSettings"] = (
            capo_medialive.types.hls_id3_segment_tagging_schedule_action_settings.serialize_json(
                value["hls_id3_segment_tagging_settings"]
            )
        )
    if "hls_timed_metadata_settings" in value:
        import capo_medialive.types.hls_timed_metadata_schedule_action_settings

        out["hlsTimedMetadataSettings"] = (
            capo_medialive.types.hls_timed_metadata_schedule_action_settings.serialize_json(
                value["hls_timed_metadata_settings"]
            )
        )
    if "input_prepare_settings" in value:
        import capo_medialive.types.input_prepare_schedule_action_settings

        out["inputPrepareSettings"] = (
            capo_medialive.types.input_prepare_schedule_action_settings.serialize_json(
                value["input_prepare_settings"]
            )
        )
    if "input_switch_settings" in value:
        import capo_medialive.types.input_switch_schedule_action_settings

        out["inputSwitchSettings"] = (
            capo_medialive.types.input_switch_schedule_action_settings.serialize_json(
                value["input_switch_settings"]
            )
        )
    if "motion_graphics_image_activate_settings" in value:
        import capo_medialive.types.motion_graphics_activate_schedule_action_settings

        out["motionGraphicsImageActivateSettings"] = (
            capo_medialive.types.motion_graphics_activate_schedule_action_settings.serialize_json(
                value["motion_graphics_image_activate_settings"]
            )
        )
    if "motion_graphics_image_deactivate_settings" in value:
        import capo_medialive.types.motion_graphics_deactivate_schedule_action_settings

        out["motionGraphicsImageDeactivateSettings"] = (
            capo_medialive.types.motion_graphics_deactivate_schedule_action_settings.serialize_json(
                value["motion_graphics_image_deactivate_settings"]
            )
        )
    if "pause_state_settings" in value:
        import capo_medialive.types.pause_state_schedule_action_settings

        out["pauseStateSettings"] = (
            capo_medialive.types.pause_state_schedule_action_settings.serialize_json(
                value["pause_state_settings"]
            )
        )
    if "scte35_input_settings" in value:
        import capo_medialive.types.scte35_input_schedule_action_settings

        out["scte35InputSettings"] = (
            capo_medialive.types.scte35_input_schedule_action_settings.serialize_json(
                value["scte35_input_settings"]
            )
        )
    if "scte35_return_to_network_settings" in value:
        import capo_medialive.types.scte35_return_to_network_schedule_action_settings

        out["scte35ReturnToNetworkSettings"] = (
            capo_medialive.types.scte35_return_to_network_schedule_action_settings.serialize_json(
                value["scte35_return_to_network_settings"]
            )
        )
    if "scte35_splice_insert_settings" in value:
        import capo_medialive.types.scte35_splice_insert_schedule_action_settings

        out["scte35SpliceInsertSettings"] = (
            capo_medialive.types.scte35_splice_insert_schedule_action_settings.serialize_json(
                value["scte35_splice_insert_settings"]
            )
        )
    if "scte35_time_signal_settings" in value:
        import capo_medialive.types.scte35_time_signal_schedule_action_settings

        out["scte35TimeSignalSettings"] = (
            capo_medialive.types.scte35_time_signal_schedule_action_settings.serialize_json(
                value["scte35_time_signal_settings"]
            )
        )
    if "static_image_activate_settings" in value:
        import capo_medialive.types.static_image_activate_schedule_action_settings

        out["staticImageActivateSettings"] = (
            capo_medialive.types.static_image_activate_schedule_action_settings.serialize_json(
                value["static_image_activate_settings"]
            )
        )
    if "static_image_deactivate_settings" in value:
        import capo_medialive.types.static_image_deactivate_schedule_action_settings

        out["staticImageDeactivateSettings"] = (
            capo_medialive.types.static_image_deactivate_schedule_action_settings.serialize_json(
                value["static_image_deactivate_settings"]
            )
        )
    if "static_image_output_activate_settings" in value:
        import capo_medialive.types.static_image_output_activate_schedule_action_settings

        out["staticImageOutputActivateSettings"] = (
            capo_medialive.types.static_image_output_activate_schedule_action_settings.serialize_json(
                value["static_image_output_activate_settings"]
            )
        )
    if "static_image_output_deactivate_settings" in value:
        import capo_medialive.types.static_image_output_deactivate_schedule_action_settings

        out["staticImageOutputDeactivateSettings"] = (
            capo_medialive.types.static_image_output_deactivate_schedule_action_settings.serialize_json(
                value["static_image_output_deactivate_settings"]
            )
        )
    if "id3_segment_tagging_settings" in value:
        import capo_medialive.types.id3_segment_tagging_schedule_action_settings

        out["id3SegmentTaggingSettings"] = (
            capo_medialive.types.id3_segment_tagging_schedule_action_settings.serialize_json(
                value["id3_segment_tagging_settings"]
            )
        )
    if "timed_metadata_settings" in value:
        import capo_medialive.types.timed_metadata_schedule_action_settings

        out["timedMetadataSettings"] = (
            capo_medialive.types.timed_metadata_schedule_action_settings.serialize_json(
                value["timed_metadata_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScheduleActionSettings:
    out: ScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "hlsId3SegmentTaggingSettings" in data:
        import capo_medialive.types.hls_id3_segment_tagging_schedule_action_settings

        out["hls_id3_segment_tagging_settings"] = (
            capo_medialive.types.hls_id3_segment_tagging_schedule_action_settings.deserialize_json(
                data["hlsId3SegmentTaggingSettings"]
            )
        )
    if "hlsTimedMetadataSettings" in data:
        import capo_medialive.types.hls_timed_metadata_schedule_action_settings

        out["hls_timed_metadata_settings"] = (
            capo_medialive.types.hls_timed_metadata_schedule_action_settings.deserialize_json(
                data["hlsTimedMetadataSettings"]
            )
        )
    if "inputPrepareSettings" in data:
        import capo_medialive.types.input_prepare_schedule_action_settings

        out["input_prepare_settings"] = (
            capo_medialive.types.input_prepare_schedule_action_settings.deserialize_json(
                data["inputPrepareSettings"]
            )
        )
    if "inputSwitchSettings" in data:
        import capo_medialive.types.input_switch_schedule_action_settings

        out["input_switch_settings"] = (
            capo_medialive.types.input_switch_schedule_action_settings.deserialize_json(
                data["inputSwitchSettings"]
            )
        )
    if "motionGraphicsImageActivateSettings" in data:
        import capo_medialive.types.motion_graphics_activate_schedule_action_settings

        out["motion_graphics_image_activate_settings"] = (
            capo_medialive.types.motion_graphics_activate_schedule_action_settings.deserialize_json(
                data["motionGraphicsImageActivateSettings"]
            )
        )
    if "motionGraphicsImageDeactivateSettings" in data:
        import capo_medialive.types.motion_graphics_deactivate_schedule_action_settings

        out["motion_graphics_image_deactivate_settings"] = (
            capo_medialive.types.motion_graphics_deactivate_schedule_action_settings.deserialize_json(
                data["motionGraphicsImageDeactivateSettings"]
            )
        )
    if "pauseStateSettings" in data:
        import capo_medialive.types.pause_state_schedule_action_settings

        out["pause_state_settings"] = (
            capo_medialive.types.pause_state_schedule_action_settings.deserialize_json(
                data["pauseStateSettings"]
            )
        )
    if "scte35InputSettings" in data:
        import capo_medialive.types.scte35_input_schedule_action_settings

        out["scte35_input_settings"] = (
            capo_medialive.types.scte35_input_schedule_action_settings.deserialize_json(
                data["scte35InputSettings"]
            )
        )
    if "scte35ReturnToNetworkSettings" in data:
        import capo_medialive.types.scte35_return_to_network_schedule_action_settings

        out["scte35_return_to_network_settings"] = (
            capo_medialive.types.scte35_return_to_network_schedule_action_settings.deserialize_json(
                data["scte35ReturnToNetworkSettings"]
            )
        )
    if "scte35SpliceInsertSettings" in data:
        import capo_medialive.types.scte35_splice_insert_schedule_action_settings

        out["scte35_splice_insert_settings"] = (
            capo_medialive.types.scte35_splice_insert_schedule_action_settings.deserialize_json(
                data["scte35SpliceInsertSettings"]
            )
        )
    if "scte35TimeSignalSettings" in data:
        import capo_medialive.types.scte35_time_signal_schedule_action_settings

        out["scte35_time_signal_settings"] = (
            capo_medialive.types.scte35_time_signal_schedule_action_settings.deserialize_json(
                data["scte35TimeSignalSettings"]
            )
        )
    if "staticImageActivateSettings" in data:
        import capo_medialive.types.static_image_activate_schedule_action_settings

        out["static_image_activate_settings"] = (
            capo_medialive.types.static_image_activate_schedule_action_settings.deserialize_json(
                data["staticImageActivateSettings"]
            )
        )
    if "staticImageDeactivateSettings" in data:
        import capo_medialive.types.static_image_deactivate_schedule_action_settings

        out["static_image_deactivate_settings"] = (
            capo_medialive.types.static_image_deactivate_schedule_action_settings.deserialize_json(
                data["staticImageDeactivateSettings"]
            )
        )
    if "staticImageOutputActivateSettings" in data:
        import capo_medialive.types.static_image_output_activate_schedule_action_settings

        out["static_image_output_activate_settings"] = (
            capo_medialive.types.static_image_output_activate_schedule_action_settings.deserialize_json(
                data["staticImageOutputActivateSettings"]
            )
        )
    if "staticImageOutputDeactivateSettings" in data:
        import capo_medialive.types.static_image_output_deactivate_schedule_action_settings

        out["static_image_output_deactivate_settings"] = (
            capo_medialive.types.static_image_output_deactivate_schedule_action_settings.deserialize_json(
                data["staticImageOutputDeactivateSettings"]
            )
        )
    if "id3SegmentTaggingSettings" in data:
        import capo_medialive.types.id3_segment_tagging_schedule_action_settings

        out["id3_segment_tagging_settings"] = (
            capo_medialive.types.id3_segment_tagging_schedule_action_settings.deserialize_json(
                data["id3SegmentTaggingSettings"]
            )
        )
    if "timedMetadataSettings" in data:
        import capo_medialive.types.timed_metadata_schedule_action_settings

        out["timed_metadata_settings"] = (
            capo_medialive.types.timed_metadata_schedule_action_settings.deserialize_json(
                data["timedMetadataSettings"]
            )
        )
    return out
