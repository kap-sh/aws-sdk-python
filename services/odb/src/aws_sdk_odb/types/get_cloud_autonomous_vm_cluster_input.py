"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudAutonomousVmClusterInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class GetCloudAutonomousVmClusterInput(TypedDict):
    cloud_autonomous_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudAutonomousVmClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudAutonomousVmClusterInput:
    out: GetCloudAutonomousVmClusterInput = {}  # type: ignore[typeddict-item]
    return out
