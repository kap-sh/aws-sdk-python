"""Generated from Smithy shape ``com.amazonaws.managedblockchain#VotingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.approval_threshold_policy


class VotingPolicy(TypedDict, closed=True):
    approval_threshold_policy: NotRequired[
        "capo_managedblockchain.types.approval_threshold_policy.ApprovalThresholdPolicy"
    ]
    """<p>Defines the rules for the network for voting on proposals, such as the percentage of <code>YES</code> votes required for the proposal to be approved and the duration of the proposal. The policy applies to all proposals and is specified when the network is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VotingPolicy) -> dict:
    out: dict = {}
    if "approval_threshold_policy" in value:
        import capo_managedblockchain.types.approval_threshold_policy

        out["ApprovalThresholdPolicy"] = (
            capo_managedblockchain.types.approval_threshold_policy.serialize_json(
                value["approval_threshold_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> VotingPolicy:
    out: VotingPolicy = {}  # type: ignore[typeddict-item]
    if "ApprovalThresholdPolicy" in data:
        import capo_managedblockchain.types.approval_threshold_policy

        out["approval_threshold_policy"] = (
            capo_managedblockchain.types.approval_threshold_policy.deserialize_json(
                data["ApprovalThresholdPolicy"]
            )
        )
    return out
