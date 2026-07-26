"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class GetJobTemplateRequest(TypedDict, closed=True):
    name: "capo_mediaconvert.types.__string.__string"
    """The name of the job template."""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobTemplateRequest:
    out: GetJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
