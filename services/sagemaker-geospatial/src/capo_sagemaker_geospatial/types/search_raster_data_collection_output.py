"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#SearchRasterDataCollectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.item_source_list
    import capo_sagemaker_geospatial.types.next_token


class SearchRasterDataCollectionOutput(TypedDict, closed=True):
    approximate_result_count: "int"
    """<p>Approximate number of results in the response.</p>"""
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""
    items: NotRequired[
        "capo_sagemaker_geospatial.types.item_source_list.ItemSourceList"
    ]
    """<p>List of items matching the Raster DataCollectionQuery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRasterDataCollectionOutput) -> dict:
    out: dict = {}
    out["ApproximateResultCount"] = value["approximate_result_count"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "items" in value:
        import capo_sagemaker_geospatial.types.item_source_list

        out["Items"] = capo_sagemaker_geospatial.types.item_source_list.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> SearchRasterDataCollectionOutput:
    out: SearchRasterDataCollectionOutput = {}  # type: ignore[typeddict-item]
    if "ApproximateResultCount" in data:
        out["approximate_result_count"] = data["ApproximateResultCount"]
    else:
        raise DeserializationError(
            "SearchRasterDataCollectionOutput.approximate_result_count required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Items" in data:
        import capo_sagemaker_geospatial.types.item_source_list

        out["items"] = (
            capo_sagemaker_geospatial.types.item_source_list.deserialize_json(
                data["Items"]
            )
        )
    return out
