"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeleteBackendResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class DeleteBackendResponse(TypedDict, closed=True):
    app_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the backend environment.</p>"""
    error: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>If the request fails, this error is returned.</p>"""
    job_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The ID for the job.</p>"""
    operation: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of the operation.</p>"""
    status: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The current status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackendResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "error" in value:
        out["error"] = value["error"]
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DeleteBackendResponse:
    out: DeleteBackendResponse = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if "error" in data:
        out["error"] = data["error"]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "status" in data:
        out["status"] = data["status"]
    return out
