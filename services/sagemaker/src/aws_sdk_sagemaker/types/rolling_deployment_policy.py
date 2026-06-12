"""Generated from Smithy shape ``com.amazonaws.sagemaker#RollingDeploymentPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_size_config


class RollingDeploymentPolicy(TypedDict):
    maximum_batch_size: NotRequired[
        "aws_sdk_sagemaker.types.capacity_size_config.CapacitySizeConfig"
    ]
    """<p>The maximum amount of instances in the cluster that SageMaker can update at a time.</p>"""
    rollback_maximum_batch_size: NotRequired[
        "aws_sdk_sagemaker.types.capacity_size_config.CapacitySizeConfig"
    ]
    """<p>The maximum amount of instances in the cluster that SageMaker can roll back at a time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollingDeploymentPolicy) -> dict:
    out: dict = {}
    if "maximum_batch_size" in value:
        import aws_sdk_sagemaker.types.capacity_size_config

        out["MaximumBatchSize"] = (
            aws_sdk_sagemaker.types.capacity_size_config.serialize_aws_json_1_1(
                value["maximum_batch_size"]
            )
        )
    if "rollback_maximum_batch_size" in value:
        import aws_sdk_sagemaker.types.capacity_size_config

        out["RollbackMaximumBatchSize"] = (
            aws_sdk_sagemaker.types.capacity_size_config.serialize_aws_json_1_1(
                value["rollback_maximum_batch_size"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RollingDeploymentPolicy:
    out: RollingDeploymentPolicy = {}  # type: ignore[typeddict-item]
    if "MaximumBatchSize" in data:
        import aws_sdk_sagemaker.types.capacity_size_config

        out["maximum_batch_size"] = (
            aws_sdk_sagemaker.types.capacity_size_config.deserialize_aws_json_1_1(
                data["MaximumBatchSize"]
            )
        )
    if "RollbackMaximumBatchSize" in data:
        import aws_sdk_sagemaker.types.capacity_size_config

        out["rollback_maximum_batch_size"] = (
            aws_sdk_sagemaker.types.capacity_size_config.deserialize_aws_json_1_1(
                data["RollbackMaximumBatchSize"]
            )
        )
    return out
