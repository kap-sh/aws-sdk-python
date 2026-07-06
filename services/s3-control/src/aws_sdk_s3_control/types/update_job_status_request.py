"""Generated from Smithy shape ``com.amazonaws.s3control#UpdateJobStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.job_id
    import aws_sdk_s3_control.types.job_status_update_reason
    import aws_sdk_s3_control.types.requested_job_status


class UpdateJobStatusRequest(TypedDict, closed=True):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>"""
    job_id: "aws_sdk_s3_control.types.job_id.JobId"
    """<p>The ID of the job whose status you want to update.</p>"""
    requested_job_status: (
        "aws_sdk_s3_control.types.requested_job_status.RequestedJobStatus"
    )
    """<p>The status that you want to move the specified job to.</p>"""
    status_update_reason: NotRequired[
        "aws_sdk_s3_control.types.job_status_update_reason.JobStatusUpdateReason"
    ]
    """<p>A description of the reason why you want to change the specified job's status. This field can be any string up to the maximum length.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateJobStatusRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> UpdateJobStatusRequest:
    out: UpdateJobStatusRequest = {}  # type: ignore[typeddict-item]
    return out
