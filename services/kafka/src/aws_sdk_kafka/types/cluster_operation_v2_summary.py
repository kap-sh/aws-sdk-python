"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterOperationV2Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.cluster_type


class ClusterOperationV2Summary(TypedDict, closed=True):
    cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>ARN of the cluster.</p>"""
    cluster_type: NotRequired["aws_sdk_kafka.types.cluster_type.ClusterType"]
    """<p>Type of the backend cluster.</p>"""
    start_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time at which operation was started.</p>"""
    end_time: NotRequired["aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The time at which the operation finished.</p>"""
    operation_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>ARN of the cluster operation.</p>"""
    operation_state: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>State of the cluster operation.</p>"""
    operation_type: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Type of the cluster operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterOperationV2Summary) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_type" in value:
        import aws_sdk_kafka.types.cluster_type

        out["clusterType"] = aws_sdk_kafka.types.cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "start_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["startTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["endTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    if "operation_arn" in value:
        out["operationArn"] = value["operation_arn"]
    if "operation_state" in value:
        out["operationState"] = value["operation_state"]
    if "operation_type" in value:
        out["operationType"] = value["operation_type"]
    return out


def deserialize_json(data: dict) -> ClusterOperationV2Summary:
    out: ClusterOperationV2Summary = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "clusterType" in data:
        import aws_sdk_kafka.types.cluster_type

        out["cluster_type"] = aws_sdk_kafka.types.cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "startTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["start_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["end_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["endTime"]
        )
    if "operationArn" in data:
        out["operation_arn"] = data["operationArn"]
    if "operationState" in data:
        out["operation_state"] = data["operationState"]
    if "operationType" in data:
        out["operation_type"] = data["operationType"]
    return out
