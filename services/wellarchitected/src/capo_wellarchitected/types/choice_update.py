"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_notes
    import capo_wellarchitected.types.choice_reason
    import capo_wellarchitected.types.choice_status


class ChoiceUpdate(TypedDict, closed=True):
    status: NotRequired["capo_wellarchitected.types.choice_status.ChoiceStatus"]
    """<p>The status of a choice.</p>"""
    reason: NotRequired["capo_wellarchitected.types.choice_reason.ChoiceReason"]
    """<p>The reason why a choice is non-applicable to a question in your workload.</p>"""
    notes: NotRequired["capo_wellarchitected.types.choice_notes.ChoiceNotes"]
    """<p>The notes associated with a choice.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceUpdate) -> dict:
    out: dict = {}
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
    if "notes" in value:
        out["Notes"] = value["notes"]
    return out


def deserialize_json(data: dict) -> ChoiceUpdate:
    out: ChoiceUpdate = {}  # type: ignore[typeddict-item]
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
    if "Notes" in data:
        out["notes"] = data["Notes"]
    return out
