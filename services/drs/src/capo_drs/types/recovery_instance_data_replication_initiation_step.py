"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInitiationStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_data_replication_initiation_step_name
    import capo_drs.types.recovery_instance_data_replication_initiation_step_status


class RecoveryInstanceDataReplicationInitiationStep(TypedDict, closed=True):
    name: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_initiation_step_name.RecoveryInstanceDataReplicationInitiationStepName"
    ]
    """<p>The name of the step.</p>"""
    status: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_initiation_step_status.RecoveryInstanceDataReplicationInitiationStepStatus"
    ]
    """<p>The status of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInitiationStep) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDataReplicationInitiationStep:
    out: RecoveryInstanceDataReplicationInitiationStep = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
