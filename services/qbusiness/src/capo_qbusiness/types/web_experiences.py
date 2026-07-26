"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperiences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.web_experience

WebExperiences: TypeAlias = list["capo_qbusiness.types.web_experience.WebExperience"]


# --- restJson1 ser/de ---
def serialize_json(value: WebExperiences) -> list:
    import capo_qbusiness.types.web_experience

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.web_experience.serialize_json(item))
    return out


def deserialize_json(data: list) -> WebExperiences:
    import capo_qbusiness.types.web_experience

    out: WebExperiences = []
    for item in data:
        out.append(capo_qbusiness.types.web_experience.deserialize_json(item))
    return out
