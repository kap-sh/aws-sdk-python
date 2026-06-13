"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudVmClusterInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class GetCloudVmClusterInput(TypedDict):
    cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudVmClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudVmClusterInput:
    out: GetCloudVmClusterInput = {}  # type: ignore[typeddict-item]
    return out
