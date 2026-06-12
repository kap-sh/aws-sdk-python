"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.data_value_list
    import aws_sdk_iottwinmaker.types.data_value_map
    import aws_sdk_iottwinmaker.types.double
    import aws_sdk_iottwinmaker.types.expression
    import aws_sdk_iottwinmaker.types.integer
    import aws_sdk_iottwinmaker.types.long
    import aws_sdk_iottwinmaker.types.relationship_value
    import aws_sdk_iottwinmaker.types.string


class DataValue(TypedDict):
    boolean_value: NotRequired["aws_sdk_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value.</p>"""
    double_value: NotRequired["aws_sdk_iottwinmaker.types.double.Double"]
    """<p>A double value.</p>"""
    integer_value: NotRequired["aws_sdk_iottwinmaker.types.integer.Integer"]
    """<p>An integer value.</p>"""
    long_value: NotRequired["aws_sdk_iottwinmaker.types.long.Long"]
    """<p>A long value.</p>"""
    string_value: NotRequired["aws_sdk_iottwinmaker.types.string.String"]
    """<p>A string value.</p>"""
    list_value: NotRequired["aws_sdk_iottwinmaker.types.data_value_list.DataValueList"]
    """<p>A list of multiple values.</p>"""
    map_value: NotRequired["aws_sdk_iottwinmaker.types.data_value_map.DataValueMap"]
    """<p>An object that maps strings to multiple <code>DataValue</code> objects.</p>"""
    relationship_value: NotRequired[
        "aws_sdk_iottwinmaker.types.relationship_value.RelationshipValue"
    ]
    """<p>A value that relates a component to another component.</p>"""
    expression: NotRequired["aws_sdk_iottwinmaker.types.expression.Expression"]
    """<p>An expression that produces the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataValue) -> dict:
    out: dict = {}
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    if "double_value" in value:
        out["doubleValue"] = value["double_value"]
    if "integer_value" in value:
        out["integerValue"] = value["integer_value"]
    if "long_value" in value:
        out["longValue"] = value["long_value"]
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "list_value" in value:
        import aws_sdk_iottwinmaker.types.data_value_list

        out["listValue"] = aws_sdk_iottwinmaker.types.data_value_list.serialize_json(
            value["list_value"]
        )
    if "map_value" in value:
        import aws_sdk_iottwinmaker.types.data_value_map

        out["mapValue"] = aws_sdk_iottwinmaker.types.data_value_map.serialize_json(
            value["map_value"]
        )
    if "relationship_value" in value:
        import aws_sdk_iottwinmaker.types.relationship_value

        out["relationshipValue"] = (
            aws_sdk_iottwinmaker.types.relationship_value.serialize_json(
                value["relationship_value"]
            )
        )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> DataValue:
    out: DataValue = {}  # type: ignore[typeddict-item]
    if "booleanValue" in data:
        out["boolean_value"] = data["booleanValue"]
    if "doubleValue" in data:
        out["double_value"] = data["doubleValue"]
    if "integerValue" in data:
        out["integer_value"] = data["integerValue"]
    if "longValue" in data:
        out["long_value"] = data["longValue"]
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    if "listValue" in data:
        import aws_sdk_iottwinmaker.types.data_value_list

        out["list_value"] = aws_sdk_iottwinmaker.types.data_value_list.deserialize_json(
            data["listValue"]
        )
    if "mapValue" in data:
        import aws_sdk_iottwinmaker.types.data_value_map

        out["map_value"] = aws_sdk_iottwinmaker.types.data_value_map.deserialize_json(
            data["mapValue"]
        )
    if "relationshipValue" in data:
        import aws_sdk_iottwinmaker.types.relationship_value

        out["relationship_value"] = (
            aws_sdk_iottwinmaker.types.relationship_value.deserialize_json(
                data["relationshipValue"]
            )
        )
    if "expression" in data:
        out["expression"] = data["expression"]
    return out
