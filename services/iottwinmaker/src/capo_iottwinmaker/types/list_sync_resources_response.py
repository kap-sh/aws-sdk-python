"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListSyncResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.sync_resource_summaries


class ListSyncResourcesResponse(TypedDict, closed=True):
    sync_resources: NotRequired[
        "capo_iottwinmaker.types.sync_resource_summaries.SyncResourceSummaries"
    ]
    """<p>The sync resources.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSyncResourcesResponse) -> dict:
    out: dict = {}
    if "sync_resources" in value:
        import capo_iottwinmaker.types.sync_resource_summaries

        out["syncResources"] = (
            capo_iottwinmaker.types.sync_resource_summaries.serialize_json(
                value["sync_resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSyncResourcesResponse:
    out: ListSyncResourcesResponse = {}  # type: ignore[typeddict-item]
    if "syncResources" in data:
        import capo_iottwinmaker.types.sync_resource_summaries

        out["sync_resources"] = (
            capo_iottwinmaker.types.sync_resource_summaries.deserialize_json(
                data["syncResources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
