"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAppImageConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_image_config_arn
    import aws_sdk_sagemaker.types.app_image_config_name
    import aws_sdk_sagemaker.types.code_editor_app_image_config
    import aws_sdk_sagemaker.types.jupyter_lab_app_image_config
    import aws_sdk_sagemaker.types.kernel_gateway_image_config
    import aws_sdk_sagemaker.types.timestamp


class DescribeAppImageConfigResponse(TypedDict, closed=True):
    app_image_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.app_image_config_arn.AppImageConfigArn"
    ]
    """<p>The ARN of the AppImageConfig.</p>"""
    app_image_config_name: NotRequired[
        "aws_sdk_sagemaker.types.app_image_config_name.AppImageConfigName"
    ]
    """<p>The name of the AppImageConfig.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the AppImageConfig was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the AppImageConfig was last modified.</p>"""
    kernel_gateway_image_config: NotRequired[
        "aws_sdk_sagemaker.types.kernel_gateway_image_config.KernelGatewayImageConfig"
    ]
    """<p>The configuration of a KernelGateway app.</p>"""
    jupyter_lab_app_image_config: NotRequired[
        "aws_sdk_sagemaker.types.jupyter_lab_app_image_config.JupyterLabAppImageConfig"
    ]
    """<p>The configuration of the JupyterLab app.</p>"""
    code_editor_app_image_config: NotRequired[
        "aws_sdk_sagemaker.types.code_editor_app_image_config.CodeEditorAppImageConfig"
    ]
    """<p>The configuration of the Code Editor app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppImageConfigResponse) -> dict:
    out: dict = {}
    if "app_image_config_arn" in value:
        out["AppImageConfigArn"] = value["app_image_config_arn"]
    if "app_image_config_name" in value:
        out["AppImageConfigName"] = value["app_image_config_name"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> DescribeAppImageConfigResponse:
    out: DescribeAppImageConfigResponse = {}  # type: ignore[typeddict-item]
    if "AppImageConfigArn" in data:
        out["app_image_config_arn"] = data["AppImageConfigArn"]
    if "AppImageConfigName" in data:
        out["app_image_config_name"] = data["AppImageConfigName"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
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
