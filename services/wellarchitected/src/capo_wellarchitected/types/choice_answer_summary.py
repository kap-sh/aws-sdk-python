"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceAnswerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.choice_reason
    import capo_wellarchitected.types.choice_status


class ChoiceAnswerSummary(TypedDict, closed=True):
    choice_id: NotRequired["capo_wellarchitected.types.choice_id.ChoiceId"]
    status: NotRequired["capo_wellarchitected.types.choice_status.ChoiceStatus"]
    """<p>The status of a choice.</p>"""
    reason: NotRequired["capo_wellarchitected.types.choice_reason.ChoiceReason"]
    """<p>The reason why a choice is non-applicable to a question in your workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceAnswerSummary) -> dict:
    out: dict = {}
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "status" in value:
        import capo_wellarchitected.types.choice_status

        out["Status"] = capo_wellarchitected.types.choice_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        import capo_wellarchitected.types.choice_reason

        out["Reason"] = capo_wellarchitected.types.choice_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> ChoiceAnswerSummary:
    out: ChoiceAnswerSummary = {}  # type: ignore[typeddict-item]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "Status" in data:
        import capo_wellarchitected.types.choice_status

        out["status"] = capo_wellarchitected.types.choice_status.deserialize_json(
            data["Status"]
        )
    if "Reason" in data:
        import capo_wellarchitected.types.choice_reason

        out["reason"] = capo_wellarchitected.types.choice_reason.deserialize_json(
            data["Reason"]
        )
    return out
