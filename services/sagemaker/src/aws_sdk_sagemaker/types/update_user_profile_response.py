"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateUserProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.user_profile_arn


class UpdateUserProfileResponse(TypedDict, closed=True):
    user_profile_arn: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_arn.UserProfileArn"
    ]
    """<p>The user profile Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserProfileResponse) -> dict:
    out: dict = {}
    if "user_profile_arn" in value:
        out["UserProfileArn"] = value["user_profile_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserProfileResponse:
    out: UpdateUserProfileResponse = {}  # type: ignore[typeddict-item]
    if "UserProfileArn" in data:
        out["user_profile_arn"] = data["UserProfileArn"]
    return out
