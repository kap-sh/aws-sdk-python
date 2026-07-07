"""Generated from Smithy shape ``com.amazonaws.databrew#RecipeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.operation
    import aws_sdk_databrew.types.parameter_map


class RecipeAction(TypedDict, closed=True):
    operation: "aws_sdk_databrew.types.operation.Operation"
    """<p>The name of a valid DataBrew transformation to be performed on the data.</p>"""
    parameters: NotRequired["aws_sdk_databrew.types.parameter_map.ParameterMap"]
    """<p>Contextual parameters for the transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecipeAction) -> dict:
    out: dict = {}
    out["Operation"] = value["operation"]
    if "parameters" in value:
        import aws_sdk_databrew.types.parameter_map

        out["Parameters"] = aws_sdk_databrew.types.parameter_map.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> RecipeAction:
    out: RecipeAction = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    else:
        raise DeserializationError("RecipeAction.operation required")
    if "Parameters" in data:
        import aws_sdk_databrew.types.parameter_map

        out["parameters"] = aws_sdk_databrew.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    return out
