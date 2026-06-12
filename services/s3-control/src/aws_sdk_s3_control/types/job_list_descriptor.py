"""Generated from Smithy shape ``com.amazonaws.s3control#JobListDescriptor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.job_creation_time
    import aws_sdk_s3_control.types.job_id
    import aws_sdk_s3_control.types.job_priority
    import aws_sdk_s3_control.types.job_progress_summary
    import aws_sdk_s3_control.types.job_status
    import aws_sdk_s3_control.types.job_termination_date
    import aws_sdk_s3_control.types.non_empty_max_length256_string
    import aws_sdk_s3_control.types.operation_name


class JobListDescriptor(TypedDict):
    job_id: NotRequired["aws_sdk_s3_control.types.job_id.JobId"]
    """<p>The ID for the specified job.</p>"""
    description: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length256_string.NonEmptyMaxLength256String"
    ]
    """<p>The user-specified description that was included in the specified job's <code>Create Job</code> request.</p>"""
    operation: NotRequired["aws_sdk_s3_control.types.operation_name.OperationName"]
    """<p>The operation that the specified job is configured to run on every object listed in the manifest.</p>"""
    priority: "aws_sdk_s3_control.types.job_priority.JobPriority"
    """<p>The current priority for the specified job.</p>"""
    status: NotRequired["aws_sdk_s3_control.types.job_status.JobStatus"]
    """<p>The specified job's current status.</p>"""
    creation_time: NotRequired[
        "aws_sdk_s3_control.types.job_creation_time.JobCreationTime"
    ]
    """<p>A timestamp indicating when the specified job was created.</p>"""
    termination_date: NotRequired[
        "aws_sdk_s3_control.types.job_termination_date.JobTerminationDate"
    ]
    """<p>A timestamp indicating when the specified job terminated. A job's termination date is the date and time when it succeeded, failed, or was canceled.</p>"""
    progress_summary: NotRequired[
        "aws_sdk_s3_control.types.job_progress_summary.JobProgressSummary"
    ]
    """<p>Describes the total number of tasks that the specified job has run, the number of tasks that succeeded, and the number of tasks that failed.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobListDescriptor, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "job_id" in value:
        SubElement(el, "JobId").text = str(value["job_id"])
    if "description" in value:
        SubElement(el, "Description").text = str(value["description"])
    if "operation" in value:
        import aws_sdk_s3_control.types.operation_name

        aws_sdk_s3_control.types.operation_name.serialize_xml(
            value["operation"], el, "Operation"
        )
    SubElement(el, "Priority").text = str(value.get("priority", 0))
    if "status" in value:
        import aws_sdk_s3_control.types.job_status

        aws_sdk_s3_control.types.job_status.serialize_xml(value["status"], el, "Status")
    if "creation_time" in value:
        import aws_sdk_s3_control.types.job_creation_time

        aws_sdk_s3_control.types.job_creation_time.serialize_xml(
            value["creation_time"], el, "CreationTime"
        )
    if "termination_date" in value:
        import aws_sdk_s3_control.types.job_termination_date

        aws_sdk_s3_control.types.job_termination_date.serialize_xml(
            value["termination_date"], el, "TerminationDate"
        )
    if "progress_summary" in value:
        import aws_sdk_s3_control.types.job_progress_summary

        aws_sdk_s3_control.types.job_progress_summary.serialize_xml(
            value["progress_summary"], el, "ProgressSummary"
        )


def deserialize_xml(el: Element) -> JobListDescriptor:
    out: JobListDescriptor = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_operation = el.find("Operation")
    if child_operation is not None:
        import aws_sdk_s3_control.types.operation_name

        out["operation"] = aws_sdk_s3_control.types.operation_name.deserialize_xml(
            child_operation
        )
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    else:
        out["priority"] = 0
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3_control.types.job_status

        out["status"] = aws_sdk_s3_control.types.job_status.deserialize_xml(
            child_status
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_s3_control.types.job_creation_time

        out["creation_time"] = (
            aws_sdk_s3_control.types.job_creation_time.deserialize_xml(
                child_creation_time
            )
        )
    child_termination_date = el.find("TerminationDate")
    if child_termination_date is not None:
        import aws_sdk_s3_control.types.job_termination_date

        out["termination_date"] = (
            aws_sdk_s3_control.types.job_termination_date.deserialize_xml(
                child_termination_date
            )
        )
    child_progress_summary = el.find("ProgressSummary")
    if child_progress_summary is not None:
        import aws_sdk_s3_control.types.job_progress_summary

        out["progress_summary"] = (
            aws_sdk_s3_control.types.job_progress_summary.deserialize_xml(
                child_progress_summary
            )
        )
    return out
