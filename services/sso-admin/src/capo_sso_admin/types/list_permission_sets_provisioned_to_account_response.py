"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListPermissionSetsProvisionedToAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.permission_set_list
    import capo_sso_admin.types.token


class ListPermissionSetsProvisionedToAccountResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""
    permission_sets: NotRequired[
        "capo_sso_admin.types.permission_set_list.PermissionSetList"
    ]
    """<p>Defines the level of access that an Amazon Web Services account has.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListPermissionSetsProvisionedToAccountResponse,
) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "permission_sets" in value:
        import capo_sso_admin.types.permission_set_list

        out["PermissionSets"] = (
            capo_sso_admin.types.permission_set_list.serialize_aws_json_1_1(
                value["permission_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListPermissionSetsProvisionedToAccountResponse:
    out: ListPermissionSetsProvisionedToAccountResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PermissionSets" in data:
        import capo_sso_admin.types.permission_set_list

        out["permission_sets"] = (
            capo_sso_admin.types.permission_set_list.deserialize_aws_json_1_1(
                data["PermissionSets"]
            )
        )
    return out
