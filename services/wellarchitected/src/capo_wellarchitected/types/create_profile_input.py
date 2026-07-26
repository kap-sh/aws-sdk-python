"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.profile_description
    import capo_wellarchitected.types.profile_name
    import capo_wellarchitected.types.profile_question_updates
    import capo_wellarchitected.types.tag_map


class CreateProfileInput(TypedDict, closed=True):
    profile_name: NotRequired["capo_wellarchitected.types.profile_name.ProfileName"]
    """<p>Name of the profile.</p>"""
    profile_description: NotRequired[
        "capo_wellarchitected.types.profile_description.ProfileDescription"
    ]
    """<p>The profile description.</p>"""
    profile_questions: NotRequired[
        "capo_wellarchitected.types.profile_question_updates.ProfileQuestionUpdates"
    ]
    """<p>The profile questions.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["capo_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags assigned to the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileInput) -> dict:
    out: dict = {}
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "profile_description" in value:
        out["ProfileDescription"] = value["profile_description"]
    if "profile_questions" in value:
        import capo_wellarchitected.types.profile_question_updates

        out["ProfileQuestions"] = (
            capo_wellarchitected.types.profile_question_updates.serialize_json(
                value["profile_questions"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_wellarchitected.types.tag_map

        out["Tags"] = capo_wellarchitected.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProfileInput:
    out: CreateProfileInput = {}  # type: ignore[typeddict-item]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "ProfileDescription" in data:
        out["profile_description"] = data["ProfileDescription"]
    if "ProfileQuestions" in data:
        import capo_wellarchitected.types.profile_question_updates

        out["profile_questions"] = (
            capo_wellarchitected.types.profile_question_updates.deserialize_json(
                data["ProfileQuestions"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import capo_wellarchitected.types.tag_map

        out["tags"] = capo_wellarchitected.types.tag_map.deserialize_json(data["Tags"])
    return out
