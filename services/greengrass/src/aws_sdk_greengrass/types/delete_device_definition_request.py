"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteDeviceDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class DeleteDeviceDefinitionRequest(TypedDict, closed=True):
    device_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the device definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeviceDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeviceDefinitionRequest:
    out: DeleteDeviceDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
