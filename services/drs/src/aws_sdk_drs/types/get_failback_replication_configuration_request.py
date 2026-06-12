"""Generated from Smithy shape ``com.amazonaws.drs#GetFailbackReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_drs.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_id

class GetFailbackReplicationConfigurationRequest(TypedDict):
    recovery_instance_id: "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    """<p>The ID of the Recovery Instance whose failback replication configuration should be returned.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetFailbackReplicationConfigurationRequest) -> dict:
    out: dict = {}
    out["recoveryInstanceID"] = value["recovery_instance_id"]
    return out


def deserialize_json(data: dict) -> GetFailbackReplicationConfigurationRequest:
    out: GetFailbackReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceID" in data:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    else:
        raise DeserializationError("GetFailbackReplicationConfigurationRequest.recovery_instance_id required")
    return out