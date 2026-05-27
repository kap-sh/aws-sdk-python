"""Generated from Smithy shape ``com.amazonaws.ecs#ListAccountSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.settings
    import aws_sdk_ecs.types.string


class ListAccountSettingsResponse(TypedDict):
    settings: NotRequired["aws_sdk_ecs.types.settings.Settings"]
    """<p>The account settings for the resource.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListAccountSettings</code> request. When the results of a <code>ListAccountSettings</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
