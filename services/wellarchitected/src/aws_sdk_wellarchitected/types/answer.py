"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Answer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.answer_reason
    import aws_sdk_wellarchitected.types.choice_answers
    import aws_sdk_wellarchitected.types.choices
    import aws_sdk_wellarchitected.types.display_text
    import aws_sdk_wellarchitected.types.helpful_resource_url
    import aws_sdk_wellarchitected.types.improvement_plan_url
    import aws_sdk_wellarchitected.types.is_applicable
    import aws_sdk_wellarchitected.types.jira_configuration
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.question_description
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.question_title
    import aws_sdk_wellarchitected.types.risk
    import aws_sdk_wellarchitected.types.selected_choices


class Answer(TypedDict):
    question_id: NotRequired["aws_sdk_wellarchitected.types.question_id.QuestionId"]
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    question_title: NotRequired[
        "aws_sdk_wellarchitected.types.question_title.QuestionTitle"
    ]
    question_description: NotRequired[
        "aws_sdk_wellarchitected.types.question_description.QuestionDescription"
    ]
    improvement_plan_url: NotRequired[
        "aws_sdk_wellarchitected.types.improvement_plan_url.ImprovementPlanUrl"
    ]
    helpful_resource_url: NotRequired[
        "aws_sdk_wellarchitected.types.helpful_resource_url.HelpfulResourceUrl"
    ]
    helpful_resource_display_text: NotRequired[
        "aws_sdk_wellarchitected.types.display_text.DisplayText"
    ]
    """<p>The helpful resource text to be displayed for a custom lens.</p> <p>This field does not apply to Amazon Web Services official lenses.</p>"""
    choices: NotRequired["aws_sdk_wellarchitected.types.choices.Choices"]
    selected_choices: NotRequired[
        "aws_sdk_wellarchitected.types.selected_choices.SelectedChoices"
    ]
    choice_answers: NotRequired[
        "aws_sdk_wellarchitected.types.choice_answers.ChoiceAnswers"
    ]
    """<p>A list of selected choices to a question in your workload.</p>"""
    is_applicable: NotRequired[
        "aws_sdk_wellarchitected.types.is_applicable.IsApplicable"
    ]
    risk: NotRequired["aws_sdk_wellarchitected.types.risk.Risk"]
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    reason: NotRequired["aws_sdk_wellarchitected.types.answer_reason.AnswerReason"]
    """<p>The reason why the question is not applicable to your workload.</p>"""
    jira_configuration: NotRequired[
        "aws_sdk_wellarchitected.types.jira_configuration.JiraConfiguration"
    ]
    """<p>Configuration of the Jira integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Answer) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "question_description" in value:
        out["QuestionDescription"] = value["question_description"]
    if "improvement_plan_url" in value:
        out["ImprovementPlanUrl"] = value["improvement_plan_url"]
    if "helpful_resource_url" in value:
        out["HelpfulResourceUrl"] = value["helpful_resource_url"]
    if "helpful_resource_display_text" in value:
        out["HelpfulResourceDisplayText"] = value["helpful_resource_display_text"]
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
    if "choice_answers" in value:
        import aws_sdk_wellarchitected.types.choice_answers

        out["ChoiceAnswers"] = (
            aws_sdk_wellarchitected.types.choice_answers.serialize_json(
                value["choice_answers"]
            )
        )
    if "is_applicable" in value:
        out["IsApplicable"] = value["is_applicable"]
    if "risk" in value:
        import aws_sdk_wellarchitected.types.risk

        out["Risk"] = aws_sdk_wellarchitected.types.risk.serialize_json(value["risk"])
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "reason" in value:
        import aws_sdk_wellarchitected.types.answer_reason

        out["Reason"] = aws_sdk_wellarchitected.types.answer_reason.serialize_json(
            value["reason"]
        )
    if "jira_configuration" in value:
        import aws_sdk_wellarchitected.types.jira_configuration

        out["JiraConfiguration"] = (
            aws_sdk_wellarchitected.types.jira_configuration.serialize_json(
                value["jira_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Answer:
    out: Answer = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "QuestionTitle" in data:
        out["question_title"] = data["QuestionTitle"]
    if "QuestionDescription" in data:
        out["question_description"] = data["QuestionDescription"]
    if "ImprovementPlanUrl" in data:
        out["improvement_plan_url"] = data["ImprovementPlanUrl"]
    if "HelpfulResourceUrl" in data:
        out["helpful_resource_url"] = data["HelpfulResourceUrl"]
    if "HelpfulResourceDisplayText" in data:
        out["helpful_resource_display_text"] = data["HelpfulResourceDisplayText"]
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
    if "ChoiceAnswers" in data:
        import aws_sdk_wellarchitected.types.choice_answers

        out["choice_answers"] = (
            aws_sdk_wellarchitected.types.choice_answers.deserialize_json(
                data["ChoiceAnswers"]
            )
        )
    if "IsApplicable" in data:
        out["is_applicable"] = data["IsApplicable"]
    if "Risk" in data:
        import aws_sdk_wellarchitected.types.risk

        out["risk"] = aws_sdk_wellarchitected.types.risk.deserialize_json(data["Risk"])
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "Reason" in data:
        import aws_sdk_wellarchitected.types.answer_reason

        out["reason"] = aws_sdk_wellarchitected.types.answer_reason.deserialize_json(
            data["Reason"]
        )
    if "JiraConfiguration" in data:
        import aws_sdk_wellarchitected.types.jira_configuration

        out["jira_configuration"] = (
            aws_sdk_wellarchitected.types.jira_configuration.deserialize_json(
                data["JiraConfiguration"]
            )
        )
    return out
