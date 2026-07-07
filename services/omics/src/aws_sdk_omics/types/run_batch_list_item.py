"""Generated from Smithy shape ``com.amazonaws.omics#RunBatchListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_arn
    import aws_sdk_omics.types.run_id
    import aws_sdk_omics.types.run_setting_id
    import aws_sdk_omics.types.run_uuid
    import aws_sdk_omics.types.submission_failure_message
    import aws_sdk_omics.types.submission_failure_reason
    import aws_sdk_omics.types.submission_status


class RunBatchListItem(TypedDict, closed=True):
    run_setting_id: NotRequired["aws_sdk_omics.types.run_setting_id.RunSettingId"]
    """<p>The customer-provided identifier for the run configuration. Use this to correlate results back to the input configuration provided in <code>inlineSettings</code> or <code>s3UriSettings</code>.</p>"""
    run_id: NotRequired["aws_sdk_omics.types.run_id.RunId"]
    """<p>The HealthOmics-generated identifier for the workflow run. Empty if submission failed.</p>"""
    run_internal_uuid: NotRequired["aws_sdk_omics.types.run_uuid.RunUuid"]
    """<p>The universally unique identifier (UUID) for the run.</p>"""
    run_arn: NotRequired["aws_sdk_omics.types.run_arn.RunArn"]
    """<p>The unique ARN of the workflow run.</p>"""
    submission_status: NotRequired[
        "aws_sdk_omics.types.submission_status.SubmissionStatus"
    ]
    """<p>The submission outcome for this run.</p>"""
    submission_failure_reason: NotRequired[
        "aws_sdk_omics.types.submission_failure_reason.SubmissionFailureReason"
    ]
    """<p>The error category for a failed submission. See the run-level failure table in the HealthOmics User Guide for details on each value.</p>"""
    submission_failure_message: NotRequired[
        "aws_sdk_omics.types.submission_failure_message.SubmissionFailureMessage"
    ]
    """<p>A detailed message describing the submission failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunBatchListItem) -> dict:
    out: dict = {}
    if "run_setting_id" in value:
        out["runSettingId"] = value["run_setting_id"]
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "run_internal_uuid" in value:
        out["runInternalUuid"] = value["run_internal_uuid"]
    if "run_arn" in value:
        out["runArn"] = value["run_arn"]
    if "submission_status" in value:
        out["submissionStatus"] = value["submission_status"]
    if "submission_failure_reason" in value:
        out["submissionFailureReason"] = value["submission_failure_reason"]
    if "submission_failure_message" in value:
        out["submissionFailureMessage"] = value["submission_failure_message"]
    return out


def deserialize_json(data: dict) -> RunBatchListItem:
    out: RunBatchListItem = {}  # type: ignore[typeddict-item]
    if "runSettingId" in data:
        out["run_setting_id"] = data["runSettingId"]
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "runInternalUuid" in data:
        out["run_internal_uuid"] = data["runInternalUuid"]
    if "runArn" in data:
        out["run_arn"] = data["runArn"]
    if "submissionStatus" in data:
        out["submission_status"] = data["submissionStatus"]
    if "submissionFailureReason" in data:
        out["submission_failure_reason"] = data["submissionFailureReason"]
    if "submissionFailureMessage" in data:
        out["submission_failure_message"] = data["submissionFailureMessage"]
    return out
