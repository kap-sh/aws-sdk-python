"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListUserProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.user_profile_list


class ListUserProfilesResponse(TypedDict, closed=True):
    user_profiles: NotRequired["capo_sagemaker.types.user_profile_list.UserProfileList"]
    """<p>The list of user profiles.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserProfilesResponse) -> dict:
    out: dict = {}
    if "user_profiles" in value:
        import capo_sagemaker.types.user_profile_list

        out["UserProfiles"] = (
            capo_sagemaker.types.user_profile_list.serialize_aws_json_1_1(
                value["user_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserProfilesResponse:
    out: ListUserProfilesResponse = {}  # type: ignore[typeddict-item]
    if "UserProfiles" in data:
        import capo_sagemaker.types.user_profile_list

        out["user_profiles"] = (
            capo_sagemaker.types.user_profile_list.deserialize_aws_json_1_1(
                data["UserProfiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
