"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureUnallocatedResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cloud_exadata_infrastructure_unallocated_resources


class GetCloudExadataInfrastructureUnallocatedResourcesOutput(TypedDict, closed=True):
    cloud_exadata_infrastructure_unallocated_resources: NotRequired[
        "capo_odb.types.cloud_exadata_infrastructure_unallocated_resources.CloudExadataInfrastructureUnallocatedResources"
    ]
    """<p>Details about the unallocated resources in the specified Cloud Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetCloudExadataInfrastructureUnallocatedResourcesOutput,
) -> dict:
    out: dict = {}
    if "cloud_exadata_infrastructure_unallocated_resources" in value:
        import capo_odb.types.cloud_exadata_infrastructure_unallocated_resources

        out["cloudExadataInfrastructureUnallocatedResources"] = (
            capo_odb.types.cloud_exadata_infrastructure_unallocated_resources.serialize_aws_json_1_0(
                value["cloud_exadata_infrastructure_unallocated_resources"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetCloudExadataInfrastructureUnallocatedResourcesOutput:
    out: GetCloudExadataInfrastructureUnallocatedResourcesOutput = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructureUnallocatedResources" in data:
        import capo_odb.types.cloud_exadata_infrastructure_unallocated_resources

        out["cloud_exadata_infrastructure_unallocated_resources"] = (
            capo_odb.types.cloud_exadata_infrastructure_unallocated_resources.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructureUnallocatedResources"]
            )
        )
    return out
