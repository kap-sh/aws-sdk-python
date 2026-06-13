"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#InputConfigOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn
    import aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_output


class InputConfigOutput(TypedDict):
    previous_earth_observation_job_arn: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the previous Earth Observation job.</p>"""
    raster_data_collection_query: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_output.RasterDataCollectionQueryOutput"
    ]
    """<p>The structure representing the RasterDataCollection Query consisting of the Area of Interest, RasterDataCollectionArn, RasterDataCollectionName, TimeRange, and Property Filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfigOutput) -> dict:
    out: dict = {}
    if "previous_earth_observation_job_arn" in value:
        out["PreviousEarthObservationJobArn"] = value[
            "previous_earth_observation_job_arn"
        ]
    if "raster_data_collection_query" in value:
        import aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_output

        out["RasterDataCollectionQuery"] = (
            aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_output.serialize_json(
                value["raster_data_collection_query"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputConfigOutput:
    out: InputConfigOutput = {}  # type: ignore[typeddict-item]
    if "PreviousEarthObservationJobArn" in data:
        out["previous_earth_observation_job_arn"] = data[
            "PreviousEarthObservationJobArn"
        ]
    if "RasterDataCollectionQuery" in data:
        import aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_output

        out["raster_data_collection_query"] = (
            aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_output.deserialize_json(
                data["RasterDataCollectionQuery"]
            )
        )
    return out
