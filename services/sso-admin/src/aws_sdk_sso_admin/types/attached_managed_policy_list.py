"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AttachedManagedPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.attached_managed_policy

AttachedManagedPolicyList: TypeAlias = list[
    "aws_sdk_sso_admin.types.attached_managed_policy.AttachedManagedPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachedManagedPolicyList) -> list:
    import aws_sdk_sso_admin.types.attached_managed_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sso_admin.types.attached_managed_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttachedManagedPolicyList:
    import aws_sdk_sso_admin.types.attached_managed_policy

    out: AttachedManagedPolicyList = []
    for item in data:
        out.append(
            aws_sdk_sso_admin.types.attached_managed_policy.deserialize_aws_json_1_1(
                item
            )
        )
    return out
