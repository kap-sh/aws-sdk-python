"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#RasterDataCollectionQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.area_of_interest
    import aws_sdk_sagemaker_geospatial.types.data_collection_arn
    import aws_sdk_sagemaker_geospatial.types.property_filters
    import aws_sdk_sagemaker_geospatial.types.time_range_filter_input


class RasterDataCollectionQueryInput(TypedDict):
    raster_data_collection_arn: (
        "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""
    time_range_filter: "aws_sdk_sagemaker_geospatial.types.time_range_filter_input.TimeRangeFilterInput"
    """<p>The TimeRange Filter used in the RasterDataCollection Query.</p>"""
    area_of_interest: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.area_of_interest.AreaOfInterest"
    ]
    """<p>The area of interest being queried for the raster data collection.</p>"""
    property_filters: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.property_filters.PropertyFilters"
    ]
    """<p>The list of Property filters used in the Raster Data Collection Query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RasterDataCollectionQueryInput) -> dict:
    out: dict = {}
    out["RasterDataCollectionArn"] = value["raster_data_collection_arn"]
    import aws_sdk_sagemaker_geospatial.types.time_range_filter_input

    out["TimeRangeFilter"] = (
        aws_sdk_sagemaker_geospatial.types.time_range_filter_input.serialize_json(
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


def deserialize_json(data: dict) -> RasterDataCollectionQueryInput:
    out: RasterDataCollectionQueryInput = {}  # type: ignore[typeddict-item]
    if "RasterDataCollectionArn" in data:
        out["raster_data_collection_arn"] = data["RasterDataCollectionArn"]
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryInput.raster_data_collection_arn required"
        )
    if "TimeRangeFilter" in data:
        import aws_sdk_sagemaker_geospatial.types.time_range_filter_input

        out["time_range_filter"] = (
            aws_sdk_sagemaker_geospatial.types.time_range_filter_input.deserialize_json(
                data["TimeRangeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryInput.time_range_filter required"
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
