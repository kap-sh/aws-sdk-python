"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AnswerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.answer_reason
    import aws_sdk_wellarchitected.types.choice_answer_summaries
    import aws_sdk_wellarchitected.types.choices
    import aws_sdk_wellarchitected.types.is_applicable
    import aws_sdk_wellarchitected.types.jira_configuration
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.question_title
    import aws_sdk_wellarchitected.types.question_type
    import aws_sdk_wellarchitected.types.risk
    import aws_sdk_wellarchitected.types.selected_choices


class AnswerSummary(TypedDict, closed=True):
    question_id: NotRequired["aws_sdk_wellarchitected.types.question_id.QuestionId"]
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    question_title: NotRequired[
        "aws_sdk_wellarchitected.types.question_title.QuestionTitle"
    ]
    choices: NotRequired["aws_sdk_wellarchitected.types.choices.Choices"]
    selected_choices: NotRequired[
        "aws_sdk_wellarchitected.types.selected_choices.SelectedChoices"
    ]
    choice_answer_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.choice_answer_summaries.ChoiceAnswerSummaries"
    ]
    """<p>A list of selected choices to a question in your workload.</p>"""
    is_applicable: NotRequired[
        "aws_sdk_wellarchitected.types.is_applicable.IsApplicable"
    ]
    risk: NotRequired["aws_sdk_wellarchitected.types.risk.Risk"]
    reason: NotRequired["aws_sdk_wellarchitected.types.answer_reason.AnswerReason"]
    """<p>The reason why a choice is non-applicable to a question in your workload.</p>"""
    question_type: NotRequired[
        "aws_sdk_wellarchitected.types.question_type.QuestionType"
    ]
    """<p>The type of the question.</p>"""
    jira_configuration: NotRequired[
        "aws_sdk_wellarchitected.types.jira_configuration.JiraConfiguration"
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
        import aws_sdk_wellarchitected.types.choices

        out["Choices"] = aws_sdk_wellarchitected.types.choices.serialize_json(
            value["choices"]
        )
    if "selected_choices" in value:
        import aws_sdk_wellarchitected.types.selected_choices

        out["SelectedChoices"] = (
            aws_sdk_wellarchitected.types.selected_choices.serialize_json(
                value["selected_choices"]
            )
        )
    if "choice_answer_summaries" in value:
        import aws_sdk_wellarchitected.types.choice_answer_summaries

        out["ChoiceAnswerSummaries"] = (
            aws_sdk_wellarchitected.types.choice_answer_summaries.serialize_json(
                value["choice_answer_summaries"]
            )
        )
    if "is_applicable" in value:
        out["IsApplicable"] = value["is_applicable"]
    if "risk" in value:
        import aws_sdk_wellarchitected.types.risk

        out["Risk"] = aws_sdk_wellarchitected.types.risk.serialize_json(value["risk"])
    if "reason" in value:
        import aws_sdk_wellarchitected.types.answer_reason

        out["Reason"] = aws_sdk_wellarchitected.types.answer_reason.serialize_json(
            value["reason"]
        )
    if "question_type" in value:
        import aws_sdk_wellarchitected.types.question_type

        out["QuestionType"] = (
            aws_sdk_wellarchitected.types.question_type.serialize_json(
                value["question_type"]
            )
        )
    if "jira_configuration" in value:
        import aws_sdk_wellarchitected.types.jira_configuration

        out["JiraConfiguration"] = (
            aws_sdk_wellarchitected.types.jira_configuration.serialize_json(
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
        import aws_sdk_wellarchitected.types.choices

        out["choices"] = aws_sdk_wellarchitected.types.choices.deserialize_json(
            data["Choices"]
        )
    if "SelectedChoices" in data:
        import aws_sdk_wellarchitected.types.selected_choices

        out["selected_choices"] = (
            aws_sdk_wellarchitected.types.selected_choices.deserialize_json(
                data["SelectedChoices"]
            )
        )
    if "ChoiceAnswerSummaries" in data:
        import aws_sdk_wellarchitected.types.choice_answer_summaries

        out["choice_answer_summaries"] = (
            aws_sdk_wellarchitected.types.choice_answer_summaries.deserialize_json(
                data["ChoiceAnswerSummaries"]
            )
        )
    if "IsApplicable" in data:
        out["is_applicable"] = data["IsApplicable"]
    if "Risk" in data:
        import aws_sdk_wellarchitected.types.risk

        out["risk"] = aws_sdk_wellarchitected.types.risk.deserialize_json(data["Risk"])
    if "Reason" in data:
        import aws_sdk_wellarchitected.types.answer_reason

        out["reason"] = aws_sdk_wellarchitected.types.answer_reason.deserialize_json(
            data["Reason"]
        )
    if "QuestionType" in data:
        import aws_sdk_wellarchitected.types.question_type

        out["question_type"] = (
            aws_sdk_wellarchitected.types.question_type.deserialize_json(
                data["QuestionType"]
            )
        )
    if "JiraConfiguration" in data:
        import aws_sdk_wellarchitected.types.jira_configuration

        out["jira_configuration"] = (
            aws_sdk_wellarchitected.types.jira_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
