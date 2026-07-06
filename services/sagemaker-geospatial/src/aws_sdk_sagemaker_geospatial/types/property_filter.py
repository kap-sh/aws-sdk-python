"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PropertyFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.property


class PropertyFilter(TypedDict, closed=True):
    property: "aws_sdk_sagemaker_geospatial.types.property.Property"
    """<p>Represents a single property to match with when searching a raster data collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyFilter) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.property

    out["Property"] = aws_sdk_sagemaker_geospatial.types.property.serialize_json(
        value["property"]
    )
    return out


def deserialize_json(data: dict) -> PropertyFilter:
    out: PropertyFilter = {}  # type: ignore[typeddict-item]
    if "Property" in data:
        import aws_sdk_sagemaker_geospatial.types.property

        out["property"] = aws_sdk_sagemaker_geospatial.types.property.deserialize_json(
            data["Property"]
        )
    else:
        raise DeserializationError("PropertyFilter.property required")
    return out
