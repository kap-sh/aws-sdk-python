"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetRasterDataCollectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.data_collection_arn
    import aws_sdk_sagemaker_geospatial.types.data_collection_type
    import aws_sdk_sagemaker_geospatial.types.filter_list
    import aws_sdk_sagemaker_geospatial.types.image_source_band_list
    import aws_sdk_sagemaker_geospatial.types.tags


class GetRasterDataCollectionOutput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the raster data collection.</p>"""
    arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""
    type: "aws_sdk_sagemaker_geospatial.types.data_collection_type.DataCollectionType"
    """<p>The raster data collection type.</p>"""
    description: "str"
    """<p>A description of the raster data collection.</p>"""
    description_page_url: "str"
    """<p>The URL of the description page.</p>"""
    supported_filters: "aws_sdk_sagemaker_geospatial.types.filter_list.FilterList"
    """<p>The filters supported by the raster data collection.</p>"""
    image_source_bands: (
        "aws_sdk_sagemaker_geospatial.types.image_source_band_list.ImageSourceBandList"
    )
    """<p>The list of image source bands in the raster data collection.</p>"""
    tags: NotRequired["aws_sdk_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRasterDataCollectionOutput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["Type"] = value["type"]
    out["Description"] = value["description"]
    out["DescriptionPageUrl"] = value["description_page_url"]
    import aws_sdk_sagemaker_geospatial.types.filter_list

    out["SupportedFilters"] = (
        aws_sdk_sagemaker_geospatial.types.filter_list.serialize_json(
            value["supported_filters"]
        )
    )
    import aws_sdk_sagemaker_geospatial.types.image_source_band_list

    out["ImageSourceBands"] = (
        aws_sdk_sagemaker_geospatial.types.image_source_band_list.serialize_json(
            value["image_source_bands"]
        )
    )
    if "tags" in value:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["Tags"] = aws_sdk_sagemaker_geospatial.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetRasterDataCollectionOutput:
    out: GetRasterDataCollectionOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetRasterDataCollectionOutput.name required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetRasterDataCollectionOutput.arn required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("GetRasterDataCollectionOutput.type required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("GetRasterDataCollectionOutput.description required")
    if "DescriptionPageUrl" in data:
        out["description_page_url"] = data["DescriptionPageUrl"]
    else:
        raise DeserializationError(
            "GetRasterDataCollectionOutput.description_page_url required"
        )
    if "SupportedFilters" in data:
        import aws_sdk_sagemaker_geospatial.types.filter_list

        out["supported_filters"] = (
            aws_sdk_sagemaker_geospatial.types.filter_list.deserialize_json(
                data["SupportedFilters"]
            )
        )
    else:
        raise DeserializationError(
            "GetRasterDataCollectionOutput.supported_filters required"
        )
    if "ImageSourceBands" in data:
        import aws_sdk_sagemaker_geospatial.types.image_source_band_list

        out["image_source_bands"] = (
            aws_sdk_sagemaker_geospatial.types.image_source_band_list.deserialize_json(
                data["ImageSourceBands"]
            )
        )
    else:
        raise DeserializationError(
            "GetRasterDataCollectionOutput.image_source_bands required"
        )
    if "Tags" in data:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["tags"] = aws_sdk_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
