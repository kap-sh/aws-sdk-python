"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetEngagementInvitationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_description
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type
    import aws_sdk_partnercentral_selling.types.engagement_member_summaries
    import aws_sdk_partnercentral_selling.types.engagement_title
    import aws_sdk_partnercentral_selling.types.invitation_message
    import aws_sdk_partnercentral_selling.types.invitation_status
    import aws_sdk_partnercentral_selling.types.payload
    import aws_sdk_partnercentral_selling.types.receiver
    import aws_sdk_partnercentral_selling.types.rejection_reason_string


class GetEngagementInvitationResponse(TypedDict):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) that identifies the engagement invitation.</p>"""
    payload_type: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_invitation_payload_type.EngagementInvitationPayloadType"
    ]
    """<p>The type of payload contained in the engagement invitation, indicating what data or context the payload covers.</p>"""
    id: "aws_sdk_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
    """<p>Unique identifier assigned to the engagement invitation being retrieved.</p>"""
    engagement_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The identifier of the engagement associated with this invitation.This ID links the invitation to its corresponding engagement.</p>"""
    engagement_title: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>The title of the engagement invitation, summarizing the purpose or objectives of the opportunity shared by AWS.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_selling.types.invitation_status.InvitationStatus"
    ]
    """<p>The current status of the engagement invitation.</p>"""
    invitation_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>The date when the engagement invitation was sent to the partner.</p>"""
    expiration_date: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>Indicates the date on which the engagement invitation will expire if not accepted by the partner.</p>"""
    sender_aws_account_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>Specifies the AWS Account ID of the sender, which identifies the AWS team responsible for sharing the engagement invitation.</p>"""
    sender_company_name: NotRequired["str"]
    """<p>The name of the AWS organization or team that sent the engagement invitation.</p>"""
    receiver: NotRequired["aws_sdk_partnercentral_selling.types.receiver.Receiver"]
    """<p>Information about the partner organization or team that received the engagement invitation, including contact details and identifiers.</p>"""
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Indicates the catalog from which the engagement invitation details are retrieved. This field helps in identifying the appropriate catalog (e.g., <code>AWS</code> or <code>Sandbox</code>) used in the request.</p>"""
    rejection_reason: NotRequired[
        "aws_sdk_partnercentral_selling.types.rejection_reason_string.RejectionReasonString"
    ]
    """<p>If the engagement invitation was rejected, this field specifies the reason provided by the partner for the rejection.</p>"""
    payload: NotRequired["aws_sdk_partnercentral_selling.types.payload.Payload"]
    """<p>Details of the engagement invitation payload, including specific data relevant to the invitation's contents, such as customer information and opportunity insights.</p>"""
    invitation_message: NotRequired[
        "aws_sdk_partnercentral_selling.types.invitation_message.InvitationMessage"
    ]
    """<p>The message sent to the invited partner when the invitation was created.</p>"""
    engagement_description: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_description.EngagementDescription"
    ]
    """<p>The description of the engagement associated with this invitation.</p>"""
    existing_members: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_member_summaries.EngagementMemberSummaries"
    ]
    """<p>A list of active members currently part of the Engagement. This array contains a maximum of 10 members, each represented by an object with the following properties.</p> <ul> <li> <p>CompanyName: The name of the member's company.</p> </li> <li> <p>WebsiteUrl: The website URL of the member's company.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEngagementInvitationResponse) -> dict:
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
    if "rejection_reason" in value:
        out["RejectionReason"] = value["rejection_reason"]
    if "payload" in value:
        import aws_sdk_partnercentral_selling.types.payload

        out["Payload"] = (
            aws_sdk_partnercentral_selling.types.payload.serialize_aws_json_1_0(
                value["payload"]
            )
        )
    if "invitation_message" in value:
        out["InvitationMessage"] = value["invitation_message"]
    if "engagement_description" in value:
        out["EngagementDescription"] = value["engagement_description"]
    if "existing_members" in value:
        import aws_sdk_partnercentral_selling.types.engagement_member_summaries

        out["ExistingMembers"] = (
            aws_sdk_partnercentral_selling.types.engagement_member_summaries.serialize_aws_json_1_0(
                value["existing_members"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEngagementInvitationResponse:
    out: GetEngagementInvitationResponse = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("GetEngagementInvitationResponse.id required")
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
        raise DeserializationError("GetEngagementInvitationResponse.catalog required")
    if "RejectionReason" in data:
        out["rejection_reason"] = data["RejectionReason"]
    if "Payload" in data:
        import aws_sdk_partnercentral_selling.types.payload

        out["payload"] = (
            aws_sdk_partnercentral_selling.types.payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    if "InvitationMessage" in data:
        out["invitation_message"] = data["InvitationMessage"]
    if "EngagementDescription" in data:
        out["engagement_description"] = data["EngagementDescription"]
    if "ExistingMembers" in data:
        import aws_sdk_partnercentral_selling.types.engagement_member_summaries

        out["existing_members"] = (
            aws_sdk_partnercentral_selling.types.engagement_member_summaries.deserialize_aws_json_1_0(
                data["ExistingMembers"]
            )
        )
    return out
