"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamGroupPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_group_policy

AwsIamGroupPolicyList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_iam_group_policy.AwsIamGroupPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamGroupPolicyList) -> list:
    import aws_sdk_securityhub.types.aws_iam_group_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.aws_iam_group_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsIamGroupPolicyList:
    import aws_sdk_securityhub.types.aws_iam_group_policy

    out: AwsIamGroupPolicyList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_iam_group_policy.deserialize_json(item)
        )
    return out
