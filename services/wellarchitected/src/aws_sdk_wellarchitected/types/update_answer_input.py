"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAnswerInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.answer_reason
    import aws_sdk_wellarchitected.types.choice_updates
    import aws_sdk_wellarchitected.types.is_applicable
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.selected_choices
    import aws_sdk_wellarchitected.types.workload_id


class UpdateAnswerInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    question_id: "aws_sdk_wellarchitected.types.question_id.QuestionId"
    selected_choices: NotRequired[
        "aws_sdk_wellarchitected.types.selected_choices.SelectedChoices"
    ]
    choice_updates: NotRequired[
        "aws_sdk_wellarchitected.types.choice_updates.ChoiceUpdates"
    ]
    """<p>A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated.</p>"""
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    is_applicable: NotRequired[
        "aws_sdk_wellarchitected.types.is_applicable.IsApplicable"
    ]
    reason: NotRequired["aws_sdk_wellarchitected.types.answer_reason.AnswerReason"]
    """<p>The reason why a question is not applicable to your workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnswerInput) -> dict:
    out: dict = {}
    if "selected_choices" in value:
        import aws_sdk_wellarchitected.types.selected_choices

        out["SelectedChoices"] = (
            aws_sdk_wellarchitected.types.selected_choices.serialize_json(
                value["selected_choices"]
            )
        )
    if "choice_updates" in value:
        import aws_sdk_wellarchitected.types.choice_updates

        out["ChoiceUpdates"] = (
            aws_sdk_wellarchitected.types.choice_updates.serialize_json(
                value["choice_updates"]
            )
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "is_applicable" in value:
        out["IsApplicable"] = value["is_applicable"]
    if "reason" in value:
        import aws_sdk_wellarchitected.types.answer_reason

        out["Reason"] = aws_sdk_wellarchitected.types.answer_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAnswerInput:
    out: UpdateAnswerInput = {}  # type: ignore[typeddict-item]
    if "SelectedChoices" in data:
        import aws_sdk_wellarchitected.types.selected_choices

        out["selected_choices"] = (
            aws_sdk_wellarchitected.types.selected_choices.deserialize_json(
                data["SelectedChoices"]
            )
        )
    if "ChoiceUpdates" in data:
        import aws_sdk_wellarchitected.types.choice_updates

        out["choice_updates"] = (
            aws_sdk_wellarchitected.types.choice_updates.deserialize_json(
                data["ChoiceUpdates"]
            )
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "IsApplicable" in data:
        out["is_applicable"] = data["IsApplicable"]
    if "Reason" in data:
        import aws_sdk_wellarchitected.types.answer_reason

        out["reason"] = aws_sdk_wellarchitected.types.answer_reason.deserialize_json(
            data["Reason"]
        )
    return out
