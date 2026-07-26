"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListChannelGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.channel_groups_list


class ListChannelGroupsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mediapackagev2.types.channel_groups_list.ChannelGroupsList"
    ]
    """<p>The objects being returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelGroupsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mediapackagev2.types.channel_groups_list

        out["Items"] = capo_mediapackagev2.types.channel_groups_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelGroupsResponse:
    out: ListChannelGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_mediapackagev2.types.channel_groups_list

        out["items"] = capo_mediapackagev2.types.channel_groups_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
