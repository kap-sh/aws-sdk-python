"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateShareInvitationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.share_invitation_action
    import aws_sdk_wellarchitected.types.share_invitation_id


class UpdateShareInvitationInput(TypedDict, closed=True):
    share_invitation_id: (
        "aws_sdk_wellarchitected.types.share_invitation_id.ShareInvitationId"
    )
    """<p>The ID assigned to the share invitation.</p>"""
    share_invitation_action: NotRequired[
        "aws_sdk_wellarchitected.types.share_invitation_action.ShareInvitationAction"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateShareInvitationInput) -> dict:
    out: dict = {}
    if "share_invitation_action" in value:
        import aws_sdk_wellarchitected.types.share_invitation_action

        out["ShareInvitationAction"] = (
            aws_sdk_wellarchitected.types.share_invitation_action.serialize_json(
                value["share_invitation_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateShareInvitationInput:
    out: UpdateShareInvitationInput = {}  # type: ignore[typeddict-item]
    if "ShareInvitationAction" in data:
        import aws_sdk_wellarchitected.types.share_invitation_action

        out["share_invitation_action"] = (
            aws_sdk_wellarchitected.types.share_invitation_action.deserialize_json(
                data["ShareInvitationAction"]
            )
        )
    return out
