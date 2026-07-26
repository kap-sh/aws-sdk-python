"""Generated from Smithy shape ``com.amazonaws.deadline#JobAttachmentDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.attachments
    import capo_deadline.types.job_id


class JobAttachmentDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID.</p>"""
    attachments: "capo_deadline.types.attachments.Attachments"
    """<p>The job attachments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobAttachmentDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_deadline.types.attachments

    out["attachments"] = capo_deadline.types.attachments.serialize_json(
        value["attachments"]
    )
    return out


def deserialize_json(data: dict) -> JobAttachmentDetailsEntity:
    out: JobAttachmentDetailsEntity = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("JobAttachmentDetailsEntity.job_id required")
    if "attachments" in data:
        import capo_deadline.types.attachments

        out["attachments"] = capo_deadline.types.attachments.deserialize_json(
            data["attachments"]
        )
    else:
        raise DeserializationError("JobAttachmentDetailsEntity.attachments required")
    return out
