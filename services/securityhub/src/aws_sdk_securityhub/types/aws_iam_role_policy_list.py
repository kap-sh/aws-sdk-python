"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamRolePolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_role_policy

AwsIamRolePolicyList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_iam_role_policy.AwsIamRolePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamRolePolicyList) -> list:
    import aws_sdk_securityhub.types.aws_iam_role_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.aws_iam_role_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsIamRolePolicyList:
    import aws_sdk_securityhub.types.aws_iam_role_policy

    out: AwsIamRolePolicyList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.aws_iam_role_policy.deserialize_json(item))
    return out
