"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_stop_job_run_job_run_id_list
    import aws_sdk_glue.types.name_string


class BatchStopJobRunRequest(TypedDict):
    job_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the job definition for which to stop job runs.</p>"""
    job_run_ids: "aws_sdk_glue.types.batch_stop_job_run_job_run_id_list.BatchStopJobRunJobRunIdList"
    """<p>A list of the <code>JobRunIds</code> that should be stopped for that job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    import aws_sdk_glue.types.batch_stop_job_run_job_run_id_list

    out["JobRunIds"] = (
        aws_sdk_glue.types.batch_stop_job_run_job_run_id_list.serialize_aws_json_1_1(
            value["job_run_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStopJobRunRequest:
    out: BatchStopJobRunRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("BatchStopJobRunRequest.job_name required")
    if "JobRunIds" in data:
        import aws_sdk_glue.types.batch_stop_job_run_job_run_id_list

        out["job_run_ids"] = (
            aws_sdk_glue.types.batch_stop_job_run_job_run_id_list.deserialize_aws_json_1_1(
                data["JobRunIds"]
            )
        )
    else:
        raise DeserializationError("BatchStopJobRunRequest.job_run_ids required")
    return out
