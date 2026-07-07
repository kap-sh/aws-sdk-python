"""Generated from Smithy shape ``com.amazonaws.iot#CommandParameterValueCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_parameter_value_comparison_operand
    import aws_sdk_iot.types.command_parameter_value_comparison_operator


class CommandParameterValueCondition(TypedDict, closed=True):
    comparison_operator: "aws_sdk_iot.types.command_parameter_value_comparison_operator.CommandParameterValueComparisonOperator"
    """<p>The comparison operator for the command parameter.</p> <note> <p>IN_RANGE, and NOT_IN_RANGE operators include boundary values.</p> </note>"""
    operand: "aws_sdk_iot.types.command_parameter_value_comparison_operand.CommandParameterValueComparisonOperand"
    """<p>The comparison operand for the command parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandParameterValueCondition) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.command_parameter_value_comparison_operator

    out["comparisonOperator"] = (
        aws_sdk_iot.types.command_parameter_value_comparison_operator.serialize_json(
            value["comparison_operator"]
        )
    )
    import aws_sdk_iot.types.command_parameter_value_comparison_operand

    out["operand"] = (
        aws_sdk_iot.types.command_parameter_value_comparison_operand.serialize_json(
            value["operand"]
        )
    )
    return out


def deserialize_json(data: dict) -> CommandParameterValueCondition:
    out: CommandParameterValueCondition = {}  # type: ignore[typeddict-item]
    if "comparisonOperator" in data:
        import aws_sdk_iot.types.command_parameter_value_comparison_operator

        out["comparison_operator"] = (
            aws_sdk_iot.types.command_parameter_value_comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    else:
        raise DeserializationError(
            "CommandParameterValueCondition.comparison_operator required"
        )
    if "operand" in data:
        import aws_sdk_iot.types.command_parameter_value_comparison_operand

        out["operand"] = (
            aws_sdk_iot.types.command_parameter_value_comparison_operand.deserialize_json(
                data["operand"]
            )
        )
    else:
        raise DeserializationError("CommandParameterValueCondition.operand required")
    return out
