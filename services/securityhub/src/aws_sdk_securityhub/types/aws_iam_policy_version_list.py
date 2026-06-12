"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamPolicyVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_iam_policy_version

AwsIamPolicyVersionList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_iam_policy_version.AwsIamPolicyVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamPolicyVersionList) -> list:
    import aws_sdk_securityhub.types.aws_iam_policy_version

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_iam_policy_version.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsIamPolicyVersionList:
    import aws_sdk_securityhub.types.aws_iam_policy_version

    out: AwsIamPolicyVersionList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_iam_policy_version.deserialize_json(item)
        )
    return out
