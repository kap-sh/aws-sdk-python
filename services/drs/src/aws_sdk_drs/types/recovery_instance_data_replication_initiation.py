"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInitiation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.recovery_instance_data_replication_initiation_steps

class RecoveryInstanceDataReplicationInitiation(TypedDict):
    start_date_time: NotRequired["aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"]
    """<p>The date and time of the current attempt to initiate data replication.</p>"""
    steps: NotRequired["aws_sdk_drs.types.recovery_instance_data_replication_initiation_steps.RecoveryInstanceDataReplicationInitiationSteps"]
    """<p>The steps of the current attempt to initiate data replication.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInitiation) -> dict:
    out: dict = {}
    if "start_date_time" in value:
        out["startDateTime"] = value["start_date_time"]
    if "steps" in value:
        import aws_sdk_drs.types.recovery_instance_data_replication_initiation_steps
        out["steps"] = aws_sdk_drs.types.recovery_instance_data_replication_initiation_steps.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDataReplicationInitiation:
    out: RecoveryInstanceDataReplicationInitiation = {}  # type: ignore[typeddict-item]
    if "startDateTime" in data:
        out["start_date_time"] = data["startDateTime"]
    if "steps" in data:
        import aws_sdk_drs.types.recovery_instance_data_replication_initiation_steps
        out["steps"] = aws_sdk_drs.types.recovery_instance_data_replication_initiation_steps.deserialize_json(data["steps"])
    return out