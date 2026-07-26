"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ImportBackendStorageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.service_name


class ImportBackendStorageRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "capo_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    bucket_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the S3 bucket.</p>"""
    service_name: NotRequired["capo_amplifybackend.types.service_name.ServiceName"]
    """<p>The name of the storage service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportBackendStorageRequest) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "service_name" in value:
        import capo_amplifybackend.types.service_name

        out["serviceName"] = capo_amplifybackend.types.service_name.serialize_json(
            value["service_name"]
        )
    return out


def deserialize_json(data: dict) -> ImportBackendStorageRequest:
    out: ImportBackendStorageRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "serviceName" in data:
        import capo_amplifybackend.types.service_name

        out["service_name"] = capo_amplifybackend.types.service_name.deserialize_json(
            data["serviceName"]
        )
    return out
