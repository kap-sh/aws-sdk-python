"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterSpace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.combination_expression
    import aws_sdk_deadline.types.step_parameter_list


class ParameterSpace(TypedDict):
    parameters: "aws_sdk_deadline.types.step_parameter_list.StepParameterList"
    """<p>The parameters to search for.</p>"""
    combination: NotRequired[
        "aws_sdk_deadline.types.combination_expression.CombinationExpression"
    ]
    """<p>The combination expression to use in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSpace) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.step_parameter_list

    out["parameters"] = aws_sdk_deadline.types.step_parameter_list.serialize_json(
        value["parameters"]
    )
    if "combination" in value:
        out["combination"] = value["combination"]
    return out


def deserialize_json(data: dict) -> ParameterSpace:
    out: ParameterSpace = {}  # type: ignore[typeddict-item]
    if "parameters" in data:
        import aws_sdk_deadline.types.step_parameter_list

        out["parameters"] = aws_sdk_deadline.types.step_parameter_list.deserialize_json(
            data["parameters"]
        )
    else:
        raise DeserializationError("ParameterSpace.parameters required")
    if "combination" in data:
        out["combination"] = data["combination"]
    return out
