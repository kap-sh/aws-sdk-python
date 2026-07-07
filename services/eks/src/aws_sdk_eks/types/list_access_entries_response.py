"""Generated from Smithy shape ``com.amazonaws.eks#ListAccessEntriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class ListAccessEntriesResponse(TypedDict, closed=True):
    access_entries: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The list of access entries that exist for the cluster.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessEntriesResponse) -> dict:
    out: dict = {}
    if "access_entries" in value:
        import aws_sdk_eks.types.string_list

        out["accessEntries"] = aws_sdk_eks.types.string_list.serialize_json(
            value["access_entries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessEntriesResponse:
    out: ListAccessEntriesResponse = {}  # type: ignore[typeddict-item]
    if "accessEntries" in data:
        import aws_sdk_eks.types.string_list

        out["access_entries"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["accessEntries"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
