"""Generated from Smithy shape ``com.amazonaws.omics#GetAnnotationStoreVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.arn
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.resource_id
    import aws_sdk_omics.types.status_message
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.update_time
    import aws_sdk_omics.types.version_name
    import aws_sdk_omics.types.version_options
    import aws_sdk_omics.types.version_status


class GetAnnotationStoreVersionResponse(TypedDict):
    store_id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p> The store ID for annotation store version. </p>"""
    id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p> The annotation store version ID. </p>"""
    status: "aws_sdk_omics.types.version_status.VersionStatus"
    """<p> The status of an annotation store version. </p>"""
    version_arn: "aws_sdk_omics.types.arn.Arn"
    """<p> The Arn for the annotation store. </p>"""
    name: "aws_sdk_omics.types.store_name.StoreName"
    """<p> The name of the annotation store. </p>"""
    version_name: "aws_sdk_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from others. </p>"""
    description: "aws_sdk_omics.types.description.Description"
    """<p> The description for an annotation store version. </p>"""
    creation_time: "aws_sdk_omics.types.creation_time.CreationTime"
    """<p> The time stamp for when an annotation store version was created. </p>"""
    update_time: "aws_sdk_omics.types.update_time.UpdateTime"
    """<p> The time stamp for when an annotation store version was updated. </p>"""
    tags: "aws_sdk_omics.types.tag_map.TagMap"
    """<p> Any tags associated with an annotation store version. </p>"""
    version_options: NotRequired["aws_sdk_omics.types.version_options.VersionOptions"]
    """<p> The options for an annotation store version. </p>"""
    status_message: "aws_sdk_omics.types.status_message.StatusMessage"
    """<p> The status of an annotation store version. </p>"""
    version_size_bytes: "int"
    """<p> The size of the annotation store version in Bytes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnnotationStoreVersionResponse) -> dict:
    out: dict = {}
    out["storeId"] = value["store_id"]
    out["id"] = value["id"]
    out["status"] = value["status"]
    out["versionArn"] = value["version_arn"]
    out["name"] = value["name"]
    out["versionName"] = value["version_name"]
    out["description"] = value["description"]
    import aws_sdk_omics.types.creation_time

    out["creationTime"] = aws_sdk_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_omics.types.update_time

    out["updateTime"] = aws_sdk_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    import aws_sdk_omics.types.tag_map

    out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    if "version_options" in value:
        import aws_sdk_omics.types.version_options

        out["versionOptions"] = aws_sdk_omics.types.version_options.serialize_json(
            value["version_options"]
        )
    out["statusMessage"] = value["status_message"]
    out["versionSizeBytes"] = value["version_size_bytes"]
    return out


def deserialize_json(data: dict) -> GetAnnotationStoreVersionResponse:
    out: GetAnnotationStoreVersionResponse = {}  # type: ignore[typeddict-item]
    if "storeId" in data:
        out["store_id"] = data["storeId"]
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.store_id required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetAnnotationStoreVersionResponse.id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetAnnotationStoreVersionResponse.status required")
    if "versionArn" in data:
        out["version_arn"] = data["versionArn"]
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.version_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetAnnotationStoreVersionResponse.name required")
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.version_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.description required"
        )
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.creation_time required"
        )
    if "updateTime" in data:
        import aws_sdk_omics.types.update_time

        out["update_time"] = aws_sdk_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.update_time required"
        )
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("GetAnnotationStoreVersionResponse.tags required")
    if "versionOptions" in data:
        import aws_sdk_omics.types.version_options

        out["version_options"] = aws_sdk_omics.types.version_options.deserialize_json(
            data["versionOptions"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.status_message required"
        )
    if "versionSizeBytes" in data:
        out["version_size_bytes"] = data["versionSizeBytes"]
    else:
        raise DeserializationError(
            "GetAnnotationStoreVersionResponse.version_size_bytes required"
        )
    return out
