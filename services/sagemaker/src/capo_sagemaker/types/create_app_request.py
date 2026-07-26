"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_name
    import capo_sagemaker.types.app_type
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.resource_spec
    import capo_sagemaker.types.space_name
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.user_profile_name


class CreateAppRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    user_profile_name: NotRequired[
        "capo_sagemaker.types.user_profile_name.UserProfileName"
    ]
    """<p>The user profile name. If this value is not set, then <code>SpaceName</code> must be set.</p>"""
    space_name: NotRequired["capo_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space. If this value is not set, then <code>UserProfileName</code> must be set.</p>"""
    app_type: NotRequired["capo_sagemaker.types.app_type.AppType"]
    """<p>The type of app.</p>"""
    app_name: NotRequired["capo_sagemaker.types.app_name.AppName"]
    """<p>The name of the app.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Each tag consists of a key and an optional value. Tag keys must be unique per resource.</p>"""
    resource_spec: NotRequired["capo_sagemaker.types.resource_spec.ResourceSpec"]
    """<p>The instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.</p> <note> <p>The value of <code>InstanceType</code> passed as part of the <code>ResourceSpec</code> in the <code>CreateApp</code> call overrides the value passed as part of the <code>ResourceSpec</code> configured for the user profile or the domain. If <code>InstanceType</code> is not specified in any of those three <code>ResourceSpec</code> values for a <code>KernelGateway</code> app, the <code>CreateApp</code> call fails with a request validation error.</p> </note>"""
    recovery_mode: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p> Indicates whether the application is launched in recovery mode. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppRequest) -> dict:
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
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["ResourceSpec"] = capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
            value["resource_spec"]
        )
    if "recovery_mode" in value:
        out["RecoveryMode"] = value["recovery_mode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppRequest:
    out: CreateAppRequest = {}  # type: ignore[typeddict-item]
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
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ResourceSpec" in data:
        import capo_sagemaker.types.resource_spec

        out["resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["ResourceSpec"]
            )
        )
    if "RecoveryMode" in data:
        out["recovery_mode"] = data["RecoveryMode"]
    return out
