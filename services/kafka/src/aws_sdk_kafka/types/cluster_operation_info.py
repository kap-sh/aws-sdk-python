"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_cluster_operation_step
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.error_info
    import aws_sdk_kafka.types.mutable_cluster_info
    import aws_sdk_kafka.types.vpc_connection_info


class ClusterOperationInfo(TypedDict, closed=True):
    client_request_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The ID of the API request that triggered this operation.</p>"""
    cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>ARN of the cluster.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the operation was created.</p>"""
    end_time: NotRequired["aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time at which the operation finished.</p>"""
    error_info: NotRequired["aws_sdk_kafka.types.error_info.ErrorInfo"]
    """<p>Describes the error if the operation fails.</p>"""
    operation_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>ARN of the cluster operation.</p>"""
    operation_state: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>State of the cluster operation.</p>"""
    operation_steps: NotRequired[
        "aws_sdk_kafka.types.__list_of_cluster_operation_step.__listOfClusterOperationStep"
    ]
    """<p>Steps completed during the operation.</p>"""
    operation_type: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Type of the cluster operation.</p>"""
    source_cluster_info: NotRequired[
        "aws_sdk_kafka.types.mutable_cluster_info.MutableClusterInfo"
    ]
    """<p>Information about cluster attributes before a cluster is updated.</p>"""
    target_cluster_info: NotRequired[
        "aws_sdk_kafka.types.mutable_cluster_info.MutableClusterInfo"
    ]
    """<p>Information about cluster attributes after a cluster is updated.</p>"""
    vpc_connection_info: NotRequired[
        "aws_sdk_kafka.types.vpc_connection_info.VpcConnectionInfo"
    ]
    """<p>Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationInfo) -> dict:
    out: dict = {}
    if "client_request_id" in value:
        out["clientRequestId"] = value["client_request_id"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["endTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    if "error_info" in value:
        import aws_sdk_kafka.types.error_info

        out["errorInfo"] = aws_sdk_kafka.types.error_info.serialize_json(
            value["error_info"]
        )
    if "operation_arn" in value:
        out["operationArn"] = value["operation_arn"]
    if "operation_state" in value:
        out["operationState"] = value["operation_state"]
    if "operation_steps" in value:
        import aws_sdk_kafka.types.__list_of_cluster_operation_step

        out["operationSteps"] = (
            aws_sdk_kafka.types.__list_of_cluster_operation_step.serialize_json(
                value["operation_steps"]
            )
        )
    if "operation_type" in value:
        out["operationType"] = value["operation_type"]
    if "source_cluster_info" in value:
        import aws_sdk_kafka.types.mutable_cluster_info

        out["sourceClusterInfo"] = (
            aws_sdk_kafka.types.mutable_cluster_info.serialize_json(
                value["source_cluster_info"]
            )
        )
    if "target_cluster_info" in value:
        import aws_sdk_kafka.types.mutable_cluster_info

        out["targetClusterInfo"] = (
            aws_sdk_kafka.types.mutable_cluster_info.serialize_json(
                value["target_cluster_info"]
            )
        )
    if "vpc_connection_info" in value:
        import aws_sdk_kafka.types.vpc_connection_info

        out["vpcConnectionInfo"] = (
            aws_sdk_kafka.types.vpc_connection_info.serialize_json(
                value["vpc_connection_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterOperationInfo:
    out: ClusterOperationInfo = {}  # type: ignore[typeddict-item]
    if "clientRequestId" in data:
        out["client_request_id"] = data["clientRequestId"]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "endTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["end_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["endTime"]
        )
    if "errorInfo" in data:
        import aws_sdk_kafka.types.error_info

        out["error_info"] = aws_sdk_kafka.types.error_info.deserialize_json(
            data["errorInfo"]
        )
    if "operationArn" in data:
        out["operation_arn"] = data["operationArn"]
    if "operationState" in data:
        out["operation_state"] = data["operationState"]
    if "operationSteps" in data:
        import aws_sdk_kafka.types.__list_of_cluster_operation_step

        out["operation_steps"] = (
            aws_sdk_kafka.types.__list_of_cluster_operation_step.deserialize_json(
                data["operationSteps"]
            )
        )
    if "operationType" in data:
        out["operation_type"] = data["operationType"]
    if "sourceClusterInfo" in data:
        import aws_sdk_kafka.types.mutable_cluster_info

        out["source_cluster_info"] = (
            aws_sdk_kafka.types.mutable_cluster_info.deserialize_json(
                data["sourceClusterInfo"]
            )
        )
    if "targetClusterInfo" in data:
        import aws_sdk_kafka.types.mutable_cluster_info

        out["target_cluster_info"] = (
            aws_sdk_kafka.types.mutable_cluster_info.deserialize_json(
                data["targetClusterInfo"]
            )
        )
    if "vpcConnectionInfo" in data:
        import aws_sdk_kafka.types.vpc_connection_info

        out["vpc_connection_info"] = (
            aws_sdk_kafka.types.vpc_connection_info.deserialize_json(
                data["vpcConnectionInfo"]
            )
        )
    return out
