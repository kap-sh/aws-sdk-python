"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_name
    import aws_sdk_sagemaker.types.app_status
    import aws_sdk_sagemaker.types.app_type
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.resource_spec
    import aws_sdk_sagemaker.types.space_name
    import aws_sdk_sagemaker.types.user_profile_name


class AppDetails(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "aws_sdk_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name.</p>"""
    space_name: NotRequired["aws_sdk_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    app_type: NotRequired["aws_sdk_sagemaker.types.app_type.AppType"]
    """<p>The type of app.</p>"""
    app_name: NotRequired["aws_sdk_sagemaker.types.app_name.AppName"]
    """<p>The name of the app.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.app_status.AppStatus"]
    """<p>The status.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    resource_spec: NotRequired["aws_sdk_sagemaker.types.resource_spec.ResourceSpec"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppDetails) -> dict:
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
    if "status" in value:
        import aws_sdk_sagemaker.types.app_status

        out["Status"] = aws_sdk_sagemaker.types.app_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "resource_spec" in value:
        import aws_sdk_sagemaker.types.resource_spec

        out["ResourceSpec"] = (
            aws_sdk_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["resource_spec"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppDetails:
    out: AppDetails = {}  # type: ignore[typeddict-item]
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
    if "Status" in data:
        import aws_sdk_sagemaker.types.app_status

        out["status"] = aws_sdk_sagemaker.types.app_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ResourceSpec" in data:
        import aws_sdk_sagemaker.types.resource_spec

        out["resource_spec"] = (
            aws_sdk_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["ResourceSpec"]
            )
        )
    return out
