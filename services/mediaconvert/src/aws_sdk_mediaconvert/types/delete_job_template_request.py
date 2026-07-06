"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DeleteJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class DeleteJobTemplateRequest(TypedDict, closed=True):
    name: "aws_sdk_mediaconvert.types.__string.__string"
    """The name of the job template to be deleted."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteJobTemplateRequest:
    out: DeleteJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
