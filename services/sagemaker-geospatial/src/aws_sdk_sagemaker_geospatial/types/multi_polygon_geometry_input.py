"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#MultiPolygonGeometryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.linear_rings_list


class MultiPolygonGeometryInput(TypedDict):
    coordinates: "aws_sdk_sagemaker_geospatial.types.linear_rings_list.LinearRingsList"
    """<p>The coordinates of the multipolygon geometry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiPolygonGeometryInput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.linear_rings_list

    out["Coordinates"] = (
        aws_sdk_sagemaker_geospatial.types.linear_rings_list.serialize_json(
            value["coordinates"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiPolygonGeometryInput:
    out: MultiPolygonGeometryInput = {}  # type: ignore[typeddict-item]
    if "Coordinates" in data:
        import aws_sdk_sagemaker_geospatial.types.linear_rings_list

        out["coordinates"] = (
            aws_sdk_sagemaker_geospatial.types.linear_rings_list.deserialize_json(
                data["Coordinates"]
            )
        )
    else:
        raise DeserializationError("MultiPolygonGeometryInput.coordinates required")
    return out
