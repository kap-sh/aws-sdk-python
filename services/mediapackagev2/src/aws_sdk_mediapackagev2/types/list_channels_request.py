"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListChannelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.list_resource_max_results
    import aws_sdk_mediapackagev2.types.resource_name


class ListChannelsRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    max_results: (
        "aws_sdk_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
    )
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    return out
