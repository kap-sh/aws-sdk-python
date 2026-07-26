"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class UpdateBackendJobResponse(TypedDict, closed=True):
    app_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the backend environment.</p>"""
    create_time: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The time when the job was created.</p>"""
    error: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>If the request fails, this error is returned.</p>"""
    job_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID for the job.</p>"""
    operation: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the operation.</p>"""
    status: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The current status of the request.</p>"""
    update_time: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The time when the job was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendJobResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "create_time" in value:
        out["createTime"] = value["create_time"]
    if "error" in value:
        out["error"] = value["error"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "status" in value:
        out["status"] = value["status"]
    if "update_time" in value:
        out["updateTime"] = value["update_time"]
    return out


def deserialize_json(data: dict) -> UpdateBackendJobResponse:
    out: UpdateBackendJobResponse = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    if "error" in data:
        out["error"] = data["error"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "status" in data:
        out["status"] = data["status"]
    if "updateTime" in data:
        out["update_time"] = data["updateTime"]
    return out
