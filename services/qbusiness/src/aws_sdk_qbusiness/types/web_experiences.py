"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperiences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.web_experience

WebExperiences: TypeAlias = list["aws_sdk_qbusiness.types.web_experience.WebExperience"]


# --- restJson1 ser/de ---
def serialize_json(value: WebExperiences) -> list:
    import aws_sdk_qbusiness.types.web_experience

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.web_experience.serialize_json(item))
    return out


def deserialize_json(data: list) -> WebExperiences:
    import aws_sdk_qbusiness.types.web_experience

    out: WebExperiences = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.web_experience.deserialize_json(item))
    return out
