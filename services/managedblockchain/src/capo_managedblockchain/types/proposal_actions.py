"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ProposalActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.invite_action_list
    import capo_managedblockchain.types.remove_action_list


class ProposalActions(TypedDict, closed=True):
    invitations: NotRequired[
        "capo_managedblockchain.types.invite_action_list.InviteActionList"
    ]
    """<p> The actions to perform for an <code>APPROVED</code> proposal to invite an Amazon Web Services account to create a member and join the network. </p>"""
    removals: NotRequired[
        "capo_managedblockchain.types.remove_action_list.RemoveActionList"
    ]
    """<p> The actions to perform for an <code>APPROVED</code> proposal to remove a member from the network, which deletes the member and all associated member resources from the network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProposalActions) -> dict:
    out: dict = {}
    if "invitations" in value:
        import capo_managedblockchain.types.invite_action_list

        out["Invitations"] = (
            capo_managedblockchain.types.invite_action_list.serialize_json(
                value["invitations"]
            )
        )
    if "removals" in value:
        import capo_managedblockchain.types.remove_action_list

        out["Removals"] = (
            capo_managedblockchain.types.remove_action_list.serialize_json(
                value["removals"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProposalActions:
    out: ProposalActions = {}  # type: ignore[typeddict-item]
    if "Invitations" in data:
        import capo_managedblockchain.types.invite_action_list

        out["invitations"] = (
            capo_managedblockchain.types.invite_action_list.deserialize_json(
                data["Invitations"]
            )
        )
    if "Removals" in data:
        import capo_managedblockchain.types.remove_action_list

        out["removals"] = (
            capo_managedblockchain.types.remove_action_list.deserialize_json(
                data["Removals"]
            )
        )
    return out
