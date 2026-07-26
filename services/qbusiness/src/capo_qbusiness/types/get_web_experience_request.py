"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetWebExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.web_experience_id


class GetWebExperienceRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to the web experience.</p>"""
    web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId"
    """<p>The identifier of the Amazon Q Business web experience. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWebExperienceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWebExperienceRequest:
    out: GetWebExperienceRequest = {}  # type: ignore[typeddict-item]
    return out
