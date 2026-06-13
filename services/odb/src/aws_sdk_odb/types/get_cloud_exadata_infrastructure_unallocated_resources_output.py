"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureUnallocatedResourcesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.cloud_exadata_infrastructure_unallocated_resources


class GetCloudExadataInfrastructureUnallocatedResourcesOutput(TypedDict):
    cloud_exadata_infrastructure_unallocated_resources: NotRequired[
        "aws_sdk_odb.types.cloud_exadata_infrastructure_unallocated_resources.CloudExadataInfrastructureUnallocatedResources"
    ]
    """<p>Details about the unallocated resources in the specified Cloud Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetCloudExadataInfrastructureUnallocatedResourcesOutput,
) -> dict:
    out: dict = {}
    if "cloud_exadata_infrastructure_unallocated_resources" in value:
        import aws_sdk_odb.types.cloud_exadata_infrastructure_unallocated_resources

        out["cloudExadataInfrastructureUnallocatedResources"] = (
            aws_sdk_odb.types.cloud_exadata_infrastructure_unallocated_resources.serialize_aws_json_1_0(
                value["cloud_exadata_infrastructure_unallocated_resources"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetCloudExadataInfrastructureUnallocatedResourcesOutput:
    out: GetCloudExadataInfrastructureUnallocatedResourcesOutput = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructureUnallocatedResources" in data:
        import aws_sdk_odb.types.cloud_exadata_infrastructure_unallocated_resources

        out["cloud_exadata_infrastructure_unallocated_resources"] = (
            aws_sdk_odb.types.cloud_exadata_infrastructure_unallocated_resources.deserialize_aws_json_1_0(
                data["cloudExadataInfrastructureUnallocatedResources"]
            )
        )
    return out
