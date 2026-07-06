"""Generated from Smithy shape ``com.amazonaws.odb#CloudExadataInfrastructureUnallocatedResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details_list
    import aws_sdk_odb.types.resource_id_or_arn


class CloudExadataInfrastructureUnallocatedResources(TypedDict, closed=True):
    cloud_autonomous_vm_clusters: NotRequired[
        "aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details_list.CloudAutonomousVmClusterResourceDetailsList"
    ]
    """<p>A list of Autonomous VM clusters associated with this Cloud Exadata Infrastructure.</p>"""
    cloud_exadata_infrastructure_display_name: NotRequired["str"]
    """<p>The display name of the Cloud Exadata infrastructure.</p>"""
    exadata_storage_in_t_bs: NotRequired["float"]
    """<p>The amount of unallocated Exadata storage available, in terabytes (TB).</p>"""
    cloud_exadata_infrastructure_id: NotRequired[
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    ]
    """<p>The unique identifier of the Cloud Exadata infrastructure.</p>"""
    local_storage_in_g_bs: NotRequired["int"]
    """<p>The amount of unallocated local storage available, in gigabytes (GB).</p>"""
    memory_in_g_bs: NotRequired["int"]
    """<p>The amount of unallocated memory available, in gigabytes (GB).</p>"""
    ocpus: NotRequired["int"]
    """<p>The number of unallocated Oracle CPU Units (OCPUs) available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: CloudExadataInfrastructureUnallocatedResources,
) -> dict:
    out: dict = {}
    if "cloud_autonomous_vm_clusters" in value:
        import aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details_list

        out["cloudAutonomousVmClusters"] = (
            aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details_list.serialize_aws_json_1_0(
                value["cloud_autonomous_vm_clusters"]
            )
        )
    if "cloud_exadata_infrastructure_display_name" in value:
        out["cloudExadataInfrastructureDisplayName"] = value[
            "cloud_exadata_infrastructure_display_name"
        ]
    if "exadata_storage_in_t_bs" in value:
        out["exadataStorageInTBs"] = value["exadata_storage_in_t_bs"]
    if "cloud_exadata_infrastructure_id" in value:
        out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    if "local_storage_in_g_bs" in value:
        out["localStorageInGBs"] = value["local_storage_in_g_bs"]
    if "memory_in_g_bs" in value:
        out["memoryInGBs"] = value["memory_in_g_bs"]
    if "ocpus" in value:
        out["ocpus"] = value["ocpus"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> CloudExadataInfrastructureUnallocatedResources:
    out: CloudExadataInfrastructureUnallocatedResources = {}  # type: ignore[typeddict-item]
    if "cloudAutonomousVmClusters" in data:
        import aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details_list

        out["cloud_autonomous_vm_clusters"] = (
            aws_sdk_odb.types.cloud_autonomous_vm_cluster_resource_details_list.deserialize_aws_json_1_0(
                data["cloudAutonomousVmClusters"]
            )
        )
    if "cloudExadataInfrastructureDisplayName" in data:
        out["cloud_exadata_infrastructure_display_name"] = data[
            "cloudExadataInfrastructureDisplayName"
        ]
    if "exadataStorageInTBs" in data:
        out["exadata_storage_in_t_bs"] = data["exadataStorageInTBs"]
    if "cloudExadataInfrastructureId" in data:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    if "localStorageInGBs" in data:
        out["local_storage_in_g_bs"] = data["localStorageInGBs"]
    if "memoryInGBs" in data:
        out["memory_in_g_bs"] = data["memoryInGBs"]
    if "ocpus" in data:
        out["ocpus"] = data["ocpus"]
    return out
