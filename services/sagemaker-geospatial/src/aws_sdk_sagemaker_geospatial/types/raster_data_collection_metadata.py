"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#RasterDataCollectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.data_collection_arn
    import aws_sdk_sagemaker_geospatial.types.data_collection_type
    import aws_sdk_sagemaker_geospatial.types.filter_list
    import aws_sdk_sagemaker_geospatial.types.tags


class RasterDataCollectionMetadata(TypedDict, closed=True):
    name: "str"
    """<p>The name of the raster data collection.</p>"""
    arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""
    type: "aws_sdk_sagemaker_geospatial.types.data_collection_type.DataCollectionType"
    """<p>The type of raster data collection.</p>"""
    description: "str"
    """<p>A description of the raster data collection.</p>"""
    description_page_url: NotRequired["str"]
    """<p>The description URL of the raster data collection.</p>"""
    supported_filters: "aws_sdk_sagemaker_geospatial.types.filter_list.FilterList"
    """<p>The list of filters supported by the raster data collection.</p>"""
    tags: NotRequired["aws_sdk_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RasterDataCollectionMetadata) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["Type"] = value["type"]
    out["Description"] = value["description"]
    if "description_page_url" in value:
        out["DescriptionPageUrl"] = value["description_page_url"]
    import aws_sdk_sagemaker_geospatial.types.filter_list

    out["SupportedFilters"] = (
        aws_sdk_sagemaker_geospatial.types.filter_list.serialize_json(
            value["supported_filters"]
        )
    )
    if "tags" in value:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["Tags"] = aws_sdk_sagemaker_geospatial.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> RasterDataCollectionMetadata:
    out: RasterDataCollectionMetadata = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RasterDataCollectionMetadata.name required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("RasterDataCollectionMetadata.arn required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("RasterDataCollectionMetadata.type required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("RasterDataCollectionMetadata.description required")
    if "DescriptionPageUrl" in data:
        out["description_page_url"] = data["DescriptionPageUrl"]
    if "SupportedFilters" in data:
        import aws_sdk_sagemaker_geospatial.types.filter_list

        out["supported_filters"] = (
            aws_sdk_sagemaker_geospatial.types.filter_list.deserialize_json(
                data["SupportedFilters"]
            )
        )
    else:
        raise DeserializationError(
            "RasterDataCollectionMetadata.supported_filters required"
        )
    if "Tags" in data:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["tags"] = aws_sdk_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
