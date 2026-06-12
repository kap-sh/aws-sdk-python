"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityEngagementInvitationSort``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.opportunity_engagement_invitation_sort_name
    import aws_sdk_partnercentral_selling.types.sort_order


class OpportunityEngagementInvitationSort(TypedDict):
    sort_order: "aws_sdk_partnercentral_selling.types.sort_order.SortOrder"
    """<p>Defines the order in which the Engagement Invitations are sorted. The values can be <code>ASC</code> (ascending) or <code>DESC</code> (descending).</p>"""
    sort_by: "aws_sdk_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.OpportunityEngagementInvitationSortName"
    """<p>Specifies the field by which the Engagement Invitations are sorted. Common values include <code>InvitationDate</code> and <code>Status</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityEngagementInvitationSort) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.sort_order

    out["SortOrder"] = (
        aws_sdk_partnercentral_selling.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import aws_sdk_partnercentral_selling.types.opportunity_engagement_invitation_sort_name

    out["SortBy"] = (
        aws_sdk_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunityEngagementInvitationSort:
    out: OpportunityEngagementInvitationSort = {}  # type: ignore[typeddict-item]
    if "SortOrder" in data:
        import aws_sdk_partnercentral_selling.types.sort_order

        out["sort_order"] = (
            aws_sdk_partnercentral_selling.types.sort_order.deserialize_aws_json_1_0(
                data["SortOrder"]
            )
        )
    else:
        raise DeserializationError(
            "OpportunityEngagementInvitationSort.sort_order required"
        )
    if "SortBy" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_engagement_invitation_sort_name

        out["sort_by"] = (
            aws_sdk_partnercentral_selling.types.opportunity_engagement_invitation_sort_name.deserialize_aws_json_1_0(
                data["SortBy"]
            )
        )
    else:
        raise DeserializationError(
            "OpportunityEngagementInvitationSort.sort_by required"
        )
    return out
