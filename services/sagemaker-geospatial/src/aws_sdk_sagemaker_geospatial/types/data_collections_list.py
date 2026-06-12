"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#DataCollectionsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata

DataCollectionsList: TypeAlias = list["aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata.RasterDataCollectionMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: DataCollectionsList) -> list:
    import aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata
    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataCollectionsList:
    import aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata
    out: DataCollectionsList = []
    for item in data:
        out.append(aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata.deserialize_json(item))
    return out