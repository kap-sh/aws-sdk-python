"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationV2Provisioned``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_cluster_operation_step
    import capo_kafka.types.mutable_cluster_info
    import capo_kafka.types.vpc_connection_info


class ClusterOperationV2Provisioned(TypedDict, closed=True):
    operation_steps: NotRequired[
        "capo_kafka.types.__list_of_cluster_operation_step.__listOfClusterOperationStep"
    ]
    """<p>Steps completed during the operation.</p>"""
    source_cluster_info: NotRequired[
        "capo_kafka.types.mutable_cluster_info.MutableClusterInfo"
    ]
    """<p>Information about cluster attributes before a cluster is updated.</p>"""
    target_cluster_info: NotRequired[
        "capo_kafka.types.mutable_cluster_info.MutableClusterInfo"
    ]
    """<p>Information about cluster attributes after a cluster is updated.</p>"""
    vpc_connection_info: NotRequired[
        "capo_kafka.types.vpc_connection_info.VpcConnectionInfo"
    ]
    """<p>Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationV2Provisioned) -> dict:
    out: dict = {}
    if "operation_steps" in value:
        import capo_kafka.types.__list_of_cluster_operation_step

        out["operationSteps"] = (
            capo_kafka.types.__list_of_cluster_operation_step.serialize_json(
                value["operation_steps"]
            )
        )
    if "source_cluster_info" in value:
        import capo_kafka.types.mutable_cluster_info

        out["sourceClusterInfo"] = capo_kafka.types.mutable_cluster_info.serialize_json(
            value["source_cluster_info"]
        )
    if "target_cluster_info" in value:
        import capo_kafka.types.mutable_cluster_info

        out["targetClusterInfo"] = capo_kafka.types.mutable_cluster_info.serialize_json(
            value["target_cluster_info"]
        )
    if "vpc_connection_info" in value:
        import capo_kafka.types.vpc_connection_info

        out["vpcConnectionInfo"] = capo_kafka.types.vpc_connection_info.serialize_json(
            value["vpc_connection_info"]
        )
    return out


def deserialize_json(data: dict) -> ClusterOperationV2Provisioned:
    out: ClusterOperationV2Provisioned = {}  # type: ignore[typeddict-item]
    if "operationSteps" in data:
        import capo_kafka.types.__list_of_cluster_operation_step

        out["operation_steps"] = (
            capo_kafka.types.__list_of_cluster_operation_step.deserialize_json(
                data["operationSteps"]
            )
        )
    if "sourceClusterInfo" in data:
        import capo_kafka.types.mutable_cluster_info

        out["source_cluster_info"] = (
            capo_kafka.types.mutable_cluster_info.deserialize_json(
                data["sourceClusterInfo"]
            )
        )
    if "targetClusterInfo" in data:
        import capo_kafka.types.mutable_cluster_info

        out["target_cluster_info"] = (
            capo_kafka.types.mutable_cluster_info.deserialize_json(
                data["targetClusterInfo"]
            )
        )
    if "vpcConnectionInfo" in data:
        import capo_kafka.types.vpc_connection_info

        out["vpc_connection_info"] = (
            capo_kafka.types.vpc_connection_info.deserialize_json(
                data["vpcConnectionInfo"]
            )
        )
    return out
