"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.profile_description
    import capo_wellarchitected.types.profile_question_updates


class UpdateProfileInput(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    profile_description: NotRequired[
        "capo_wellarchitected.types.profile_description.ProfileDescription"
    ]
    """<p>The profile description.</p>"""
    profile_questions: NotRequired[
        "capo_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates"
    ]
    """<p>Profile questions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileInput) -> dict:
    out: dict = {}
    if "profile_description" in value:
        out["ProfileDescription"] = value["profile_description"]
    if "profile_questions" in value:
        import capo_wellarchitected.types.profile_question_updates

        out["ProfileQuestions"] = (
            capo_wellarchitected.types.profile_question_updates.serialize_json(
                value["profile_questions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateProfileInput:
    out: UpdateProfileInput = {}  # type: ignore[typeddict-item]
    if "ProfileDescription" in data:
        out["profile_description"] = data["ProfileDescription"]
    if "ProfileQuestions" in data:
        import capo_wellarchitected.types.profile_question_updates

        out["profile_questions"] = (
            capo_wellarchitected.types.profile_question_updates.deserialize_json(
                data["ProfileQuestions"]
            )
        )
    return out
