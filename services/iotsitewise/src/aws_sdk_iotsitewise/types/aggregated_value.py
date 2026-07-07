"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregatedValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.aggregates
    import aws_sdk_iotsitewise.types.quality
    import aws_sdk_iotsitewise.types.timestamp


class AggregatedValue(TypedDict, closed=True):
    timestamp: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the aggregating computations occurred, in Unix epoch time.</p>"""
    quality: NotRequired["aws_sdk_iotsitewise.types.quality.Quality"]
    """<p>The quality of the aggregated data.</p>"""
    value: "aws_sdk_iotsitewise.types.aggregates.Aggregates"
    """<p>The value of the aggregates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedValue) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.timestamp

    out["timestamp"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["timestamp"]
    )
    if "quality" in value:
        import aws_sdk_iotsitewise.types.quality

        out["quality"] = aws_sdk_iotsitewise.types.quality.serialize_json(
            value["quality"]
        )
    import aws_sdk_iotsitewise.types.aggregates

    out["value"] = aws_sdk_iotsitewise.types.aggregates.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> AggregatedValue:
    out: AggregatedValue = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["timestamp"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("AggregatedValue.timestamp required")
    if "quality" in data:
        import aws_sdk_iotsitewise.types.quality

        out["quality"] = aws_sdk_iotsitewise.types.quality.deserialize_json(
            data["quality"]
        )
    if "value" in data:
        import aws_sdk_iotsitewise.types.aggregates

        out["value"] = aws_sdk_iotsitewise.types.aggregates.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("AggregatedValue.value required")
    return out
