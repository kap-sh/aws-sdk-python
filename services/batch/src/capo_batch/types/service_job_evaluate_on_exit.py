"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobEvaluateOnExit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.service_job_retry_action
    import capo_batch.types.string


class ServiceJobEvaluateOnExit(TypedDict, closed=True):
    action: NotRequired[
        "capo_batch.types.service_job_retry_action.ServiceJobRetryAction"
    ]
    """<p>The action to take if the service job exits with the specified condition. Valid values are <code>RETRY</code> and <code>EXIT</code>.</p>"""
    on_status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>Contains a glob pattern to match against the StatusReason returned for a job. The pattern can contain up to 512 characters and can contain all printable characters. It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobEvaluateOnExit) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_batch.types.service_job_retry_action

        out["action"] = capo_batch.types.service_job_retry_action.serialize_json(
            value["action"]
        )
    if "on_status_reason" in value:
        out["onStatusReason"] = value["on_status_reason"]
    return out


def deserialize_json(data: dict) -> ServiceJobEvaluateOnExit:
    out: ServiceJobEvaluateOnExit = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import capo_batch.types.service_job_retry_action

        out["action"] = capo_batch.types.service_job_retry_action.deserialize_json(
            data["action"]
        )
    if "onStatusReason" in data:
        out["on_status_reason"] = data["onStatusReason"]
    return out
