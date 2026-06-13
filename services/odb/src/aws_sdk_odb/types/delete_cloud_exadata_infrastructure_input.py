"""Generated from Smithy shape ``com.amazonaws.odb#DeleteCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class DeleteCloudExadataInfrastructureInput(TypedDict):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Exadata infrastructure to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCloudExadataInfrastructureInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCloudExadataInfrastructureInput:
    out: DeleteCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    return out
