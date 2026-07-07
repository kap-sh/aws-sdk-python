"""Generated from Smithy shape ``com.amazonaws.iot#AssetPropertyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.asset_property_quality
    import aws_sdk_iot.types.asset_property_timestamp
    import aws_sdk_iot.types.asset_property_variant


class AssetPropertyValue(TypedDict, closed=True):
    value: "aws_sdk_iot.types.asset_property_variant.AssetPropertyVariant"
    """<p>The value of the asset property.</p>"""
    timestamp: "aws_sdk_iot.types.asset_property_timestamp.AssetPropertyTimestamp"
    """<p>The asset property value timestamp.</p>"""
    quality: NotRequired[
        "aws_sdk_iot.types.asset_property_quality.AssetPropertyQuality"
    ]
    """<p>Optional. A string that describes the quality of the value. Accepts substitution templates. Must be <code>GOOD</code>, <code>BAD</code>, or <code>UNCERTAIN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyValue) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.asset_property_variant

    out["value"] = aws_sdk_iot.types.asset_property_variant.serialize_json(
        value["value"]
    )
    import aws_sdk_iot.types.asset_property_timestamp

    out["timestamp"] = aws_sdk_iot.types.asset_property_timestamp.serialize_json(
        value["timestamp"]
    )
    if "quality" in value:
        out["quality"] = value["quality"]
    return out


def deserialize_json(data: dict) -> AssetPropertyValue:
    out: AssetPropertyValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_iot.types.asset_property_variant

        out["value"] = aws_sdk_iot.types.asset_property_variant.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("AssetPropertyValue.value required")
    if "timestamp" in data:
        import aws_sdk_iot.types.asset_property_timestamp

        out["timestamp"] = aws_sdk_iot.types.asset_property_timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("AssetPropertyValue.timestamp required")
    if "quality" in data:
        out["quality"] = data["quality"]
    return out
