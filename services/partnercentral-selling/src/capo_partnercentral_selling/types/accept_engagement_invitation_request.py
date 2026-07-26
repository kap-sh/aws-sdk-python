"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AcceptEngagementInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier


class AcceptEngagementInvitationRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>The <code>CatalogType</code> parameter specifies the catalog associated with the engagement invitation. Accepted values are <code>AWS</code> and <code>Sandbox</code>, which determine the environment in which the engagement invitation is managed.</p>"""
    identifier: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
    """<p> The <code>Identifier</code> parameter in the <code>AcceptEngagementInvitationRequest</code> specifies the unique identifier of the <code>EngagementInvitation</code> to be accepted. Providing the correct identifier ensures that the intended invitation is accepted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptEngagementInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptEngagementInvitationRequest:
    out: AcceptEngagementInvitationRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("AcceptEngagementInvitationRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "AcceptEngagementInvitationRequest.identifier required"
        )
    return out
