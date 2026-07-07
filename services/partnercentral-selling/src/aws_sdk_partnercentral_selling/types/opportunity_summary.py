"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.customer_summary
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.life_cycle_summary
    import aws_sdk_partnercentral_selling.types.opportunity_arn
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_type
    import aws_sdk_partnercentral_selling.types.project_summary


class OpportunitySummary(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the opportunity, either <code>AWS</code> or <code>Sandbox</code>. This indicates the environment in which the opportunity is managed.</p>"""
    id: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Read-only, system-generated <code>Opportunity</code> unique identifier.</p>"""
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_arn.OpportunityArn"
    ]
    """<p> The Amazon Resource Name (ARN) for the opportunity. This globally unique identifier can be used for IAM policies and cross-service references. </p>"""
    partner_opportunity_identifier: NotRequired["str"]
    """<p>Specifies the <code>Opportunity</code>'s unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner. It allows partners to link an opportunity to their CRM.</p>"""
    opportunity_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_type.OpportunityType"
    ]
    """<p>Specifies opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New Opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal Opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion Opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>"""
    last_modified_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p> <code>DateTime</code> when the <code>Opportunity</code> was last modified.</p>"""
    created_date: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    """<p> <code>DateTime</code> when the <code>Opportunity</code> was last created.</p>"""
    life_cycle: NotRequired[
        "aws_sdk_partnercentral_selling.types.life_cycle_summary.LifeCycleSummary"
    ]
    """<p>An object that contains the <code>Opportunity</code>'s lifecycle details.</p>"""
    customer: NotRequired[
        "aws_sdk_partnercentral_selling.types.customer_summary.CustomerSummary"
    ]
    """<p>An object that contains the <code>Opportunity</code>'s customer details.</p>"""
    project: NotRequired[
        "aws_sdk_partnercentral_selling.types.project_summary.ProjectSummary"
    ]
    """<p>An object that contains the <code>Opportunity</code>'s project details summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySummary) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "partner_opportunity_identifier" in value:
        out["PartnerOpportunityIdentifier"] = value["partner_opportunity_identifier"]
    if "opportunity_type" in value:
        import aws_sdk_partnercentral_selling.types.opportunity_type

        out["OpportunityType"] = (
            aws_sdk_partnercentral_selling.types.opportunity_type.serialize_aws_json_1_0(
                value["opportunity_type"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["LastModifiedDate"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["last_modified_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["CreatedDate"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["created_date"]
            )
        )
    if "life_cycle" in value:
        import aws_sdk_partnercentral_selling.types.life_cycle_summary

        out["LifeCycle"] = (
            aws_sdk_partnercentral_selling.types.life_cycle_summary.serialize_aws_json_1_0(
                value["life_cycle"]
            )
        )
    if "customer" in value:
        import aws_sdk_partnercentral_selling.types.customer_summary

        out["Customer"] = (
            aws_sdk_partnercentral_selling.types.customer_summary.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import aws_sdk_partnercentral_selling.types.project_summary

        out["Project"] = (
            aws_sdk_partnercentral_selling.types.project_summary.serialize_aws_json_1_0(
                value["project"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunitySummary:
    out: OpportunitySummary = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("OpportunitySummary.catalog required")
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "PartnerOpportunityIdentifier" in data:
        out["partner_opportunity_identifier"] = data["PartnerOpportunityIdentifier"]
    if "OpportunityType" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_type

        out["opportunity_type"] = (
            aws_sdk_partnercentral_selling.types.opportunity_type.deserialize_aws_json_1_0(
                data["OpportunityType"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["last_modified_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    if "CreatedDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["created_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    if "LifeCycle" in data:
        import aws_sdk_partnercentral_selling.types.life_cycle_summary

        out["life_cycle"] = (
            aws_sdk_partnercentral_selling.types.life_cycle_summary.deserialize_aws_json_1_0(
                data["LifeCycle"]
            )
        )
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.customer_summary

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.customer_summary.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if "Project" in data:
        import aws_sdk_partnercentral_selling.types.project_summary

        out["project"] = (
            aws_sdk_partnercentral_selling.types.project_summary.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    return out
