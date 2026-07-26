"""Generated from Smithy shape ``com.amazonaws.s3control#JobDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.confirmation_required
    import capo_s3_control.types.iam_role_arn
    import capo_s3_control.types.job_arn
    import capo_s3_control.types.job_creation_time
    import capo_s3_control.types.job_failure_list
    import capo_s3_control.types.job_id
    import capo_s3_control.types.job_manifest
    import capo_s3_control.types.job_manifest_generator
    import capo_s3_control.types.job_operation
    import capo_s3_control.types.job_priority
    import capo_s3_control.types.job_progress_summary
    import capo_s3_control.types.job_report
    import capo_s3_control.types.job_status
    import capo_s3_control.types.job_status_update_reason
    import capo_s3_control.types.job_termination_date
    import capo_s3_control.types.non_empty_max_length256_string
    import capo_s3_control.types.s3_generated_manifest_descriptor
    import capo_s3_control.types.suspended_cause
    import capo_s3_control.types.suspended_date


class JobDescriptor(TypedDict, closed=True):
    job_id: NotRequired["capo_s3_control.types.job_id.JobId"]
    """<p>The ID for the specified job.</p>"""
    confirmation_required: NotRequired[
        "capo_s3_control.types.confirmation_required.ConfirmationRequired"
    ]
    """<p>Indicates whether confirmation is required before Amazon S3 begins running the specified job. Confirmation is required only for jobs created through the Amazon S3 console.</p>"""
    description: NotRequired[
        "capo_s3_control.types.non_empty_max_length256_string.NonEmptyMaxLength256String"
    ]
    """<p>The description for this job, if one was provided in this job's <code>Create Job</code> request.</p>"""
    job_arn: NotRequired["capo_s3_control.types.job_arn.JobArn"]
    """<p>The Amazon Resource Name (ARN) for this job.</p>"""
    status: NotRequired["capo_s3_control.types.job_status.JobStatus"]
    """<p>The current status of the specified job.</p>"""
    manifest: NotRequired["capo_s3_control.types.job_manifest.JobManifest"]
    """<p>The configuration information for the specified job's manifest object.</p>"""
    operation: NotRequired["capo_s3_control.types.job_operation.JobOperation"]
    """<p>The operation that the specified job is configured to run on the objects listed in the manifest.</p>"""
    priority: "capo_s3_control.types.job_priority.JobPriority"
    """<p>The priority of the specified job.</p>"""
    progress_summary: NotRequired[
        "capo_s3_control.types.job_progress_summary.JobProgressSummary"
    ]
    """<p>Describes the total number of tasks that the specified job has run, the number of tasks that succeeded, and the number of tasks that failed.</p>"""
    status_update_reason: NotRequired[
        "capo_s3_control.types.job_status_update_reason.JobStatusUpdateReason"
    ]
    """<p>The reason for updating the job.</p>"""
    failure_reasons: NotRequired[
        "capo_s3_control.types.job_failure_list.JobFailureList"
    ]
    """<p>If the specified job failed, this field contains information describing the failure.</p>"""
    report: NotRequired["capo_s3_control.types.job_report.JobReport"]
    """<p>Contains the configuration information for the job-completion report if you requested one in the <code>Create Job</code> request.</p>"""
    creation_time: NotRequired[
        "capo_s3_control.types.job_creation_time.JobCreationTime"
    ]
    """<p>A timestamp indicating when this job was created.</p>"""
    termination_date: NotRequired[
        "capo_s3_control.types.job_termination_date.JobTerminationDate"
    ]
    """<p>A timestamp indicating when this job terminated. A job's termination date is the date and time when it succeeded, failed, or was canceled.</p>"""
    role_arn: NotRequired["capo_s3_control.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) role assigned to run the tasks for this job.</p>"""
    suspended_date: NotRequired["capo_s3_control.types.suspended_date.SuspendedDate"]
    """<p>The timestamp when this job was suspended, if it has been suspended.</p>"""
    suspended_cause: NotRequired["capo_s3_control.types.suspended_cause.SuspendedCause"]
    """<p>The reason why the specified job was suspended. A job is only suspended if you create it through the Amazon S3 console. When you create the job, it enters the <code>Suspended</code> state to await confirmation before running. After you confirm the job, it automatically exits the <code>Suspended</code> state.</p>"""
    manifest_generator: NotRequired[
        "capo_s3_control.types.job_manifest_generator.JobManifestGenerator"
    ]
    """<p>The manifest generator that was used to generate a job manifest for this job.</p>"""
    generated_manifest_descriptor: NotRequired[
        "capo_s3_control.types.s3_generated_manifest_descriptor.S3GeneratedManifestDescriptor"
    ]
    """<p>The attribute of the JobDescriptor containing details about the job's generated manifest.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobDescriptor, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "job_id" in value:
        SubElement(el, "JobId").text = str(value["job_id"])
    if "confirmation_required" in value:
        SubElement(el, "ConfirmationRequired").text = (
            "true" if value["confirmation_required"] else "false"
        )
    if "description" in value:
        SubElement(el, "Description").text = str(value["description"])
    if "job_arn" in value:
        SubElement(el, "JobArn").text = str(value["job_arn"])
    if "status" in value:
        import capo_s3_control.types.job_status

        capo_s3_control.types.job_status.serialize_xml(value["status"], el, "Status")
    if "manifest" in value:
        import capo_s3_control.types.job_manifest

        capo_s3_control.types.job_manifest.serialize_xml(
            value["manifest"], el, "Manifest"
        )
    if "operation" in value:
        import capo_s3_control.types.job_operation

        capo_s3_control.types.job_operation.serialize_xml(
            value["operation"], el, "Operation"
        )
    SubElement(el, "Priority").text = str(value.get("priority", 0))
    if "progress_summary" in value:
        import capo_s3_control.types.job_progress_summary

        capo_s3_control.types.job_progress_summary.serialize_xml(
            value["progress_summary"], el, "ProgressSummary"
        )
    if "status_update_reason" in value:
        SubElement(el, "StatusUpdateReason").text = str(value["status_update_reason"])
    if "failure_reasons" in value:
        import capo_s3_control.types.job_failure_list

        capo_s3_control.types.job_failure_list.serialize_xml(
            value["failure_reasons"], el, "FailureReasons"
        )
    if "report" in value:
        import capo_s3_control.types.job_report

        capo_s3_control.types.job_report.serialize_xml(value["report"], el, "Report")
    if "creation_time" in value:
        import capo_s3_control.types.job_creation_time

        capo_s3_control.types.job_creation_time.serialize_xml(
            value["creation_time"], el, "CreationTime"
        )
    if "termination_date" in value:
        import capo_s3_control.types.job_termination_date

        capo_s3_control.types.job_termination_date.serialize_xml(
            value["termination_date"], el, "TerminationDate"
        )
    if "role_arn" in value:
        SubElement(el, "RoleArn").text = str(value["role_arn"])
    if "suspended_date" in value:
        import capo_s3_control.types.suspended_date

        capo_s3_control.types.suspended_date.serialize_xml(
            value["suspended_date"], el, "SuspendedDate"
        )
    if "suspended_cause" in value:
        SubElement(el, "SuspendedCause").text = str(value["suspended_cause"])
    if "manifest_generator" in value:
        import capo_s3_control.types.job_manifest_generator

        capo_s3_control.types.job_manifest_generator.serialize_xml(
            value["manifest_generator"], el, "ManifestGenerator"
        )
    if "generated_manifest_descriptor" in value:
        import capo_s3_control.types.s3_generated_manifest_descriptor

        capo_s3_control.types.s3_generated_manifest_descriptor.serialize_xml(
            value["generated_manifest_descriptor"], el, "GeneratedManifestDescriptor"
        )


def deserialize_xml(el: Element) -> JobDescriptor:
    out: JobDescriptor = {}  # type: ignore[typeddict-item]
    child_job_id = el.find("JobId")
    if child_job_id is not None:
        out["job_id"] = str(child_job_id.text or "")
    child_confirmation_required = el.find("ConfirmationRequired")
    if child_confirmation_required is not None:
        out["confirmation_required"] = (
            child_confirmation_required.text or ""
        ).lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_job_arn = el.find("JobArn")
    if child_job_arn is not None:
        out["job_arn"] = str(child_job_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.job_status

        out["status"] = capo_s3_control.types.job_status.deserialize_xml(child_status)
    child_manifest = el.find("Manifest")
    if child_manifest is not None:
        import capo_s3_control.types.job_manifest

        out["manifest"] = capo_s3_control.types.job_manifest.deserialize_xml(
            child_manifest
        )
    child_operation = el.find("Operation")
    if child_operation is not None:
        import capo_s3_control.types.job_operation

        out["operation"] = capo_s3_control.types.job_operation.deserialize_xml(
            child_operation
        )
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    else:
        out["priority"] = 0
    child_progress_summary = el.find("ProgressSummary")
    if child_progress_summary is not None:
        import capo_s3_control.types.job_progress_summary

        out["progress_summary"] = (
            capo_s3_control.types.job_progress_summary.deserialize_xml(
                child_progress_summary
            )
        )
    child_status_update_reason = el.find("StatusUpdateReason")
    if child_status_update_reason is not None:
        out["status_update_reason"] = str(child_status_update_reason.text or "")
    child_failure_reasons = el.find("FailureReasons")
    if child_failure_reasons is not None:
        import capo_s3_control.types.job_failure_list

        out["failure_reasons"] = capo_s3_control.types.job_failure_list.deserialize_xml(
            child_failure_reasons
        )
    child_report = el.find("Report")
    if child_report is not None:
        import capo_s3_control.types.job_report

        out["report"] = capo_s3_control.types.job_report.deserialize_xml(child_report)
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_s3_control.types.job_creation_time

        out["creation_time"] = capo_s3_control.types.job_creation_time.deserialize_xml(
            child_creation_time
        )
    child_termination_date = el.find("TerminationDate")
    if child_termination_date is not None:
        import capo_s3_control.types.job_termination_date

        out["termination_date"] = (
            capo_s3_control.types.job_termination_date.deserialize_xml(
                child_termination_date
            )
        )
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_suspended_date = el.find("SuspendedDate")
    if child_suspended_date is not None:
        import capo_s3_control.types.suspended_date

        out["suspended_date"] = capo_s3_control.types.suspended_date.deserialize_xml(
            child_suspended_date
        )
    child_suspended_cause = el.find("SuspendedCause")
    if child_suspended_cause is not None:
        out["suspended_cause"] = str(child_suspended_cause.text or "")
    child_manifest_generator = el.find("ManifestGenerator")
    if child_manifest_generator is not None:
        import capo_s3_control.types.job_manifest_generator

        out["manifest_generator"] = (
            capo_s3_control.types.job_manifest_generator.deserialize_xml(
                child_manifest_generator
            )
        )
    child_generated_manifest_descriptor = el.find("GeneratedManifestDescriptor")
    if child_generated_manifest_descriptor is not None:
        import capo_s3_control.types.s3_generated_manifest_descriptor

        out["generated_manifest_descriptor"] = (
            capo_s3_control.types.s3_generated_manifest_descriptor.deserialize_xml(
                child_generated_manifest_descriptor
            )
        )
    return out
