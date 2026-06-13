"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListRasterDataCollectionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.data_collections_list
    import aws_sdk_sagemaker_geospatial.types.next_token


class ListRasterDataCollectionsOutput(TypedDict):
    raster_data_collection_summaries: (
        "aws_sdk_sagemaker_geospatial.types.data_collections_list.DataCollectionsList"
    )
    """<p>Contains summary information about the raster data collection.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRasterDataCollectionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.data_collections_list

    out["RasterDataCollectionSummaries"] = (
        aws_sdk_sagemaker_geospatial.types.data_collections_list.serialize_json(
            value["raster_data_collection_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRasterDataCollectionsOutput:
    out: ListRasterDataCollectionsOutput = {}  # type: ignore[typeddict-item]
    if "RasterDataCollectionSummaries" in data:
        import aws_sdk_sagemaker_geospatial.types.data_collections_list

        out["raster_data_collection_summaries"] = (
            aws_sdk_sagemaker_geospatial.types.data_collections_list.deserialize_json(
                data["RasterDataCollectionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListRasterDataCollectionsOutput.raster_data_collection_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
