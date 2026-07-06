"""Generated from Smithy shape ``com.amazonaws.ssmsap#Resilience``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.cluster_status
    import aws_sdk_ssm_sap.types.operation_mode
    import aws_sdk_ssm_sap.types.replication_mode


class Resilience(TypedDict, closed=True):
    hsr_tier: NotRequired["str"]
    """<p>The tier of the component.</p>"""
    hsr_replication_mode: NotRequired[
        "aws_sdk_ssm_sap.types.replication_mode.ReplicationMode"
    ]
    """<p>The replication mode of the component.</p>"""
    hsr_operation_mode: NotRequired[
        "aws_sdk_ssm_sap.types.operation_mode.OperationMode"
    ]
    """<p>The operation mode of the component.</p>"""
    cluster_status: NotRequired["aws_sdk_ssm_sap.types.cluster_status.ClusterStatus"]
    """<p>The cluster status of the component.</p>"""
    enqueue_replication: NotRequired["bool"]
    """<p>Indicates if or not enqueue replication is enabled for the ASCS component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resilience) -> dict:
    out: dict = {}
    if "hsr_tier" in value:
        out["HsrTier"] = value["hsr_tier"]
    if "hsr_replication_mode" in value:
        import aws_sdk_ssm_sap.types.replication_mode

        out["HsrReplicationMode"] = (
            aws_sdk_ssm_sap.types.replication_mode.serialize_json(
                value["hsr_replication_mode"]
            )
        )
    if "hsr_operation_mode" in value:
        import aws_sdk_ssm_sap.types.operation_mode

        out["HsrOperationMode"] = aws_sdk_ssm_sap.types.operation_mode.serialize_json(
            value["hsr_operation_mode"]
        )
    if "cluster_status" in value:
        import aws_sdk_ssm_sap.types.cluster_status

        out["ClusterStatus"] = aws_sdk_ssm_sap.types.cluster_status.serialize_json(
            value["cluster_status"]
        )
    if "enqueue_replication" in value:
        out["EnqueueReplication"] = value["enqueue_replication"]
    return out


def deserialize_json(data: dict) -> Resilience:
    out: Resilience = {}  # type: ignore[typeddict-item]
    if "HsrTier" in data:
        out["hsr_tier"] = data["HsrTier"]
    if "HsrReplicationMode" in data:
        import aws_sdk_ssm_sap.types.replication_mode

        out["hsr_replication_mode"] = (
            aws_sdk_ssm_sap.types.replication_mode.deserialize_json(
                data["HsrReplicationMode"]
            )
        )
    if "HsrOperationMode" in data:
        import aws_sdk_ssm_sap.types.operation_mode

        out["hsr_operation_mode"] = (
            aws_sdk_ssm_sap.types.operation_mode.deserialize_json(
                data["HsrOperationMode"]
            )
        )
    if "ClusterStatus" in data:
        import aws_sdk_ssm_sap.types.cluster_status

        out["cluster_status"] = aws_sdk_ssm_sap.types.cluster_status.deserialize_json(
            data["ClusterStatus"]
        )
    if "EnqueueReplication" in data:
        out["enqueue_replication"] = data["EnqueueReplication"]
    return out
