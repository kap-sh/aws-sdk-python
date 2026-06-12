"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueComparisonOperand``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_parameter_value_number_range
    import aws_sdk_iot.types.command_parameter_value_string_list
    import aws_sdk_iot.types.string_parameter_value


class CommandParameterValueComparisonOperand(TypedDict):
    number: NotRequired["aws_sdk_iot.types.string_parameter_value.StringParameterValue"]
    """<p>An operand of number value type, defined as a string.</p>"""
    numbers: NotRequired[
        "aws_sdk_iot.types.command_parameter_value_string_list.CommandParameterValueStringList"
    ]
    """<p>A List of operands of numerical value type, defined as strings.</p>"""
    string: NotRequired["aws_sdk_iot.types.string_parameter_value.StringParameterValue"]
    """<p>An operand of string value type.</p>"""
    strings: NotRequired[
        "aws_sdk_iot.types.command_parameter_value_string_list.CommandParameterValueStringList"
    ]
    """<p>A List of operands of string value type.</p>"""
    number_range: NotRequired[
        "aws_sdk_iot.types.command_parameter_value_number_range.CommandParameterValueNumberRange"
    ]
    """<p>An operand of numerical range value type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueComparisonOperand) -> dict:
    out: dict = {}
    if "number" in value:
        out["number"] = value["number"]
    if "numbers" in value:
        import aws_sdk_iot.types.command_parameter_value_string_list

        out["numbers"] = (
            aws_sdk_iot.types.command_parameter_value_string_list.serialize_json(
                value["numbers"]
            )
        )
    if "string" in value:
        out["string"] = value["string"]
    if "strings" in value:
        import aws_sdk_iot.types.command_parameter_value_string_list

        out["strings"] = (
            aws_sdk_iot.types.command_parameter_value_string_list.serialize_json(
                value["strings"]
            )
        )
    if "number_range" in value:
        import aws_sdk_iot.types.command_parameter_value_number_range

        out["numberRange"] = (
            aws_sdk_iot.types.command_parameter_value_number_range.serialize_json(
                value["number_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommandParameterValueComparisonOperand:
    out: CommandParameterValueComparisonOperand = {}  # type: ignore[typeddict-item]
    if "number" in data:
        out["number"] = data["number"]
    if "numbers" in data:
        import aws_sdk_iot.types.command_parameter_value_string_list

        out["numbers"] = (
            aws_sdk_iot.types.command_parameter_value_string_list.deserialize_json(
                data["numbers"]
            )
        )
    if "string" in data:
        out["string"] = data["string"]
    if "strings" in data:
        import aws_sdk_iot.types.command_parameter_value_string_list

        out["strings"] = (
            aws_sdk_iot.types.command_parameter_value_string_list.deserialize_json(
                data["strings"]
            )
        )
    if "numberRange" in data:
        import aws_sdk_iot.types.command_parameter_value_number_range

        out["number_range"] = (
            aws_sdk_iot.types.command_parameter_value_number_range.deserialize_json(
                data["numberRange"]
            )
        )
    return out
