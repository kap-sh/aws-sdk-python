"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateMonitoringRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.enhanced_monitoring
    import aws_sdk_kafka.types.logging_info
    import aws_sdk_kafka.types.open_monitoring_info


class UpdateMonitoringRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.</p>"""
    enhanced_monitoring: NotRequired[
        "aws_sdk_kafka.types.enhanced_monitoring.EnhancedMonitoring"
    ]
    """<p>Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.</p>"""
    open_monitoring: NotRequired[
        "aws_sdk_kafka.types.open_monitoring_info.OpenMonitoringInfo"
    ]
    """<p>The settings for open monitoring.</p>"""
    logging_info: NotRequired["aws_sdk_kafka.types.logging_info.LoggingInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitoringRequest) -> dict:
    out: dict = {}
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "enhanced_monitoring" in value:
        import aws_sdk_kafka.types.enhanced_monitoring

        out["enhancedMonitoring"] = (
            aws_sdk_kafka.types.enhanced_monitoring.serialize_json(
                value["enhanced_monitoring"]
            )
        )
    if "open_monitoring" in value:
        import aws_sdk_kafka.types.open_monitoring_info

        out["openMonitoring"] = aws_sdk_kafka.types.open_monitoring_info.serialize_json(
            value["open_monitoring"]
        )
    if "logging_info" in value:
        import aws_sdk_kafka.types.logging_info

        out["loggingInfo"] = aws_sdk_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    return out


def deserialize_json(data: dict) -> UpdateMonitoringRequest:
    out: UpdateMonitoringRequest = {}  # type: ignore[typeddict-item]
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "enhancedMonitoring" in data:
        import aws_sdk_kafka.types.enhanced_monitoring

        out["enhanced_monitoring"] = (
            aws_sdk_kafka.types.enhanced_monitoring.deserialize_json(
                data["enhancedMonitoring"]
            )
        )
    if "openMonitoring" in data:
        import aws_sdk_kafka.types.open_monitoring_info

        out["open_monitoring"] = (
            aws_sdk_kafka.types.open_monitoring_info.deserialize_json(
                data["openMonitoring"]
            )
        )
    if "loggingInfo" in data:
        import aws_sdk_kafka.types.logging_info

        out["logging_info"] = aws_sdk_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    return out
