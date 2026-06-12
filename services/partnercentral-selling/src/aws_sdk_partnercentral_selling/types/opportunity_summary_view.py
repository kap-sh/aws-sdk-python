"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunitySummaryView``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.customer
    import aws_sdk_partnercentral_selling.types.life_cycle_for_view
    import aws_sdk_partnercentral_selling.types.opportunity_type
    import aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list
    import aws_sdk_partnercentral_selling.types.primary_needs_from_aws
    import aws_sdk_partnercentral_selling.types.project_view
    import aws_sdk_partnercentral_selling.types.related_entity_identifiers


class OpportunitySummaryView(TypedDict):
    opportunity_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_type.OpportunityType"
    ]
    """<p> Specifies the opportunity type. </p>"""
    lifecycle: NotRequired[
        "aws_sdk_partnercentral_selling.types.life_cycle_for_view.LifeCycleForView"
    ]
    """<p> Contains information about the opportunity's lifecycle, including its current stage, status, and important dates such as creation and last modification times. </p>"""
    opportunity_team: NotRequired[
        "aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
    ]
    """<p> Represents the internal team handling the opportunity. Specify the members involved in collaborating on an opportunity within the partner's organization. </p>"""
    primary_needs_from_aws: NotRequired[
        "aws_sdk_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
    ]
    """<p> Identifies the type of support the partner needs from AWS. </p>"""
    customer: NotRequired["aws_sdk_partnercentral_selling.types.customer.Customer"]
    project: NotRequired[
        "aws_sdk_partnercentral_selling.types.project_view.ProjectView"
    ]
    """<p> Contains summary information about the project associated with the opportunity, including project name, description, timeline, and other relevant details. </p>"""
    related_entity_identifiers: NotRequired[
        "aws_sdk_partnercentral_selling.types.related_entity_identifiers.RelatedEntityIdentifiers"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunitySummaryView) -> dict:
    out: dict = {}
    if "opportunity_type" in value:
        import aws_sdk_partnercentral_selling.types.opportunity_type

        out["OpportunityType"] = (
            aws_sdk_partnercentral_selling.types.opportunity_type.serialize_aws_json_1_0(
                value["opportunity_type"]
            )
        )
    if "lifecycle" in value:
        import aws_sdk_partnercentral_selling.types.life_cycle_for_view

        out["Lifecycle"] = (
            aws_sdk_partnercentral_selling.types.life_cycle_for_view.serialize_aws_json_1_0(
                value["lifecycle"]
            )
        )
    if "opportunity_team" in value:
        import aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list

        out["OpportunityTeam"] = (
            aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list.serialize_aws_json_1_0(
                value["opportunity_team"]
            )
        )
    if "primary_needs_from_aws" in value:
        import aws_sdk_partnercentral_selling.types.primary_needs_from_aws

        out["PrimaryNeedsFromAws"] = (
            aws_sdk_partnercentral_selling.types.primary_needs_from_aws.serialize_aws_json_1_0(
                value["primary_needs_from_aws"]
            )
        )
    if "customer" in value:
        import aws_sdk_partnercentral_selling.types.customer

        out["Customer"] = (
            aws_sdk_partnercentral_selling.types.customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import aws_sdk_partnercentral_selling.types.project_view

        out["Project"] = (
            aws_sdk_partnercentral_selling.types.project_view.serialize_aws_json_1_0(
                value["project"]
            )
        )
    if "related_entity_identifiers" in value:
        import aws_sdk_partnercentral_selling.types.related_entity_identifiers

        out["RelatedEntityIdentifiers"] = (
            aws_sdk_partnercentral_selling.types.related_entity_identifiers.serialize_aws_json_1_0(
                value["related_entity_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunitySummaryView:
    out: OpportunitySummaryView = {}  # type: ignore[typeddict-item]
    if "OpportunityType" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_type

        out["opportunity_type"] = (
            aws_sdk_partnercentral_selling.types.opportunity_type.deserialize_aws_json_1_0(
                data["OpportunityType"]
            )
        )
    if "Lifecycle" in data:
        import aws_sdk_partnercentral_selling.types.life_cycle_for_view

        out["lifecycle"] = (
            aws_sdk_partnercentral_selling.types.life_cycle_for_view.deserialize_aws_json_1_0(
                data["Lifecycle"]
            )
        )
    if "OpportunityTeam" in data:
        import aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list

        out["opportunity_team"] = (
            aws_sdk_partnercentral_selling.types.partner_opportunity_team_members_list.deserialize_aws_json_1_0(
                data["OpportunityTeam"]
            )
        )
    if "PrimaryNeedsFromAws" in data:
        import aws_sdk_partnercentral_selling.types.primary_needs_from_aws

        out["primary_needs_from_aws"] = (
            aws_sdk_partnercentral_selling.types.primary_needs_from_aws.deserialize_aws_json_1_0(
                data["PrimaryNeedsFromAws"]
            )
        )
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.customer

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if "Project" in data:
        import aws_sdk_partnercentral_selling.types.project_view

        out["project"] = (
            aws_sdk_partnercentral_selling.types.project_view.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    if "RelatedEntityIdentifiers" in data:
        import aws_sdk_partnercentral_selling.types.related_entity_identifiers

        out["related_entity_identifiers"] = (
            aws_sdk_partnercentral_selling.types.related_entity_identifiers.deserialize_aws_json_1_0(
                data["RelatedEntityIdentifiers"]
            )
        )
    return out
