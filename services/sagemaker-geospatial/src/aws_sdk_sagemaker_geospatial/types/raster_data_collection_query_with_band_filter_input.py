"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#RasterDataCollectionQueryWithBandFilterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.area_of_interest
    import aws_sdk_sagemaker_geospatial.types.property_filters
    import aws_sdk_sagemaker_geospatial.types.string_list_input
    import aws_sdk_sagemaker_geospatial.types.time_range_filter_input


class RasterDataCollectionQueryWithBandFilterInput(TypedDict, closed=True):
    time_range_filter: "aws_sdk_sagemaker_geospatial.types.time_range_filter_input.TimeRangeFilterInput"
    """<p>The TimeRange Filter used in the search query.</p>"""
    area_of_interest: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.area_of_interest.AreaOfInterest"
    ]
    """<p>The Area of interest to be used in the search query.</p>"""
    property_filters: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.property_filters.PropertyFilters"
    ]
    """<p>The Property Filters used in the search query.</p>"""
    band_filter: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.string_list_input.StringListInput"
    ]
    """<p>The list of Bands to be displayed in the result for each item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RasterDataCollectionQueryWithBandFilterInput) -> dict:
    out: dict = {}
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
    if "band_filter" in value:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["BandFilter"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.serialize_json(
                value["band_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> RasterDataCollectionQueryWithBandFilterInput:
    out: RasterDataCollectionQueryWithBandFilterInput = {}  # type: ignore[typeddict-item]
    if "TimeRangeFilter" in data:
        import aws_sdk_sagemaker_geospatial.types.time_range_filter_input

        out["time_range_filter"] = (
            aws_sdk_sagemaker_geospatial.types.time_range_filter_input.deserialize_json(
                data["TimeRangeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryWithBandFilterInput.time_range_filter required"
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
    if "BandFilter" in data:
        import aws_sdk_sagemaker_geospatial.types.string_list_input

        out["band_filter"] = (
            aws_sdk_sagemaker_geospatial.types.string_list_input.deserialize_json(
                data["BandFilter"]
            )
        )
    return out
