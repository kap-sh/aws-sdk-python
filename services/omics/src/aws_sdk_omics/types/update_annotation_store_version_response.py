"""Generated from Smithy shape ``com.amazonaws.omics#UpdateAnnotationStoreVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.creation_time
    import aws_sdk_omics.types.description
    import aws_sdk_omics.types.resource_id
    import aws_sdk_omics.types.store_name
    import aws_sdk_omics.types.update_time
    import aws_sdk_omics.types.version_name
    import aws_sdk_omics.types.version_status


class UpdateAnnotationStoreVersionResponse(TypedDict, closed=True):
    store_id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p> The annotation store ID. </p>"""
    id: "aws_sdk_omics.types.resource_id.ResourceId"
    """<p> The annotation store version ID. </p>"""
    status: "aws_sdk_omics.types.version_status.VersionStatus"
    """<p> The status of an annotation store version. </p>"""
    name: "aws_sdk_omics.types.store_name.StoreName"
    """<p> The name of an annotation store. </p>"""
    version_name: "aws_sdk_omics.types.version_name.VersionName"
    """<p> The name of an annotation store version. </p>"""
    description: "aws_sdk_omics.types.description.Description"
    """<p> The description of an annotation store version. </p>"""
    creation_time: "aws_sdk_omics.types.creation_time.CreationTime"
    """<p> The time stamp for when an annotation store version was created. </p>"""
    update_time: "aws_sdk_omics.types.update_time.UpdateTime"
    """<p> The time stamp for when an annotation store version was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnnotationStoreVersionResponse) -> dict:
    out: dict = {}
    out["storeId"] = value["store_id"]
    out["id"] = value["id"]
    out["status"] = value["status"]
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
    return out


def deserialize_json(data: dict) -> UpdateAnnotationStoreVersionResponse:
    out: UpdateAnnotationStoreVersionResponse = {}  # type: ignore[typeddict-item]
    if "storeId" in data:
        out["store_id"] = data["storeId"]
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreVersionResponse.store_id required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateAnnotationStoreVersionResponse.id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreVersionResponse.status required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateAnnotationStoreVersionResponse.name required")
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreVersionResponse.version_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreVersionResponse.description required"
        )
    if "creationTime" in data:
        import aws_sdk_omics.types.creation_time

        out["creation_time"] = aws_sdk_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreVersionResponse.creation_time required"
        )
    if "updateTime" in data:
        import aws_sdk_omics.types.update_time

        out["update_time"] = aws_sdk_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError(
            "UpdateAnnotationStoreVersionResponse.update_time required"
        )
    return out
