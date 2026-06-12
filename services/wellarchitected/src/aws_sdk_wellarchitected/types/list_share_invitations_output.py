"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListShareInvitationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.share_invitation_summaries


class ListShareInvitationsOutput(TypedDict):
    share_invitation_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.share_invitation_summaries.ShareInvitationSummaries"
    ]
    """<p>List of share invitation summaries in a workload.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListShareInvitationsOutput) -> dict:
    out: dict = {}
    if "share_invitation_summaries" in value:
        import aws_sdk_wellarchitected.types.share_invitation_summaries

        out["ShareInvitationSummaries"] = (
            aws_sdk_wellarchitected.types.share_invitation_summaries.serialize_json(
                value["share_invitation_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListShareInvitationsOutput:
    out: ListShareInvitationsOutput = {}  # type: ignore[typeddict-item]
    if "ShareInvitationSummaries" in data:
        import aws_sdk_wellarchitected.types.share_invitation_summaries

        out["share_invitation_summaries"] = (
            aws_sdk_wellarchitected.types.share_invitation_summaries.deserialize_json(
                data["ShareInvitationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
