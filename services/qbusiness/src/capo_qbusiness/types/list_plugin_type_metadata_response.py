"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginTypeMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.list_plugin_type_metadata_summaries
    import capo_qbusiness.types.next_token


class ListPluginTypeMetadataResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of plugin metadata.</p>"""
    items: NotRequired[
        "capo_qbusiness.types.list_plugin_type_metadata_summaries.ListPluginTypeMetadataSummaries"
    ]
    """<p>An array of information on plugin metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginTypeMetadataResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import capo_qbusiness.types.list_plugin_type_metadata_summaries

        out["items"] = (
            capo_qbusiness.types.list_plugin_type_metadata_summaries.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPluginTypeMetadataResponse:
    out: ListPluginTypeMetadataResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import capo_qbusiness.types.list_plugin_type_metadata_summaries

        out["items"] = (
            capo_qbusiness.types.list_plugin_type_metadata_summaries.deserialize_json(
                data["items"]
            )
        )
    return out
