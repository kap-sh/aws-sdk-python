"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppImageConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_image_config_arn
    import capo_sagemaker.types.app_image_config_name
    import capo_sagemaker.types.code_editor_app_image_config
    import capo_sagemaker.types.jupyter_lab_app_image_config
    import capo_sagemaker.types.kernel_gateway_image_config
    import capo_sagemaker.types.timestamp


class AppImageConfigDetails(TypedDict, closed=True):
    app_image_config_arn: NotRequired[
        "capo_sagemaker.types.app_image_config_arn.AppImageConfigArn"
    ]
    """<p>The ARN of the AppImageConfig.</p>"""
    app_image_config_name: NotRequired[
        "capo_sagemaker.types.app_image_config_name.AppImageConfigName"
    ]
    """<p>The name of the AppImageConfig. Must be unique to your account.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the AppImageConfig was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the AppImageConfig was last modified.</p>"""
    kernel_gateway_image_config: NotRequired[
        "capo_sagemaker.types.kernel_gateway_image_config.KernelGatewayImageConfig"
    ]
    """<p>The configuration for the file system and kernels in the SageMaker AI image.</p>"""
    jupyter_lab_app_image_config: NotRequired[
        "capo_sagemaker.types.jupyter_lab_app_image_config.JupyterLabAppImageConfig"
    ]
    """<p>The configuration for the file system and the runtime, such as the environment variables and entry point.</p>"""
    code_editor_app_image_config: NotRequired[
        "capo_sagemaker.types.code_editor_app_image_config.CodeEditorAppImageConfig"
    ]
    """<p>The configuration for the file system and the runtime, such as the environment variables and entry point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppImageConfigDetails) -> dict:
    out: dict = {}
    if "app_image_config_arn" in value:
        out["AppImageConfigArn"] = value["app_image_config_arn"]
    if "app_image_config_name" in value:
        out["AppImageConfigName"] = value["app_image_config_name"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "kernel_gateway_image_config" in value:
        import capo_sagemaker.types.kernel_gateway_image_config

        out["KernelGatewayImageConfig"] = (
            capo_sagemaker.types.kernel_gateway_image_config.serialize_aws_json_1_1(
                value["kernel_gateway_image_config"]
            )
        )
    if "jupyter_lab_app_image_config" in value:
        import capo_sagemaker.types.jupyter_lab_app_image_config

        out["JupyterLabAppImageConfig"] = (
            capo_sagemaker.types.jupyter_lab_app_image_config.serialize_aws_json_1_1(
                value["jupyter_lab_app_image_config"]
            )
        )
    if "code_editor_app_image_config" in value:
        import capo_sagemaker.types.code_editor_app_image_config

        out["CodeEditorAppImageConfig"] = (
            capo_sagemaker.types.code_editor_app_image_config.serialize_aws_json_1_1(
                value["code_editor_app_image_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppImageConfigDetails:
    out: AppImageConfigDetails = {}  # type: ignore[typeddict-item]
    if "AppImageConfigArn" in data:
        out["app_image_config_arn"] = data["AppImageConfigArn"]
    if "AppImageConfigName" in data:
        out["app_image_config_name"] = data["AppImageConfigName"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "KernelGatewayImageConfig" in data:
        import capo_sagemaker.types.kernel_gateway_image_config

        out["kernel_gateway_image_config"] = (
            capo_sagemaker.types.kernel_gateway_image_config.deserialize_aws_json_1_1(
                data["KernelGatewayImageConfig"]
            )
        )
    if "JupyterLabAppImageConfig" in data:
        import capo_sagemaker.types.jupyter_lab_app_image_config

        out["jupyter_lab_app_image_config"] = (
            capo_sagemaker.types.jupyter_lab_app_image_config.deserialize_aws_json_1_1(
                data["JupyterLabAppImageConfig"]
            )
        )
    if "CodeEditorAppImageConfig" in data:
        import capo_sagemaker.types.code_editor_app_image_config

        out["code_editor_app_image_config"] = (
            capo_sagemaker.types.code_editor_app_image_config.deserialize_aws_json_1_1(
                data["CodeEditorAppImageConfig"]
            )
        )
    return out
