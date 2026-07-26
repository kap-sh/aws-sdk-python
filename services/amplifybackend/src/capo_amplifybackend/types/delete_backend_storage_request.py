"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeleteBackendStorageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.service_name


class DeleteBackendStorageRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "capo_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    resource_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the storage resource.</p>"""
    service_name: NotRequired["capo_amplifybackend.types.service_name.ServiceName"]
    """<p>The name of the storage service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackendStorageRequest) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "service_name" in value:
        import capo_amplifybackend.types.service_name

        out["serviceName"] = capo_amplifybackend.types.service_name.serialize_json(
            value["service_name"]
        )
    return out


def deserialize_json(data: dict) -> DeleteBackendStorageRequest:
    out: DeleteBackendStorageRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "serviceName" in data:
        import capo_amplifybackend.types.service_name

        out["service_name"] = capo_amplifybackend.types.service_name.deserialize_json(
            data["serviceName"]
        )
    return out
