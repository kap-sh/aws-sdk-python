"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioWebPortalSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.execution_role_session_name_mode
    import aws_sdk_sagemaker.types.hidden_app_types_list
    import aws_sdk_sagemaker.types.hidden_instance_types_list
    import aws_sdk_sagemaker.types.hidden_ml_tools_list
    import aws_sdk_sagemaker.types.hidden_sage_maker_image_version_aliases_list


class StudioWebPortalSettings(TypedDict):
    hidden_ml_tools: NotRequired[
        "aws_sdk_sagemaker.types.hidden_ml_tools_list.HiddenMlToolsList"
    ]
    """<p>The machine learning tools that are hidden from the Studio left navigation pane.</p>"""
    hidden_app_types: NotRequired[
        "aws_sdk_sagemaker.types.hidden_app_types_list.HiddenAppTypesList"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html\">Applications supported in Studio</a> that are hidden from the Studio left navigation pane.</p>"""
    hidden_instance_types: NotRequired[
        "aws_sdk_sagemaker.types.hidden_instance_types_list.HiddenInstanceTypesList"
    ]
    """<p> The instance types you are hiding from the Studio user interface. </p>"""
    hidden_sage_maker_image_version_aliases: NotRequired[
        "aws_sdk_sagemaker.types.hidden_sage_maker_image_version_aliases_list.HiddenSageMakerImageVersionAliasesList"
    ]
    """<p> The version aliases you are hiding from the Studio user interface. </p>"""
    execution_role_session_name_mode: NotRequired[
        "aws_sdk_sagemaker.types.execution_role_session_name_mode.ExecutionRoleSessionNameMode"
    ]
    """<p>The execution role session name mode. If this value is set to <code>USER_IDENTITY</code>, the session name of the execution role corresponds to the user's identity. For IAM domains, the session name is the IAM session name used to generate the presigned URL. For IAM Identity Center domains, the session name is the username of the associated IAM Identity Center user. If this value is set to <code>STATIC</code> or is not set, the session name defaults to <code>SageMaker</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StudioWebPortalSettings) -> dict:
    out: dict = {}
    if "hidden_ml_tools" in value:
        import aws_sdk_sagemaker.types.hidden_ml_tools_list

        out["HiddenMlTools"] = (
            aws_sdk_sagemaker.types.hidden_ml_tools_list.serialize_aws_json_1_1(
                value["hidden_ml_tools"]
            )
        )
    if "hidden_app_types" in value:
        import aws_sdk_sagemaker.types.hidden_app_types_list

        out["HiddenAppTypes"] = (
            aws_sdk_sagemaker.types.hidden_app_types_list.serialize_aws_json_1_1(
                value["hidden_app_types"]
            )
        )
    if "hidden_instance_types" in value:
        import aws_sdk_sagemaker.types.hidden_instance_types_list

        out["HiddenInstanceTypes"] = (
            aws_sdk_sagemaker.types.hidden_instance_types_list.serialize_aws_json_1_1(
                value["hidden_instance_types"]
            )
        )
    if "hidden_sage_maker_image_version_aliases" in value:
        import aws_sdk_sagemaker.types.hidden_sage_maker_image_version_aliases_list

        out["HiddenSageMakerImageVersionAliases"] = (
            aws_sdk_sagemaker.types.hidden_sage_maker_image_version_aliases_list.serialize_aws_json_1_1(
                value["hidden_sage_maker_image_version_aliases"]
            )
        )
    if "execution_role_session_name_mode" in value:
        import aws_sdk_sagemaker.types.execution_role_session_name_mode

        out["ExecutionRoleSessionNameMode"] = (
            aws_sdk_sagemaker.types.execution_role_session_name_mode.serialize_aws_json_1_1(
                value["execution_role_session_name_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StudioWebPortalSettings:
    out: StudioWebPortalSettings = {}  # type: ignore[typeddict-item]
    if "HiddenMlTools" in data:
        import aws_sdk_sagemaker.types.hidden_ml_tools_list

        out["hidden_ml_tools"] = (
            aws_sdk_sagemaker.types.hidden_ml_tools_list.deserialize_aws_json_1_1(
                data["HiddenMlTools"]
            )
        )
    if "HiddenAppTypes" in data:
        import aws_sdk_sagemaker.types.hidden_app_types_list

        out["hidden_app_types"] = (
            aws_sdk_sagemaker.types.hidden_app_types_list.deserialize_aws_json_1_1(
                data["HiddenAppTypes"]
            )
        )
    if "HiddenInstanceTypes" in data:
        import aws_sdk_sagemaker.types.hidden_instance_types_list

        out["hidden_instance_types"] = (
            aws_sdk_sagemaker.types.hidden_instance_types_list.deserialize_aws_json_1_1(
                data["HiddenInstanceTypes"]
            )
        )
    if "HiddenSageMakerImageVersionAliases" in data:
        import aws_sdk_sagemaker.types.hidden_sage_maker_image_version_aliases_list

        out["hidden_sage_maker_image_version_aliases"] = (
            aws_sdk_sagemaker.types.hidden_sage_maker_image_version_aliases_list.deserialize_aws_json_1_1(
                data["HiddenSageMakerImageVersionAliases"]
            )
        )
    if "ExecutionRoleSessionNameMode" in data:
        import aws_sdk_sagemaker.types.execution_role_session_name_mode

        out["execution_role_session_name_mode"] = (
            aws_sdk_sagemaker.types.execution_role_session_name_mode.deserialize_aws_json_1_1(
                data["ExecutionRoleSessionNameMode"]
            )
        )
    return out
