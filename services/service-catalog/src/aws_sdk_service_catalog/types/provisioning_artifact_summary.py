"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.provisioning_artifact_created_time
    import aws_sdk_service_catalog.types.provisioning_artifact_description
    import aws_sdk_service_catalog.types.provisioning_artifact_info
    import aws_sdk_service_catalog.types.provisioning_artifact_name


class ProvisioningArtifactSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    name: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_description.ProvisioningArtifactDescription"
    ]
    """<p>The description of the provisioning artifact.</p>"""
    created_time: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_created_time.ProvisioningArtifactCreatedTime"
    ]
    """<p>The UTC time stamp of the creation time.</p>"""
    provisioning_artifact_metadata: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_info.ProvisioningArtifactInfo"
    ]
    """<p>The metadata for the provisioning artifact. This is used with Amazon Web Services Marketplace products.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_created_time

        out["CreatedTime"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "provisioning_artifact_metadata" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_info

        out["ProvisioningArtifactMetadata"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_info.serialize_aws_json_1_1(
                value["provisioning_artifact_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactSummary:
    out: ProvisioningArtifactSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedTime" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_created_time

        out["created_time"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if "ProvisioningArtifactMetadata" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_info

        out["provisioning_artifact_metadata"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_info.deserialize_aws_json_1_1(
                data["ProvisioningArtifactMetadata"]
            )
        )
    return out
