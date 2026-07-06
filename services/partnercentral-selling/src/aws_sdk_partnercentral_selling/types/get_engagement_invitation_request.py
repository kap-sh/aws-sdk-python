"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetEngagementInvitationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier


class GetEngagementInvitationRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. The field accepts values from the predefined set: <code>AWS</code> for live operations or <code>Sandbox</code> for testing environments.</p>"""
    identifier: "aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
    """<p>Specifies the unique identifier for the retrieved engagement invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEngagementInvitationRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEngagementInvitationRequest:
    out: GetEngagementInvitationRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetEngagementInvitationRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetEngagementInvitationRequest.identifier required")
    return out
