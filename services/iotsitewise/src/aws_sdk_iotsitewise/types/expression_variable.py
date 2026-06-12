"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExpressionVariable``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.variable_name
    import aws_sdk_iotsitewise.types.variable_value


class ExpressionVariable(TypedDict):
    name: "aws_sdk_iotsitewise.types.variable_name.VariableName"
    """<p>The friendly name of the variable to be used in the expression.</p>"""
    value: "aws_sdk_iotsitewise.types.variable_value.VariableValue"
    """<p>The variable that identifies an asset property from which to use values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressionVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_iotsitewise.types.variable_value

    out["value"] = aws_sdk_iotsitewise.types.variable_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> ExpressionVariable:
    out: ExpressionVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ExpressionVariable.name required")
    if "value" in data:
        import aws_sdk_iotsitewise.types.variable_value

        out["value"] = aws_sdk_iotsitewise.types.variable_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("ExpressionVariable.value required")
    return out
