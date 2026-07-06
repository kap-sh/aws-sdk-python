"""Generated from Smithy shape ``com.amazonaws.connectcases#BooleanOperands``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.operand_one
    import aws_sdk_connectcases.types.operand_two


class BooleanOperands(TypedDict, closed=True):
    operand_one: "aws_sdk_connectcases.types.operand_one.OperandOne"
    """<p>Represents the left hand operand in the condition.</p>"""
    operand_two: "aws_sdk_connectcases.types.operand_two.OperandTwo"
    """<p>Represents the right hand operand in the condition.</p>"""
    result: "bool"
    """<p>The value of the outer rule if the condition evaluates to true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BooleanOperands) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.operand_one

    out["operandOne"] = aws_sdk_connectcases.types.operand_one.serialize_json(
        value["operand_one"]
    )
    import aws_sdk_connectcases.types.operand_two

    out["operandTwo"] = aws_sdk_connectcases.types.operand_two.serialize_json(
        value["operand_two"]
    )
    out["result"] = value["result"]
    return out


def deserialize_json(data: dict) -> BooleanOperands:
    out: BooleanOperands = {}  # type: ignore[typeddict-item]
    if "operandOne" in data:
        import aws_sdk_connectcases.types.operand_one

        out["operand_one"] = aws_sdk_connectcases.types.operand_one.deserialize_json(
            data["operandOne"]
        )
    else:
        raise DeserializationError("BooleanOperands.operand_one required")
    if "operandTwo" in data:
        import aws_sdk_connectcases.types.operand_two

        out["operand_two"] = aws_sdk_connectcases.types.operand_two.deserialize_json(
            data["operandTwo"]
        )
    else:
        raise DeserializationError("BooleanOperands.operand_two required")
    if "result" in data:
        out["result"] = data["result"]
    else:
        raise DeserializationError("BooleanOperands.result required")
    return out
