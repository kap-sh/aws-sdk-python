"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Invitation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.invitation_status
    import aws_sdk_managedblockchain.types.network_summary
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.timestamp


class Invitation(TypedDict):
    invitation_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier for the invitation.</p>"""
    creation_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the invitation was created.</p>"""
    expiration_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the invitation expires. This is the <code>CreationDate</code> plus the <code>ProposalDurationInHours</code> that is specified in the <code>ProposalThresholdPolicy</code>. After this date and time, the invitee can no longer create a member and join the network using this <code>InvitationId</code>.</p>"""
    status: NotRequired[
        "aws_sdk_managedblockchain.types.invitation_status.InvitationStatus"
    ]
    """<p>The status of the invitation:</p> <ul> <li> <p> <code>PENDING</code> - The invitee hasn't created a member to join the network, and the invitation hasn't yet expired.</p> </li> <li> <p> <code>ACCEPTING</code> - The invitee has begun creating a member, and creation hasn't yet completed.</p> </li> <li> <p> <code>ACCEPTED</code> - The invitee created a member and joined the network using the <code>InvitationID</code>.</p> </li> <li> <p> <code>REJECTED</code> - The invitee rejected the invitation.</p> </li> <li> <p> <code>EXPIRED</code> - The invitee neither created a member nor rejected the invitation before the <code>ExpirationDate</code>.</p> </li> </ul>"""
    network_summary: NotRequired[
        "aws_sdk_managedblockchain.types.network_summary.NetworkSummary"
    ]
    arn: NotRequired["aws_sdk_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the invitation. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Invitation) -> dict:
    out: dict = {}
    if "invitation_id" in value:
        out["InvitationId"] = value["invitation_id"]
    if "creation_date" in value:
        import aws_sdk_managedblockchain.types.timestamp

        out["CreationDate"] = aws_sdk_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "expiration_date" in value:
        import aws_sdk_managedblockchain.types.timestamp

        out["ExpirationDate"] = (
            aws_sdk_managedblockchain.types.timestamp.serialize_json(
                value["expiration_date"]
            )
        )
    if "status" in value:
        import aws_sdk_managedblockchain.types.invitation_status

        out["Status"] = (
            aws_sdk_managedblockchain.types.invitation_status.serialize_json(
                value["status"]
            )
        )
    if "network_summary" in value:
        import aws_sdk_managedblockchain.types.network_summary

        out["NetworkSummary"] = (
            aws_sdk_managedblockchain.types.network_summary.serialize_json(
                value["network_summary"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> Invitation:
    out: Invitation = {}  # type: ignore[typeddict-item]
    if "InvitationId" in data:
        out["invitation_id"] = data["InvitationId"]
    if "CreationDate" in data:
        import aws_sdk_managedblockchain.types.timestamp

        out["creation_date"] = (
            aws_sdk_managedblockchain.types.timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    if "ExpirationDate" in data:
        import aws_sdk_managedblockchain.types.timestamp

        out["expiration_date"] = (
            aws_sdk_managedblockchain.types.timestamp.deserialize_json(
                data["ExpirationDate"]
            )
        )
    if "Status" in data:
        import aws_sdk_managedblockchain.types.invitation_status

        out["status"] = (
            aws_sdk_managedblockchain.types.invitation_status.deserialize_json(
                data["Status"]
            )
        )
    if "NetworkSummary" in data:
        import aws_sdk_managedblockchain.types.network_summary

        out["network_summary"] = (
            aws_sdk_managedblockchain.types.network_summary.deserialize_json(
                data["NetworkSummary"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
