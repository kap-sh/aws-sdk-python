"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.date_time
    import aws_sdk_ram.types.resource_share_association_list
    import aws_sdk_ram.types.resource_share_invitation_status
    import aws_sdk_ram.types.string


class ResourceShareInvitation(TypedDict):
    resource_share_invitation_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the invitation.</p>"""
    resource_share_name: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The name of the resource share.</p>"""
    resource_share_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the resource share</p>"""
    sender_account_id: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The ID of the Amazon Web Services account that sent the invitation.</p>"""
    receiver_account_id: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The ID of the Amazon Web Services account that received the invitation.</p>"""
    invitation_timestamp: NotRequired["aws_sdk_ram.types.date_time.DateTime"]
    """<p>The date and time when the invitation was sent.</p>"""
    status: NotRequired[
        "aws_sdk_ram.types.resource_share_invitation_status.ResourceShareInvitationStatus"
    ]
    """<p>The current status of the invitation.</p>"""
    resource_share_associations: NotRequired[
        "aws_sdk_ram.types.resource_share_association_list.ResourceShareAssociationList"
    ]
    """<p>To view the resources associated with a pending resource share invitation, use <a>ListPendingInvitationResources</a>.</p>"""
    receiver_arn: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the IAM user or role that received the invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitation) -> dict:
    out: dict = {}
    if "resource_share_invitation_arn" in value:
        out["resourceShareInvitationArn"] = value["resource_share_invitation_arn"]
    if "resource_share_name" in value:
        out["resourceShareName"] = value["resource_share_name"]
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "sender_account_id" in value:
        out["senderAccountId"] = value["sender_account_id"]
    if "receiver_account_id" in value:
        out["receiverAccountId"] = value["receiver_account_id"]
    if "invitation_timestamp" in value:
        import aws_sdk_ram.types.date_time

        out["invitationTimestamp"] = aws_sdk_ram.types.date_time.serialize_json(
            value["invitation_timestamp"]
        )
    if "status" in value:
        import aws_sdk_ram.types.resource_share_invitation_status

        out["status"] = (
            aws_sdk_ram.types.resource_share_invitation_status.serialize_json(
                value["status"]
            )
        )
    if "resource_share_associations" in value:
        import aws_sdk_ram.types.resource_share_association_list

        out["resourceShareAssociations"] = (
            aws_sdk_ram.types.resource_share_association_list.serialize_json(
                value["resource_share_associations"]
            )
        )
    if "receiver_arn" in value:
        out["receiverArn"] = value["receiver_arn"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitation:
    out: ResourceShareInvitation = {}  # type: ignore[typeddict-item]
    if "resourceShareInvitationArn" in data:
        out["resource_share_invitation_arn"] = data["resourceShareInvitationArn"]
    if "resourceShareName" in data:
        out["resource_share_name"] = data["resourceShareName"]
    if "resourceShareArn" in data:
        out["resource_share_arn"] = data["resourceShareArn"]
    if "senderAccountId" in data:
        out["sender_account_id"] = data["senderAccountId"]
    if "receiverAccountId" in data:
        out["receiver_account_id"] = data["receiverAccountId"]
    if "invitationTimestamp" in data:
        import aws_sdk_ram.types.date_time

        out["invitation_timestamp"] = aws_sdk_ram.types.date_time.deserialize_json(
            data["invitationTimestamp"]
        )
    if "status" in data:
        import aws_sdk_ram.types.resource_share_invitation_status

        out["status"] = (
            aws_sdk_ram.types.resource_share_invitation_status.deserialize_json(
                data["status"]
            )
        )
    if "resourceShareAssociations" in data:
        import aws_sdk_ram.types.resource_share_association_list

        out["resource_share_associations"] = (
            aws_sdk_ram.types.resource_share_association_list.deserialize_json(
                data["resourceShareAssociations"]
            )
        )
    if "receiverArn" in data:
        out["receiver_arn"] = data["receiverArn"]
    return out
