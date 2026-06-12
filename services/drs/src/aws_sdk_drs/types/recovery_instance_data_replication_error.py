"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.failback_replication_error
    import aws_sdk_drs.types.large_bounded_string

class RecoveryInstanceDataReplicationError(TypedDict):
    error: NotRequired["aws_sdk_drs.types.failback_replication_error.FailbackReplicationError"]
    """<p>Error in data replication.</p>"""
    raw_error: NotRequired["aws_sdk_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Error in data replication.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationError) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "raw_error" in value:
        out["rawError"] = value["raw_error"]
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDataReplicationError:
    out: RecoveryInstanceDataReplicationError = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "rawError" in data:
        out["raw_error"] = data["rawError"]
    return out