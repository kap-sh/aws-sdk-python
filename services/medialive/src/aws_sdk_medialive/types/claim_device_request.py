"""Generated from Smithy shape ``com.amazonaws.medialive#ClaimDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class ClaimDeviceRequest(TypedDict):
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The id of the device you want to claim."""


# --- restJson1 ser/de ---
def serialize_json(value: ClaimDeviceRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ClaimDeviceRequest:
    out: ClaimDeviceRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
