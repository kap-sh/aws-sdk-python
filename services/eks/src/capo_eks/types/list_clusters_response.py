"""Generated from Smithy shape ``com.amazonaws.eks#ListClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class ListClustersResponse(TypedDict, closed=True):
    clusters: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>A list of all of the clusters for your account in the specified Amazon Web Services Region .</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "clusters" in value:
        import capo_eks.types.string_list

        out["clusters"] = capo_eks.types.string_list.serialize_json(value["clusters"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "clusters" in data:
        import capo_eks.types.string_list

        out["clusters"] = capo_eks.types.string_list.deserialize_json(data["clusters"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
