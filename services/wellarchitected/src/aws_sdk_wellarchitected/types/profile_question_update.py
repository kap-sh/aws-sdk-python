"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestionUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.question_id
    import aws_sdk_wellarchitected.types.selected_profile_choice_ids


class ProfileQuestionUpdate(TypedDict, closed=True):
    question_id: NotRequired["aws_sdk_wellarchitected.types.question_id.QuestionId"]
    selected_choice_ids: NotRequired[
        "aws_sdk_wellarchitected.types.selected_profile_choice_ids.SelectedProfileChoiceIds"
    ]
    """<p>The selected choices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestionUpdate) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "selected_choice_ids" in value:
        import aws_sdk_wellarchitected.types.selected_profile_choice_ids

        out["SelectedChoiceIds"] = (
            aws_sdk_wellarchitected.types.selected_profile_choice_ids.serialize_json(
                value["selected_choice_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileQuestionUpdate:
    out: ProfileQuestionUpdate = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "SelectedChoiceIds" in data:
        import aws_sdk_wellarchitected.types.selected_profile_choice_ids

        out["selected_choice_ids"] = (
            aws_sdk_wellarchitected.types.selected_profile_choice_ids.deserialize_json(
                data["SelectedChoiceIds"]
            )
        )
    return out
