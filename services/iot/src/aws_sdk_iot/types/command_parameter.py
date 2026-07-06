"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_parameter_description
    import aws_sdk_iot.types.command_parameter_name
    import aws_sdk_iot.types.command_parameter_type
    import aws_sdk_iot.types.command_parameter_value
    import aws_sdk_iot.types.command_parameter_value_condition_list


class CommandParameter(TypedDict, closed=True):
    name: "aws_sdk_iot.types.command_parameter_name.CommandParameterName"
    """<p>The name of a specific parameter used in a command and command execution.</p>"""
    type: NotRequired["aws_sdk_iot.types.command_parameter_type.CommandParameterType"]
    """<p>The type of the command parameter.</p>"""
    value: NotRequired[
        "aws_sdk_iot.types.command_parameter_value.CommandParameterValue"
    ]
    """<p>Parameter value that overrides the default value, if set.</p>"""
    default_value: NotRequired[
        "aws_sdk_iot.types.command_parameter_value.CommandParameterValue"
    ]
    """<p>The default value used to describe the command. This is the value assumed by the parameter if no other value is assigned to it.</p>"""
    value_conditions: NotRequired[
        "aws_sdk_iot.types.command_parameter_value_condition_list.CommandParameterValueConditionList"
    ]
    """<p>The list of conditions that a command parameter value must satisfy to create a command execution.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.command_parameter_description.CommandParameterDescription"
    ]
    """<p>The description of the command parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_iot.types.command_parameter_type

        out["type"] = aws_sdk_iot.types.command_parameter_type.serialize_json(
            value["type"]
        )
    if "value" in value:
        import aws_sdk_iot.types.command_parameter_value

        out["value"] = aws_sdk_iot.types.command_parameter_value.serialize_json(
            value["value"]
        )
    if "default_value" in value:
        import aws_sdk_iot.types.command_parameter_value

        out["defaultValue"] = aws_sdk_iot.types.command_parameter_value.serialize_json(
            value["default_value"]
        )
    if "value_conditions" in value:
        import aws_sdk_iot.types.command_parameter_value_condition_list

        out["valueConditions"] = (
            aws_sdk_iot.types.command_parameter_value_condition_list.serialize_json(
                value["value_conditions"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CommandParameter:
    out: CommandParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CommandParameter.name required")
    if "type" in data:
        import aws_sdk_iot.types.command_parameter_type

        out["type"] = aws_sdk_iot.types.command_parameter_type.deserialize_json(
            data["type"]
        )
    if "value" in data:
        import aws_sdk_iot.types.command_parameter_value

        out["value"] = aws_sdk_iot.types.command_parameter_value.deserialize_json(
            data["value"]
        )
    if "defaultValue" in data:
        import aws_sdk_iot.types.command_parameter_value

        out["default_value"] = (
            aws_sdk_iot.types.command_parameter_value.deserialize_json(
                data["defaultValue"]
            )
        )
    if "valueConditions" in data:
        import aws_sdk_iot.types.command_parameter_value_condition_list

        out["value_conditions"] = (
            aws_sdk_iot.types.command_parameter_value_condition_list.deserialize_json(
                data["valueConditions"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
