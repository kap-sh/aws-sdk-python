"""Generated from Smithy shape ``com.amazonaws.workmail#ListImpersonationRolesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_role_list
    import capo_workmail.types.next_token


class ListImpersonationRolesResponse(TypedDict, closed=True):
    roles: NotRequired[
        "capo_workmail.types.impersonation_role_list.ImpersonationRoleList"
    ]
    """<p>The list of impersonation roles under the given WorkMail organization.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. The value is <code>null</code> when there are no results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImpersonationRolesResponse) -> dict:
    out: dict = {}
    if "roles" in value:
        import capo_workmail.types.impersonation_role_list

        out["Roles"] = (
            capo_workmail.types.impersonation_role_list.serialize_aws_json_1_1(
                value["roles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImpersonationRolesResponse:
    out: ListImpersonationRolesResponse = {}  # type: ignore[typeddict-item]
    if "Roles" in data:
        import capo_workmail.types.impersonation_role_list

        out["roles"] = (
            capo_workmail.types.impersonation_role_list.deserialize_aws_json_1_1(
                data["Roles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
