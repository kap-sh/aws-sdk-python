"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.job_name_list


class BatchGetJobsRequest(TypedDict):
    job_names: "aws_sdk_glue.types.job_name_list.JobNameList"
    """<p>A list of job names, which might be the names returned from the <code>ListJobs</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetJobsRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.job_name_list

    out["JobNames"] = aws_sdk_glue.types.job_name_list.serialize_aws_json_1_1(
        value["job_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetJobsRequest:
    out: BatchGetJobsRequest = {}  # type: ignore[typeddict-item]
    if "JobNames" in data:
        import aws_sdk_glue.types.job_name_list

        out["job_names"] = aws_sdk_glue.types.job_name_list.deserialize_aws_json_1_1(
            data["JobNames"]
        )
    else:
        raise DeserializationError("BatchGetJobsRequest.job_names required")
    return out
