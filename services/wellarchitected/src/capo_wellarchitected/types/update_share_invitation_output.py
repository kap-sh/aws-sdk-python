"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateShareInvitationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.share_invitation


class UpdateShareInvitationOutput(TypedDict, closed=True):
    share_invitation: NotRequired[
        "capo_wellarchitected.types.share_invitation.ShareInvitation"
    ]
    """<p>The updated workload or custom lens share invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateShareInvitationOutput) -> dict:
    out: dict = {}
    if "share_invitation" in value:
        import capo_wellarchitected.types.share_invitation

        out["ShareInvitation"] = (
            capo_wellarchitected.types.share_invitation.serialize_json(
                value["share_invitation"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateShareInvitationOutput:
    out: UpdateShareInvitationOutput = {}  # type: ignore[typeddict-item]
    if "ShareInvitation" in data:
        import capo_wellarchitected.types.share_invitation

        out["share_invitation"] = (
            capo_wellarchitected.types.share_invitation.deserialize_json(
                data["ShareInvitation"]
            )
        )
    return out
