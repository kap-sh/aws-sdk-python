"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamUserPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_user_policy

AwsIamUserPolicyList: TypeAlias = list[
    "capo_securityhub.types.aws_iam_user_policy.AwsIamUserPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamUserPolicyList) -> list:
    import capo_securityhub.types.aws_iam_user_policy

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_iam_user_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsIamUserPolicyList:
    import capo_securityhub.types.aws_iam_user_policy

    out: AwsIamUserPolicyList = []
    for item in data:
        out.append(capo_securityhub.types.aws_iam_user_policy.deserialize_json(item))
    return out
