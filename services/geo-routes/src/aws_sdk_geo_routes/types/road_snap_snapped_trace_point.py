"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapSnappedTracePoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.sensitive_double


class RoadSnapSnappedTracePoint(TypedDict):
    confidence: "aws_sdk_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Confidence value for the correctness of this point match.</p>"""
    original_position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position of the TracePoint provided within the request, at the same index.</p>"""
    snapped_position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Snapped position of the TracePoint provided within the request, at the same index. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapSnappedTracePoint) -> dict:
    out: dict = {}
    out["Confidence"] = value["confidence"]
    import aws_sdk_geo_routes.types.position

    out["OriginalPosition"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["original_position"]
    )
    import aws_sdk_geo_routes.types.position

    out["SnappedPosition"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["snapped_position"]
    )
    return out


def deserialize_json(data: dict) -> RoadSnapSnappedTracePoint:
    out: RoadSnapSnappedTracePoint = {}  # type: ignore[typeddict-item]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    else:
        raise DeserializationError("RoadSnapSnappedTracePoint.confidence required")
    if "OriginalPosition" in data:
        import aws_sdk_geo_routes.types.position

        out["original_position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["OriginalPosition"]
        )
    else:
        raise DeserializationError(
            "RoadSnapSnappedTracePoint.original_position required"
        )
    if "SnappedPosition" in data:
        import aws_sdk_geo_routes.types.position

        out["snapped_position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["SnappedPosition"]
        )
    else:
        raise DeserializationError(
            "RoadSnapSnappedTracePoint.snapped_position required"
        )
    return out
