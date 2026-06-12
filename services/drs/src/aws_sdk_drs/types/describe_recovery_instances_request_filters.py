"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoveryInstancesRequestFilters``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_i_ds
    import aws_sdk_drs.types.source_server_i_ds

class DescribeRecoveryInstancesRequestFilters(TypedDict):
    recovery_instance_i_ds: NotRequired["aws_sdk_drs.types.recovery_instance_i_ds.RecoveryInstanceIDs"]
    """<p>An array of Recovery Instance IDs that should be returned. An empty array means all Recovery Instances.</p>"""
    source_server_i_ds: NotRequired["aws_sdk_drs.types.source_server_i_ds.SourceServerIDs"]
    """<p>An array of Source Server IDs for which associated Recovery Instances should be returned.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryInstancesRequestFilters) -> dict:
    out: dict = {}
    if "recovery_instance_i_ds" in value:
        import aws_sdk_drs.types.recovery_instance_i_ds
        out["recoveryInstanceIDs"] = aws_sdk_drs.types.recovery_instance_i_ds.serialize_json(value["recovery_instance_i_ds"])
    if "source_server_i_ds" in value:
        import aws_sdk_drs.types.source_server_i_ds
        out["sourceServerIDs"] = aws_sdk_drs.types.source_server_i_ds.serialize_json(value["source_server_i_ds"])
    return out


def deserialize_json(data: dict) -> DescribeRecoveryInstancesRequestFilters:
    out: DescribeRecoveryInstancesRequestFilters = {}  # type: ignore[typeddict-item]
    if "recoveryInstanceIDs" in data:
        import aws_sdk_drs.types.recovery_instance_i_ds
        out["recovery_instance_i_ds"] = aws_sdk_drs.types.recovery_instance_i_ds.deserialize_json(data["recoveryInstanceIDs"])
    if "sourceServerIDs" in data:
        import aws_sdk_drs.types.source_server_i_ds
        out["source_server_i_ds"] = aws_sdk_drs.types.source_server_i_ds.deserialize_json(data["sourceServerIDs"])
    return out