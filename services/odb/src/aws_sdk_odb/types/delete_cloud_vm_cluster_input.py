"""Generated from Smithy shape ``com.amazonaws.odb#DeleteCloudVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class DeleteCloudVmClusterInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCloudVmClusterInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCloudVmClusterInput:
    out: DeleteCloudVmClusterInput = {}  # type: ignore[typeddict-item]
    return out
