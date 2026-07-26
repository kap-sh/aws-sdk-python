"""Generated from Smithy shape ``com.amazonaws.omics#GetBatchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.batch_arn
    import capo_omics.types.batch_id
    import capo_omics.types.batch_name
    import capo_omics.types.batch_status
    import capo_omics.types.batch_timestamp
    import capo_omics.types.batch_uuid
    import capo_omics.types.default_run_setting
    import capo_omics.types.run_summary
    import capo_omics.types.submission_summary
    import capo_omics.types.tag_map


class GetBatchResponse(TypedDict, closed=True):
    id: NotRequired["capo_omics.types.batch_id.BatchId"]
    """<p>The identifier portion of the run batch ARN.</p>"""
    arn: NotRequired["capo_omics.types.batch_arn.BatchArn"]
    """<p>The unique ARN of the run batch.</p>"""
    uuid: NotRequired["capo_omics.types.batch_uuid.BatchUuid"]
    """<p>The universally unique identifier (UUID) for the run batch.</p>"""
    name: NotRequired["capo_omics.types.batch_name.BatchName"]
    """<p>The optional user-friendly name of the batch.</p>"""
    status: NotRequired["capo_omics.types.batch_status.BatchStatus"]
    """<p>The current status of the run batch. Possible values: <code>CREATING</code> (initial setup), <code>PENDING</code> (ready to submit runs), <code>SUBMITTING</code> (submitting runs), <code>INPROGRESS</code> (runs executing), <code>STOPPING</code> (cancellation in progress), <code>PROCESSED</code> (all runs completed), <code>CANCELLED</code> (batch cancelled), <code>FAILED</code> (batch failed), <code>RUNS_DELETING</code> (deleting runs), <code>RUNS_DELETED</code> (runs deleted).</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>AWS tags associated with the run batch.</p>"""
    total_runs: NotRequired["int"]
    """<p>The total number of runs in the batch.</p>"""
    default_run_setting: NotRequired[
        "capo_omics.types.default_run_setting.DefaultRunSetting"
    ]
    """<p>The shared configuration applied to all runs in the batch. See <code>DefaultRunSetting</code>.</p>"""
    submission_summary: NotRequired[
        "capo_omics.types.submission_summary.SubmissionSummary"
    ]
    """<p>A summary of run submission outcomes. See <code>SubmissionSummary</code>.</p>"""
    run_summary: NotRequired["capo_omics.types.run_summary.RunSummary"]
    """<p>A summary of run execution states. Run execution counts are eventually consistent and may lag behind actual run states. Final counts are accurate once the batch reaches <code>PROCESSED</code> status. See <code>RunSummary</code>.</p>"""
    creation_time: NotRequired["capo_omics.types.batch_timestamp.BatchTimestamp"]
    """<p>The timestamp when the batch was created.</p>"""
    submitted_time: NotRequired["capo_omics.types.batch_timestamp.BatchTimestamp"]
    """<p>The timestamp when all run submissions completed.</p>"""
    processed_time: NotRequired["capo_omics.types.batch_timestamp.BatchTimestamp"]
    """<p>The timestamp when all run executions completed.</p>"""
    failed_time: NotRequired["capo_omics.types.batch_timestamp.BatchTimestamp"]
    """<p>The timestamp when the batch transitioned to a <code>FAILED</code> status.</p>"""
    failure_reason: NotRequired["str"]
    """<p>A description of the batch failure. Present only when status is <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBatchResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "total_runs" in value:
        out["totalRuns"] = value["total_runs"]
    if "default_run_setting" in value:
        import capo_omics.types.default_run_setting

        out["defaultRunSetting"] = capo_omics.types.default_run_setting.serialize_json(
            value["default_run_setting"]
        )
    if "submission_summary" in value:
        import capo_omics.types.submission_summary

        out["submissionSummary"] = capo_omics.types.submission_summary.serialize_json(
            value["submission_summary"]
        )
    if "run_summary" in value:
        import capo_omics.types.run_summary

        out["runSummary"] = capo_omics.types.run_summary.serialize_json(
            value["run_summary"]
        )
    if "creation_time" in value:
        import capo_omics.types.batch_timestamp

        out["creationTime"] = capo_omics.types.batch_timestamp.serialize_json(
            value["creation_time"]
        )
    if "submitted_time" in value:
        import capo_omics.types.batch_timestamp

        out["submittedTime"] = capo_omics.types.batch_timestamp.serialize_json(
            value["submitted_time"]
        )
    if "processed_time" in value:
        import capo_omics.types.batch_timestamp

        out["processedTime"] = capo_omics.types.batch_timestamp.serialize_json(
            value["processed_time"]
        )
    if "failed_time" in value:
        import capo_omics.types.batch_timestamp

        out["failedTime"] = capo_omics.types.batch_timestamp.serialize_json(
            value["failed_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetBatchResponse:
    out: GetBatchResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "uuid" in data:
        out["uuid"] = data["uuid"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "tags" in data:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if "totalRuns" in data:
        out["total_runs"] = data["totalRuns"]
    if "defaultRunSetting" in data:
        import capo_omics.types.default_run_setting

        out["default_run_setting"] = (
            capo_omics.types.default_run_setting.deserialize_json(
                data["defaultRunSetting"]
            )
        )
    if "submissionSummary" in data:
        import capo_omics.types.submission_summary

        out["submission_summary"] = (
            capo_omics.types.submission_summary.deserialize_json(
                data["submissionSummary"]
            )
        )
    if "runSummary" in data:
        import capo_omics.types.run_summary

        out["run_summary"] = capo_omics.types.run_summary.deserialize_json(
            data["runSummary"]
        )
    if "creationTime" in data:
        import capo_omics.types.batch_timestamp

        out["creation_time"] = capo_omics.types.batch_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "submittedTime" in data:
        import capo_omics.types.batch_timestamp

        out["submitted_time"] = capo_omics.types.batch_timestamp.deserialize_json(
            data["submittedTime"]
        )
    if "processedTime" in data:
        import capo_omics.types.batch_timestamp

        out["processed_time"] = capo_omics.types.batch_timestamp.deserialize_json(
            data["processedTime"]
        )
    if "failedTime" in data:
        import capo_omics.types.batch_timestamp

        out["failed_time"] = capo_omics.types.batch_timestamp.deserialize_json(
            data["failedTime"]
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
