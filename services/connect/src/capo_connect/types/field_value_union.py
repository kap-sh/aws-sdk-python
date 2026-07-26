"""Generated from Smithy shape ``com.amazonaws.connect#FieldValueUnion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.double
    import capo_connect.types.empty_field_value
    import capo_connect.types.field_string_value


class FieldValueUnion(TypedDict, closed=True):
    boolean_value: "capo_connect.types.boolean.Boolean"
    """<p>A Boolean number value type.</p>"""
    double_value: NotRequired["capo_connect.types.double.Double"]
    """<p>A Double number value type.</p>"""
    empty_value: NotRequired["capo_connect.types.empty_field_value.EmptyFieldValue"]
    """<p>An empty value.</p>"""
    string_value: NotRequired["capo_connect.types.field_string_value.FieldStringValue"]
    """<p>String value type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueUnion) -> dict:
    out: dict = {}
    out["BooleanValue"] = value.get("boolean_value", False)
    if "double_value" in value:
        out["DoubleValue"] = value["double_value"]
    if "empty_value" in value:
        import capo_connect.types.empty_field_value

        out["EmptyValue"] = capo_connect.types.empty_field_value.serialize_json(
            value["empty_value"]
        )
    if "string_value" in value:
        out["StringValue"] = value["string_value"]
    return out


def deserialize_json(data: dict) -> FieldValueUnion:
    out: FieldValueUnion = {}  # type: ignore[typeddict-item]
    if "BooleanValue" in data:
        out["boolean_value"] = data["BooleanValue"]
    else:
        out["boolean_value"] = False
    if "DoubleValue" in data:
        out["double_value"] = data["DoubleValue"]
    if "EmptyValue" in data:
        import capo_connect.types.empty_field_value

        out["empty_value"] = capo_connect.types.empty_field_value.deserialize_json(
            data["EmptyValue"]
        )
    if "StringValue" in data:
        out["string_value"] = data["StringValue"]
    return out
