"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginTypeMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.max_results_integer_for_list_plugin_type_metadata
    import capo_qbusiness.types.next_token


class ListPluginTypeMetadataRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the metadata returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of metadata.</p>"""
    max_results: NotRequired[
        "capo_qbusiness.types.max_results_integer_for_list_plugin_type_metadata.MaxResultsIntegerForListPluginTypeMetadata"
    ]
    """<p>The maximum number of plugin metadata items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginTypeMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPluginTypeMetadataRequest:
    out: ListPluginTypeMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
