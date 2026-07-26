"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateAnonymousWebExperienceUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.session_duration_in_minutes
    import capo_qbusiness.types.web_experience_id


class CreateAnonymousWebExperienceUrlRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application environment attached to the web experience.</p>"""
    web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId"
    """<p>The identifier of the web experience.</p>"""
    session_duration_in_minutes: NotRequired[
        "capo_qbusiness.types.session_duration_in_minutes.SessionDurationInMinutes"
    ]
    """<p>The duration of the session associated with the unique URL for the web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnonymousWebExperienceUrlRequest) -> dict:
    out: dict = {}
    if "session_duration_in_minutes" in value:
        out["sessionDurationInMinutes"] = value["session_duration_in_minutes"]
    return out


def deserialize_json(data: dict) -> CreateAnonymousWebExperienceUrlRequest:
    out: CreateAnonymousWebExperienceUrlRequest = {}  # type: ignore[typeddict-item]
    if "sessionDurationInMinutes" in data:
        out["session_duration_in_minutes"] = data["sessionDurationInMinutes"]
    return out
