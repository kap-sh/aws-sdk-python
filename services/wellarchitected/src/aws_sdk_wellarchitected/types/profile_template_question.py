"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileTemplateQuestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.max_selected_profile_choices
    import aws_sdk_wellarchitected.types.min_selected_profile_choices
    import aws_sdk_wellarchitected.types.profile_template_question_choices
    import aws_sdk_wellarchitected.types.question_description
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.question_title


class ProfileTemplateQuestion(TypedDict, closed=True):
    question_id: NotRequired["aws_sdk_wellarchitected.types.question_id.QuestionId"]
    question_title: NotRequired[
        "aws_sdk_wellarchitected.types.question_title.QuestionTitle"
    ]
    question_description: NotRequired[
        "aws_sdk_wellarchitected.types.question_description.QuestionDescription"
    ]
    question_choices: NotRequired[
        "aws_sdk_wellarchitected.types.profile_template_question_choices.ProfileTemplateQuestionChoices"
    ]
    """<p>The question choices.</p>"""
    min_selected_choices: NotRequired[
        "aws_sdk_wellarchitected.types.min_selected_profile_choices.MinSelectedProfileChoices"
    ]
    """<p>The minimum number of choices selected.</p>"""
    max_selected_choices: NotRequired[
        "aws_sdk_wellarchitected.types.max_selected_profile_choices.MaxSelectedProfileChoices"
    ]
    """<p>The maximum number of choices selected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTemplateQuestion) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "question_description" in value:
        out["QuestionDescription"] = value["question_description"]
    if "question_choices" in value:
        import aws_sdk_wellarchitected.types.profile_template_question_choices

        out["QuestionChoices"] = (
            aws_sdk_wellarchitected.types.profile_template_question_choices.serialize_json(
                value["question_choices"]
            )
        )
    if "min_selected_choices" in value:
        out["MinSelectedChoices"] = value["min_selected_choices"]
    if "max_selected_choices" in value:
        out["MaxSelectedChoices"] = value["max_selected_choices"]
    return out


def deserialize_json(data: dict) -> ProfileTemplateQuestion:
    out: ProfileTemplateQuestion = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "QuestionTitle" in data:
        out["question_title"] = data["QuestionTitle"]
    if "QuestionDescription" in data:
        out["question_description"] = data["QuestionDescription"]
    if "QuestionChoices" in data:
        import aws_sdk_wellarchitected.types.profile_template_question_choices

        out["question_choices"] = (
            aws_sdk_wellarchitected.types.profile_template_question_choices.deserialize_json(
                data["QuestionChoices"]
            )
        )
    if "MinSelectedChoices" in data:
        out["min_selected_choices"] = data["MinSelectedChoices"]
    if "MaxSelectedChoices" in data:
        out["max_selected_choices"] = data["MaxSelectedChoices"]
    return out
