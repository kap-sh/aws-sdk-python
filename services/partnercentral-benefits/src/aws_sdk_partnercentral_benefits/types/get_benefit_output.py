"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#GetBenefitOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_status
    import aws_sdk_partnercentral_benefits.types.catalog_name
    import aws_sdk_partnercentral_benefits.types.fulfillment_types
    import aws_sdk_partnercentral_benefits.types.programs


class GetBenefitOutput(TypedDict):
    id: NotRequired["str"]
    """<p>The unique identifier of the benefit.</p>"""
    catalog: NotRequired[
        "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    ]
    """<p>The catalog identifier that the benefit belongs to.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the benefit.</p>"""
    name: NotRequired["str"]
    """<p>The human-readable name of the benefit.</p>"""
    description: NotRequired["str"]
    """<p>A detailed description of the benefit and its purpose.</p>"""
    programs: NotRequired["aws_sdk_partnercentral_benefits.types.programs.Programs"]
    """<p>The AWS partner programs that this benefit is associated with.</p>"""
    fulfillment_types: NotRequired[
        "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>The available fulfillment types for this benefit (e.g., credits, access, disbursement).</p>"""
    benefit_request_schema: NotRequired["object"]
    """<p>The schema definition that describes the required fields for requesting this benefit.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_status.BenefitStatus"
    ]
    """<p>The current status of the benefit (e.g., active, inactive, deprecated).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBenefitOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "programs" in value:
        import aws_sdk_partnercentral_benefits.types.programs

        out["Programs"] = (
            aws_sdk_partnercentral_benefits.types.programs.serialize_aws_json_1_0(
                value["programs"]
            )
        )
    if "fulfillment_types" in value:
        import aws_sdk_partnercentral_benefits.types.fulfillment_types

        out["FulfillmentTypes"] = (
            aws_sdk_partnercentral_benefits.types.fulfillment_types.serialize_aws_json_1_0(
                value["fulfillment_types"]
            )
        )
    if "benefit_request_schema" in value:
        out["BenefitRequestSchema"] = value["benefit_request_schema"]
    if "status" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_status

        out["Status"] = (
            aws_sdk_partnercentral_benefits.types.benefit_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBenefitOutput:
    out: GetBenefitOutput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Programs" in data:
        import aws_sdk_partnercentral_benefits.types.programs

        out["programs"] = (
            aws_sdk_partnercentral_benefits.types.programs.deserialize_aws_json_1_0(
                data["Programs"]
            )
        )
    if "FulfillmentTypes" in data:
        import aws_sdk_partnercentral_benefits.types.fulfillment_types

        out["fulfillment_types"] = (
            aws_sdk_partnercentral_benefits.types.fulfillment_types.deserialize_aws_json_1_0(
                data["FulfillmentTypes"]
            )
        )
    if "BenefitRequestSchema" in data:
        out["benefit_request_schema"] = data["BenefitRequestSchema"]
    if "Status" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_status

        out["status"] = (
            aws_sdk_partnercentral_benefits.types.benefit_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
