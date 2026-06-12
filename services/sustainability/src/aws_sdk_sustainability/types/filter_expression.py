"""Generated from Smithy shape ``com.amazonaws.sustainability#FilterExpression``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension_list_map


class FilterExpression(TypedDict):
    dimensions: NotRequired[
        "aws_sdk_sustainability.types.dimension_list_map.DimensionListMap"
    ]
    """<p>Filters emission values by specific dimension values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterExpression) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_sustainability.types.dimension_list_map

        out["Dimensions"] = (
            aws_sdk_sustainability.types.dimension_list_map.serialize_json(
                value["dimensions"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterExpression:
    out: FilterExpression = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_sustainability.types.dimension_list_map

        out["dimensions"] = (
            aws_sdk_sustainability.types.dimension_list_map.deserialize_json(
                data["Dimensions"]
            )
        )
    return out
