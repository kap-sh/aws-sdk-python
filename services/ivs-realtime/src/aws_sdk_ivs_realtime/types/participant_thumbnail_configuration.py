"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantThumbnailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.thumbnail_interval_seconds
    import aws_sdk_ivs_realtime.types.thumbnail_recording_mode
    import aws_sdk_ivs_realtime.types.thumbnail_storage_type_list


class ParticipantThumbnailConfiguration(TypedDict, closed=True):
    target_interval_seconds: NotRequired[
        "aws_sdk_ivs_realtime.types.thumbnail_interval_seconds.ThumbnailIntervalSeconds"
    ]
    """<p>The targeted thumbnail-generation interval in seconds. This is configurable only if <code>recordingMode</code> is <code>INTERVAL</code>. Default: 60.</p>"""
    storage: NotRequired[
        "aws_sdk_ivs_realtime.types.thumbnail_storage_type_list.ThumbnailStorageTypeList"
    ]
    """<p>Indicates the format in which thumbnails are recorded. <code>SEQUENTIAL</code> records all generated thumbnails in a serial manner, to the media/thumbnails/high directory. <code>LATEST</code> saves the latest thumbnail in media/latest_thumbnail/high/thumb.jpg and overwrites it at the interval specified by <code>targetIntervalSeconds</code>. You can enable both <code>SEQUENTIAL</code> and <code>LATEST</code>. Default: <code>SEQUENTIAL</code>.</p>"""
    recording_mode: NotRequired[
        "aws_sdk_ivs_realtime.types.thumbnail_recording_mode.ThumbnailRecordingMode"
    ]
    """<p>Thumbnail recording mode. Default: <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantThumbnailConfiguration) -> dict:
    out: dict = {}
    if "target_interval_seconds" in value:
        out["targetIntervalSeconds"] = value["target_interval_seconds"]
    if "storage" in value:
        import aws_sdk_ivs_realtime.types.thumbnail_storage_type_list

        out["storage"] = (
            aws_sdk_ivs_realtime.types.thumbnail_storage_type_list.serialize_json(
                value["storage"]
            )
        )
    if "recording_mode" in value:
        import aws_sdk_ivs_realtime.types.thumbnail_recording_mode

        out["recordingMode"] = (
            aws_sdk_ivs_realtime.types.thumbnail_recording_mode.serialize_json(
                value["recording_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipantThumbnailConfiguration:
    out: ParticipantThumbnailConfiguration = {}  # type: ignore[typeddict-item]
    if "targetIntervalSeconds" in data:
        out["target_interval_seconds"] = data["targetIntervalSeconds"]
    if "storage" in data:
        import aws_sdk_ivs_realtime.types.thumbnail_storage_type_list

        out["storage"] = (
            aws_sdk_ivs_realtime.types.thumbnail_storage_type_list.deserialize_json(
                data["storage"]
            )
        )
    if "recordingMode" in data:
        import aws_sdk_ivs_realtime.types.thumbnail_recording_mode

        out["recording_mode"] = (
            aws_sdk_ivs_realtime.types.thumbnail_recording_mode.deserialize_json(
                data["recordingMode"]
            )
        )
    return out
