"""Generated from Smithy shape ``com.amazonaws.drs#DataReplicationInitiationStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.data_replication_initiation_step_name
    import aws_sdk_drs.types.data_replication_initiation_step_status


class DataReplicationInitiationStep(TypedDict):
    name: NotRequired[
        "aws_sdk_drs.types.data_replication_initiation_step_name.DataReplicationInitiationStepName"
    ]
    """<p>The name of the step.</p>"""
    status: NotRequired[
        "aws_sdk_drs.types.data_replication_initiation_step_status.DataReplicationInitiationStepStatus"
    ]
    """<p>The status of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInitiationStep) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DataReplicationInitiationStep:
    out: DataReplicationInitiationStep = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
