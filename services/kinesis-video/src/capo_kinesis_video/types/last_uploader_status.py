"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#LastUploaderStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.job_status_details
    import capo_kinesis_video.types.timestamp
    import capo_kinesis_video.types.uploader_status


class LastUploaderStatus(TypedDict, closed=True):
    job_status_details: NotRequired[
        "capo_kinesis_video.types.job_status_details.JobStatusDetails"
    ]
    """<p>A description of an uploader job’s latest status.</p>"""
    last_collected_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp at which the uploader job was last executed and media collected to the cloud.</p>"""
    last_updated_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp at which the uploader status was last updated.</p>"""
    uploader_status: NotRequired[
        "capo_kinesis_video.types.uploader_status.UploaderStatus"
    ]
    """<p>The status of the latest uploader job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastUploaderStatus) -> dict:
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
    if "uploader_status" in value:
        import capo_kinesis_video.types.uploader_status

        out["UploaderStatus"] = capo_kinesis_video.types.uploader_status.serialize_json(
            value["uploader_status"]
        )
    return out


def deserialize_json(data: dict) -> LastUploaderStatus:
    out: LastUploaderStatus = {}  # type: ignore[typeddict-item]
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
    if "UploaderStatus" in data:
        import capo_kinesis_video.types.uploader_status

        out["uploader_status"] = (
            capo_kinesis_video.types.uploader_status.deserialize_json(
                data["UploaderStatus"]
            )
        )
    return out
