"""Generated from Smithy shape ``com.amazonaws.batch#EksAttemptContainerDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string


class EksAttemptContainerDetail(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of a container.</p>"""
    container_id: NotRequired["capo_batch.types.string.String"]
    """<p>The ID for the container.</p>"""
    exit_code: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The exit code returned for the job attempt. A non-zero exit code is considered failed.</p>"""
    reason: NotRequired["capo_batch.types.string.String"]
    """<p>A short (255 max characters) human-readable string to provide additional details for a running or stopped container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksAttemptContainerDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "container_id" in value:
        out["containerID"] = value["container_id"]
    if "exit_code" in value:
        out["exitCode"] = value["exit_code"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> EksAttemptContainerDetail:
    out: EksAttemptContainerDetail = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "containerID" in data:
        out["container_id"] = data["containerID"]
    if "exitCode" in data:
        out["exit_code"] = data["exitCode"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
