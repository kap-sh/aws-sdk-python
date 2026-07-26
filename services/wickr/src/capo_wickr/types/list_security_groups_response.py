"""Generated from Smithy shape ``com.amazonaws.wickr#ListSecurityGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.security_group_list


class ListSecurityGroupsResponse(TypedDict, closed=True):
    security_groups: NotRequired[
        "capo_wickr.types.security_group_list.SecurityGroupList"
    ]
    """<p>A list of security group objects in the current page.</p>"""
    next_token: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityGroupsResponse) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import capo_wickr.types.security_group_list

        out["securityGroups"] = capo_wickr.types.security_group_list.serialize_json(
            value["security_groups"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityGroupsResponse:
    out: ListSecurityGroupsResponse = {}  # type: ignore[typeddict-item]
    if "securityGroups" in data:
        import capo_wickr.types.security_group_list

        out["security_groups"] = capo_wickr.types.security_group_list.deserialize_json(
            data["securityGroups"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
