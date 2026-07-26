"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAppImageConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_image_config_name
    import capo_sagemaker.types.code_editor_app_image_config
    import capo_sagemaker.types.jupyter_lab_app_image_config
    import capo_sagemaker.types.kernel_gateway_image_config
    import capo_sagemaker.types.tag_list


class CreateAppImageConfigRequest(TypedDict, closed=True):
    app_image_config_name: NotRequired[
        "capo_sagemaker.types.app_image_config_name.AppImageConfigName"
    ]
    """<p>The name of the AppImageConfig. Must be unique to your account.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the AppImageConfig.</p>"""
    kernel_gateway_image_config: NotRequired[
        "capo_sagemaker.types.kernel_gateway_image_config.KernelGatewayImageConfig"
    ]
    """<p>The KernelGatewayImageConfig. You can only specify one image kernel in the AppImageConfig API. This kernel will be shown to users before the image starts. Once the image runs, all kernels are visible in JupyterLab.</p>"""
    jupyter_lab_app_image_config: NotRequired[
        "capo_sagemaker.types.jupyter_lab_app_image_config.JupyterLabAppImageConfig"
    ]
    """<p>The <code>JupyterLabAppImageConfig</code>. You can only specify one image kernel in the <code>AppImageConfig</code> API. This kernel is shown to users before the image starts. After the image runs, all kernels are visible in JupyterLab.</p>"""
    code_editor_app_image_config: NotRequired[
        "capo_sagemaker.types.code_editor_app_image_config.CodeEditorAppImageConfig"
    ]
    """<p>The <code>CodeEditorAppImageConfig</code>. You can only specify one image kernel in the AppImageConfig API. This kernel is shown to users before the image starts. After the image runs, all kernels are visible in Code Editor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppImageConfigRequest) -> dict:
    out: dict = {}
    if "app_image_config_name" in value:
        out["AppImageConfigName"] = value["app_image_config_name"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateAppImageConfigRequest:
    out: CreateAppImageConfigRequest = {}  # type: ignore[typeddict-item]
    if "AppImageConfigName" in data:
        out["app_image_config_name"] = data["AppImageConfigName"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
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
