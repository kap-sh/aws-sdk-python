"""Generated from Smithy shape ``com.amazonaws.sagemaker#OwnershipSettingsSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.user_profile_name


class OwnershipSettingsSummary(TypedDict):
    owner_user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile who is the owner of the space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OwnershipSettingsSummary) -> dict:
    out: dict = {}
    if "owner_user_profile_name" in value:
        out["OwnerUserProfileName"] = value["owner_user_profile_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OwnershipSettingsSummary:
    out: OwnershipSettingsSummary = {}  # type: ignore[typeddict-item]
    if "OwnerUserProfileName" in data:
        out["owner_user_profile_name"] = data["OwnerUserProfileName"]
    return out
