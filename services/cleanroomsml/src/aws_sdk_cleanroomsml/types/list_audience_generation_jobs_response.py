"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceGenerationJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_generation_job_list
    import aws_sdk_cleanroomsml.types.next_token


class ListAudienceGenerationJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    audience_generation_jobs: "aws_sdk_cleanroomsml.types.audience_generation_job_list.AudienceGenerationJobList"
    """<p>The audience generation jobs that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceGenerationJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.audience_generation_job_list

    out["audienceGenerationJobs"] = (
        aws_sdk_cleanroomsml.types.audience_generation_job_list.serialize_json(
            value["audience_generation_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAudienceGenerationJobsResponse:
    out: ListAudienceGenerationJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "audienceGenerationJobs" in data:
        import aws_sdk_cleanroomsml.types.audience_generation_job_list

        out["audience_generation_jobs"] = (
            aws_sdk_cleanroomsml.types.audience_generation_job_list.deserialize_json(
                data["audienceGenerationJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListAudienceGenerationJobsResponse.audience_generation_jobs required"
        )
    return out
