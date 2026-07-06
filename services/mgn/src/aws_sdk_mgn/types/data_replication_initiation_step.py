"""Generated from Smithy shape ``com.amazonaws.mgn#DataReplicationInitiationStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.data_replication_initiation_step_name
    import aws_sdk_mgn.types.data_replication_initiation_step_status


class DataReplicationInitiationStep(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_mgn.types.data_replication_initiation_step_name.DataReplicationInitiationStepName"
    ]
    """<p>Request to query data initiation step name.</p>"""
    status: NotRequired[
        "aws_sdk_mgn.types.data_replication_initiation_step_status.DataReplicationInitiationStepStatus"
    ]
    """<p>Request to query data initiation status.</p>"""


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
