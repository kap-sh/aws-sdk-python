"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601
    import capo_kafka.types.cluster_operation_v2_provisioned
    import capo_kafka.types.cluster_operation_v2_serverless
    import capo_kafka.types.cluster_type
    import capo_kafka.types.error_info


class ClusterOperationV2(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>ARN of the cluster.</p>"""
    cluster_type: NotRequired["capo_kafka.types.cluster_type.ClusterType"]
    """<p>Type of the backend cluster.</p>"""
    start_time: NotRequired["capo_kafka.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time at which operation was started.</p>"""
    end_time: NotRequired["capo_kafka.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time at which the operation finished.</p>"""
    error_info: NotRequired["capo_kafka.types.error_info.ErrorInfo"]
    """<p>If cluster operation failed from an error, it describes the error.</p>"""
    operation_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>ARN of the cluster operation.</p>"""
    operation_state: NotRequired["capo_kafka.types.__string.__string"]
    """<p>State of the cluster operation.</p>"""
    operation_type: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Type of the cluster operation.</p>"""
    provisioned: NotRequired[
        "capo_kafka.types.cluster_operation_v2_provisioned.ClusterOperationV2Provisioned"
    ]
    """<p>Properties of a provisioned cluster.</p>"""
    serverless: NotRequired[
        "capo_kafka.types.cluster_operation_v2_serverless.ClusterOperationV2Serverless"
    ]
    """<p>Properties of a serverless cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationV2) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_type" in value:
        import capo_kafka.types.cluster_type

        out["clusterType"] = capo_kafka.types.cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "start_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["startTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["endTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    if "error_info" in value:
        import capo_kafka.types.error_info

        out["errorInfo"] = capo_kafka.types.error_info.serialize_json(
            value["error_info"]
        )
    if "operation_arn" in value:
        out["operationArn"] = value["operation_arn"]
    if "operation_state" in value:
        out["operationState"] = value["operation_state"]
    if "operation_type" in value:
        out["operationType"] = value["operation_type"]
    if "provisioned" in value:
        import capo_kafka.types.cluster_operation_v2_provisioned

        out["provisioned"] = (
            capo_kafka.types.cluster_operation_v2_provisioned.serialize_json(
                value["provisioned"]
            )
        )
    if "serverless" in value:
        import capo_kafka.types.cluster_operation_v2_serverless

        out["serverless"] = (
            capo_kafka.types.cluster_operation_v2_serverless.serialize_json(
                value["serverless"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterOperationV2:
    out: ClusterOperationV2 = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "clusterType" in data:
        import capo_kafka.types.cluster_type

        out["cluster_type"] = capo_kafka.types.cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "startTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["start_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["end_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["endTime"]
        )
    if "errorInfo" in data:
        import capo_kafka.types.error_info

        out["error_info"] = capo_kafka.types.error_info.deserialize_json(
            data["errorInfo"]
        )
    if "operationArn" in data:
        out["operation_arn"] = data["operationArn"]
    if "operationState" in data:
        out["operation_state"] = data["operationState"]
    if "operationType" in data:
        out["operation_type"] = data["operationType"]
    if "provisioned" in data:
        import capo_kafka.types.cluster_operation_v2_provisioned

        out["provisioned"] = (
            capo_kafka.types.cluster_operation_v2_provisioned.deserialize_json(
                data["provisioned"]
            )
        )
    if "serverless" in data:
        import capo_kafka.types.cluster_operation_v2_serverless

        out["serverless"] = (
            capo_kafka.types.cluster_operation_v2_serverless.deserialize_json(
                data["serverless"]
            )
        )
    return out
