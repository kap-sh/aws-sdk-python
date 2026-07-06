"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListHarvestJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.harvest_jobs_list


class ListHarvestJobsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_mediapackagev2.types.harvest_jobs_list.HarvestJobsList"]
    """<p>An array of harvest job objects that match the specified criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>A token used for pagination. Include this value in subsequent requests to retrieve the next set of results. If null, there are no more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarvestJobsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediapackagev2.types.harvest_jobs_list

        out["Items"] = aws_sdk_mediapackagev2.types.harvest_jobs_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHarvestJobsResponse:
    out: ListHarvestJobsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediapackagev2.types.harvest_jobs_list

        out["items"] = aws_sdk_mediapackagev2.types.harvest_jobs_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
