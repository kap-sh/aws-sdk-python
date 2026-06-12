"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateUserProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.user_profile_arn


class CreateUserProfileResponse(TypedDict):
    user_profile_arn: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_arn.UserProfileArn"
    ]
    """<p>The user profile Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserProfileResponse) -> dict:
    out: dict = {}
    if "user_profile_arn" in value:
        out["UserProfileArn"] = value["user_profile_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserProfileResponse:
    out: CreateUserProfileResponse = {}  # type: ignore[typeddict-item]
    if "UserProfileArn" in data:
        out["user_profile_arn"] = data["UserProfileArn"]
    return out
