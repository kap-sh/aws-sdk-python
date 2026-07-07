"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendStorageResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.backend_storage_permissions
    import aws_sdk_amplifybackend.types.service_name


class UpdateBackendStorageResourceConfig(TypedDict, closed=True):
    permissions: NotRequired[
        "aws_sdk_amplifybackend.types.backend_storage_permissions.BackendStoragePermissions"
    ]
    """<p>The authorization configuration for the storage S3 bucket.</p>"""
    service_name: NotRequired["aws_sdk_amplifybackend.types.service_name.ServiceName"]
    """<p>The name of the storage service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendStorageResourceConfig) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> UpdateBackendStorageResourceConfig:
    out: UpdateBackendStorageResourceConfig = {}  # type: ignore[typeddict-item]
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
