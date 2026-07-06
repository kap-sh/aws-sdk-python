"""Generated from Smithy shape ``com.amazonaws.drs#StopFailbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_id


class StopFailbackRequest(TypedDict, closed=True):
    recovery_instance_id: "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    """<p>The ID of the Recovery Instance we want to stop failback for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFailbackRequest) -> dict:
    out: dict = {}
    out["recoveryInstanceID"] = value["recovery_instance_id"]
    return out


def deserialize_json(data: dict) -> StopFailbackRequest:
    out: StopFailbackRequest = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceID" in data:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    else:
        raise DeserializationError("StopFailbackRequest.recovery_instance_id required")
    return out
