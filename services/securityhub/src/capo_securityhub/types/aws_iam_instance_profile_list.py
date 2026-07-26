"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamInstanceProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_instance_profile

AwsIamInstanceProfileList: TypeAlias = list[
    "capo_securityhub.types.aws_iam_instance_profile.AwsIamInstanceProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamInstanceProfileList) -> list:
    import capo_securityhub.types.aws_iam_instance_profile

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_iam_instance_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsIamInstanceProfileList:
    import capo_securityhub.types.aws_iam_instance_profile

    out: AwsIamInstanceProfileList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_iam_instance_profile.deserialize_json(item)
        )
    return out
