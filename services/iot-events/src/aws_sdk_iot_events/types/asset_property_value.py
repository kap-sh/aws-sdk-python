"""Generated from Smithy shape ``com.amazonaws.iotevents#AssetPropertyValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.asset_property_quality
    import aws_sdk_iot_events.types.asset_property_timestamp
    import aws_sdk_iot_events.types.asset_property_variant


class AssetPropertyValue(TypedDict):
    value: NotRequired[
        "aws_sdk_iot_events.types.asset_property_variant.AssetPropertyVariant"
    ]
    """<p>The value to send to an asset property.</p>"""
    timestamp: NotRequired[
        "aws_sdk_iot_events.types.asset_property_timestamp.AssetPropertyTimestamp"
    ]
    """<p>The timestamp associated with the asset property value. The default is the current event time.</p>"""
    quality: NotRequired[
        "aws_sdk_iot_events.types.asset_property_quality.AssetPropertyQuality"
    ]
    """<p>The quality of the asset property value. The value must be <code>'GOOD'</code>, <code>'BAD'</code>, or <code>'UNCERTAIN'</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyValue) -> dict:
    out: dict = {}
    if "value" in value:
        import aws_sdk_iot_events.types.asset_property_variant

        out["value"] = aws_sdk_iot_events.types.asset_property_variant.serialize_json(
            value["value"]
        )
    if "timestamp" in value:
        import aws_sdk_iot_events.types.asset_property_timestamp

        out["timestamp"] = (
            aws_sdk_iot_events.types.asset_property_timestamp.serialize_json(
                value["timestamp"]
            )
        )
    if "quality" in value:
        out["quality"] = value["quality"]
    return out


def deserialize_json(data: dict) -> AssetPropertyValue:
    out: AssetPropertyValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_iot_events.types.asset_property_variant

        out["value"] = aws_sdk_iot_events.types.asset_property_variant.deserialize_json(
            data["value"]
        )
    if "timestamp" in data:
        import aws_sdk_iot_events.types.asset_property_timestamp

        out["timestamp"] = (
            aws_sdk_iot_events.types.asset_property_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    if "quality" in data:
        out["quality"] = data["quality"]
    return out
