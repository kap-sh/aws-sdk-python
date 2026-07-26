"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareInvitationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.share_invitation_summary

ShareInvitationSummaries: TypeAlias = list[
    "capo_wellarchitected.types.share_invitation_summary.ShareInvitationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareInvitationSummaries) -> list:
    import capo_wellarchitected.types.share_invitation_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.share_invitation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ShareInvitationSummaries:
    import capo_wellarchitected.types.share_invitation_summary

    out: ShareInvitationSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.share_invitation_summary.deserialize_json(item)
        )
    return out
