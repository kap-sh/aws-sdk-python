"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteWebExperienceRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.web_experience_id

class DeleteWebExperienceRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to the Amazon Q Business web experience.</p>"""
    web_experience_id: "aws_sdk_qbusiness.types.web_experience_id.WebExperienceId"
    """<p>The identifier of the Amazon Q Business web experience being deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteWebExperienceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWebExperienceRequest:
    out: DeleteWebExperienceRequest = {}  # type: ignore[typeddict-item]
    return out