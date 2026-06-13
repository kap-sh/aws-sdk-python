"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapStyleOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.base_map_style_type


class GeospatialMapStyleOptions(TypedDict):
    base_map_style: NotRequired[
        "aws_sdk_quicksight.types.base_map_style_type.BaseMapStyleType"
    ]
    """<p>The base map style of the geospatial map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapStyleOptions) -> dict:
    out: dict = {}
    if "base_map_style" in value:
        import aws_sdk_quicksight.types.base_map_style_type

        out["BaseMapStyle"] = (
            aws_sdk_quicksight.types.base_map_style_type.serialize_json(
                value["base_map_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapStyleOptions:
    out: GeospatialMapStyleOptions = {}  # type: ignore[typeddict-item]
    if "BaseMapStyle" in data:
        import aws_sdk_quicksight.types.base_map_style_type

        out["base_map_style"] = (
            aws_sdk_quicksight.types.base_map_style_type.deserialize_json(
                data["BaseMapStyle"]
            )
        )
    return out
