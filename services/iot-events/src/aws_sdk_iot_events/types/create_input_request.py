"""Generated from Smithy shape ``com.amazonaws.iotevents#CreateInputRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_definition
    import aws_sdk_iot_events.types.input_description
    import aws_sdk_iot_events.types.input_name
    import aws_sdk_iot_events.types.tags


class CreateInputRequest(TypedDict):
    input_name: "aws_sdk_iot_events.types.input_name.InputName"
    """<p>The name you want to give to the input.</p>"""
    input_description: NotRequired[
        "aws_sdk_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_definition: "aws_sdk_iot_events.types.input_definition.InputDefinition"
    """<p>The definition of the input.</p>"""
    tags: NotRequired["aws_sdk_iot_events.types.tags.Tags"]
    """<p>Metadata that can be used to manage the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputRequest) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    if "input_description" in value:
        out["inputDescription"] = value["input_description"]
    import aws_sdk_iot_events.types.input_definition

    out["inputDefinition"] = aws_sdk_iot_events.types.input_definition.serialize_json(
        value["input_definition"]
    )
    if "tags" in value:
        import aws_sdk_iot_events.types.tags

        out["tags"] = aws_sdk_iot_events.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateInputRequest:
    out: CreateInputRequest = {}  # type: ignore[typeddict-item]
    if "inputName" in data:
        out["input_name"] = data["inputName"]
    else:
        raise DeserializationError("CreateInputRequest.input_name required")
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
        raise DeserializationError("CreateInputRequest.input_definition required")
    if "tags" in data:
        import aws_sdk_iot_events.types.tags

        out["tags"] = aws_sdk_iot_events.types.tags.deserialize_json(data["tags"])
    return out
