"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudExadataInfrastructureInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class GetCloudExadataInfrastructureInput(TypedDict, closed=True):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudExadataInfrastructureInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudExadataInfrastructureInput:
    out: GetCloudExadataInfrastructureInput = {}  # type: ignore[typeddict-item]
    return out
