"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class InputDeviceRequest(TypedDict):
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ID for the device."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> InputDeviceRequest:
    out: InputDeviceRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
