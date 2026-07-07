"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementInvitationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_invitation_arn
    import aws_sdk_partnercentral_selling.types.engagement_invitation_identifier


class CreateEngagementInvitationResponse(TypedDict, closed=True):
    id: "aws_sdk_partnercentral_selling.types.engagement_invitation_identifier.EngagementInvitationIdentifier"
    """<p> Unique identifier assigned to the newly created engagement invitation. </p>"""
    arn: "aws_sdk_partnercentral_selling.types.engagement_invitation_arn.EngagementInvitationArn"
    """<p> The Amazon Resource Name (ARN) that uniquely identifies the engagement invitation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementInvitationResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementInvitationResponse:
    out: CreateEngagementInvitationResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateEngagementInvitationResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateEngagementInvitationResponse.arn required")
    return out
