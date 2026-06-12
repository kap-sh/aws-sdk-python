"""Generated from Smithy shape ``com.amazonaws.iotevents#IotEventsInputIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_name


class IotEventsInputIdentifier(TypedDict):
    input_name: "aws_sdk_iot_events.types.input_name.InputName"
    """<p> The name of the input routed to AWS IoT Events. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotEventsInputIdentifier) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    return out


def deserialize_json(data: dict) -> IotEventsInputIdentifier:
    out: IotEventsInputIdentifier = {}  # type: ignore[typeddict-item]
    if "inputName" in data:
        out["input_name"] = data["inputName"]
    else:
        raise DeserializationError("IotEventsInputIdentifier.input_name required")
    return out
