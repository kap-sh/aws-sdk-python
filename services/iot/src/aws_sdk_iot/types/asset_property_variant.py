"""Generated from Smithy shape ``com.amazonaws.iot#AssetPropertyVariant``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iot.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.asset_property_boolean_value
    import aws_sdk_iot.types.asset_property_double_value
    import aws_sdk_iot.types.asset_property_integer_value
    import aws_sdk_iot.types.asset_property_string_value


class _AssetPropertyVariant_stringValue(TypedDict):
    stringValue: (
        "aws_sdk_iot.types.asset_property_string_value.AssetPropertyStringValue"
    )


class _AssetPropertyVariant_integerValue(TypedDict):
    integerValue: (
        "aws_sdk_iot.types.asset_property_integer_value.AssetPropertyIntegerValue"
    )


class _AssetPropertyVariant_doubleValue(TypedDict):
    doubleValue: (
        "aws_sdk_iot.types.asset_property_double_value.AssetPropertyDoubleValue"
    )


class _AssetPropertyVariant_booleanValue(TypedDict):
    booleanValue: (
        "aws_sdk_iot.types.asset_property_boolean_value.AssetPropertyBooleanValue"
    )


AssetPropertyVariant: TypeAlias = (
    _AssetPropertyVariant_stringValue
    | _AssetPropertyVariant_integerValue
    | _AssetPropertyVariant_doubleValue
    | _AssetPropertyVariant_booleanValue
)


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyVariant) -> dict:
    if "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "integerValue" in value:
        return {"integerValue": value["integerValue"]}
    elif "doubleValue" in value:
        return {"doubleValue": value["doubleValue"]}
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    else:
        raise SerializationError("AssetPropertyVariant: no variant present")


def deserialize_json(data: dict) -> AssetPropertyVariant:
    if "stringValue" in data:
        return {"stringValue": data["stringValue"]}
    elif "integerValue" in data:
        return {"integerValue": data["integerValue"]}
    elif "doubleValue" in data:
        return {"doubleValue": data["doubleValue"]}
    elif "booleanValue" in data:
        return {"booleanValue": data["booleanValue"]}
    else:
        raise DeserializationError("AssetPropertyVariant: no recognized variant key")
