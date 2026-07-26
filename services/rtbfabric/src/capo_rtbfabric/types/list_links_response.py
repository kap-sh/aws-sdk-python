"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListLinksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.link_list


class ListLinksResponse(TypedDict, closed=True):
    links: NotRequired["capo_rtbfabric.types.link_list.LinkList"]
    """<p>Information about created links.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinksResponse) -> dict:
    out: dict = {}
    if "links" in value:
        import capo_rtbfabric.types.link_list

        out["links"] = capo_rtbfabric.types.link_list.serialize_json(value["links"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinksResponse:
    out: ListLinksResponse = {}  # type: ignore[typeddict-item]
    if "links" in data:
        import capo_rtbfabric.types.link_list

        out["links"] = capo_rtbfabric.types.link_list.deserialize_json(data["links"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
