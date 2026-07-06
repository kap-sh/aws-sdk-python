"""Generated from Smithy shape ``com.amazonaws.s3control#UpdateJobStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_id
    import aws_sdk_s3_control.types.job_status
    import aws_sdk_s3_control.types.job_status_update_reason


class UpdateJobStatusResult(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_s3_control.types.job_id.JobId"]
    """<p>The ID for the job whose status was updated.</p>"""
    status: NotRequired["aws_sdk_s3_control.types.job_status.JobStatus"]
    """<p>The current status for the specified job.</p>"""
    status_update_reason: NotRequired[
        "aws_sdk_s3_control.types.job_status_update_reason.JobStatusUpdateReason"
    ]
    """<p>The reason that the specified job's status was updated.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateJobStatusResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "job_id" in value:
        SubElement(el, "JobId").text = str(value["job_id"])
    if "status" in value:
        import aws_sdk_s3_control.types.job_status

        aws_sdk_s3_control.types.job_status.serialize_xml(value["status"], el, "Status")
    if "status_update_reason" in value:
        SubElement(el, "StatusUpdateReason").text = str(value["status_update_reason"])


def deserialize_xml(el: Element) -> UpdateJobStatusResult:
    out: UpdateJobStatusResult = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3_control.types.job_status

        out["status"] = aws_sdk_s3_control.types.job_status.deserialize_xml(
            child_status
        )
    child_status_update_reason = el.find("StatusUpdateReason")
    if child_status_update_reason is not None:
        out["status_update_reason"] = str(child_status_update_reason.text or "")
    return out
