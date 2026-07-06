"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetPropertyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.quality
    import aws_sdk_iotsitewise.types.time_in_nanos
    import aws_sdk_iotsitewise.types.variant


class AssetPropertyValue(TypedDict, closed=True):
    value: "aws_sdk_iotsitewise.types.variant.Variant"
    """<p>The value of the asset property (see <code>Variant</code>).</p>"""
    timestamp: "aws_sdk_iotsitewise.types.time_in_nanos.TimeInNanos"
    """<p>The timestamp of the asset property value.</p>"""
    quality: NotRequired["aws_sdk_iotsitewise.types.quality.Quality"]
    """<p>The quality of the asset property value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyValue) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.variant

    out["value"] = aws_sdk_iotsitewise.types.variant.serialize_json(value["value"])
    import aws_sdk_iotsitewise.types.time_in_nanos

    out["timestamp"] = aws_sdk_iotsitewise.types.time_in_nanos.serialize_json(
        value["timestamp"]
    )
    if "quality" in value:
        import aws_sdk_iotsitewise.types.quality

        out["quality"] = aws_sdk_iotsitewise.types.quality.serialize_json(
            value["quality"]
        )
    return out


def deserialize_json(data: dict) -> AssetPropertyValue:
    out: AssetPropertyValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_iotsitewise.types.variant

        out["value"] = aws_sdk_iotsitewise.types.variant.deserialize_json(data["value"])
    else:
        raise DeserializationError("AssetPropertyValue.value required")
    if "timestamp" in data:
        import aws_sdk_iotsitewise.types.time_in_nanos

        out["timestamp"] = aws_sdk_iotsitewise.types.time_in_nanos.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("AssetPropertyValue.timestamp required")
    if "quality" in data:
        import aws_sdk_iotsitewise.types.quality

        out["quality"] = aws_sdk_iotsitewise.types.quality.deserialize_json(
            data["quality"]
        )
    return out
