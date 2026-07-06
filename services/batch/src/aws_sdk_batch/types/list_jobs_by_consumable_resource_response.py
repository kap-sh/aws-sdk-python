"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsByConsumableResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.list_jobs_by_consumable_resource_summary_list
    import aws_sdk_batch.types.string


class ListJobsByConsumableResourceResponse(TypedDict, closed=True):
    jobs: NotRequired[
        "aws_sdk_batch.types.list_jobs_by_consumable_resource_summary_list.ListJobsByConsumableResourceSummaryList"
    ]
    """<p>The list of jobs that require the specified consumable resources.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListJobsByConsumableResource</code> request. When the results of a <code>ListJobsByConsumableResource</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByConsumableResourceResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_batch.types.list_jobs_by_consumable_resource_summary_list

        out["jobs"] = (
            aws_sdk_batch.types.list_jobs_by_consumable_resource_summary_list.serialize_json(
                value["jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsByConsumableResourceResponse:
    out: ListJobsByConsumableResourceResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_batch.types.list_jobs_by_consumable_resource_summary_list

        out["jobs"] = (
            aws_sdk_batch.types.list_jobs_by_consumable_resource_summary_list.deserialize_json(
                data["jobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
