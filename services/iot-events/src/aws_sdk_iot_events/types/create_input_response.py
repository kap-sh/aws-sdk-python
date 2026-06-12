"""Generated from Smithy shape ``com.amazonaws.iotevents#CreateInputResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_configuration


class CreateInputResponse(TypedDict):
    input_configuration: NotRequired[
        "aws_sdk_iot_events.types.input_configuration.InputConfiguration"
    ]
    """<p>Information about the configuration of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputResponse) -> dict:
    out: dict = {}
    if "input_configuration" in value:
        import aws_sdk_iot_events.types.input_configuration

        out["inputConfiguration"] = (
            aws_sdk_iot_events.types.input_configuration.serialize_json(
                value["input_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateInputResponse:
    out: CreateInputResponse = {}  # type: ignore[typeddict-item]
    if "inputConfiguration" in data:
        import aws_sdk_iot_events.types.input_configuration

        out["input_configuration"] = (
            aws_sdk_iot_events.types.input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    return out
