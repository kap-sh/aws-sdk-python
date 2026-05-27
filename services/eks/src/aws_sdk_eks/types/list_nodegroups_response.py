"""Generated from Smithy shape ``com.amazonaws.eks#ListNodegroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class ListNodegroupsResponse(TypedDict):
    nodegroups: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>A list of all of the node groups associated with the specified cluster.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodegroupsResponse) -> dict:
    out: dict = {}
    if "nodegroups" in value:
        import aws_sdk_eks.types.string_list

        out["nodegroups"] = aws_sdk_eks.types.string_list.serialize_json(
            value["nodegroups"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNodegroupsResponse:
    out: ListNodegroupsResponse = {}  # type: ignore[typeddict-item]
    if "nodegroups" in data:
        import aws_sdk_eks.types.string_list

        out["nodegroups"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["nodegroups"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
