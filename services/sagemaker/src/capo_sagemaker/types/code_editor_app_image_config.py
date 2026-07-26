"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeEditorAppImageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.container_config
    import capo_sagemaker.types.file_system_config


class CodeEditorAppImageConfig(TypedDict, closed=True):
    file_system_config: NotRequired[
        "capo_sagemaker.types.file_system_config.FileSystemConfig"
    ]
    container_config: NotRequired[
        "capo_sagemaker.types.container_config.ContainerConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeEditorAppImageConfig) -> dict:
    out: dict = {}
    if "file_system_config" in value:
        import capo_sagemaker.types.file_system_config

        out["FileSystemConfig"] = (
            capo_sagemaker.types.file_system_config.serialize_aws_json_1_1(
                value["file_system_config"]
            )
        )
    if "container_config" in value:
        import capo_sagemaker.types.container_config

        out["ContainerConfig"] = (
            capo_sagemaker.types.container_config.serialize_aws_json_1_1(
                value["container_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeEditorAppImageConfig:
    out: CodeEditorAppImageConfig = {}  # type: ignore[typeddict-item]
    if "FileSystemConfig" in data:
        import capo_sagemaker.types.file_system_config

        out["file_system_config"] = (
            capo_sagemaker.types.file_system_config.deserialize_aws_json_1_1(
                data["FileSystemConfig"]
            )
        )
    if "ContainerConfig" in data:
        import capo_sagemaker.types.container_config

        out["container_config"] = (
            capo_sagemaker.types.container_config.deserialize_aws_json_1_1(
                data["ContainerConfig"]
            )
        )
    return out
