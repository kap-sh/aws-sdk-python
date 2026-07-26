"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#EdgeAgentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.last_recorder_status
    import capo_kinesis_video.types.last_uploader_status


class EdgeAgentStatus(TypedDict, closed=True):
    last_recorder_status: NotRequired[
        "capo_kinesis_video.types.last_recorder_status.LastRecorderStatus"
    ]
    """<p>The latest status of a stream’s edge recording job.</p>"""
    last_uploader_status: NotRequired[
        "capo_kinesis_video.types.last_uploader_status.LastUploaderStatus"
    ]
    """<p>The latest status of a stream’s edge to cloud uploader job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeAgentStatus) -> dict:
    out: dict = {}
    if "last_recorder_status" in value:
        import capo_kinesis_video.types.last_recorder_status

        out["LastRecorderStatus"] = (
            capo_kinesis_video.types.last_recorder_status.serialize_json(
                value["last_recorder_status"]
            )
        )
    if "last_uploader_status" in value:
        import capo_kinesis_video.types.last_uploader_status

        out["LastUploaderStatus"] = (
            capo_kinesis_video.types.last_uploader_status.serialize_json(
                value["last_uploader_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> EdgeAgentStatus:
    out: EdgeAgentStatus = {}  # type: ignore[typeddict-item]
    if "LastRecorderStatus" in data:
        import capo_kinesis_video.types.last_recorder_status

        out["last_recorder_status"] = (
            capo_kinesis_video.types.last_recorder_status.deserialize_json(
                data["LastRecorderStatus"]
            )
        )
    if "LastUploaderStatus" in data:
        import capo_kinesis_video.types.last_uploader_status

        out["last_uploader_status"] = (
            capo_kinesis_video.types.last_uploader_status.deserialize_json(
                data["LastUploaderStatus"]
            )
        )
    return out
