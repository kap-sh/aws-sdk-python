"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class GetBackendJobRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    job_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The ID for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackendJobRequest:
    out: GetBackendJobRequest = {}  # type: ignore[typeddict-item]
    return out
