"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.destination_name


class GetDestinationRequest(TypedDict, closed=True):
    name: "aws_sdk_iot_wireless.types.destination_name.DestinationName"
    """<p>The name of the resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDestinationRequest:
    out: GetDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
