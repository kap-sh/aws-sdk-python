"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendStorageResourceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.backend_storage_permissions
    import aws_sdk_amplifybackend.types.service_name


class CreateBackendStorageResourceConfig(TypedDict):
    bucket_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of the S3 bucket.</p>"""
    permissions: NotRequired[
        "aws_sdk_amplifybackend.types.backend_storage_permissions.BackendStoragePermissions"
    ]
    """<p>The authorization configuration for the storage S3 bucket.</p>"""
    service_name: NotRequired["aws_sdk_amplifybackend.types.service_name.ServiceName"]
    """<p>The name of the storage service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendStorageResourceConfig) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "permissions" in value:
        import aws_sdk_amplifybackend.types.backend_storage_permissions

        out["permissions"] = (
            aws_sdk_amplifybackend.types.backend_storage_permissions.serialize_json(
                value["permissions"]
            )
        )
    if "service_name" in value:
        import aws_sdk_amplifybackend.types.service_name

        out["serviceName"] = aws_sdk_amplifybackend.types.service_name.serialize_json(
            value["service_name"]
        )
    return out


def deserialize_json(data: dict) -> CreateBackendStorageResourceConfig:
    out: CreateBackendStorageResourceConfig = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "permissions" in data:
        import aws_sdk_amplifybackend.types.backend_storage_permissions

        out["permissions"] = (
            aws_sdk_amplifybackend.types.backend_storage_permissions.deserialize_json(
                data["permissions"]
            )
        )
    if "serviceName" in data:
        import aws_sdk_amplifybackend.types.service_name

        out["service_name"] = (
            aws_sdk_amplifybackend.types.service_name.deserialize_json(
                data["serviceName"]
            )
        )
    return out
