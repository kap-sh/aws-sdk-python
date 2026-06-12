"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.user_profile_details

UserProfileList: TypeAlias = list[
    "aws_sdk_sagemaker.types.user_profile_details.UserProfileDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserProfileList) -> list:
    import aws_sdk_sagemaker.types.user_profile_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.user_profile_details.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserProfileList:
    import aws_sdk_sagemaker.types.user_profile_details

    out: UserProfileList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.user_profile_details.deserialize_aws_json_1_1(item)
        )
    return out
