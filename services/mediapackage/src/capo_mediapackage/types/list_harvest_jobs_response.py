"""Generated from Smithy shape ``com.amazonaws.mediapackage#ListHarvestJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__list_of_harvest_job
    import capo_mediapackage.types.__string


class ListHarvestJobsResponse(TypedDict, closed=True):
    harvest_jobs: NotRequired[
        "capo_mediapackage.types.__list_of_harvest_job.__listOfHarvestJob"
    ]
    """A list of HarvestJob records."""
    next_token: NotRequired["capo_mediapackage.types.__string.__string"]
    """A token that can be used to resume pagination from the end of the collection."""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarvestJobsResponse) -> dict:
    out: dict = {}
    if "harvest_jobs" in value:
        import capo_mediapackage.types.__list_of_harvest_job

        out["harvestJobs"] = (
            capo_mediapackage.types.__list_of_harvest_job.serialize_json(
                value["harvest_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHarvestJobsResponse:
    out: ListHarvestJobsResponse = {}  # type: ignore[typeddict-item]
    if "harvestJobs" in data:
        import capo_mediapackage.types.__list_of_harvest_job

        out["harvest_jobs"] = (
            capo_mediapackage.types.__list_of_harvest_job.deserialize_json(
                data["harvestJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
