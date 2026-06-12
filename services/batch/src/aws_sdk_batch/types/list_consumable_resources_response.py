"""Generated from Smithy shape ``com.amazonaws.batch#ListConsumableResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.consumable_resource_summary_list
    import aws_sdk_batch.types.string


class ListConsumableResourcesResponse(TypedDict):
    consumable_resources: NotRequired[
        "aws_sdk_batch.types.consumable_resource_summary_list.ConsumableResourceSummaryList"
    ]
    """<p>A list of consumable resources that match the request.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListConsumableResources</code> request. When the results of a <code>ListConsumableResources</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConsumableResourcesResponse) -> dict:
    out: dict = {}
    if "consumable_resources" in value:
        import aws_sdk_batch.types.consumable_resource_summary_list

        out["consumableResources"] = (
            aws_sdk_batch.types.consumable_resource_summary_list.serialize_json(
                value["consumable_resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConsumableResourcesResponse:
    out: ListConsumableResourcesResponse = {}  # type: ignore[typeddict-item]
    if "consumableResources" in data:
        import aws_sdk_batch.types.consumable_resource_summary_list

        out["consumable_resources"] = (
            aws_sdk_batch.types.consumable_resource_summary_list.deserialize_json(
                data["consumableResources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
