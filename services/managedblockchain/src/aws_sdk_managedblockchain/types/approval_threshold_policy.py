"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ApprovalThresholdPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.proposal_duration_int
    import aws_sdk_managedblockchain.types.threshold_comparator
    import aws_sdk_managedblockchain.types.threshold_percentage_int


class ApprovalThresholdPolicy(TypedDict, closed=True):
    threshold_percentage: NotRequired[
        "aws_sdk_managedblockchain.types.threshold_percentage_int.ThresholdPercentageInt"
    ]
    """<p>The percentage of votes among all members that must be <code>YES</code> for a proposal to be approved. For example, a <code>ThresholdPercentage</code> value of <code>50</code> indicates 50%. The <code>ThresholdComparator</code> determines the precise comparison. If a <code>ThresholdPercentage</code> value of <code>50</code> is specified on a network with 10 members, along with a <code>ThresholdComparator</code> value of <code>GREATER_THAN</code>, this indicates that 6 <code>YES</code> votes are required for the proposal to be approved.</p>"""
    proposal_duration_in_hours: NotRequired[
        "aws_sdk_managedblockchain.types.proposal_duration_int.ProposalDurationInt"
    ]
    """<p>The duration from the time that a proposal is created until it expires. If members cast neither the required number of <code>YES</code> votes to approve the proposal nor the number of <code>NO</code> votes required to reject it before the duration expires, the proposal is <code>EXPIRED</code> and <code>ProposalActions</code> aren't carried out.</p>"""
    threshold_comparator: NotRequired[
        "aws_sdk_managedblockchain.types.threshold_comparator.ThresholdComparator"
    ]
    """<p>Determines whether the vote percentage must be greater than the <code>ThresholdPercentage</code> or must be greater than or equal to the <code>ThresholdPercentage</code> to be approved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalThresholdPolicy) -> dict:
    out: dict = {}
    if "threshold_percentage" in value:
        out["ThresholdPercentage"] = value["threshold_percentage"]
    if "proposal_duration_in_hours" in value:
        out["ProposalDurationInHours"] = value["proposal_duration_in_hours"]
    if "threshold_comparator" in value:
        import aws_sdk_managedblockchain.types.threshold_comparator

        out["ThresholdComparator"] = (
            aws_sdk_managedblockchain.types.threshold_comparator.serialize_json(
                value["threshold_comparator"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApprovalThresholdPolicy:
    out: ApprovalThresholdPolicy = {}  # type: ignore[typeddict-item]
    if "ThresholdPercentage" in data:
        out["threshold_percentage"] = data["ThresholdPercentage"]
    if "ProposalDurationInHours" in data:
        out["proposal_duration_in_hours"] = data["ProposalDurationInHours"]
    if "ThresholdComparator" in data:
        import aws_sdk_managedblockchain.types.threshold_comparator

        out["threshold_comparator"] = (
            aws_sdk_managedblockchain.types.threshold_comparator.deserialize_json(
                data["ThresholdComparator"]
            )
        )
    return out
