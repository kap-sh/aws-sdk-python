"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_plugins
    import aws_sdk_qbusiness.types.next_token


class ListPluginsRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application the plugin is attached to.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of plugins.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_plugins.MaxResultsIntegerForListPlugins"
    ]
    """<p>The maximum number of documents to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPluginsRequest:
    out: ListPluginsRequest = {}  # type: ignore[typeddict-item]
    return out
