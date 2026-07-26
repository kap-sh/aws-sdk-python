"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListTargetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.target_group_list


class ListTargetGroupsResponse(TypedDict, closed=True):
    items: NotRequired["capo_vpc_lattice.types.target_group_list.TargetGroupList"]
    """<p>Information about the target groups.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetGroupsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_vpc_lattice.types.target_group_list

        out["items"] = capo_vpc_lattice.types.target_group_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetGroupsResponse:
    out: ListTargetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_vpc_lattice.types.target_group_list

        out["items"] = capo_vpc_lattice.types.target_group_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
