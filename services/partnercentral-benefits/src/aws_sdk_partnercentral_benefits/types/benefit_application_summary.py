"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#BenefitApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.arns
    import aws_sdk_partnercentral_benefits.types.attributes
    import aws_sdk_partnercentral_benefits.types.benefit_application_id
    import aws_sdk_partnercentral_benefits.types.benefit_application_name
    import aws_sdk_partnercentral_benefits.types.benefit_application_stage
    import aws_sdk_partnercentral_benefits.types.benefit_application_status
    import aws_sdk_partnercentral_benefits.types.benefit_id
    import aws_sdk_partnercentral_benefits.types.catalog_name
    import aws_sdk_partnercentral_benefits.types.fulfillment_types
    import aws_sdk_partnercentral_benefits.types.programs
    import aws_sdk_partnercentral_benefits.types.timestamp


class BenefitApplicationSummary(TypedDict, closed=True):
    catalog: NotRequired[
        "aws_sdk_partnercentral_benefits.types.catalog_name.CatalogName"
    ]
    """<p>The catalog identifier that the benefit application belongs to.</p>"""
    name: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_name.BenefitApplicationName"
    ]
    """<p>The human-readable name of the benefit application.</p>"""
    id: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_id.BenefitApplicationId"
    ]
    """<p>The unique identifier of the benefit application.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the benefit application.</p>"""
    benefit_id: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_id.BenefitId"
    ]
    """<p>The identifier of the benefit being requested in this application.</p>"""
    programs: NotRequired["aws_sdk_partnercentral_benefits.types.programs.Programs"]
    """<p>The AWS partner programs associated with this benefit application.</p>"""
    fulfillment_types: NotRequired[
        "aws_sdk_partnercentral_benefits.types.fulfillment_types.FulfillmentTypes"
    ]
    """<p>The fulfillment types requested for this benefit application.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_status.BenefitApplicationStatus"
    ]
    """<p>The current processing status of the benefit application.</p>"""
    stage: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_stage.BenefitApplicationStage"
    ]
    """<p>The current stage in the benefit application processing workflow..</p>"""
    created_at: NotRequired["aws_sdk_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit application was created.</p>"""
    updated_at: NotRequired["aws_sdk_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the benefit application was last updated.</p>"""
    benefit_application_details: NotRequired[
        "aws_sdk_partnercentral_benefits.types.attributes.Attributes"
    ]
    """<p>Additional attributes and metadata associated with the benefit application.</p>"""
    associated_resources: NotRequired["aws_sdk_partnercentral_benefits.types.arns.Arns"]
    """<p>AWS resources that are associated with this benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BenefitApplicationSummary) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["Catalog"] = value["catalog"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "benefit_id" in value:
        out["BenefitId"] = value["benefit_id"]
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
    if "status" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_application_status

        out["Status"] = (
            aws_sdk_partnercentral_benefits.types.benefit_application_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "stage" in value:
        out["Stage"] = value["stage"]
    if "created_at" in value:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["UpdatedAt"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "benefit_application_details" in value:
        import aws_sdk_partnercentral_benefits.types.attributes

        out["BenefitApplicationDetails"] = (
            aws_sdk_partnercentral_benefits.types.attributes.serialize_aws_json_1_0(
                value["benefit_application_details"]
            )
        )
    if "associated_resources" in value:
        import aws_sdk_partnercentral_benefits.types.arns

        out["AssociatedResources"] = (
            aws_sdk_partnercentral_benefits.types.arns.serialize_aws_json_1_0(
                value["associated_resources"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BenefitApplicationSummary:
    out: BenefitApplicationSummary = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "BenefitId" in data:
        out["benefit_id"] = data["BenefitId"]
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
    if "Status" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_application_status

        out["status"] = (
            aws_sdk_partnercentral_benefits.types.benefit_application_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "Stage" in data:
        out["stage"] = data["Stage"]
    if "CreatedAt" in data:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["created_at"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_partnercentral_benefits.types.timestamp

        out["updated_at"] = (
            aws_sdk_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    if "BenefitApplicationDetails" in data:
        import aws_sdk_partnercentral_benefits.types.attributes

        out["benefit_application_details"] = (
            aws_sdk_partnercentral_benefits.types.attributes.deserialize_aws_json_1_0(
                data["BenefitApplicationDetails"]
            )
        )
    if "AssociatedResources" in data:
        import aws_sdk_partnercentral_benefits.types.arns

        out["associated_resources"] = (
            aws_sdk_partnercentral_benefits.types.arns.deserialize_aws_json_1_0(
                data["AssociatedResources"]
            )
        )
    return out
