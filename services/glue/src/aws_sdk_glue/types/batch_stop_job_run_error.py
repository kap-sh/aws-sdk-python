"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.id_string
    import aws_sdk_glue.types.name_string


class BatchStopJobRunError(TypedDict):
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the job definition that is used in the job run in question.</p>"""
    job_run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The <code>JobRunId</code> of the job run in question.</p>"""
    error_detail: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>Specifies details about the error that was encountered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunError) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    if "error_detail" in value:
        import aws_sdk_glue.types.error_detail

        out["ErrorDetail"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStopJobRunError:
    out: BatchStopJobRunError = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    if "ErrorDetail" in data:
        import aws_sdk_glue.types.error_detail

        out["error_detail"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["ErrorDetail"]
        )
    return out
