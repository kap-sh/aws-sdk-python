"""Generated from Smithy shape ``com.amazonaws.sagemaker#DebugHookConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.collection_configurations
    import aws_sdk_sagemaker.types.directory_path
    import aws_sdk_sagemaker.types.hook_parameters
    import aws_sdk_sagemaker.types.s3_uri


class DebugHookConfig(TypedDict):
    local_path: NotRequired["aws_sdk_sagemaker.types.directory_path.DirectoryPath"]
    """<p>Path to local storage location for metrics and tensors. Defaults to <code>/opt/ml/output/tensors/</code>.</p>"""
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>Path to Amazon S3 storage location for metrics and tensors.</p>"""
    hook_parameters: NotRequired[
        "aws_sdk_sagemaker.types.hook_parameters.HookParameters"
    ]
    """<p>Configuration information for the Amazon SageMaker Debugger hook parameters.</p>"""
    collection_configurations: NotRequired[
        "aws_sdk_sagemaker.types.collection_configurations.CollectionConfigurations"
    ]
    r"""<p>Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the <code>CollectionConfiguration</code> parameter, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html\">Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugHookConfig) -> dict:
    out: dict = {}
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "hook_parameters" in value:
        import aws_sdk_sagemaker.types.hook_parameters

        out["HookParameters"] = (
            aws_sdk_sagemaker.types.hook_parameters.serialize_aws_json_1_1(
                value["hook_parameters"]
            )
        )
    if "collection_configurations" in value:
        import aws_sdk_sagemaker.types.collection_configurations

        out["CollectionConfigurations"] = (
            aws_sdk_sagemaker.types.collection_configurations.serialize_aws_json_1_1(
                value["collection_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DebugHookConfig:
    out: DebugHookConfig = {}  # type: ignore[typeddict-item]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    if "HookParameters" in data:
        import aws_sdk_sagemaker.types.hook_parameters

        out["hook_parameters"] = (
            aws_sdk_sagemaker.types.hook_parameters.deserialize_aws_json_1_1(
                data["HookParameters"]
            )
        )
    if "CollectionConfigurations" in data:
        import aws_sdk_sagemaker.types.collection_configurations

        out["collection_configurations"] = (
            aws_sdk_sagemaker.types.collection_configurations.deserialize_aws_json_1_1(
                data["CollectionConfigurations"]
            )
        )
    return out
