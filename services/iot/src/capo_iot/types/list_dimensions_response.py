"""Generated from Smithy shape ``com.amazonaws.iot#ListDimensionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.dimension_names
    import capo_iot.types.next_token


class ListDimensionsResponse(TypedDict, closed=True):
    dimension_names: NotRequired["capo_iot.types.dimension_names.DimensionNames"]
    """<p>A list of the names of the defined dimensions. Use <code>DescribeDimension</code> to get details for a dimension.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDimensionsResponse) -> dict:
    out: dict = {}
    if "dimension_names" in value:
        import capo_iot.types.dimension_names

        out["dimensionNames"] = capo_iot.types.dimension_names.serialize_json(
            value["dimension_names"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDimensionsResponse:
    out: ListDimensionsResponse = {}  # type: ignore[typeddict-item]
    if "dimensionNames" in data:
        import capo_iot.types.dimension_names

        out["dimension_names"] = capo_iot.types.dimension_names.deserialize_json(
            data["dimensionNames"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
