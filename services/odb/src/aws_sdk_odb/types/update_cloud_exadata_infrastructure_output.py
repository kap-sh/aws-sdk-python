"""Generated from Smithy shape ``com.amazonaws.odb#UpdateCloudExadataInfrastructureOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_status


class UpdateCloudExadataInfrastructureOutput(TypedDict):
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the updated Exadata infrastructure.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Exadata infrastructure after the update operation.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Exadata infrastructure after the update operation.</p>"""
    cloud_exadata_infrastructure_id: "str"
    """<p>The unique identifier of the updated Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCloudExadataInfrastructureOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCloudExadataInfrastructureOutput:
    out: UpdateCloudExadataInfrastructureOutput = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "cloudExadataInfrastructureId" in data:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        raise DeserializationError(
            "UpdateCloudExadataInfrastructureOutput.cloud_exadata_infrastructure_id required"
        )
    return out
