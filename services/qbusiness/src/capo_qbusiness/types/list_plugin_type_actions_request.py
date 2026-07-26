"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginTypeActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.max_results_integer_for_list_plugin_type_actions
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.plugin_type


class ListPluginTypeActionsRequest(TypedDict, closed=True):
    plugin_type: "capo_qbusiness.types.plugin_type.PluginType"
    """<p>The type of the plugin.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the number of plugins returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugins.</p>"""
    max_results: NotRequired[
        "capo_qbusiness.types.max_results_integer_for_list_plugin_type_actions.MaxResultsIntegerForListPluginTypeActions"
    ]
    """<p>The maximum number of plugins to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginTypeActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPluginTypeActionsRequest:
    out: ListPluginTypeActionsRequest = {}  # type: ignore[typeddict-item]
    return out
