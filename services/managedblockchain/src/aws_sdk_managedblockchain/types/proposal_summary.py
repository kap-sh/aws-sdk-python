"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.description_string
    import aws_sdk_managedblockchain.types.network_member_name_string
    import aws_sdk_managedblockchain.types.proposal_status
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.timestamp


class ProposalSummary(TypedDict):
    proposal_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p> The unique identifier of the proposal. </p>"""
    description: NotRequired[
        "aws_sdk_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p> The description of the proposal. </p>"""
    proposed_by_member_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p> The unique identifier of the member that created the proposal. </p>"""
    proposed_by_member_name: NotRequired[
        "aws_sdk_managedblockchain.types.network_member_name_string.NetworkMemberNameString"
    ]
    """<p> The name of the member that created the proposal. </p>"""
    status: NotRequired[
        "aws_sdk_managedblockchain.types.proposal_status.ProposalStatus"
    ]
    """<p>The status of the proposal. Values are as follows:</p> <ul> <li> <p> <code>IN_PROGRESS</code> - The proposal is active and open for member voting.</p> </li> <li> <p> <code>APPROVED</code> - The proposal was approved with sufficient <code>YES</code> votes among members according to the <code>VotingPolicy</code> specified for the <code>Network</code>. The specified proposal actions are carried out.</p> </li> <li> <p> <code>REJECTED</code> - The proposal was rejected with insufficient <code>YES</code> votes among members according to the <code>VotingPolicy</code> specified for the <code>Network</code>. The specified <code>ProposalActions</code> aren't carried out.</p> </li> <li> <p> <code>EXPIRED</code> - Members didn't cast the number of votes required to determine the proposal outcome before the proposal expired. The specified <code>ProposalActions</code> aren't carried out.</p> </li> <li> <p> <code>ACTION_FAILED</code> - One or more of the specified <code>ProposalActions</code> in a proposal that was approved couldn't be completed because of an error.</p> </li> </ul>"""
    creation_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p> The date and time that the proposal was created. </p>"""
    expiration_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p> The date and time that the proposal expires. This is the <code>CreationDate</code> plus the <code>ProposalDurationInHours</code> that is specified in the <code>ProposalThresholdPolicy</code>. After this date and time, if members haven't cast enough votes to determine the outcome according to the voting policy, the proposal is <code>EXPIRED</code> and <code>Actions</code> aren't carried out. </p>"""
    arn: NotRequired["aws_sdk_managedblockchain.types.arn_string.ArnString"]
    r"""<p>The Amazon Resource Name (ARN) of the proposal. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProposalSummary) -> dict:
    out: dict = {}
    if "proposal_id" in value:
        out["ProposalId"] = value["proposal_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "proposed_by_member_id" in value:
        out["ProposedByMemberId"] = value["proposed_by_member_id"]
    if "proposed_by_member_name" in value:
        out["ProposedByMemberName"] = value["proposed_by_member_name"]
    if "status" in value:
        import aws_sdk_managedblockchain.types.proposal_status

        out["Status"] = aws_sdk_managedblockchain.types.proposal_status.serialize_json(
            value["status"]
        )
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
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ProposalSummary:
    out: ProposalSummary = {}  # type: ignore[typeddict-item]
    if "ProposalId" in data:
        out["proposal_id"] = data["ProposalId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ProposedByMemberId" in data:
        out["proposed_by_member_id"] = data["ProposedByMemberId"]
    if "ProposedByMemberName" in data:
        out["proposed_by_member_name"] = data["ProposedByMemberName"]
    if "Status" in data:
        import aws_sdk_managedblockchain.types.proposal_status

        out["status"] = (
            aws_sdk_managedblockchain.types.proposal_status.deserialize_json(
                data["Status"]
            )
        )
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
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
