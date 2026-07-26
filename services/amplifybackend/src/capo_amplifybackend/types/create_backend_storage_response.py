"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendStorageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class CreateBackendStorageResponse(TypedDict, closed=True):
    app_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the backend environment.</p>"""
    job_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID for the job.</p>"""
    status: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The current status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendStorageResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CreateBackendStorageResponse:
    out: CreateBackendStorageResponse = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "status" in data:
        out["status"] = data["status"]
    return out
