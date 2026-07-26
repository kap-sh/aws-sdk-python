"""Generated from Smithy shape ``com.amazonaws.iotevents#Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input_configuration
    import capo_iot_events.types.input_definition


class Input(TypedDict, closed=True):
    input_configuration: NotRequired[
        "capo_iot_events.types.input_configuration.InputConfiguration"
    ]
    """<p>Information about the configuration of an input.</p>"""
    input_definition: NotRequired[
        "capo_iot_events.types.input_definition.InputDefinition"
    ]
    """<p>The definition of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Input) -> dict:
    out: dict = {}
    if "input_configuration" in value:
        import capo_iot_events.types.input_configuration

        out["inputConfiguration"] = (
            capo_iot_events.types.input_configuration.serialize_json(
                value["input_configuration"]
            )
        )
    if "input_definition" in value:
        import capo_iot_events.types.input_definition

        out["inputDefinition"] = capo_iot_events.types.input_definition.serialize_json(
            value["input_definition"]
        )
    return out


def deserialize_json(data: dict) -> Input:
    out: Input = {}  # type: ignore[typeddict-item]
    if "inputConfiguration" in data:
        import capo_iot_events.types.input_configuration

        out["input_configuration"] = (
            capo_iot_events.types.input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    if "inputDefinition" in data:
        import capo_iot_events.types.input_definition

        out["input_definition"] = (
            capo_iot_events.types.input_definition.deserialize_json(
                data["inputDefinition"]
            )
        )
    return out
