"""Generated from Smithy shape ``com.amazonaws.batch#EvaluateOnExit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.retry_action
    import capo_batch.types.string


class EvaluateOnExit(TypedDict, closed=True):
    on_status_reason: NotRequired["capo_batch.types.string.String"]
    """<p>Contains a glob pattern to match against the <code>StatusReason</code> returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white spaces (including spaces or tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.</p>"""
    on_reason: NotRequired["capo_batch.types.string.String"]
    """<p>Contains a glob pattern to match against the <code>Reason</code> returned for a job. The pattern can contain up to 512 characters. It can contain letters, numbers, periods (.), colons (:), and white space (including spaces and tabs). It can optionally end with an asterisk (*) so that only the start of the string needs to be an exact match.</p>"""
    on_exit_code: NotRequired["capo_batch.types.string.String"]
    """<p>Contains a glob pattern to match against the decimal representation of the <code>ExitCode</code> returned for a job. The pattern can be up to 512 characters long. It can contain only numbers, and can end with an asterisk (*) so that only the start of the string needs to be an exact match.</p> <p>The string can contain up to 512 characters.</p>"""
    action: NotRequired["capo_batch.types.retry_action.RetryAction"]
    """<p>Specifies the action to take if all of the specified conditions (<code>onStatusReason</code>, <code>onReason</code>, and <code>onExitCode</code>) are met. The values aren't case sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateOnExit) -> dict:
    out: dict = {}
    if "on_status_reason" in value:
        out["onStatusReason"] = value["on_status_reason"]
    if "on_reason" in value:
        out["onReason"] = value["on_reason"]
    if "on_exit_code" in value:
        out["onExitCode"] = value["on_exit_code"]
    if "action" in value:
        import capo_batch.types.retry_action

        out["action"] = capo_batch.types.retry_action.serialize_json(value["action"])
    return out


def deserialize_json(data: dict) -> EvaluateOnExit:
    out: EvaluateOnExit = {}  # type: ignore[typeddict-item]
    if "onStatusReason" in data:
        out["on_status_reason"] = data["onStatusReason"]
    if "onReason" in data:
        out["on_reason"] = data["onReason"]
    if "onExitCode" in data:
        out["on_exit_code"] = data["onExitCode"]
    if "action" in data:
        import capo_batch.types.retry_action

        out["action"] = capo_batch.types.retry_action.deserialize_json(data["action"])
    return out
