"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateAnswerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.answer_reason
    import capo_wellarchitected.types.choice_answer_summaries
    import capo_wellarchitected.types.choices
    import capo_wellarchitected.types.is_applicable
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_title
    import capo_wellarchitected.types.question_type
    import capo_wellarchitected.types.review_template_answer_status
    import capo_wellarchitected.types.selected_choices


class ReviewTemplateAnswerSummary(TypedDict, closed=True):
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    question_title: NotRequired[
        "capo_wellarchitected.types.question_title.QuestionTitle"
    ]
    choices: NotRequired["capo_wellarchitected.types.choices.Choices"]
    selected_choices: NotRequired[
        "capo_wellarchitected.types.selected_choices.SelectedChoices"
    ]
    choice_answer_summaries: NotRequired[
        "capo_wellarchitected.types.choice_answer_summaries.ChoiceAnswerSummaries"
    ]
    """<p>A list of selected choices to a question in the review template.</p>"""
    is_applicable: NotRequired["capo_wellarchitected.types.is_applicable.IsApplicable"]
    answer_status: NotRequired[
        "capo_wellarchitected.types.review_template_answer_status.ReviewTemplateAnswerStatus"
    ]
    """<p>The status of whether or not this question has been answered.</p>"""
    reason: NotRequired["capo_wellarchitected.types.answer_reason.AnswerReason"]
    """<p>The reason why a choice is not-applicable to a question in the review template.</p>"""
    question_type: NotRequired["capo_wellarchitected.types.question_type.QuestionType"]
    """<p>The type of question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateAnswerSummary) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "choices" in value:
        import capo_wellarchitected.types.choices

        out["Choices"] = capo_wellarchitected.types.choices.serialize_json(
            value["choices"]
        )
    if "selected_choices" in value:
        import capo_wellarchitected.types.selected_choices

        out["SelectedChoices"] = (
            capo_wellarchitected.types.selected_choices.serialize_json(
                value["selected_choices"]
            )
        )
    if "choice_answer_summaries" in value:
        import capo_wellarchitected.types.choice_answer_summaries

        out["ChoiceAnswerSummaries"] = (
            capo_wellarchitected.types.choice_answer_summaries.serialize_json(
                value["choice_answer_summaries"]
            )
        )
    if "is_applicable" in value:
        out["IsApplicable"] = value["is_applicable"]
    if "answer_status" in value:
        import capo_wellarchitected.types.review_template_answer_status

        out["AnswerStatus"] = (
            capo_wellarchitected.types.review_template_answer_status.serialize_json(
                value["answer_status"]
            )
        )
    if "reason" in value:
        import capo_wellarchitected.types.answer_reason

        out["Reason"] = capo_wellarchitected.types.answer_reason.serialize_json(
            value["reason"]
        )
    if "question_type" in value:
        import capo_wellarchitected.types.question_type

        out["QuestionType"] = capo_wellarchitected.types.question_type.serialize_json(
            value["question_type"]
        )
    return out


def deserialize_json(data: dict) -> ReviewTemplateAnswerSummary:
    out: ReviewTemplateAnswerSummary = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "QuestionTitle" in data:
        out["question_title"] = data["QuestionTitle"]
    if "Choices" in data:
        import capo_wellarchitected.types.choices

        out["choices"] = capo_wellarchitected.types.choices.deserialize_json(
            data["Choices"]
        )
    if "SelectedChoices" in data:
        import capo_wellarchitected.types.selected_choices

        out["selected_choices"] = (
            capo_wellarchitected.types.selected_choices.deserialize_json(
                data["SelectedChoices"]
            )
        )
    if "ChoiceAnswerSummaries" in data:
        import capo_wellarchitected.types.choice_answer_summaries

        out["choice_answer_summaries"] = (
            capo_wellarchitected.types.choice_answer_summaries.deserialize_json(
                data["ChoiceAnswerSummaries"]
            )
        )
    if "IsApplicable" in data:
        out["is_applicable"] = data["IsApplicable"]
    if "AnswerStatus" in data:
        import capo_wellarchitected.types.review_template_answer_status

        out["answer_status"] = (
            capo_wellarchitected.types.review_template_answer_status.deserialize_json(
                data["AnswerStatus"]
            )
        )
    if "Reason" in data:
        import capo_wellarchitected.types.answer_reason

        out["reason"] = capo_wellarchitected.types.answer_reason.deserialize_json(
            data["Reason"]
        )
    if "QuestionType" in data:
        import capo_wellarchitected.types.question_type

        out["question_type"] = (
            capo_wellarchitected.types.question_type.deserialize_json(
                data["QuestionType"]
            )
        )
    return out
