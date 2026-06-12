"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#UpdateBenefitApplicationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_description
    import aws_sdk_partnercentral_benefits.types.benefit_application_identifier
    import aws_sdk_partnercentral_benefits.types.benefit_application_name
    import aws_sdk_partnercentral_benefits.types.catalog_name
    import aws_sdk_partnercentral_benefits.types.contacts
    import aws_sdk_partnercentral_benefits.types.file_input_details


class UpdateBenefitApplicationInput(TypedDict):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog the application belongs to.</p>"""
    client_token: "str"
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the update request.</p>"""
    name: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
    ]
    """<p>The updated human-readable name for the benefit application.</p>"""
    description: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_description.BenefitApplicationDescription"
    ]
    """<p>The updated detailed description of the benefit application.</p>"""
    identifier: "aws_sdk_partnercentral_benefits.types.benefit_application_identifier.BenefitApplicationIdentifier"
    """<p>The unique identifier of the benefit application to update.</p>"""
    revision: "str"
    """<p>The current revision number of the benefit application to ensure optimistic concurrency control.</p>"""
    benefit_application_details: NotRequired["object"]
    """<p>Updated detailed information and requirements specific to the benefit being requested.</p>"""
    partner_contacts: NotRequired[
        "aws_sdk_partnercentral_benefits.types.contacts.Contacts"
    ]
    """<p>Updated contact information for partner representatives responsible for this benefit application.</p>"""
    file_details: NotRequired[
        "aws_sdk_partnercentral_benefits.types.file_input_details.FileInputDetails"
    ]
    """<p>Updated supporting documents and files attached to the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Identifier"] = value["identifier"]
    out["Revision"] = value["revision"]
    if "benefit_application_details" in value:
        out["BenefitApplicationDetails"] = value["benefit_application_details"]
    if "partner_contacts" in value:
        import aws_sdk_partnercentral_benefits.types.contacts

        out["PartnerContacts"] = (
            aws_sdk_partnercentral_benefits.types.contacts.serialize_aws_json_1_0(
                value["partner_contacts"]
            )
        )
    if "file_details" in value:
        import aws_sdk_partnercentral_benefits.types.file_input_details

        out["FileDetails"] = (
            aws_sdk_partnercentral_benefits.types.file_input_details.serialize_aws_json_1_0(
                value["file_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBenefitApplicationInput:
    out: UpdateBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("UpdateBenefitApplicationInput.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "UpdateBenefitApplicationInput.client_token required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("UpdateBenefitApplicationInput.identifier required")
    if "Revision" in data:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError("UpdateBenefitApplicationInput.revision required")
    if "BenefitApplicationDetails" in data:
        out["benefit_application_details"] = data["BenefitApplicationDetails"]
    if "PartnerContacts" in data:
        import aws_sdk_partnercentral_benefits.types.contacts

        out["partner_contacts"] = (
            aws_sdk_partnercentral_benefits.types.contacts.deserialize_aws_json_1_0(
                data["PartnerContacts"]
            )
        )
    if "FileDetails" in data:
        import aws_sdk_partnercentral_benefits.types.file_input_details

        out["file_details"] = (
            aws_sdk_partnercentral_benefits.types.file_input_details.deserialize_aws_json_1_0(
                data["FileDetails"]
            )
        )
    return out
