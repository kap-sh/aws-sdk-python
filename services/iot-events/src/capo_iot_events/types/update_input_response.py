"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input_configuration


class UpdateInputResponse(TypedDict, closed=True):
    input_configuration: NotRequired[
        "capo_iot_events.types.input_configuration.InputConfiguration"
    ]
    """<p>Information about the configuration of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputResponse) -> dict:
    out: dict = {}
    if "input_configuration" in value:
        import capo_iot_events.types.input_configuration

        out["inputConfiguration"] = (
            capo_iot_events.types.input_configuration.serialize_json(
                value["input_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateInputResponse:
    out: UpdateInputResponse = {}  # type: ignore[typeddict-item]
    if "inputConfiguration" in data:
        import capo_iot_events.types.input_configuration

        out["input_configuration"] = (
            capo_iot_events.types.input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    return out
