"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementInvitationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type
    import aws_sdk_partnercentral_selling.types.engagement_title
    import aws_sdk_partnercentral_selling.types.invitation_status
    import aws_sdk_partnercentral_selling.types.participant_type
    import aws_sdk_partnercentral_selling.types.receiver


class EngagementInvitationSummary(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Engagement Invitation. The ARN is a unique identifier that allows partners to reference the invitation in their system and manage its lifecycle.</p>"""
    payload_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type.EngagementInvitationPayloadType"
    ]
    """<p>Describes the type of payload associated with the Engagement Invitation, such as <code>Opportunity</code> or <code>MarketplaceOffer</code>. This helps partners understand the nature of the engagement request from AWS.</p>"""
    id: "aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
    """<p>Represents the unique identifier of the Engagement Invitation. This identifier is used to track the invitation and to manage responses like acceptance or rejection.</p>"""
    engagement_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p> The identifier of the Engagement associated with this invitation. This links the invitation to its parent Engagement. </p>"""
    engagement_title: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>Provides a short title or description of the Engagement Invitation. This title helps partners quickly identify and differentiate between multiple engagement opportunities.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_selling.types.invitation_status.InvitationStatus"
    ]
    """<p>Represents the current status of the Engagement Invitation, such as <code>Pending</code>, <code>Accepted</code>, or <code>Rejected</code>. The status helps track the progress and response to the invitation.</p>"""
    invitation_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Indicates the date when the Engagement Invitation was sent to the partner. This provides context for when the opportunity was shared and helps in tracking the timeline for engagement.</p>"""
    expiration_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Indicates the date and time when the Engagement Invitation will expire. After this date, the invitation can no longer be accepted, and the opportunity will be unavailable to the partner.</p>"""
    sender_aws_account_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>Specifies the AWS account ID of the sender who initiated the Engagement Invitation. This allows the partner to identify the AWS entity or representative responsible for sharing the opportunity.</p>"""
    sender_company_name: NotRequired["str"]
    """<p>Indicates the name of the company or AWS division that sent the Engagement Invitation. This information is useful for partners to know which part of AWS is requesting engagement.</p>"""
    receiver: NotRequired["aws_sdk_partnercentral_selling.types.receiver.Receiver"]
    """<p>Specifies the partner company or individual that received the Engagement Invitation. This field is important for tracking who the invitation was sent to within the partner organization.</p>"""
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the Engagement Invitation resides. This can be either the <code>AWS</code> or <code>Sandbox</code> catalog, indicating whether the opportunity is live or being tested.</p>"""
    participant_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.participant_type.ParticipantType"
    ]
    """<p>Identifies the role of the caller in the engagement invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementInvitationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "payload_type" in value:
        import aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type

        out["PayloadType"] = (
            aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type.serialize_aws_json_1_0(
                value["payload_type"]
            )
        )
    out["Id"] = value["id"]
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "engagement_title" in value:
        out["EngagementTitle"] = value["engagement_title"]
    if "status" in value:
        import aws_sdk_partnercentral_selling.types.invitation_status

        out["Status"] = (
            aws_sdk_partnercentral_selling.types.invitation_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "invitation_date" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["InvitationDate"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["invitation_date"]
            )
        )
    if "expiration_date" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["ExpirationDate"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["expiration_date"]
            )
        )
    if "sender_aws_account_id" in value:
        out["SenderAwsAccountId"] = value["sender_aws_account_id"]
    if "sender_company_name" in value:
        out["SenderCompanyName"] = value["sender_company_name"]
    if "receiver" in value:
        import aws_sdk_partnercentral_selling.types.receiver

        out["Receiver"] = (
            aws_sdk_partnercentral_selling.types.receiver.serialize_aws_json_1_0(
                value["receiver"]
            )
        )
    out["Catalog"] = value["catalog"]
    if "participant_type" in value:
        import aws_sdk_partnercentral_selling.types.participant_type

        out["ParticipantType"] = (
            aws_sdk_partnercentral_selling.types.participant_type.serialize_aws_json_1_0(
                value["participant_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementInvitationSummary:
    out: EngagementInvitationSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "PayloadType" in data:
        import aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type

        out["payload_type"] = (
            aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type.deserialize_aws_json_1_0(
                data["PayloadType"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("EngagementInvitationSummary.id required")
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    if "EngagementTitle" in data:
        out["engagement_title"] = data["EngagementTitle"]
    if "Status" in data:
        import aws_sdk_partnercentral_selling.types.invitation_status

        out["status"] = (
            aws_sdk_partnercentral_selling.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "InvitationDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["invitation_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["InvitationDate"]
            )
        )
    if "ExpirationDate" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["expiration_date"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["ExpirationDate"]
            )
        )
    if "SenderAwsAccountId" in data:
        out["sender_aws_account_id"] = data["SenderAwsAccountId"]
    if "SenderCompanyName" in data:
        out["sender_company_name"] = data["SenderCompanyName"]
    if "Receiver" in data:
        import aws_sdk_partnercentral_selling.types.receiver

        out["receiver"] = (
            aws_sdk_partnercentral_selling.types.receiver.deserialize_aws_json_1_0(
                data["Receiver"]
            )
        )
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("EngagementInvitationSummary.catalog required")
    if "ParticipantType" in data:
        import aws_sdk_partnercentral_selling.types.participant_type

        out["participant_type"] = (
            aws_sdk_partnercentral_selling.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    return out
