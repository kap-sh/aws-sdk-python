"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.invitation


class CreateEngagementInvitationRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the engagement. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement is managed. </p>"""
    client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken"
    """<p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate invitation creations. </p>"""
    engagement_identifier: "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    """<p> The unique identifier of the <code>Engagement</code> associated with the invitation. This parameter ensures the invitation is created within the correct <code>Engagement</code> context. </p>"""
    invitation: "aws_sdk_partnercentral_selling.types.invitation.Invitation"
    """<p> The <code>Invitation</code> object all information necessary to initiate an engagement invitation to a partner. It contains a personalized message from the sender, the invitation's receiver, and a payload. The <code>Payload</code> can be the <code>OpportunityInvitation</code>, which includes detailed structures for sender contacts, partner responsibilities, customer information, and project details, or <code>LeadInvitation</code>, which includes structures for customer information and interaction details. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    import aws_sdk_partnercentral_selling.types.invitation

    out["Invitation"] = (
        aws_sdk_partnercentral_selling.types.invitation.serialize_aws_json_1_0(
            value["invitation"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementInvitationRequest:
    out: CreateEngagementInvitationRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreateEngagementInvitationRequest.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateEngagementInvitationRequest.client_token required"
        )
    if "EngagementIdentifier" in data:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        raise DeserializationError(
            "CreateEngagementInvitationRequest.engagement_identifier required"
        )
    if "Invitation" in data:
        import aws_sdk_partnercentral_selling.types.invitation

        out["invitation"] = (
            aws_sdk_partnercentral_selling.types.invitation.deserialize_aws_json_1_0(
                data["Invitation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEngagementInvitationRequest.invitation required"
        )
    return out
