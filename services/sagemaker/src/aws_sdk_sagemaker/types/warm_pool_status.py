"""Generated from Smithy shape ``com.amazonaws.sagemaker#WarmPoolStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_retained_billable_time_in_seconds
    import aws_sdk_sagemaker.types.training_job_name
    import aws_sdk_sagemaker.types.warm_pool_resource_status


class WarmPoolStatus(TypedDict):
    status: NotRequired[
        "aws_sdk_sagemaker.types.warm_pool_resource_status.WarmPoolResourceStatus"
    ]
    """<p>The status of the warm pool.</p> <ul> <li> <p> <code>InUse</code>: The warm pool is in use for the training job.</p> </li> <li> <p> <code>Available</code>: The warm pool is available to reuse for a matching training job.</p> </li> <li> <p> <code>Reused</code>: The warm pool moved to a matching training job for reuse.</p> </li> <li> <p> <code>Terminated</code>: The warm pool is no longer available. Warm pools are unavailable if they are terminated by a user, terminated for a patch update, or terminated for exceeding the specified <code>KeepAlivePeriodInSeconds</code>.</p> </li> </ul>"""
    resource_retained_billable_time_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.resource_retained_billable_time_in_seconds.ResourceRetainedBillableTimeInSeconds"
    ]
    """<p>The billable time in seconds used by the warm pool. Billable time refers to the absolute wall-clock time.</p> <p>Multiply <code>ResourceRetainedBillableTimeInSeconds</code> by the number of instances (<code>InstanceCount</code>) in your training cluster to get the total compute time SageMaker bills you if you run warm pool training. The formula is as follows: <code>ResourceRetainedBillableTimeInSeconds * InstanceCount</code>.</p>"""
    reused_by_job: NotRequired[
        "aws_sdk_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the matching training job that reused the warm pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WarmPoolStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.warm_pool_resource_status

        out["Status"] = (
            aws_sdk_sagemaker.types.warm_pool_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "resource_retained_billable_time_in_seconds" in value:
        out["ResourceRetainedBillableTimeInSeconds"] = value[
            "resource_retained_billable_time_in_seconds"
        ]
    if "reused_by_job" in value:
        out["ReusedByJob"] = value["reused_by_job"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WarmPoolStatus:
    out: WarmPoolStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.warm_pool_resource_status

        out["status"] = (
            aws_sdk_sagemaker.types.warm_pool_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ResourceRetainedBillableTimeInSeconds" in data:
        out["resource_retained_billable_time_in_seconds"] = data[
            "ResourceRetainedBillableTimeInSeconds"
        ]
    if "ReusedByJob" in data:
        out["reused_by_job"] = data["ReusedByJob"]
    return out
