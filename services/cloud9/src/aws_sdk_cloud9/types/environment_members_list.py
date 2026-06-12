"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentMembersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_member

EnvironmentMembersList: TypeAlias = list[
    "aws_sdk_cloud9.types.environment_member.EnvironmentMember"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentMembersList) -> list:
    import aws_sdk_cloud9.types.environment_member

    out: list = []
    for item in value:
        out.append(aws_sdk_cloud9.types.environment_member.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentMembersList:
    import aws_sdk_cloud9.types.environment_member

    out: EnvironmentMembersList = []
    for item in data:
        out.append(
            aws_sdk_cloud9.types.environment_member.deserialize_aws_json_1_1(item)
        )
    return out
