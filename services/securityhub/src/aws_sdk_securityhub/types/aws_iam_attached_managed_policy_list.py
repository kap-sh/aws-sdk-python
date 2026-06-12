"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamAttachedManagedPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_attached_managed_policy

AwsIamAttachedManagedPolicyList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_iam_attached_managed_policy.AwsIamAttachedManagedPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamAttachedManagedPolicyList) -> list:
    import aws_sdk_securityhub.types.aws_iam_attached_managed_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_iam_attached_managed_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsIamAttachedManagedPolicyList:
    import aws_sdk_securityhub.types.aws_iam_attached_managed_policy

    out: AwsIamAttachedManagedPolicyList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_iam_attached_managed_policy.deserialize_json(
                item
            )
        )
    return out
