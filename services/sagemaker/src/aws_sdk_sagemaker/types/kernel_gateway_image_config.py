"""Generated from Smithy shape ``com.amazonaws.sagemaker#KernelGatewayImageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.file_system_config
    import aws_sdk_sagemaker.types.kernel_specs


class KernelGatewayImageConfig(TypedDict, closed=True):
    kernel_specs: NotRequired["aws_sdk_sagemaker.types.kernel_specs.KernelSpecs"]
    """<p>The specification of the Jupyter kernels in the image.</p>"""
    file_system_config: NotRequired[
        "aws_sdk_sagemaker.types.file_system_config.FileSystemConfig"
    ]
    """<p>The Amazon Elastic File System storage configuration for a SageMaker AI image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KernelGatewayImageConfig) -> dict:
    out: dict = {}
    if "kernel_specs" in value:
        import aws_sdk_sagemaker.types.kernel_specs

        out["KernelSpecs"] = (
            aws_sdk_sagemaker.types.kernel_specs.serialize_aws_json_1_1(
                value["kernel_specs"]
            )
        )
    if "file_system_config" in value:
        import aws_sdk_sagemaker.types.file_system_config

        out["FileSystemConfig"] = (
            aws_sdk_sagemaker.types.file_system_config.serialize_aws_json_1_1(
                value["file_system_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KernelGatewayImageConfig:
    out: KernelGatewayImageConfig = {}  # type: ignore[typeddict-item]
    if "KernelSpecs" in data:
        import aws_sdk_sagemaker.types.kernel_specs

        out["kernel_specs"] = (
            aws_sdk_sagemaker.types.kernel_specs.deserialize_aws_json_1_1(
                data["KernelSpecs"]
            )
        )
    if "FileSystemConfig" in data:
        import aws_sdk_sagemaker.types.file_system_config

        out["file_system_config"] = (
            aws_sdk_sagemaker.types.file_system_config.deserialize_aws_json_1_1(
                data["FileSystemConfig"]
            )
        )
    return out
