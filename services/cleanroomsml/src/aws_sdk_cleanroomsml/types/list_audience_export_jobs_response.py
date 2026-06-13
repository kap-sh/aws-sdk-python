"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceExportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_export_job_list
    import aws_sdk_cleanroomsml.types.next_token


class ListAudienceExportJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    audience_export_jobs: (
        "aws_sdk_cleanroomsml.types.audience_export_job_list.AudienceExportJobList"
    )
    """<p>The audience export jobs that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceExportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.audience_export_job_list

    out["audienceExportJobs"] = (
        aws_sdk_cleanroomsml.types.audience_export_job_list.serialize_json(
            value["audience_export_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAudienceExportJobsResponse:
    out: ListAudienceExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "audienceExportJobs" in data:
        import aws_sdk_cleanroomsml.types.audience_export_job_list

        out["audience_export_jobs"] = (
            aws_sdk_cleanroomsml.types.audience_export_job_list.deserialize_json(
                data["audienceExportJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListAudienceExportJobsResponse.audience_export_jobs required"
        )
    return out
