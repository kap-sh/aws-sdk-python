"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_export_job_list
    import capo_cleanroomsml.types.next_token


class ListAudienceExportJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    audience_export_jobs: (
        "capo_cleanroomsml.types.audience_export_job_list.AudienceExportJobList"
    )
    """<p>The audience export jobs that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceExportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.audience_export_job_list

    out["audienceExportJobs"] = (
        capo_cleanroomsml.types.audience_export_job_list.serialize_json(
            value["audience_export_jobs"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAudienceExportJobsResponse:
    out: ListAudienceExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "audienceExportJobs" in data:
        import capo_cleanroomsml.types.audience_export_job_list

        out["audience_export_jobs"] = (
            capo_cleanroomsml.types.audience_export_job_list.deserialize_json(
                data["audienceExportJobs"]
            )
        )
    else:
        raise DeserializationError(
            "ListAudienceExportJobsResponse.audience_export_jobs required"
        )
    return out
