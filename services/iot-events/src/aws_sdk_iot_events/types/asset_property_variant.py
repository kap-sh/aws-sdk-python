"""Generated from Smithy shape ``com.amazonaws.iotevents#AssetPropertyVariant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.asset_property_boolean_value
    import aws_sdk_iot_events.types.asset_property_double_value
    import aws_sdk_iot_events.types.asset_property_integer_value
    import aws_sdk_iot_events.types.asset_property_string_value


class AssetPropertyVariant(TypedDict):
    string_value: NotRequired[
        "aws_sdk_iot_events.types.asset_property_string_value.AssetPropertyStringValue"
    ]
    """<p>The asset property value is a string. You must use an expression, and the evaluated result should be a string.</p>"""
    integer_value: NotRequired[
        "aws_sdk_iot_events.types.asset_property_integer_value.AssetPropertyIntegerValue"
    ]
    """<p>The asset property value is an integer. You must use an expression, and the evaluated result should be an integer.</p>"""
    double_value: NotRequired[
        "aws_sdk_iot_events.types.asset_property_double_value.AssetPropertyDoubleValue"
    ]
    """<p>The asset property value is a double. You must use an expression, and the evaluated result should be a double.</p>"""
    boolean_value: NotRequired[
        "aws_sdk_iot_events.types.asset_property_boolean_value.AssetPropertyBooleanValue"
    ]
    """<p>The asset property value is a Boolean value that must be <code>'TRUE'</code> or <code>'FALSE'</code>. You must use an expression, and the evaluated result should be a Boolean value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyVariant) -> dict:
    out: dict = {}
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "integer_value" in value:
        out["integerValue"] = value["integer_value"]
    if "double_value" in value:
        out["doubleValue"] = value["double_value"]
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    return out


def deserialize_json(data: dict) -> AssetPropertyVariant:
    out: AssetPropertyVariant = {}  # type: ignore[typeddict-item]
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    if "integerValue" in data:
        out["integer_value"] = data["integerValue"]
    if "doubleValue" in data:
        out["double_value"] = data["doubleValue"]
    if "booleanValue" in data:
        out["boolean_value"] = data["booleanValue"]
    return out
