"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AnswerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.answer_reason
    import capo_wellarchitected.types.choice_answer_summaries
    import capo_wellarchitected.types.choices
    import capo_wellarchitected.types.is_applicable
    import capo_wellarchitected.types.jira_configuration
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_title
    import capo_wellarchitected.types.question_type
    import capo_wellarchitected.types.risk
    import capo_wellarchitected.types.selected_choices


class AnswerSummary(TypedDict, closed=True):
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
    """<p>A list of selected choices to a question in your workload.</p>"""
    is_applicable: NotRequired["capo_wellarchitected.types.is_applicable.IsApplicable"]
    risk: NotRequired["capo_wellarchitected.types.risk.Risk"]
    reason: NotRequired["capo_wellarchitected.types.answer_reason.AnswerReason"]
    """<p>The reason why a choice is non-applicable to a question in your workload.</p>"""
    question_type: NotRequired["capo_wellarchitected.types.question_type.QuestionType"]
    """<p>The type of the question.</p>"""
    jira_configuration: NotRequired[
        "capo_wellarchitected.types.jira_configuration.JiraConfiguration"
    ]
    """<p>Configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnswerSummary) -> dict:
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
    if "risk" in value:
        import capo_wellarchitected.types.risk

        out["Risk"] = capo_wellarchitected.types.risk.serialize_json(value["risk"])
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
    if "jira_configuration" in value:
        import capo_wellarchitected.types.jira_configuration

        out["JiraConfiguration"] = (
            capo_wellarchitected.types.jira_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnswerSummary:
    out: AnswerSummary = {}  # type: ignore[typeddict-item]
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
    if "Risk" in data:
        import capo_wellarchitected.types.risk

        out["risk"] = capo_wellarchitected.types.risk.deserialize_json(data["Risk"])
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
    if "JiraConfiguration" in data:
        import capo_wellarchitected.types.jira_configuration

        out["jira_configuration"] = (
            capo_wellarchitected.types.jira_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
