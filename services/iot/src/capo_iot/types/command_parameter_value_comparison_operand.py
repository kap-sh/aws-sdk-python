"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueComparisonOperand``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_parameter_value_number_range
    import capo_iot.types.command_parameter_value_string_list
    import capo_iot.types.string_parameter_value


class CommandParameterValueComparisonOperand(TypedDict, closed=True):
    number: NotRequired["capo_iot.types.string_parameter_value.StringParameterValue"]
    """<p>An operand of number value type, defined as a string.</p>"""
    numbers: NotRequired[
        "capo_iot.types.command_parameter_value_string_list.CommandParameterValueStringList"
    ]
    """<p>A List of operands of numerical value type, defined as strings.</p>"""
    string: NotRequired["capo_iot.types.string_parameter_value.StringParameterValue"]
    """<p>An operand of string value type.</p>"""
    strings: NotRequired[
        "capo_iot.types.command_parameter_value_string_list.CommandParameterValueStringList"
    ]
    """<p>A List of operands of string value type.</p>"""
    number_range: NotRequired[
        "capo_iot.types.command_parameter_value_number_range.CommandParameterValueNumberRange"
    ]
    """<p>An operand of numerical range value type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueComparisonOperand) -> dict:
    out: dict = {}
    if "number" in value:
        out["number"] = value["number"]
    if "numbers" in value:
        import capo_iot.types.command_parameter_value_string_list

        out["numbers"] = (
            capo_iot.types.command_parameter_value_string_list.serialize_json(
                value["numbers"]
            )
        )
    if "string" in value:
        out["string"] = value["string"]
    if "strings" in value:
        import capo_iot.types.command_parameter_value_string_list

        out["strings"] = (
            capo_iot.types.command_parameter_value_string_list.serialize_json(
                value["strings"]
            )
        )
    if "number_range" in value:
        import capo_iot.types.command_parameter_value_number_range

        out["numberRange"] = (
            capo_iot.types.command_parameter_value_number_range.serialize_json(
                value["number_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> CommandParameterValueComparisonOperand:
    out: CommandParameterValueComparisonOperand = {}  # type: ignore[typeddict-item]
    if "number" in data:
        out["number"] = data["number"]
    if "numbers" in data:
        import capo_iot.types.command_parameter_value_string_list

        out["numbers"] = (
            capo_iot.types.command_parameter_value_string_list.deserialize_json(
                data["numbers"]
            )
        )
    if "string" in data:
        out["string"] = data["string"]
    if "strings" in data:
        import capo_iot.types.command_parameter_value_string_list

        out["strings"] = (
            capo_iot.types.command_parameter_value_string_list.deserialize_json(
                data["strings"]
            )
        )
    if "numberRange" in data:
        import capo_iot.types.command_parameter_value_number_range

        out["number_range"] = (
            capo_iot.types.command_parameter_value_number_range.deserialize_json(
                data["numberRange"]
            )
        )
    return out
