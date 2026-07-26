"""Generated from Smithy shape ``com.amazonaws.personalize#ListDataDeletionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.data_deletion_jobs
    import capo_personalize.types.next_token


class ListDataDeletionJobsResponse(TypedDict, closed=True):
    data_deletion_jobs: NotRequired[
        "capo_personalize.types.data_deletion_jobs.DataDeletionJobs"
    ]
    """<p>The list of data deletion jobs.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of data deletion jobs (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataDeletionJobsResponse) -> dict:
    out: dict = {}
    if "data_deletion_jobs" in value:
        import capo_personalize.types.data_deletion_jobs

        out["dataDeletionJobs"] = (
            capo_personalize.types.data_deletion_jobs.serialize_aws_json_1_1(
                value["data_deletion_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataDeletionJobsResponse:
    out: ListDataDeletionJobsResponse = {}  # type: ignore[typeddict-item]
    if "dataDeletionJobs" in data:
        import capo_personalize.types.data_deletion_jobs

        out["data_deletion_jobs"] = (
            capo_personalize.types.data_deletion_jobs.deserialize_aws_json_1_1(
                data["dataDeletionJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
