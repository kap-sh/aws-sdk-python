"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Variant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.property_value_boolean_value
    import aws_sdk_iotsitewise.types.property_value_double_value
    import aws_sdk_iotsitewise.types.property_value_integer_value
    import aws_sdk_iotsitewise.types.property_value_null_value
    import aws_sdk_iotsitewise.types.property_value_string_value


class Variant(TypedDict):
    string_value: NotRequired[
        "aws_sdk_iotsitewise.types.property_value_string_value.PropertyValueStringValue"
    ]
    """<p> Asset property data of type string (sequence of characters). The allowed pattern: \"^$|[^\u0000-\u001f\u007f]+\". The max length is 1024. </p>"""
    integer_value: NotRequired[
        "aws_sdk_iotsitewise.types.property_value_integer_value.PropertyValueIntegerValue"
    ]
    """<p>Asset property data of type integer (whole number).</p>"""
    double_value: NotRequired[
        "aws_sdk_iotsitewise.types.property_value_double_value.PropertyValueDoubleValue"
    ]
    """<p> Asset property data of type double (floating point number). The min value is -10^10. The max value is 10^10. Double.NaN is allowed. </p>"""
    boolean_value: NotRequired[
        "aws_sdk_iotsitewise.types.property_value_boolean_value.PropertyValueBooleanValue"
    ]
    """<p>Asset property data of type Boolean (true or false).</p>"""
    null_value: NotRequired[
        "aws_sdk_iotsitewise.types.property_value_null_value.PropertyValueNullValue"
    ]
    """<p>The type of null asset property data with BAD and UNCERTAIN qualities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Variant) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "integer_value" in value:
        out["integerValue"] = value["integer_value"]
    if "double_value" in value:
        out["doubleValue"] = value["double_value"]
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    if "null_value" in value:
        import aws_sdk_iotsitewise.types.property_value_null_value

        out["nullValue"] = (
            aws_sdk_iotsitewise.types.property_value_null_value.serialize_json(
                value["null_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> Variant:
    out: Variant = {}  # type: ignore[typeddict-item]
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    if "integerValue" in data:
        out["integer_value"] = data["integerValue"]
    if "doubleValue" in data:
        out["double_value"] = data["doubleValue"]
    if "booleanValue" in data:
        out["boolean_value"] = data["booleanValue"]
    if "nullValue" in data:
        import aws_sdk_iotsitewise.types.property_value_null_value

        out["null_value"] = (
            aws_sdk_iotsitewise.types.property_value_null_value.deserialize_json(
                data["nullValue"]
            )
        )
    return out
