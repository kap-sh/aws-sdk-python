"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateUserProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.user_profile_name
    import capo_sagemaker.types.user_settings


class UpdateUserProfileRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "capo_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    user_settings: NotRequired["capo_sagemaker.types.user_settings.UserSettings"]
    """<p>A collection of settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserProfileRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "user_settings" in value:
        import capo_sagemaker.types.user_settings

        out["UserSettings"] = capo_sagemaker.types.user_settings.serialize_aws_json_1_1(
            value["user_settings"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserProfileRequest:
    out: UpdateUserProfileRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "UserSettings" in data:
        import capo_sagemaker.types.user_settings

        out["user_settings"] = (
            capo_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    return out
