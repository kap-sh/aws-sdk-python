"""Generated from Smithy shape ``com.amazonaws.glacier#SelectParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.expression_type
    import capo_glacier.types.input_serialization
    import capo_glacier.types.output_serialization
    import capo_glacier.types.string


class SelectParameters(TypedDict, closed=True):
    input_serialization: NotRequired[
        "capo_glacier.types.input_serialization.InputSerialization"
    ]
    """<p>Describes the serialization format of the object.</p>"""
    expression_type: NotRequired["capo_glacier.types.expression_type.ExpressionType"]
    """<p>The type of the provided expression, for example <code>SQL</code>.</p>"""
    expression: NotRequired["capo_glacier.types.string.string"]
    """<p>The expression that is used to select the object.</p>"""
    output_serialization: NotRequired[
        "capo_glacier.types.output_serialization.OutputSerialization"
    ]
    """<p>Describes how the results of the select job are serialized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectParameters) -> dict:
    out: dict = {}
    if "input_serialization" in value:
        import capo_glacier.types.input_serialization

        out["InputSerialization"] = (
            capo_glacier.types.input_serialization.serialize_json(
                value["input_serialization"]
            )
        )
    if "expression_type" in value:
        import capo_glacier.types.expression_type

        out["ExpressionType"] = capo_glacier.types.expression_type.serialize_json(
            value["expression_type"]
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "output_serialization" in value:
        import capo_glacier.types.output_serialization

        out["OutputSerialization"] = (
            capo_glacier.types.output_serialization.serialize_json(
                value["output_serialization"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectParameters:
    out: SelectParameters = {}  # type: ignore[typeddict-item]
    if "InputSerialization" in data:
        import capo_glacier.types.input_serialization

        out["input_serialization"] = (
            capo_glacier.types.input_serialization.deserialize_json(
                data["InputSerialization"]
            )
        )
    if "ExpressionType" in data:
        import capo_glacier.types.expression_type

        out["expression_type"] = capo_glacier.types.expression_type.deserialize_json(
            data["ExpressionType"]
        )
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "OutputSerialization" in data:
        import capo_glacier.types.output_serialization

        out["output_serialization"] = (
            capo_glacier.types.output_serialization.deserialize_json(
                data["OutputSerialization"]
            )
        )
    return out
