"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingResources``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_cluster_config


class ProcessingResources(TypedDict):
    cluster_config: NotRequired[
        "aws_sdk_sagemaker.types.processing_cluster_config.ProcessingClusterConfig"
    ]
    """<p>The configuration for the resources in a cluster used to run the processing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingResources) -> dict:
    out: dict = {}
    if "cluster_config" in value:
        import aws_sdk_sagemaker.types.processing_cluster_config

        out["ClusterConfig"] = (
            aws_sdk_sagemaker.types.processing_cluster_config.serialize_aws_json_1_1(
                value["cluster_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingResources:
    out: ProcessingResources = {}  # type: ignore[typeddict-item]
    if "ClusterConfig" in data:
        import aws_sdk_sagemaker.types.processing_cluster_config

        out["cluster_config"] = (
            aws_sdk_sagemaker.types.processing_cluster_config.deserialize_aws_json_1_1(
                data["ClusterConfig"]
            )
        )
    return out
