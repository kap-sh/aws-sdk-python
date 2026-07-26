"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#LastRecorderStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.job_status_details
    import capo_kinesis_video.types.recorder_status
    import capo_kinesis_video.types.timestamp


class LastRecorderStatus(TypedDict, closed=True):
    job_status_details: NotRequired[
        "capo_kinesis_video.types.job_status_details.JobStatusDetails"
    ]
    """<p>A description of a recorder job’s latest status.</p>"""
    last_collected_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp at which the recorder job was last executed and media stored to local disk.</p>"""
    last_updated_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp at which the recorder status was last updated.</p>"""
    recorder_status: NotRequired[
        "capo_kinesis_video.types.recorder_status.RecorderStatus"
    ]
    """<p>The status of the latest recorder job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastRecorderStatus) -> dict:
    out: dict = {}
    if "job_status_details" in value:
        out["JobStatusDetails"] = value["job_status_details"]
    if "last_collected_time" in value:
        import capo_kinesis_video.types.timestamp

        out["LastCollectedTime"] = capo_kinesis_video.types.timestamp.serialize_json(
            value["last_collected_time"]
        )
    if "last_updated_time" in value:
        import capo_kinesis_video.types.timestamp

        out["LastUpdatedTime"] = capo_kinesis_video.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "recorder_status" in value:
        import capo_kinesis_video.types.recorder_status

        out["RecorderStatus"] = capo_kinesis_video.types.recorder_status.serialize_json(
            value["recorder_status"]
        )
    return out


def deserialize_json(data: dict) -> LastRecorderStatus:
    out: LastRecorderStatus = {}  # type: ignore[typeddict-item]
    if "JobStatusDetails" in data:
        out["job_status_details"] = data["JobStatusDetails"]
    if "LastCollectedTime" in data:
        import capo_kinesis_video.types.timestamp

        out["last_collected_time"] = (
            capo_kinesis_video.types.timestamp.deserialize_json(
                data["LastCollectedTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import capo_kinesis_video.types.timestamp

        out["last_updated_time"] = capo_kinesis_video.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "RecorderStatus" in data:
        import capo_kinesis_video.types.recorder_status

        out["recorder_status"] = (
            capo_kinesis_video.types.recorder_status.deserialize_json(
                data["RecorderStatus"]
            )
        )
    return out
