"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetPresetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class GetPresetRequest(TypedDict, closed=True):
    name: "aws_sdk_mediaconvert.types.__string.__string"
    """The name of the preset."""


# --- restJson1 ser/de ---
def serialize_json(value: GetPresetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPresetRequest:
    out: GetPresetRequest = {}  # type: ignore[typeddict-item]
    return out
