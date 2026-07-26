"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendStorageResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__boolean
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.backend_storage_permissions
    import capo_amplifybackend.types.service_name


class GetBackendStorageResourceConfig(TypedDict, closed=True):
    bucket_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the S3 bucket.</p>"""
    imported: NotRequired["capo_amplifybackend.types.__boolean.__boolean"]
    """<p>Returns True if the storage resource has been imported.</p>"""
    permissions: NotRequired[
        "capo_amplifybackend.types.backend_storage_permissions.BackendStoragePermissions"
    ]
    """<p>The authorization configuration for the storage S3 bucket.</p>"""
    service_name: NotRequired["capo_amplifybackend.types.service_name.ServiceName"]
    """<p>The name of the storage service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendStorageResourceConfig) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "imported" in value:
        out["imported"] = value["imported"]
    if "permissions" in value:
        import capo_amplifybackend.types.backend_storage_permissions

        out["permissions"] = (
            capo_amplifybackend.types.backend_storage_permissions.serialize_json(
                value["permissions"]
            )
        )
    if "service_name" in value:
        import capo_amplifybackend.types.service_name

        out["serviceName"] = capo_amplifybackend.types.service_name.serialize_json(
            value["service_name"]
        )
    return out


def deserialize_json(data: dict) -> GetBackendStorageResourceConfig:
    out: GetBackendStorageResourceConfig = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "imported" in data:
        out["imported"] = data["imported"]
    if "permissions" in data:
        import capo_amplifybackend.types.backend_storage_permissions

        out["permissions"] = (
            capo_amplifybackend.types.backend_storage_permissions.deserialize_json(
                data["permissions"]
            )
        )
    if "serviceName" in data:
        import capo_amplifybackend.types.service_name

        out["service_name"] = capo_amplifybackend.types.service_name.deserialize_json(
            data["serviceName"]
        )
    return out
