"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PolygonGeometryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.linear_rings


class PolygonGeometryInput(TypedDict):
    coordinates: "aws_sdk_sagemaker_geospatial.types.linear_rings.LinearRings"
    """<p>Coordinates representing a Polygon based on the <a href=\"https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6\">GeoJson spec</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolygonGeometryInput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.linear_rings

    out["Coordinates"] = aws_sdk_sagemaker_geospatial.types.linear_rings.serialize_json(
        value["coordinates"]
    )
    return out


def deserialize_json(data: dict) -> PolygonGeometryInput:
    out: PolygonGeometryInput = {}  # type: ignore[typeddict-item]
    if "Coordinates" in data:
        import aws_sdk_sagemaker_geospatial.types.linear_rings

        out["coordinates"] = (
            aws_sdk_sagemaker_geospatial.types.linear_rings.deserialize_json(
                data["Coordinates"]
            )
        )
    else:
        raise DeserializationError("PolygonGeometryInput.coordinates required")
    return out
