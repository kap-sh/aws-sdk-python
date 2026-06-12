"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_name
    import aws_sdk_sagemaker.types.app_type
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.space_name
    import aws_sdk_sagemaker.types.user_profile_name


class DeleteAppRequest(TypedDict):
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name. If this value is not set, then <code>SpaceName</code> must be set.</p>"""
    space_name: NotRequired["aws_sdk_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space. If this value is not set, then <code>UserProfileName</code> must be set.</p>"""
    app_type: NotRequired["aws_sdk_sagemaker.types.app_type.AppType"]
    """<p>The type of app.</p>"""
    app_name: NotRequired["aws_sdk_sagemaker.types.app_name.AppName"]
    """<p>The name of the app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAppRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "app_type" in value:
        import aws_sdk_sagemaker.types.app_type

        out["AppType"] = aws_sdk_sagemaker.types.app_type.serialize_aws_json_1_1(
            value["app_type"]
        )
    if "app_name" in value:
        out["AppName"] = value["app_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAppRequest:
    out: DeleteAppRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "AppType" in data:
        import aws_sdk_sagemaker.types.app_type

        out["app_type"] = aws_sdk_sagemaker.types.app_type.deserialize_aws_json_1_1(
            data["AppType"]
        )
    if "AppName" in data:
        out["app_name"] = data["AppName"]
    return out
