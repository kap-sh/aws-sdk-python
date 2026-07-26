"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserProfileDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.user_profile_name
    import capo_sagemaker.types.user_profile_status


class UserProfileDetails(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "capo_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    status: NotRequired["capo_sagemaker.types.user_profile_status.UserProfileStatus"]
    """<p>The status.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserProfileDetails) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "status" in value:
        import capo_sagemaker.types.user_profile_status

        out["Status"] = capo_sagemaker.types.user_profile_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserProfileDetails:
    out: UserProfileDetails = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "Status" in data:
        import capo_sagemaker.types.user_profile_status

        out["status"] = (
            capo_sagemaker.types.user_profile_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
