"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListCustomerManagedPolicyReferencesInPermissionSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.customer_managed_policy_reference_list
    import aws_sdk_sso_admin.types.token


class ListCustomerManagedPolicyReferencesInPermissionSetResponse(TypedDict):
    customer_managed_policy_references: NotRequired[
        "aws_sdk_sso_admin.types.customer_managed_policy_reference_list.CustomerManagedPolicyReferenceList"
    ]
    """<p>Specifies the names and paths of the customer managed policies that you have attached to your permission set.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListCustomerManagedPolicyReferencesInPermissionSetResponse,
) -> dict:
    out: dict = {}
    if "customer_managed_policy_references" in value:
        import aws_sdk_sso_admin.types.customer_managed_policy_reference_list

        out["CustomerManagedPolicyReferences"] = (
            aws_sdk_sso_admin.types.customer_managed_policy_reference_list.serialize_aws_json_1_1(
                value["customer_managed_policy_references"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListCustomerManagedPolicyReferencesInPermissionSetResponse:
    out: ListCustomerManagedPolicyReferencesInPermissionSetResponse = {}  # type: ignore[typeddict-item]
    if "CustomerManagedPolicyReferences" in data:
        import aws_sdk_sso_admin.types.customer_managed_policy_reference_list

        out["customer_managed_policy_references"] = (
            aws_sdk_sso_admin.types.customer_managed_policy_reference_list.deserialize_aws_json_1_1(
                data["CustomerManagedPolicyReferences"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
