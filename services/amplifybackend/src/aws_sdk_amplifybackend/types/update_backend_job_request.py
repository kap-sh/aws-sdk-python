"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class UpdateBackendJobRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    job_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The ID for the job.</p>"""
    operation: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Filters the list of response objects to include only those with the specified operation name.</p>"""
    status: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>Filters the list of response objects to include only those with the specified status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendJobRequest) -> dict:
    out: dict = {}
    if "operation" in value:
        out["operation"] = value["operation"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> UpdateBackendJobRequest:
    out: UpdateBackendJobRequest = {}  # type: ignore[typeddict-item]
    if "operation" in data:
        out["operation"] = data["operation"]
    if "status" in data:
        out["status"] = data["status"]
    return out
