"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateProposalInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.client_request_token_string
    import aws_sdk_managedblockchain.types.description_string
    import aws_sdk_managedblockchain.types.input_tag_map
    import aws_sdk_managedblockchain.types.proposal_actions
    import aws_sdk_managedblockchain.types.resource_id_string


class CreateProposalInput(TypedDict):
    client_request_token: "aws_sdk_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>"""
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the network for which the proposal is made.</p>"""
    member_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the member that is creating the proposal. This identifier is especially useful for identifying the member making the proposal when multiple members exist in a single Amazon Web Services account.</p>"""
    actions: "aws_sdk_managedblockchain.types.proposal_actions.ProposalActions"
    """<p>The type of actions proposed, such as inviting a member or removing a member. The types of <code>Actions</code> in a proposal are mutually exclusive. For example, a proposal with <code>Invitations</code> actions cannot also contain <code>Removals</code> actions.</p>"""
    description: NotRequired[
        "aws_sdk_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>A description for the proposal that is visible to voting members, for example, \"Proposal to add Example Corp. as member.\"</p>"""
    tags: NotRequired["aws_sdk_managedblockchain.types.input_tag_map.InputTagMap"]
    """<p>Tags to assign to the proposal.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProposalInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    out["MemberId"] = value["member_id"]
    import aws_sdk_managedblockchain.types.proposal_actions

    out["Actions"] = aws_sdk_managedblockchain.types.proposal_actions.serialize_json(
        value["actions"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_managedblockchain.types.input_tag_map

        out["Tags"] = aws_sdk_managedblockchain.types.input_tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateProposalInput:
    out: CreateProposalInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateProposalInput.client_request_token required")
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    else:
        raise DeserializationError("CreateProposalInput.member_id required")
    if "Actions" in data:
        import aws_sdk_managedblockchain.types.proposal_actions

        out["actions"] = (
            aws_sdk_managedblockchain.types.proposal_actions.deserialize_json(
                data["Actions"]
            )
        )
    else:
        raise DeserializationError("CreateProposalInput.actions required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_managedblockchain.types.input_tag_map

        out["tags"] = aws_sdk_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    return out
