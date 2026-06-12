"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetOpportunityResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.customer
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.life_cycle
    import aws_sdk_partnercentral_selling.types.marketing
    import aws_sdk_partnercentral_selling.types.national_security
    import aws_sdk_partnercentral_selling.types.opportunity_arn
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_type
    import aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list
    import aws_sdk_partnercentral_selling.types.primary_needs_from_aws
    import aws_sdk_partnercentral_selling.types.project
    import aws_sdk_partnercentral_selling.types.related_entity_identifiers
    import aws_sdk_partnercentral_selling.types.software_revenue


class GetOpportunityResponse(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity information is retrieved from. Use <code>AWS</code> to retrieve opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> to retrieve opportunities in a secure and isolated testing environment.</p>"""
    primary_needs_from_aws: NotRequired[
        "aws_sdk_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
    ]
    """<p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an Amazon Web Services seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connect with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs Amazon Web Services RFx support.</p> </li> </ul>"""
    national_security: NotRequired[
        "aws_sdk_partnercentral_selling.types.national_security.NationalSecurity"
    ]
    """<p>Indicates whether the <code>Opportunity</code> pertains to a national security project. This field must be set to <code>true</code> only when the customer's industry is <i>Government</i>. Additional privacy and security measures apply during the review and management process for opportunities marked as <code>NationalSecurity</code>.</p>"""
    partner_opportunity_identifier: NotRequired["str"]
    """<p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.</p>"""
    customer: NotRequired["aws_sdk_partnercentral_selling.types.customer.Customer"]
    """<p>Specifies details of the customer associated with the <code>Opportunity</code>.</p>"""
    project: NotRequired["aws_sdk_partnercentral_selling.types.project.Project"]
    """<p>An object that contains project details summary for the <code>Opportunity</code>.</p>"""
    opportunity_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_type.OpportunityType"
    ]
    """<p>Specifies the opportunity type as renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, which helps to ensure service continuity.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of a customer's contract or subscription, either by adding new services or increasing the volume of existing services.</p> </li> </ul>"""
    marketing: NotRequired["aws_sdk_partnercentral_selling.types.marketing.Marketing"]
    """<p>An object that contains marketing details for the <code>Opportunity</code>.</p>"""
    software_revenue: NotRequired[
        "aws_sdk_partnercentral_selling.types.software_revenue.SoftwareRevenue"
    ]
    """<p>Specifies details of a customer's procurement terms. Required only for partners in eligible programs.</p>"""
    id: "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    """<p>Read-only, system generated <code>Opportunity</code> unique identifier.</p>"""
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_arn.OpportunityArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the opportunity.</p>"""
    last_modified_date: "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    """<p> <code>DateTime</code> when the opportunity was last modified.</p>"""
    created_date: "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    """<p> <code>DateTime</code> when the <code>Opportunity</code> was last created.</p>"""
    related_entity_identifiers: "aws_sdk_partnercentral_selling.types.related_entity_identifiers.RelatedEntityIdentifiers"
    """<p>Provides information about the associations of other entities with the opportunity. These entities include identifiers for <code>AWSProducts</code>, <code>Partner Solutions</code>, and <code>AWSMarketplaceOffers</code>.</p>"""
    life_cycle: NotRequired["aws_sdk_partnercentral_selling.types.life_cycle.LifeCycle"]
    """<p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>"""
    opportunity_team: NotRequired[
        "aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
    ]
    """<p>Represents the internal team handling the opportunity. Specify the members involved in collaborating on this opportunity within the partner's organization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOpportunityResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "primary_needs_from_aws" in value:
        import aws_sdk_partnercentral_selling.types.primary_needs_from_aws

        out["PrimaryNeedsFromAws"] = (
            aws_sdk_partnercentral_selling.types.primary_needs_from_aws.serialize_aws_json_1_0(
                value["primary_needs_from_aws"]
            )
        )
    if "national_security" in value:
        import aws_sdk_partnercentral_selling.types.national_security

        out["NationalSecurity"] = (
            aws_sdk_partnercentral_selling.types.national_security.serialize_aws_json_1_0(
                value["national_security"]
            )
        )
    if "partner_opportunity_identifier" in value:
        out["PartnerOpportunityIdentifier"] = value["partner_opportunity_identifier"]
    if "customer" in value:
        import aws_sdk_partnercentral_selling.types.customer

        out["Customer"] = (
            aws_sdk_partnercentral_selling.types.customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import aws_sdk_partnercentral_selling.types.project

        out["Project"] = (
            aws_sdk_partnercentral_selling.types.project.serialize_aws_json_1_0(
                value["project"]
            )
        )
    if "opportunity_type" in value:
        import aws_sdk_partnercentral_selling.types.opportunity_type

        out["OpportunityType"] = (
            aws_sdk_partnercentral_selling.types.opportunity_type.serialize_aws_json_1_0(
                value["opportunity_type"]
            )
        )
    if "marketing" in value:
        import aws_sdk_partnercentral_selling.types.marketing

        out["Marketing"] = (
            aws_sdk_partnercentral_selling.types.marketing.serialize_aws_json_1_0(
                value["marketing"]
            )
        )
    if "software_revenue" in value:
        import aws_sdk_partnercentral_selling.types.software_revenue

        out["SoftwareRevenue"] = (
            aws_sdk_partnercentral_selling.types.software_revenue.serialize_aws_json_1_0(
                value["software_revenue"]
            )
        )
    out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    import aws_sdk_partnercentral_selling.types.date_time

    out["LastModifiedDate"] = (
        aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["last_modified_date"]
        )
    )
    import aws_sdk_partnercentral_selling.types.date_time

    out["CreatedDate"] = (
        aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import aws_sdk_partnercentral_selling.types.related_entity_identifiers

    out["RelatedEntityIdentifiers"] = (
        aws_sdk_partnercentral_selling.types.related_entity_identifiers.serialize_aws_json_1_0(
            value["related_entity_identifiers"]
        )
    )
    if "life_cycle" in value:
        import aws_sdk_partnercentral_selling.types.life_cycle

        out["LifeCycle"] = (
            aws_sdk_partnercentral_selling.types.life_cycle.serialize_aws_json_1_0(
                value["life_cycle"]
            )
        )
    if "opportunity_team" in value:
        import aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list

        out["OpportunityTeam"] = (
            aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list.serialize_aws_json_1_0(
                value["opportunity_team"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOpportunityResponse:
    out: GetOpportunityResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetOpportunityResponse.catalog required")
    if "PrimaryNeedsFromAws" in data:
        import aws_sdk_partnercentral_selling.types.primary_needs_from_aws

        out["primary_needs_from_aws"] = (
            aws_sdk_partnercentral_selling.types.primary_needs_from_aws.deserialize_aws_json_1_0(
                data["PrimaryNeedsFromAws"]
            )
        )
    if "NationalSecurity" in data:
        import aws_sdk_partnercentral_selling.types.national_security

        out["national_security"] = (
            aws_sdk_partnercentral_selling.types.national_security.deserialize_aws_json_1_0(
                data["NationalSecurity"]
            )
        )
    if "PartnerOpportunityIdentifier" in data:
        out["partner_opportunity_identifier"] = data["PartnerOpportunityIdentifier"]
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.customer

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if "Project" in data:
        import aws_sdk_partnercentral_selling.types.project

        out["project"] = (
            aws_sdk_partnercentral_selling.types.project.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    if "OpportunityType" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_type

        out["opportunity_type"] = (
            aws_sdk_partnercentral_selling.types.opportunity_type.deserialize_aws_json_1_0(
                data["OpportunityType"]
            )
        )
    if "Marketing" in data:
        import aws_sdk_partnercentral_selling.types.marketing

        out["marketing"] = (
            aws_sdk_partnercentral_selling.types.marketing.deserialize_aws_json_1_0(
                data["Marketing"]
            )
        )
    if "SoftwareRevenue" in data:
        import aws_sdk_partnercentral_selling.types.software_revenue

        out["software_revenue"] = (
            aws_sdk_partnercentral_selling.types.software_revenue.deserialize_aws_json_1_0(
                data["SoftwareRevenue"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetOpportunityResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "LastModifiedDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["last_modified_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    else:
        raise DeserializationError("GetOpportunityResponse.last_modified_date required")
    if "CreatedDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["created_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    else:
        raise DeserializationError("GetOpportunityResponse.created_date required")
    if "RelatedEntityIdentifiers" in data:
        import aws_sdk_partnercentral_selling.types.related_entity_identifiers

        out["related_entity_identifiers"] = (
            aws_sdk_partnercentral_selling.types.related_entity_identifiers.deserialize_aws_json_1_0(
                data["RelatedEntityIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "GetOpportunityResponse.related_entity_identifiers required"
        )
    if "LifeCycle" in data:
        import aws_sdk_partnercentral_selling.types.life_cycle

        out["life_cycle"] = (
            aws_sdk_partnercentral_selling.types.life_cycle.deserialize_aws_json_1_0(
                data["LifeCycle"]
            )
        )
    if "OpportunityTeam" in data:
        import aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list

        out["opportunity_team"] = (
            aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list.deserialize_aws_json_1_0(
                data["OpportunityTeam"]
            )
        )
    return out
