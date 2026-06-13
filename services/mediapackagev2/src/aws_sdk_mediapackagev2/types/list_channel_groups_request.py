"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListChannelGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.list_resource_max_results


class ListChannelGroupsRequest(TypedDict):
    max_results: (
        "aws_sdk_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
    )
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelGroupsRequest:
    out: ListChannelGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
