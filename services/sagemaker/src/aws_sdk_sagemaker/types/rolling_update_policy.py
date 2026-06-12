"""Generated from Smithy shape ``com.amazonaws.sagemaker#RollingUpdatePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_size
    import aws_sdk_sagemaker.types.maximum_execution_timeout_in_seconds
    import aws_sdk_sagemaker.types.wait_interval_in_seconds


class RollingUpdatePolicy(TypedDict):
    maximum_batch_size: NotRequired[
        "aws_sdk_sagemaker.types.capacity_size.CapacitySize"
    ]
    """<p>Batch size for each rolling step to provision capacity and turn on traffic on the new endpoint fleet, and terminate capacity on the old endpoint fleet. Value must be between 5% to 50% of the variant's total instance count.</p>"""
    wait_interval_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.wait_interval_in_seconds.WaitIntervalInSeconds"
    ]
    """<p>The length of the baking period, during which SageMaker monitors alarms for each batch on the new fleet.</p>"""
    maximum_execution_timeout_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.maximum_execution_timeout_in_seconds.MaximumExecutionTimeoutInSeconds"
    ]
    """<p>The time limit for the total deployment. Exceeding this limit causes a timeout.</p>"""
    rollback_maximum_batch_size: NotRequired[
        "aws_sdk_sagemaker.types.capacity_size.CapacitySize"
    ]
    """<p>Batch size for rollback to the old endpoint fleet. Each rolling step to provision capacity and turn on traffic on the old endpoint fleet, and terminate capacity on the new endpoint fleet. If this field is absent, the default value will be set to 100% of total capacity which means to bring up the whole capacity of the old fleet at once during rollback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollingUpdatePolicy) -> dict:
    out: dict = {}
    if "maximum_batch_size" in value:
        import aws_sdk_sagemaker.types.capacity_size

        out["MaximumBatchSize"] = (
            aws_sdk_sagemaker.types.capacity_size.serialize_aws_json_1_1(
                value["maximum_batch_size"]
            )
        )
    if "wait_interval_in_seconds" in value:
        out["WaitIntervalInSeconds"] = value["wait_interval_in_seconds"]
    if "maximum_execution_timeout_in_seconds" in value:
        out["MaximumExecutionTimeoutInSeconds"] = value[
            "maximum_execution_timeout_in_seconds"
        ]
    if "rollback_maximum_batch_size" in value:
        import aws_sdk_sagemaker.types.capacity_size

        out["RollbackMaximumBatchSize"] = (
            aws_sdk_sagemaker.types.capacity_size.serialize_aws_json_1_1(
                value["rollback_maximum_batch_size"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RollingUpdatePolicy:
    out: RollingUpdatePolicy = {}  # type: ignore[typeddict-item]
    if "MaximumBatchSize" in data:
        import aws_sdk_sagemaker.types.capacity_size

        out["maximum_batch_size"] = (
            aws_sdk_sagemaker.types.capacity_size.deserialize_aws_json_1_1(
                data["MaximumBatchSize"]
            )
        )
    if "WaitIntervalInSeconds" in data:
        out["wait_interval_in_seconds"] = data["WaitIntervalInSeconds"]
    if "MaximumExecutionTimeoutInSeconds" in data:
        out["maximum_execution_timeout_in_seconds"] = data[
            "MaximumExecutionTimeoutInSeconds"
        ]
    if "RollbackMaximumBatchSize" in data:
        import aws_sdk_sagemaker.types.capacity_size

        out["rollback_maximum_batch_size"] = (
            aws_sdk_sagemaker.types.capacity_size.deserialize_aws_json_1_1(
                data["RollbackMaximumBatchSize"]
            )
        )
    return out
