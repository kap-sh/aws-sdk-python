"""Generated from Smithy shape ``com.amazonaws.eks#ListUpdatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class ListUpdatesResponse(TypedDict, closed=True):
    update_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>A list of all the updates for the specified cluster and Region.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUpdatesResponse) -> dict:
    out: dict = {}
    if "update_ids" in value:
        import capo_eks.types.string_list

        out["updateIds"] = capo_eks.types.string_list.serialize_json(
            value["update_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUpdatesResponse:
    out: ListUpdatesResponse = {}  # type: ignore[typeddict-item]
    if "updateIds" in data:
        import capo_eks.types.string_list

        out["update_ids"] = capo_eks.types.string_list.deserialize_json(
            data["updateIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
