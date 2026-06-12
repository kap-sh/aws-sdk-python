"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxScalingGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_scaling_group_list
    import aws_sdk_finspace.types.pagination_token


class ListKxScalingGroupsResponse(TypedDict):
    scaling_groups: NotRequired[
        "aws_sdk_finspace.types.kx_scaling_group_list.KxScalingGroupList"
    ]
    """<p> A list of scaling groups available in a kdb environment.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p> A token that indicates where a results page should begin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxScalingGroupsResponse) -> dict:
    out: dict = {}
    if "scaling_groups" in value:
        import aws_sdk_finspace.types.kx_scaling_group_list

        out["scalingGroups"] = (
            aws_sdk_finspace.types.kx_scaling_group_list.serialize_json(
                value["scaling_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxScalingGroupsResponse:
    out: ListKxScalingGroupsResponse = {}  # type: ignore[typeddict-item]
    if "scalingGroups" in data:
        import aws_sdk_finspace.types.kx_scaling_group_list

        out["scaling_groups"] = (
            aws_sdk_finspace.types.kx_scaling_group_list.deserialize_json(
                data["scalingGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
