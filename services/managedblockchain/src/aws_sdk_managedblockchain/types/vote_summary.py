"""Generated from Smithy shape ``com.amazonaws.managedblockchain#VoteSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.network_member_name_string
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.vote_value


class VoteSummary(TypedDict, closed=True):
    vote: NotRequired["aws_sdk_managedblockchain.types.vote_value.VoteValue"]
    """<p> The vote value, either <code>YES</code> or <code>NO</code>. </p>"""
    member_name: NotRequired[
        "aws_sdk_managedblockchain.types.network_member_name_string.NetworkMemberNameString"
    ]
    """<p> The name of the member that cast the vote. </p>"""
    member_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p> The unique identifier of the member that cast the vote. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoteSummary) -> dict:
    out: dict = {}
    if "vote" in value:
        import aws_sdk_managedblockchain.types.vote_value

        out["Vote"] = aws_sdk_managedblockchain.types.vote_value.serialize_json(
            value["vote"]
        )
    if "member_name" in value:
        out["MemberName"] = value["member_name"]
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    return out


def deserialize_json(data: dict) -> VoteSummary:
    out: VoteSummary = {}  # type: ignore[typeddict-item]
    if "Vote" in data:
        import aws_sdk_managedblockchain.types.vote_value

        out["vote"] = aws_sdk_managedblockchain.types.vote_value.deserialize_json(
            data["Vote"]
        )
    if "MemberName" in data:
        out["member_name"] = data["MemberName"]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    return out
