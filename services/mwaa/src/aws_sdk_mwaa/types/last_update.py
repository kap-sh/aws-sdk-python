"""Generated from Smithy shape ``com.amazonaws.mwaa#LastUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mwaa.types.update_created_at
    import aws_sdk_mwaa.types.update_error
    import aws_sdk_mwaa.types.update_source
    import aws_sdk_mwaa.types.update_status
    import aws_sdk_mwaa.types.worker_replacement_strategy

class LastUpdate(TypedDict):
    status: NotRequired["aws_sdk_mwaa.types.update_status.UpdateStatus"]
    """<p>The status of the last update on the environment.</p>"""
    created_at: NotRequired["aws_sdk_mwaa.types.update_created_at.UpdateCreatedAt"]
    """<p>The day and time of the last update on the environment.</p>"""
    error: NotRequired["aws_sdk_mwaa.types.update_error.UpdateError"]
    """<p>The error that was encountered during the last update of the environment.</p>"""
    source: NotRequired["aws_sdk_mwaa.types.update_source.UpdateSource"]
    """<p>The source of the last update to the environment. Includes internal processes by Amazon MWAA, such as an environment maintenance update.</p>"""
    worker_replacement_strategy: NotRequired["aws_sdk_mwaa.types.worker_replacement_strategy.WorkerReplacementStrategy"]
    """<p>The worker replacement strategy used in the last update of the environment.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: LastUpdate) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "created_at" in value:
        import aws_sdk_mwaa.types.update_created_at
        out["CreatedAt"] = aws_sdk_mwaa.types.update_created_at.serialize_json(value["created_at"])
    if "error" in value:
        import aws_sdk_mwaa.types.update_error
        out["Error"] = aws_sdk_mwaa.types.update_error.serialize_json(value["error"])
    if "source" in value:
        out["Source"] = value["source"]
    if "worker_replacement_strategy" in value:
        out["WorkerReplacementStrategy"] = value["worker_replacement_strategy"]
    return out


def deserialize_json(data: dict) -> LastUpdate:
    out: LastUpdate = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "CreatedAt" in data:
        import aws_sdk_mwaa.types.update_created_at
        out["created_at"] = aws_sdk_mwaa.types.update_created_at.deserialize_json(data["CreatedAt"])
    if "Error" in data:
        import aws_sdk_mwaa.types.update_error
        out["error"] = aws_sdk_mwaa.types.update_error.deserialize_json(data["Error"])
    if "Source" in data:
        out["source"] = data["Source"]
    if "WorkerReplacementStrategy" in data:
        out["worker_replacement_strategy"] = data["WorkerReplacementStrategy"]
    return out