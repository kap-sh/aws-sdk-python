"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CustomerManagedPolicyReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sso_admin.types.customer_managed_policy_reference

CustomerManagedPolicyReferenceList: TypeAlias = list[
    "capo_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerManagedPolicyReferenceList) -> list:
    import capo_sso_admin.types.customer_managed_policy_reference

    out: list = []
    for item in value:
        out.append(
            capo_sso_admin.types.customer_managed_policy_reference.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomerManagedPolicyReferenceList:
    import capo_sso_admin.types.customer_managed_policy_reference

    out: CustomerManagedPolicyReferenceList = []
    for item in data:
        out.append(
            capo_sso_admin.types.customer_managed_policy_reference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
