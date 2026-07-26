"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListPluginsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.plugins


class ListPluginsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of plugins.</p>"""
    plugins: NotRequired["capo_qbusiness.types.plugins.Plugins"]
    """<p>Information about a configured plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "plugins" in value:
        import capo_qbusiness.types.plugins

        out["plugins"] = capo_qbusiness.types.plugins.serialize_json(value["plugins"])
    return out


def deserialize_json(data: dict) -> ListPluginsResponse:
    out: ListPluginsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "plugins" in data:
        import capo_qbusiness.types.plugins

        out["plugins"] = capo_qbusiness.types.plugins.deserialize_json(data["plugins"])
    return out
