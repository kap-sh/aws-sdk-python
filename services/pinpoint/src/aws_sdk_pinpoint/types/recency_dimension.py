"""Generated from Smithy shape ``com.amazonaws.pinpoint#RecencyDimension``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.duration
    import aws_sdk_pinpoint.types.recency_type


class RecencyDimension(TypedDict):
    duration: NotRequired["aws_sdk_pinpoint.types.duration.Duration"]
    """<p>The duration to use when determining whether an endpoint is active or inactive.</p>"""
    recency_type: NotRequired["aws_sdk_pinpoint.types.recency_type.RecencyType"]
    """<p>The type of recency dimension to use for the segment. Valid values are: ACTIVE, endpoints that were active within the specified duration are included in the segment; and, INACTIVE, endpoints that weren't active within the specified duration are included in the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecencyDimension) -> dict:
    out: dict = {}
    if "duration" in value:
        import aws_sdk_pinpoint.types.duration

        out["Duration"] = aws_sdk_pinpoint.types.duration.serialize_json(
            value["duration"]
        )
    if "recency_type" in value:
        import aws_sdk_pinpoint.types.recency_type

        out["RecencyType"] = aws_sdk_pinpoint.types.recency_type.serialize_json(
            value["recency_type"]
        )
    return out


def deserialize_json(data: dict) -> RecencyDimension:
    out: RecencyDimension = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        import aws_sdk_pinpoint.types.duration

        out["duration"] = aws_sdk_pinpoint.types.duration.deserialize_json(
            data["Duration"]
        )
    if "RecencyType" in data:
        import aws_sdk_pinpoint.types.recency_type

        out["recency_type"] = aws_sdk_pinpoint.types.recency_type.deserialize_json(
            data["RecencyType"]
        )
    return out
