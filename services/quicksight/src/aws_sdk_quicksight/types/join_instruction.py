"""Generated from Smithy shape ``com.amazonaws.quicksight#JoinInstruction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.join_key_properties
    import aws_sdk_quicksight.types.join_type
    import aws_sdk_quicksight.types.logical_table_id
    import aws_sdk_quicksight.types.on_clause


class JoinInstruction(TypedDict, closed=True):
    left_operand: "aws_sdk_quicksight.types.logical_table_id.LogicalTableId"
    """<p>The operand on the left side of a join.</p>"""
    right_operand: "aws_sdk_quicksight.types.logical_table_id.LogicalTableId"
    """<p>The operand on the right side of a join.</p>"""
    left_join_key_properties: NotRequired[
        "aws_sdk_quicksight.types.join_key_properties.JoinKeyProperties"
    ]
    """<p>Join key properties of the left operand.</p>"""
    right_join_key_properties: NotRequired[
        "aws_sdk_quicksight.types.join_key_properties.JoinKeyProperties"
    ]
    """<p>Join key properties of the right operand.</p>"""
    type: "aws_sdk_quicksight.types.join_type.JoinType"
    """<p>The type of join that it is.</p>"""
    on_clause: "aws_sdk_quicksight.types.on_clause.OnClause"
    """<p>The join instructions provided in the <code>ON</code> clause of a join.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinInstruction) -> dict:
    out: dict = {}
    out["LeftOperand"] = value["left_operand"]
    out["RightOperand"] = value["right_operand"]
    if "left_join_key_properties" in value:
        import aws_sdk_quicksight.types.join_key_properties

        out["LeftJoinKeyProperties"] = (
            aws_sdk_quicksight.types.join_key_properties.serialize_json(
                value["left_join_key_properties"]
            )
        )
    if "right_join_key_properties" in value:
        import aws_sdk_quicksight.types.join_key_properties

        out["RightJoinKeyProperties"] = (
            aws_sdk_quicksight.types.join_key_properties.serialize_json(
                value["right_join_key_properties"]
            )
        )
    import aws_sdk_quicksight.types.join_type

    out["Type"] = aws_sdk_quicksight.types.join_type.serialize_json(value["type"])
    out["OnClause"] = value["on_clause"]
    return out


def deserialize_json(data: dict) -> JoinInstruction:
    out: JoinInstruction = {}  # type: ignore[typeddict-item]
    if "LeftOperand" in data:
        out["left_operand"] = data["LeftOperand"]
    else:
        raise DeserializationError("JoinInstruction.left_operand required")
    if "RightOperand" in data:
        out["right_operand"] = data["RightOperand"]
    else:
        raise DeserializationError("JoinInstruction.right_operand required")
    if "LeftJoinKeyProperties" in data:
        import aws_sdk_quicksight.types.join_key_properties

        out["left_join_key_properties"] = (
            aws_sdk_quicksight.types.join_key_properties.deserialize_json(
                data["LeftJoinKeyProperties"]
            )
        )
    if "RightJoinKeyProperties" in data:
        import aws_sdk_quicksight.types.join_key_properties

        out["right_join_key_properties"] = (
            aws_sdk_quicksight.types.join_key_properties.deserialize_json(
                data["RightJoinKeyProperties"]
            )
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.join_type

        out["type"] = aws_sdk_quicksight.types.join_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("JoinInstruction.type required")
    if "OnClause" in data:
        out["on_clause"] = data["OnClause"]
    else:
        raise DeserializationError("JoinInstruction.on_clause required")
    return out
