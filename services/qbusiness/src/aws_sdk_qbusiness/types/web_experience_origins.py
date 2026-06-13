"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceOrigins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.origin

WebExperienceOrigins: TypeAlias = list["aws_sdk_qbusiness.types.origin.Origin"]


# --- restJson1 ser/de ---
def serialize_json(value: WebExperienceOrigins) -> list:
    return list(value)


def deserialize_json(data: list) -> WebExperienceOrigins:
    return list(data)
