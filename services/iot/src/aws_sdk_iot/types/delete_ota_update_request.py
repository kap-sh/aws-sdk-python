"""Generated from Smithy shape ``com.amazonaws.iot#DeleteOTAUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.delete_stream_
    import aws_sdk_iot.types.force_delete_aws_job
    import aws_sdk_iot.types.ota_update_id


class DeleteOTAUpdateRequest(TypedDict):
    ota_update_id: "aws_sdk_iot.types.ota_update_id.OTAUpdateId"
    """<p>The ID of the OTA update to delete.</p>"""
    delete_stream: "aws_sdk_iot.types.delete_stream_.DeleteStream_"
    """<p>When true, the stream created by the OTAUpdate process is deleted when the OTA update is deleted. Ignored if the stream specified in the OTAUpdate is supplied by the user.</p>"""
    force_delete_aws_job: "aws_sdk_iot.types.force_delete_aws_job.ForceDeleteAWSJob"
    """<p>When true, deletes the IoT job created by the OTAUpdate process even if it is \"IN_PROGRESS\". Otherwise, if the job is not in a terminal state (\"COMPLETED\" or \"CANCELED\") an exception will occur. The default is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOTAUpdateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOTAUpdateRequest:
    out: DeleteOTAUpdateRequest = {}  # type: ignore[typeddict-item]
    return out
