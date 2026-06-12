"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalousLogGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.log_anomaly_showcases
    import aws_sdk_devops_guru.types.log_group_name
    import aws_sdk_devops_guru.types.number_of_log_lines_scanned
    import aws_sdk_devops_guru.types.timestamp


class AnomalousLogGroup(TypedDict):
    log_group_name: NotRequired["aws_sdk_devops_guru.types.log_group_name.LogGroupName"]
    """<p> The name of the CloudWatch log group. </p>"""
    impact_start_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time the anomalous log events began. The impact start time indicates the time of the first log anomaly event that occurs. </p>"""
    impact_end_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The time the anomalous log events stopped. </p>"""
    number_of_log_lines_scanned: (
        "aws_sdk_devops_guru.types.number_of_log_lines_scanned.NumberOfLogLinesScanned"
    )
    """<p> The number of log lines that were scanned for anomalous log events. </p>"""
    log_anomaly_showcases: NotRequired[
        "aws_sdk_devops_guru.types.log_anomaly_showcases.LogAnomalyShowcases"
    ]
    """<p> The log anomalies in the log group. Each log anomaly displayed represents a cluster of similar anomalous log events. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnomalousLogGroup) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "impact_start_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["ImpactStartTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["impact_start_time"]
        )
    if "impact_end_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["ImpactEndTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["impact_end_time"]
        )
    out["NumberOfLogLinesScanned"] = value.get("number_of_log_lines_scanned", 0)
    if "log_anomaly_showcases" in value:
        import aws_sdk_devops_guru.types.log_anomaly_showcases

        out["LogAnomalyShowcases"] = (
            aws_sdk_devops_guru.types.log_anomaly_showcases.serialize_json(
                value["log_anomaly_showcases"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnomalousLogGroup:
    out: AnomalousLogGroup = {}  # type: ignore[typeddict-item]
    if "LogGroupName" in data:
        out["log_group_name"] = data["LogGroupName"]
    if "ImpactStartTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["impact_start_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["ImpactStartTime"]
        )
    if "ImpactEndTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["impact_end_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["ImpactEndTime"]
        )
    if "NumberOfLogLinesScanned" in data:
        out["number_of_log_lines_scanned"] = data["NumberOfLogLinesScanned"]
    else:
        out["number_of_log_lines_scanned"] = 0
    if "LogAnomalyShowcases" in data:
        import aws_sdk_devops_guru.types.log_anomaly_showcases

        out["log_anomaly_showcases"] = (
            aws_sdk_devops_guru.types.log_anomaly_showcases.deserialize_json(
                data["LogAnomalyShowcases"]
            )
        )
    return out
