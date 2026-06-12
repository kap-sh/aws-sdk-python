"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DeletePresetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class DeletePresetRequest(TypedDict):
    name: "aws_sdk_mediaconvert.types.__string.__string"
    """The name of the preset to be deleted."""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePresetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePresetRequest:
    out: DeletePresetRequest = {}  # type: ignore[typeddict-item]
    return out
