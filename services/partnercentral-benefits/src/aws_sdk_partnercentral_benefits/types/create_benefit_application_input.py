"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#CreateBenefitApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.arns
    import aws_sdk_partnercentral_benefits.types.benefit_application_description
    import aws_sdk_partnercentral_benefits.types.benefit_application_name
    import aws_sdk_partnercentral_benefits.types.catalog_name
    import aws_sdk_partnercentral_benefits.types.contacts
    import aws_sdk_partnercentral_benefits.types.file_input_details
    import aws_sdk_partnercentral_benefits.types.fulfillment_types
    import aws_sdk_partnercentral_benefits.types.tags


class CreateBenefitApplicationInput(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog to create the application in.</p>"""
    client_token: "str"
    """<p>A unique, case-sensitive identifier to ensure idempotent processing of the creation request.</p>"""
    name: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
    ]
    """<p>A human-readable name for the benefit application.</p>"""
    description: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_description.BenefitApplicationDescription"
    ]
    """<p>A detailed description of the benefit application and its intended use.</p>"""
    benefit_identifier: "str"
    """<p>The unique identifier of the benefit being requested in this application.</p>"""
    fulfillment_types: NotRequired[
        "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>The types of fulfillment requested for this benefit application (e.g., credits, access, disbursement).</p>"""
    benefit_application_details: NotRequired["object"]
    """<p>Detailed information and requirements specific to the benefit being requested.</p>"""
    tags: NotRequired["aws_sdk_partnercentral_benefits.types.tags.Tags"]
    """<p>Key-value pairs to categorize and organize the benefit application.</p>"""
    associated_resources: NotRequired["aws_sdk_partnercentral_benefits.types.arns.Arns"]
    """<p>AWS resources that are associated with this benefit application.</p>"""
    partner_contacts: NotRequired[
        "aws_sdk_partnercentral_benefits.types.contacts.Contacts"
    ]
    """<p>Contact information for partner representatives responsible for this benefit application.</p>"""
    file_details: NotRequired[
        "aws_sdk_partnercentral_benefits.types.file_input_details.FileInputDetails"
    ]
    """<p>Supporting documents and files attached to the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBenefitApplicationInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["BenefitIdentifier"] = value["benefit_identifier"]
    if "fulfillment_types" in value:
        import aws_sdk_partnercentral_benefits.types.fulfillment_types

        out["FulfillmentTypes"] = (
            aws_sdk_partnercentral_benefits.types.fulfillment_types.serialize_aws_json_1_0(
                value["fulfillment_types"]
            )
        )
    if "benefit_application_details" in value:
        out["BenefitApplicationDetails"] = value["benefit_application_details"]
    if "tags" in value:
        import aws_sdk_partnercentral_benefits.types.tags

        out["Tags"] = aws_sdk_partnercentral_benefits.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    if "associated_resources" in value:
        import aws_sdk_partnercentral_benefits.types.arns

        out["AssociatedResources"] = (
            aws_sdk_partnercentral_benefits.types.arns.serialize_aws_json_1_0(
                value["associated_resources"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> CreateBenefitApplicationInput:
    out: CreateBenefitApplicationInput = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreateBenefitApplicationInput.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateBenefitApplicationInput.client_token required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "BenefitIdentifier" in data:
        out["benefit_identifier"] = data["BenefitIdentifier"]
    else:
        raise DeserializationError(
            "CreateBenefitApplicationInput.benefit_identifier required"
        )
    if "FulfillmentTypes" in data:
        import aws_sdk_partnercentral_benefits.types.fulfillment_types

        out["fulfillment_types"] = (
            aws_sdk_partnercentral_benefits.types.fulfillment_types.deserialize_aws_json_1_0(
                data["FulfillmentTypes"]
            )
        )
    if "BenefitApplicationDetails" in data:
        out["benefit_application_details"] = data["BenefitApplicationDetails"]
    if "Tags" in data:
        import aws_sdk_partnercentral_benefits.types.tags

        out["tags"] = (
            aws_sdk_partnercentral_benefits.types.tags.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "AssociatedResources" in data:
        import aws_sdk_partnercentral_benefits.types.arns

        out["associated_resources"] = (
            aws_sdk_partnercentral_benefits.types.arns.deserialize_aws_json_1_0(
                data["AssociatedResources"]
            )
        )
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
