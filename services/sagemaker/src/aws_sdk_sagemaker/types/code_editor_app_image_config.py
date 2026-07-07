"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeEditorAppImageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.container_config
    import aws_sdk_sagemaker.types.file_system_config


class CodeEditorAppImageConfig(TypedDict, closed=True):
    file_system_config: NotRequired[
        "aws_sdk_sagemaker.types.file_system_config.FileSystemConfig"
    ]
    container_config: NotRequired[
        "aws_sdk_sagemaker.types.container_config.ContainerConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeEditorAppImageConfig) -> dict:
    out: dict = {}
    if "file_system_config" in value:
        import aws_sdk_sagemaker.types.file_system_config

        out["FileSystemConfig"] = (
            aws_sdk_sagemaker.types.file_system_config.serialize_aws_json_1_1(
                value["file_system_config"]
            )
        )
    if "container_config" in value:
        import aws_sdk_sagemaker.types.container_config

        out["ContainerConfig"] = (
            aws_sdk_sagemaker.types.container_config.serialize_aws_json_1_1(
                value["container_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeEditorAppImageConfig:
    out: CodeEditorAppImageConfig = {}  # type: ignore[typeddict-item]
    if "FileSystemConfig" in data:
        import aws_sdk_sagemaker.types.file_system_config

        out["file_system_config"] = (
            aws_sdk_sagemaker.types.file_system_config.deserialize_aws_json_1_1(
                data["FileSystemConfig"]
            )
        )
    if "ContainerConfig" in data:
        import aws_sdk_sagemaker.types.container_config

        out["container_config"] = (
            aws_sdk_sagemaker.types.container_config.deserialize_aws_json_1_1(
                data["ContainerConfig"]
            )
        )
    return out
