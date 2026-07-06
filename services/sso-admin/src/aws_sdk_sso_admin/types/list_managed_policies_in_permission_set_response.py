"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListManagedPoliciesInPermissionSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.attached_managed_policy_list
    import aws_sdk_sso_admin.types.token


class ListManagedPoliciesInPermissionSetResponse(TypedDict, closed=True):
    attached_managed_policies: NotRequired[
        "aws_sdk_sso_admin.types.attached_managed_policy_list.AttachedManagedPolicyList"
    ]
    """<p>An array of the <a>AttachedManagedPolicy</a> data type object.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListManagedPoliciesInPermissionSetResponse) -> dict:
    out: dict = {}
    if "attached_managed_policies" in value:
        import aws_sdk_sso_admin.types.attached_managed_policy_list

        out["AttachedManagedPolicies"] = (
            aws_sdk_sso_admin.types.attached_managed_policy_list.serialize_aws_json_1_1(
                value["attached_managed_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListManagedPoliciesInPermissionSetResponse:
    out: ListManagedPoliciesInPermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "AttachedManagedPolicies" in data:
        import aws_sdk_sso_admin.types.attached_managed_policy_list

        out["attached_managed_policies"] = (
            aws_sdk_sso_admin.types.attached_managed_policy_list.deserialize_aws_json_1_1(
                data["AttachedManagedPolicies"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
