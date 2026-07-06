"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_actions
    import aws_sdk_qbusiness.types.next_token
    import aws_sdk_qbusiness.types.plugin_id


class ListPluginActionsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application the plugin is attached to.</p>"""
    plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the Amazon Q Business plugin.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the number of plugin actions returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugin actions.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_plugin_actions.MaxResultsIntegerForListPluginActions"
    ]
    """<p>The maximum number of plugin actions to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPluginActionsRequest:
    out: ListPluginActionsRequest = {}  # type: ignore[typeddict-item]
    return out
