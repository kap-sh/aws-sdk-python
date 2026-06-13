"""Generated from Smithy shape ``com.amazonaws.drs#DisconnectRecoveryInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_id


class DisconnectRecoveryInstanceRequest(TypedDict):
    recovery_instance_id: "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    """<p>The ID of the Recovery Instance to disconnect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectRecoveryInstanceRequest) -> dict:
    out: dict = {}
    out["recoveryInstanceID"] = value["recovery_instance_id"]
    return out


def deserialize_json(data: dict) -> DisconnectRecoveryInstanceRequest:
    out: DisconnectRecoveryInstanceRequest = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceID" in data:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    else:
        raise DeserializationError(
            "DisconnectRecoveryInstanceRequest.recovery_instance_id required"
        )
    return out
