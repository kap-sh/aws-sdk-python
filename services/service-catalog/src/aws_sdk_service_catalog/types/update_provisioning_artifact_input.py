"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisioningArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.provisioning_artifact_active
    import aws_sdk_service_catalog.types.provisioning_artifact_description
    import aws_sdk_service_catalog.types.provisioning_artifact_guidance
    import aws_sdk_service_catalog.types.provisioning_artifact_name


class UpdateProvisioningArtifactInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    provisioning_artifact_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact.</p>"""
    name: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The updated name of the provisioning artifact.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_description.ProvisioningArtifactDescription"
    ]
    """<p>The updated description of the provisioning artifact.</p>"""
    active: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_active.ProvisioningArtifactActive"
    ]
    """<p>Indicates whether the product version is active.</p> <p>Inactive provisioning artifacts are invisible to end users. End users cannot launch or update a provisioned product from an inactive provisioning artifact.</p>"""
    guidance: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_guidance.ProvisioningArtifactGuidance"
    ]
    """<p>Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.</p> <p>The <code>DEFAULT</code> value indicates that the product version is active.</p> <p>The administrator can set the guidance to <code>DEPRECATED</code> to inform users that the product version is deprecated. Users are able to make updates to a provisioned product of a deprecated version but cannot launch new provisioned products using a deprecated version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisioningArtifactInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "active" in value:
        out["Active"] = value["active"]
    if "guidance" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_guidance

        out["Guidance"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_guidance.serialize_aws_json_1_1(
                value["guidance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisioningArtifactInput:
    out: UpdateProvisioningArtifactInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    else:
        raise DeserializationError(
            "UpdateProvisioningArtifactInput.product_id required"
        )
    if "ProvisioningArtifactId" in data:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        raise DeserializationError(
            "UpdateProvisioningArtifactInput.provisioning_artifact_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Active" in data:
        out["active"] = data["Active"]
    if "Guidance" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_guidance

        out["guidance"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_guidance.deserialize_aws_json_1_1(
                data["Guidance"]
            )
        )
    return out
