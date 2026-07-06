"""Generated from Smithy shape ``com.amazonaws.glue#ListJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.job_name_list


class ListJobsResponse(TypedDict, closed=True):
    job_names: NotRequired["aws_sdk_glue.types.job_name_list.JobNameList"]
    """<p>The names of all jobs in the account, or the jobs with the specified tags.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if the returned list does not contain the last metric available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListJobsResponse) -> dict:
    out: dict = {}
    if "job_names" in value:
        import aws_sdk_glue.types.job_name_list

        out["JobNames"] = aws_sdk_glue.types.job_name_list.serialize_aws_json_1_1(
            value["job_names"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "JobNames" in data:
        import aws_sdk_glue.types.job_name_list

        out["job_names"] = aws_sdk_glue.types.job_name_list.deserialize_aws_json_1_1(
            data["JobNames"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
