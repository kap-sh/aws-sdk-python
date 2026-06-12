"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.data_type
    import aws_sdk_iottwinmaker.types.data_value_list
    import aws_sdk_iottwinmaker.types.relationship
    import aws_sdk_iottwinmaker.types.string
    import aws_sdk_iottwinmaker.types.type


class DataType(TypedDict):
    type: "aws_sdk_iottwinmaker.types.type.Type"
    """<p>The underlying type of the data type.</p>"""
    nested_type: NotRequired["aws_sdk_iottwinmaker.types.data_type.DataType"]
    """<p>The nested type in the data type.</p>"""
    allowed_values: NotRequired[
        "aws_sdk_iottwinmaker.types.data_value_list.DataValueList"
    ]
    """<p>The allowed values for this data type.</p>"""
    unit_of_measure: NotRequired["aws_sdk_iottwinmaker.types.string.String"]
    """<p>The unit of measure used in this data type.</p>"""
    relationship: NotRequired["aws_sdk_iottwinmaker.types.relationship.Relationship"]
    """<p>A relationship that associates a component with another component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataType) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "nested_type" in value:
        import aws_sdk_iottwinmaker.types.data_type

        out["nestedType"] = aws_sdk_iottwinmaker.types.data_type.serialize_json(
            value["nested_type"]
        )
    if "allowed_values" in value:
        import aws_sdk_iottwinmaker.types.data_value_list

        out["allowedValues"] = (
            aws_sdk_iottwinmaker.types.data_value_list.serialize_json(
                value["allowed_values"]
            )
        )
    if "unit_of_measure" in value:
        out["unitOfMeasure"] = value["unit_of_measure"]
    if "relationship" in value:
        import aws_sdk_iottwinmaker.types.relationship

        out["relationship"] = aws_sdk_iottwinmaker.types.relationship.serialize_json(
            value["relationship"]
        )
    return out


def deserialize_json(data: dict) -> DataType:
    out: DataType = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("DataType.type required")
    if "nestedType" in data:
        import aws_sdk_iottwinmaker.types.data_type

        out["nested_type"] = aws_sdk_iottwinmaker.types.data_type.deserialize_json(
            data["nestedType"]
        )
    if "allowedValues" in data:
        import aws_sdk_iottwinmaker.types.data_value_list

        out["allowed_values"] = (
            aws_sdk_iottwinmaker.types.data_value_list.deserialize_json(
                data["allowedValues"]
            )
        )
    if "unitOfMeasure" in data:
        out["unit_of_measure"] = data["unitOfMeasure"]
    if "relationship" in data:
        import aws_sdk_iottwinmaker.types.relationship

        out["relationship"] = aws_sdk_iottwinmaker.types.relationship.deserialize_json(
            data["relationship"]
        )
    return out
