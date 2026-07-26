"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateWebExperienceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.web_experience_arn
    import capo_qbusiness.types.web_experience_id


class CreateWebExperienceResponse(TypedDict, closed=True):
    web_experience_id: NotRequired[
        "capo_qbusiness.types.web_experience_id.WebExperienceId"
    ]
    """<p>The identifier of the Amazon Q Business web experience.</p>"""
    web_experience_arn: NotRequired[
        "capo_qbusiness.types.web_experience_arn.WebExperienceArn"
    ]
    """<p> The Amazon Resource Name (ARN) of an Amazon Q Business web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWebExperienceResponse) -> dict:
    out: dict = {}
    if "web_experience_id" in value:
        out["webExperienceId"] = value["web_experience_id"]
    if "web_experience_arn" in value:
        out["webExperienceArn"] = value["web_experience_arn"]
    return out


def deserialize_json(data: dict) -> CreateWebExperienceResponse:
    out: CreateWebExperienceResponse = {}  # type: ignore[typeddict-item]
    if "webExperienceId" in data:
        out["web_experience_id"] = data["webExperienceId"]
    if "webExperienceArn" in data:
        out["web_experience_arn"] = data["webExperienceArn"]
    return out
