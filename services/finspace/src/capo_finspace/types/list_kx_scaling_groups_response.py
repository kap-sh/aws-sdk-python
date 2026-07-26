"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxScalingGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_scaling_group_list
    import capo_finspace.types.pagination_token


class ListKxScalingGroupsResponse(TypedDict, closed=True):
    scaling_groups: NotRequired[
        "capo_finspace.types.kx_scaling_group_list.KxScalingGroupList"
    ]
    """<p> A list of scaling groups available in a kdb environment.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p> A token that indicates where a results page should begin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxScalingGroupsResponse) -> dict:
    out: dict = {}
    if "scaling_groups" in value:
        import capo_finspace.types.kx_scaling_group_list

        out["scalingGroups"] = capo_finspace.types.kx_scaling_group_list.serialize_json(
            value["scaling_groups"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxScalingGroupsResponse:
    out: ListKxScalingGroupsResponse = {}  # type: ignore[typeddict-item]
    if "scalingGroups" in data:
        import capo_finspace.types.kx_scaling_group_list

        out["scaling_groups"] = (
            capo_finspace.types.kx_scaling_group_list.deserialize_json(
                data["scalingGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
