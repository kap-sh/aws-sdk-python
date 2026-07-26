"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.max_selected_profile_choices
    import capo_wellarchitected.types.min_selected_profile_choices
    import capo_wellarchitected.types.profile_question_choices
    import capo_wellarchitected.types.question_description
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_title
    import capo_wellarchitected.types.selected_choice_ids


class ProfileQuestion(TypedDict, closed=True):
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    question_title: NotRequired[
        "capo_wellarchitected.types.question_title.QuestionTitle"
    ]
    question_description: NotRequired[
        "capo_wellarchitected.types.question_description.QuestionDescription"
    ]
    question_choices: NotRequired[
        "capo_wellarchitected.types.profile_question_choices.ProfileQuestionChoices"
    ]
    """<p>The question choices.</p>"""
    selected_choice_ids: NotRequired[
        "capo_wellarchitected.types.selected_choice_ids.SelectedChoiceIds"
    ]
    """<p>The selected choices.</p>"""
    min_selected_choices: NotRequired[
        "capo_wellarchitected.types.min_selected_profile_choices.MinSelectedProfileChoices"
    ]
    """<p>The minimum number of selected choices.</p>"""
    max_selected_choices: NotRequired[
        "capo_wellarchitected.types.max_selected_profile_choices.MaxSelectedProfileChoices"
    ]
    """<p>The maximum number of selected choices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestion) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "question_description" in value:
        out["QuestionDescription"] = value["question_description"]
    if "question_choices" in value:
        import capo_wellarchitected.types.profile_question_choices

        out["QuestionChoices"] = (
            capo_wellarchitected.types.profile_question_choices.serialize_json(
                value["question_choices"]
            )
        )
    if "selected_choice_ids" in value:
        import capo_wellarchitected.types.selected_choice_ids

        out["SelectedChoiceIds"] = (
            capo_wellarchitected.types.selected_choice_ids.serialize_json(
                value["selected_choice_ids"]
            )
        )
    if "min_selected_choices" in value:
        out["MinSelectedChoices"] = value["min_selected_choices"]
    if "max_selected_choices" in value:
        out["MaxSelectedChoices"] = value["max_selected_choices"]
    return out


def deserialize_json(data: dict) -> ProfileQuestion:
    out: ProfileQuestion = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "QuestionTitle" in data:
        out["question_title"] = data["QuestionTitle"]
    if "QuestionDescription" in data:
        out["question_description"] = data["QuestionDescription"]
    if "QuestionChoices" in data:
        import capo_wellarchitected.types.profile_question_choices

        out["question_choices"] = (
            capo_wellarchitected.types.profile_question_choices.deserialize_json(
                data["QuestionChoices"]
            )
        )
    if "SelectedChoiceIds" in data:
        import capo_wellarchitected.types.selected_choice_ids

        out["selected_choice_ids"] = (
            capo_wellarchitected.types.selected_choice_ids.deserialize_json(
                data["SelectedChoiceIds"]
            )
        )
    if "MinSelectedChoices" in data:
        out["min_selected_choices"] = data["MinSelectedChoices"]
    if "MaxSelectedChoices" in data:
        out["max_selected_choices"] = data["MaxSelectedChoices"]
    return out
