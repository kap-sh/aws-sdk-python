"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunitySummaryFullView``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_opportunity_customer
    import aws_sdk_partnercentral_selling.types.aws_opportunity_insights
    import aws_sdk_partnercentral_selling.types.aws_opportunity_life_cycle
    import aws_sdk_partnercentral_selling.types.aws_opportunity_project
    import aws_sdk_partnercentral_selling.types.aws_opportunity_related_entities
    import aws_sdk_partnercentral_selling.types.aws_opportunity_team_members_list
    import aws_sdk_partnercentral_selling.types.involvement_type_change_reason
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_origin
    import aws_sdk_partnercentral_selling.types.sales_involvement_type
    import aws_sdk_partnercentral_selling.types.visibility


class AwsOpportunitySummaryFullView(TypedDict):
    related_opportunity_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    ]
    """<p>Identifier of the related partner opportunity.</p>"""
    origin: NotRequired[
        "aws_sdk_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
    ]
    """<p>Source origin of the AWS opportunity.</p>"""
    involvement_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    ]
    """<p>Type of AWS involvement in the opportunity.</p>"""
    visibility: NotRequired[
        "aws_sdk_partnercentral_selling.types.visibility.Visibility"
    ]
    """<p>Visibility level for the AWS opportunity.</p>"""
    life_cycle: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_opportunity_life_cycle.AwsOpportunityLifeCycle"
    ]
    opportunity_team: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_opportunity_team_members_list.AwsOpportunityTeamMembersList"
    ]
    """<p>AWS team members involved in the opportunity.</p>"""
    insights: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_opportunity_insights.AwsOpportunityInsights"
    ]
    involvement_type_change_reason: NotRequired[
        "aws_sdk_partnercentral_selling.types.involvement_type_change_reason.InvolvementTypeChangeReason"
    ]
    """<p>Reason for changes in AWS involvement type for the opportunity.</p>"""
    related_entity_ids: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_opportunity_related_entities.AwsOpportunityRelatedEntities"
    ]
    customer: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_opportunity_customer.AwsOpportunityCustomer"
    ]
    project: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_opportunity_project.AwsOpportunityProject"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunitySummaryFullView) -> dict:
    out: dict = {}
    if "related_opportunity_id" in value:
        out["RelatedOpportunityId"] = value["related_opportunity_id"]
    if "origin" in value:
        import aws_sdk_partnercentral_selling.types.opportunity_origin

        out["Origin"] = (
            aws_sdk_partnercentral_selling.types.opportunity_origin.serialize_aws_json_1_0(
                value["origin"]
            )
        )
    if "involvement_type" in value:
        import aws_sdk_partnercentral_selling.types.sales_involvement_type

        out["InvolvementType"] = (
            aws_sdk_partnercentral_selling.types.sales_involvement_type.serialize_aws_json_1_0(
                value["involvement_type"]
            )
        )
    if "visibility" in value:
        import aws_sdk_partnercentral_selling.types.visibility

        out["Visibility"] = (
            aws_sdk_partnercentral_selling.types.visibility.serialize_aws_json_1_0(
                value["visibility"]
            )
        )
    if "life_cycle" in value:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_life_cycle

        out["LifeCycle"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_life_cycle.serialize_aws_json_1_0(
                value["life_cycle"]
            )
        )
    if "opportunity_team" in value:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_team_members_list

        out["OpportunityTeam"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_team_members_list.serialize_aws_json_1_0(
                value["opportunity_team"]
            )
        )
    if "insights" in value:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_insights

        out["Insights"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_insights.serialize_aws_json_1_0(
                value["insights"]
            )
        )
    if "involvement_type_change_reason" in value:
        import aws_sdk_partnercentral_selling.types.involvement_type_change_reason

        out["InvolvementTypeChangeReason"] = (
            aws_sdk_partnercentral_selling.types.involvement_type_change_reason.serialize_aws_json_1_0(
                value["involvement_type_change_reason"]
            )
        )
    if "related_entity_ids" in value:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_related_entities

        out["RelatedEntityIds"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_related_entities.serialize_aws_json_1_0(
                value["related_entity_ids"]
            )
        )
    if "customer" in value:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_customer

        out["Customer"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_project

        out["Project"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_project.serialize_aws_json_1_0(
                value["project"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunitySummaryFullView:
    out: AwsOpportunitySummaryFullView = {}  # type: ignore[typeddict-item]
    if "RelatedOpportunityId" in data:
        out["related_opportunity_id"] = data["RelatedOpportunityId"]
    if "Origin" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_origin

        out["origin"] = (
            aws_sdk_partnercentral_selling.types.opportunity_origin.deserialize_aws_json_1_0(
                data["Origin"]
            )
        )
    if "InvolvementType" in data:
        import aws_sdk_partnercentral_selling.types.sales_involvement_type

        out["involvement_type"] = (
            aws_sdk_partnercentral_selling.types.sales_involvement_type.deserialize_aws_json_1_0(
                data["InvolvementType"]
            )
        )
    if "Visibility" in data:
        import aws_sdk_partnercentral_selling.types.visibility

        out["visibility"] = (
            aws_sdk_partnercentral_selling.types.visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    if "LifeCycle" in data:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_life_cycle

        out["life_cycle"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_life_cycle.deserialize_aws_json_1_0(
                data["LifeCycle"]
            )
        )
    if "OpportunityTeam" in data:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_team_members_list

        out["opportunity_team"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_team_members_list.deserialize_aws_json_1_0(
                data["OpportunityTeam"]
            )
        )
    if "Insights" in data:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_insights

        out["insights"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_insights.deserialize_aws_json_1_0(
                data["Insights"]
            )
        )
    if "InvolvementTypeChangeReason" in data:
        import aws_sdk_partnercentral_selling.types.involvement_type_change_reason

        out["involvement_type_change_reason"] = (
            aws_sdk_partnercentral_selling.types.involvement_type_change_reason.deserialize_aws_json_1_0(
                data["InvolvementTypeChangeReason"]
            )
        )
    if "RelatedEntityIds" in data:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_related_entities

        out["related_entity_ids"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_related_entities.deserialize_aws_json_1_0(
                data["RelatedEntityIds"]
            )
        )
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_customer

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if "Project" in data:
        import aws_sdk_partnercentral_selling.types.aws_opportunity_project

        out["project"] = (
            aws_sdk_partnercentral_selling.types.aws_opportunity_project.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    return out
