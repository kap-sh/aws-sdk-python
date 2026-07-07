"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.provisioning_artifact_created_time
    import aws_sdk_service_catalog.types.provisioning_artifact_description
    import aws_sdk_service_catalog.types.provisioning_artifact_guidance
    import aws_sdk_service_catalog.types.provisioning_artifact_name


class ProvisioningArtifact(TypedDict, closed=True):
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
    guidance: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_guidance.ProvisioningArtifactGuidance"
    ]
    """<p>Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifact) -> dict:
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
    if "guidance" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_guidance

        out["Guidance"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_guidance.serialize_aws_json_1_1(
                value["guidance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifact:
    out: ProvisioningArtifact = {}  # type: ignore[typeddict-item]
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
    if "Guidance" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_guidance

        out["guidance"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_guidance.deserialize_aws_json_1_1(
                data["Guidance"]
            )
        )
    return out
