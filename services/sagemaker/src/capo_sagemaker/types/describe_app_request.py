"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_name
    import capo_sagemaker.types.app_type
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.space_name
    import capo_sagemaker.types.user_profile_name


class DescribeAppRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "capo_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name. If this value is not set, then <code>SpaceName</code> must be set.</p>"""
    space_name: NotRequired["capo_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    app_type: NotRequired["capo_sagemaker.types.app_type.AppType"]
    """<p>The type of app.</p>"""
    app_name: NotRequired["capo_sagemaker.types.app_name.AppName"]
    """<p>The name of the app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "user_profile_name" in value:
        out["UserProfileName"] = value["user_profile_name"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "app_type" in value:
        import capo_sagemaker.types.app_type

        out["AppType"] = capo_sagemaker.types.app_type.serialize_aws_json_1_1(
            value["app_type"]
        )
    if "app_name" in value:
        out["AppName"] = value["app_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppRequest:
    out: DescribeAppRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "UserProfileName" in data:
        out["user_profile_name"] = data["UserProfileName"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "AppType" in data:
        import capo_sagemaker.types.app_type

        out["app_type"] = capo_sagemaker.types.app_type.deserialize_aws_json_1_1(
            data["AppType"]
        )
    if "AppName" in data:
        out["app_name"] = data["AppName"]
    return out
