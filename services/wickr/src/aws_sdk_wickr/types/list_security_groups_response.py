"""Generated from Smithy shape ``com.amazonaws.wickr#ListSecurityGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.security_group_list


class ListSecurityGroupsResponse(TypedDict):
    security_groups: NotRequired[
        "aws_sdk_wickr.types.security_group_list.SecurityGroupList"
    ]
    """<p>A list of security group objects in the current page.</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityGroupsResponse) -> dict:
    out: dict = {}
    if "security_groups" in value:
        import aws_sdk_wickr.types.security_group_list

        out["securityGroups"] = aws_sdk_wickr.types.security_group_list.serialize_json(
            value["security_groups"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityGroupsResponse:
    out: ListSecurityGroupsResponse = {}  # type: ignore[typeddict-item]
    if "securityGroups" in data:
        import aws_sdk_wickr.types.security_group_list

        out["security_groups"] = (
            aws_sdk_wickr.types.security_group_list.deserialize_json(
                data["securityGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
