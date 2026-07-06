"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputDeviceSettings(TypedDict, closed=True):
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ID for the device."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceSettings) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> InputDeviceSettings:
    out: InputDeviceSettings = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
