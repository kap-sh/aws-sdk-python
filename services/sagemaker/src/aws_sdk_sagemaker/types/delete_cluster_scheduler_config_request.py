"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteClusterSchedulerConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_scheduler_config_id


class DeleteClusterSchedulerConfigRequest(TypedDict):
    cluster_scheduler_config_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_scheduler_config_id.ClusterSchedulerConfigId"
    ]
    """<p>ID of the cluster policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterSchedulerConfigRequest) -> dict:
    out: dict = {}
    if "cluster_scheduler_config_id" in value:
        out["ClusterSchedulerConfigId"] = value["cluster_scheduler_config_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterSchedulerConfigRequest:
    out: DeleteClusterSchedulerConfigRequest = {}  # type: ignore[typeddict-item]
    if "ClusterSchedulerConfigId" in data:
        out["cluster_scheduler_config_id"] = data["ClusterSchedulerConfigId"]
    return out
