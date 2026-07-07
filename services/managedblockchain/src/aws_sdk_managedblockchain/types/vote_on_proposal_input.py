"""Generated from Smithy shape ``com.amazonaws.managedblockchain#VoteOnProposalInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.vote_value


class VoteOnProposalInput(TypedDict, closed=True):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the network. </p>"""
    proposal_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p> The unique identifier of the proposal. </p>"""
    voter_member_id: (
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    )
    """<p>The unique identifier of the member casting the vote. </p>"""
    vote: "aws_sdk_managedblockchain.types.vote_value.VoteValue"
    """<p> The value of the vote. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoteOnProposalInput) -> dict:
    out: dict = {}
    out["VoterMemberId"] = value["voter_member_id"]
    import aws_sdk_managedblockchain.types.vote_value

    out["Vote"] = aws_sdk_managedblockchain.types.vote_value.serialize_json(
        value["vote"]
    )
    return out


def deserialize_json(data: dict) -> VoteOnProposalInput:
    out: VoteOnProposalInput = {}  # type: ignore[typeddict-item]
    if "VoterMemberId" in data:
        out["voter_member_id"] = data["VoterMemberId"]
    else:
        raise DeserializationError("VoteOnProposalInput.voter_member_id required")
    if "Vote" in data:
        import aws_sdk_managedblockchain.types.vote_value

        out["vote"] = aws_sdk_managedblockchain.types.vote_value.deserialize_json(
            data["Vote"]
        )
    else:
        raise DeserializationError("VoteOnProposalInput.vote required")
    return out
