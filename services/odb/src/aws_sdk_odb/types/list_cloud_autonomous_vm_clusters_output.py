"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudAutonomousVmClustersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_autonomous_vm_cluster_list


class ListCloudAutonomousVmClustersOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The pagination token to continue listing from.</p>"""
    cloud_autonomous_vm_clusters: "aws_sdk_odb.types.cloud_autonomous_vm_cluster_list.CloudAutonomousVmClusterList"
    """<p>The list of Autonomous VM clusters in the specified Cloud Exadata Infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudAutonomousVmClustersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.cloud_autonomous_vm_cluster_list

    out["cloudAutonomousVmClusters"] = (
        aws_sdk_odb.types.cloud_autonomous_vm_cluster_list.serialize_aws_json_1_0(
            value["cloud_autonomous_vm_clusters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudAutonomousVmClustersOutput:
    out: ListCloudAutonomousVmClustersOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "cloudAutonomousVmClusters" in data:
        import aws_sdk_odb.types.cloud_autonomous_vm_cluster_list

        out["cloud_autonomous_vm_clusters"] = (
            aws_sdk_odb.types.cloud_autonomous_vm_cluster_list.deserialize_aws_json_1_0(
                data["cloudAutonomousVmClusters"]
            )
        )
    else:
        raise DeserializationError(
            "ListCloudAutonomousVmClustersOutput.cloud_autonomous_vm_clusters required"
        )
    return out
