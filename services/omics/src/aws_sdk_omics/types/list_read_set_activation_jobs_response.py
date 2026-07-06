"""Generated from Smithy shape ``com.amazonaws.omics#ListReadSetActivationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.activate_read_set_job_list
    import aws_sdk_omics.types.next_token


class ListReadSetActivationJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    activation_jobs: NotRequired[
        "aws_sdk_omics.types.activate_read_set_job_list.ActivateReadSetJobList"
    ]
    """<p>A list of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadSetActivationJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "activation_jobs" in value:
        import aws_sdk_omics.types.activate_read_set_job_list

        out["activationJobs"] = (
            aws_sdk_omics.types.activate_read_set_job_list.serialize_json(
                value["activation_jobs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReadSetActivationJobsResponse:
    out: ListReadSetActivationJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "activationJobs" in data:
        import aws_sdk_omics.types.activate_read_set_job_list

        out["activation_jobs"] = (
            aws_sdk_omics.types.activate_read_set_job_list.deserialize_json(
                data["activationJobs"]
            )
        )
    return out
