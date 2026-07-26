"""Generated from Smithy shape ``com.amazonaws.mpa#MofNApprovalStrategy``."""

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError


class MofNApprovalStrategy(TypedDict, closed=True):
    min_approvals_required: "int"
    """<p>Minimum number of approvals (M) required for a total number of approvers (N).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MofNApprovalStrategy) -> dict:
    out: dict = {}
    out["MinApprovalsRequired"] = value["min_approvals_required"]
    return out


def deserialize_json(data: dict) -> MofNApprovalStrategy:
    out: MofNApprovalStrategy = {}  # type: ignore[typeddict-item]
    if "MinApprovalsRequired" in data:
        out["min_approvals_required"] = data["MinApprovalsRequired"]
    else:
        raise DeserializationError(
            "MofNApprovalStrategy.min_approvals_required required"
        )
    return out
