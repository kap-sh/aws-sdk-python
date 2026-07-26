"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamInstanceProfileRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_instance_profile_role

AwsIamInstanceProfileRoles: TypeAlias = list[
    "capo_securityhub.types.aws_iam_instance_profile_role.AwsIamInstanceProfileRole"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamInstanceProfileRoles) -> list:
    import capo_securityhub.types.aws_iam_instance_profile_role

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_iam_instance_profile_role.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsIamInstanceProfileRoles:
    import capo_securityhub.types.aws_iam_instance_profile_role

    out: AwsIamInstanceProfileRoles = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_iam_instance_profile_role.deserialize_json(item)
        )
    return out
