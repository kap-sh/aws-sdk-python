"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#RasterDataCollectionQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.area_of_interest
    import aws_sdk_sagemaker_geospatial.types.data_collection_arn
    import aws_sdk_sagemaker_geospatial.types.property_filters
    import aws_sdk_sagemaker_geospatial.types.time_range_filter_output


class RasterDataCollectionQueryOutput(TypedDict, closed=True):
    raster_data_collection_arn: (
        "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    )
    """<p>The ARN of the Raster Data Collection against which the search is done.</p>"""
    raster_data_collection_name: "str"
    """<p>The name of the raster data collection.</p>"""
    time_range_filter: "aws_sdk_sagemaker_geospatial.types.time_range_filter_output.TimeRangeFilterOutput"
    """<p>The TimeRange filter used in the search.</p>"""
    area_of_interest: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.area_of_interest.AreaOfInterest"
    ]
    """<p>The Area of Interest used in the search.</p>"""
    property_filters: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.property_filters.PropertyFilters"
    ]
    """<p>Property filters used in the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RasterDataCollectionQueryOutput) -> dict:
    out: dict = {}
    out["RasterDataCollectionArn"] = value["raster_data_collection_arn"]
    out["RasterDataCollectionName"] = value["raster_data_collection_name"]
    import aws_sdk_sagemaker_geospatial.types.time_range_filter_output

    out["TimeRangeFilter"] = (
        aws_sdk_sagemaker_geospatial.types.time_range_filter_output.serialize_json(
            value["time_range_filter"]
        )
    )
    if "area_of_interest" in value:
        import aws_sdk_sagemaker_geospatial.types.area_of_interest

        out["AreaOfInterest"] = (
            aws_sdk_sagemaker_geospatial.types.area_of_interest.serialize_json(
                value["area_of_interest"]
            )
        )
    if "property_filters" in value:
        import aws_sdk_sagemaker_geospatial.types.property_filters

        out["PropertyFilters"] = (
            aws_sdk_sagemaker_geospatial.types.property_filters.serialize_json(
                value["property_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> RasterDataCollectionQueryOutput:
    out: RasterDataCollectionQueryOutput = {}  # type: ignore[typeddict-item]
    if "RasterDataCollectionArn" in data:
        out["raster_data_collection_arn"] = data["RasterDataCollectionArn"]
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryOutput.raster_data_collection_arn required"
        )
    if "RasterDataCollectionName" in data:
        out["raster_data_collection_name"] = data["RasterDataCollectionName"]
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryOutput.raster_data_collection_name required"
        )
    if "TimeRangeFilter" in data:
        import aws_sdk_sagemaker_geospatial.types.time_range_filter_output

        out["time_range_filter"] = (
            aws_sdk_sagemaker_geospatial.types.time_range_filter_output.deserialize_json(
                data["TimeRangeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryOutput.time_range_filter required"
        )
    if "AreaOfInterest" in data:
        import aws_sdk_sagemaker_geospatial.types.area_of_interest

        out["area_of_interest"] = (
            aws_sdk_sagemaker_geospatial.types.area_of_interest.deserialize_json(
                data["AreaOfInterest"]
            )
        )
    if "PropertyFilters" in data:
        import aws_sdk_sagemaker_geospatial.types.property_filters

        out["property_filters"] = (
            aws_sdk_sagemaker_geospatial.types.property_filters.deserialize_json(
                data["PropertyFilters"]
            )
        )
    return out
