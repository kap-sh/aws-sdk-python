"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_definition
    import aws_sdk_iot_events.types.input_description
    import aws_sdk_iot_events.types.input_name


class UpdateInputRequest(TypedDict, closed=True):
    input_name: "aws_sdk_iot_events.types.input_name.InputName"
    """<p>The name of the input you want to update.</p>"""
    input_description: NotRequired[
        "aws_sdk_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_definition: "aws_sdk_iot_events.types.input_definition.InputDefinition"
    """<p>The definition of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputRequest) -> dict:
    out: dict = {}
    if "input_description" in value:
        out["inputDescription"] = value["input_description"]
    import aws_sdk_iot_events.types.input_definition

    out["inputDefinition"] = aws_sdk_iot_events.types.input_definition.serialize_json(
        value["input_definition"]
    )
    return out


def deserialize_json(data: dict) -> UpdateInputRequest:
    out: UpdateInputRequest = {}  # type: ignore[typeddict-item]
    if "inputDescription" in data:
        out["input_description"] = data["inputDescription"]
    if "inputDefinition" in data:
        import aws_sdk_iot_events.types.input_definition

        out["input_definition"] = (
            aws_sdk_iot_events.types.input_definition.deserialize_json(
                data["inputDefinition"]
            )
        )
    else:
        raise DeserializationError("UpdateInputRequest.input_definition required")
    return out
