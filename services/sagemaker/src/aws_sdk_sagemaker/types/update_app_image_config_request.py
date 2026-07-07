"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateAppImageConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_image_config_name
    import aws_sdk_sagemaker.types.code_editor_app_image_config
    import aws_sdk_sagemaker.types.jupyter_lab_app_image_config
    import aws_sdk_sagemaker.types.kernel_gateway_image_config


class UpdateAppImageConfigRequest(TypedDict, closed=True):
    app_image_config_name: NotRequired[
        "aws_sdk_sagemaker.types.app_image_config_name.AppImageConfigName"
    ]
    """<p>The name of the AppImageConfig to update.</p>"""
    kernel_gateway_image_config: NotRequired[
        "aws_sdk_sagemaker.types.kernel_gateway_image_config.KernelGatewayImageConfig"
    ]
    """<p>The new KernelGateway app to run on the image.</p>"""
    jupyter_lab_app_image_config: NotRequired[
        "aws_sdk_sagemaker.types.jupyter_lab_app_image_config.JupyterLabAppImageConfig"
    ]
    """<p>The JupyterLab app running on the image.</p>"""
    code_editor_app_image_config: NotRequired[
        "aws_sdk_sagemaker.types.code_editor_app_image_config.CodeEditorAppImageConfig"
    ]
    """<p>The Code Editor app running on the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAppImageConfigRequest) -> dict:
    out: dict = {}
    if "app_image_config_name" in value:
        out["AppImageConfigName"] = value["app_image_config_name"]
    if "kernel_gateway_image_config" in value:
        import aws_sdk_sagemaker.types.kernel_gateway_image_config

        out["KernelGatewayImageConfig"] = (
            aws_sdk_sagemaker.types.kernel_gateway_image_config.serialize_aws_json_1_1(
                value["kernel_gateway_image_config"]
            )
        )
    if "jupyter_lab_app_image_config" in value:
        import aws_sdk_sagemaker.types.jupyter_lab_app_image_config

        out["JupyterLabAppImageConfig"] = (
            aws_sdk_sagemaker.types.jupyter_lab_app_image_config.serialize_aws_json_1_1(
                value["jupyter_lab_app_image_config"]
            )
        )
    if "code_editor_app_image_config" in value:
        import aws_sdk_sagemaker.types.code_editor_app_image_config

        out["CodeEditorAppImageConfig"] = (
            aws_sdk_sagemaker.types.code_editor_app_image_config.serialize_aws_json_1_1(
                value["code_editor_app_image_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAppImageConfigRequest:
    out: UpdateAppImageConfigRequest = {}  # type: ignore[typeddict-item]
    if "AppImageConfigName" in data:
        out["app_image_config_name"] = data["AppImageConfigName"]
    if "KernelGatewayImageConfig" in data:
        import aws_sdk_sagemaker.types.kernel_gateway_image_config

        out["kernel_gateway_image_config"] = (
            aws_sdk_sagemaker.types.kernel_gateway_image_config.deserialize_aws_json_1_1(
                data["KernelGatewayImageConfig"]
            )
        )
    if "JupyterLabAppImageConfig" in data:
        import aws_sdk_sagemaker.types.jupyter_lab_app_image_config

        out["jupyter_lab_app_image_config"] = (
            aws_sdk_sagemaker.types.jupyter_lab_app_image_config.deserialize_aws_json_1_1(
                data["JupyterLabAppImageConfig"]
            )
        )
    if "CodeEditorAppImageConfig" in data:
        import aws_sdk_sagemaker.types.code_editor_app_image_config

        out["code_editor_app_image_config"] = (
            aws_sdk_sagemaker.types.code_editor_app_image_config.deserialize_aws_json_1_1(
                data["CodeEditorAppImageConfig"]
            )
        )
    return out
