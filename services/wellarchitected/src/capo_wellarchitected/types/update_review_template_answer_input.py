"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateReviewTemplateAnswerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.answer_reason
    import capo_wellarchitected.types.choice_updates
    import capo_wellarchitected.types.is_applicable
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.selected_choices
    import capo_wellarchitected.types.template_arn


class UpdateReviewTemplateAnswerInput(TypedDict, closed=True):
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    question_id: "capo_wellarchitected.types.question_id.QuestionId"
    selected_choices: NotRequired[
        "capo_wellarchitected.types.selected_choices.SelectedChoices"
    ]
    choice_updates: NotRequired[
        "capo_wellarchitected.types.choice_updates.ChoiceUpdates"
    ]
    """<p>A list of choices to be updated.</p>"""
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    is_applicable: NotRequired["capo_wellarchitected.types.is_applicable.IsApplicable"]
    reason: NotRequired["capo_wellarchitected.types.answer_reason.AnswerReason"]
    """<p>The update reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReviewTemplateAnswerInput) -> dict:
    out: dict = {}
    if "selected_choices" in value:
        import capo_wellarchitected.types.selected_choices

        out["SelectedChoices"] = (
            capo_wellarchitected.types.selected_choices.serialize_json(
                value["selected_choices"]
            )
        )
    if "choice_updates" in value:
        import capo_wellarchitected.types.choice_updates

        out["ChoiceUpdates"] = capo_wellarchitected.types.choice_updates.serialize_json(
            value["choice_updates"]
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "is_applicable" in value:
        out["IsApplicable"] = value["is_applicable"]
    if "reason" in value:
        import capo_wellarchitected.types.answer_reason

        out["Reason"] = capo_wellarchitected.types.answer_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReviewTemplateAnswerInput:
    out: UpdateReviewTemplateAnswerInput = {}  # type: ignore[typeddict-item]
    if "SelectedChoices" in data:
        import capo_wellarchitected.types.selected_choices

        out["selected_choices"] = (
            capo_wellarchitected.types.selected_choices.deserialize_json(
                data["SelectedChoices"]
            )
        )
    if "ChoiceUpdates" in data:
        import capo_wellarchitected.types.choice_updates

        out["choice_updates"] = (
            capo_wellarchitected.types.choice_updates.deserialize_json(
                data["ChoiceUpdates"]
            )
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "IsApplicable" in data:
        out["is_applicable"] = data["IsApplicable"]
    if "Reason" in data:
        import capo_wellarchitected.types.answer_reason

        out["reason"] = capo_wellarchitected.types.answer_reason.deserialize_json(
            data["Reason"]
        )
    return out
