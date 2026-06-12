"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_name


class DeleteDestinationRequest(TypedDict):
    name: "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    """<p>The name of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDestinationRequest:
    out: DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
