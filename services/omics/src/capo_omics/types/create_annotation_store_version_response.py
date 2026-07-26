"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.creation_time
    import capo_omics.types.resource_id
    import capo_omics.types.store_name
    import capo_omics.types.version_name
    import capo_omics.types.version_options
    import capo_omics.types.version_status


class CreateAnnotationStoreVersionResponse(TypedDict, closed=True):
    id: "capo_omics.types.resource_id.ResourceId"
    """<p> A generated ID for the annotation store </p>"""
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    store_id: "capo_omics.types.resource_id.ResourceId"
    """<p> The ID for the annotation store from which new versions are being created. </p>"""
    version_options: NotRequired["capo_omics.types.version_options.VersionOptions"]
    """<p> The options for an annotation store version. </p>"""
    name: "capo_omics.types.store_name.StoreName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    status: "capo_omics.types.version_status.VersionStatus"
    """<p> The status of a annotation store version. </p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p> The time stamp for the creation of an annotation store version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreVersionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["versionName"] = value["version_name"]
    out["storeId"] = value["store_id"]
    if "version_options" in value:
        import capo_omics.types.version_options

        out["versionOptions"] = capo_omics.types.version_options.serialize_json(
            value["version_options"]
        )
    out["name"] = value["name"]
    out["status"] = value["status"]
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreVersionResponse:
    out: CreateAnnotationStoreVersionResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAnnotationStoreVersionResponse.id required")
    if "versionName" in data:
        out["version_name"] = data["versionName"]
    else:
        raise DeserializationError(
            "CreateAnnotationStoreVersionResponse.version_name required"
        )
    if "storeId" in data:
        out["store_id"] = data["storeId"]
    else:
        raise DeserializationError(
            "CreateAnnotationStoreVersionResponse.store_id required"
        )
    if "versionOptions" in data:
        import capo_omics.types.version_options

        out["version_options"] = capo_omics.types.version_options.deserialize_json(
            data["versionOptions"]
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAnnotationStoreVersionResponse.name required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError(
            "CreateAnnotationStoreVersionResponse.status required"
        )
    if "creationTime" in data:
        import capo_omics.types.creation_time

        out["creation_time"] = capo_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "CreateAnnotationStoreVersionResponse.creation_time required"
        )
    return out
