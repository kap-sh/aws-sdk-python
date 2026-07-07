"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogAnomalyDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.anomaly_detector_status
    import aws_sdk_cloudwatch_logs.types.anomaly_visibility_time
    import aws_sdk_cloudwatch_logs.types.detector_name
    import aws_sdk_cloudwatch_logs.types.epoch_millis
    import aws_sdk_cloudwatch_logs.types.evaluation_frequency
    import aws_sdk_cloudwatch_logs.types.filter_pattern
    import aws_sdk_cloudwatch_logs.types.kms_key_id
    import aws_sdk_cloudwatch_logs.types.log_group_arn_list


class GetLogAnomalyDetectorResponse(TypedDict, closed=True):
    detector_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.detector_name.DetectorName"
    ]
    """<p>The name of the log anomaly detector</p>"""
    log_group_arn_list: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_arn_list.LogGroupArnList"
    ]
    """<p>An array of structures, where each structure contains the ARN of a log group associated with this anomaly detector.</p>"""
    evaluation_frequency: NotRequired[
        "aws_sdk_cloudwatch_logs.types.evaluation_frequency.EvaluationFrequency"
    ]
    """<p>Specifies how often the anomaly detector runs and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then setting <code>evaluationFrequency</code> to <code>FIFTEEN_MIN</code> might be appropriate.</p>"""
    filter_pattern: NotRequired[
        "aws_sdk_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    anomaly_detector_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.anomaly_detector_status.AnomalyDetectorStatus"
    ]
    r"""<p>Specifies whether the anomaly detector is currently active. To change its status, use the <code>enabled</code> parameter in the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateLogAnomalyDetector.html\">UpdateLogAnomalyDetector</a> operation.</p>"""
    kms_key_id: NotRequired["aws_sdk_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key assigned to this anomaly detector, if any.</p>"""
    creation_time_stamp: "aws_sdk_cloudwatch_logs.types.epoch_millis.EpochMillis"
    """<p>The date and time when this anomaly detector was created.</p>"""
    last_modified_time_stamp: "aws_sdk_cloudwatch_logs.types.epoch_millis.EpochMillis"
    """<p>The date and time when this anomaly detector was most recently modified.</p>"""
    anomaly_visibility_time: NotRequired[
        "aws_sdk_cloudwatch_logs.types.anomaly_visibility_time.AnomalyVisibilityTime"
    ]
    """<p>The number of days used as the life cycle of anomalies. After this time, anomalies are automatically baselined and the anomaly detector model will treat new occurrences of similar event as normal. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogAnomalyDetectorResponse) -> dict:
    out: dict = {}
    if "detector_name" in value:
        out["detectorName"] = value["detector_name"]
    if "log_group_arn_list" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_arn_list

        out["logGroupArnList"] = (
            aws_sdk_cloudwatch_logs.types.log_group_arn_list.serialize_aws_json_1_1(
                value["log_group_arn_list"]
            )
        )
    if "evaluation_frequency" in value:
        import aws_sdk_cloudwatch_logs.types.evaluation_frequency

        out["evaluationFrequency"] = (
            aws_sdk_cloudwatch_logs.types.evaluation_frequency.serialize_aws_json_1_1(
                value["evaluation_frequency"]
            )
        )
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "anomaly_detector_status" in value:
        import aws_sdk_cloudwatch_logs.types.anomaly_detector_status

        out["anomalyDetectorStatus"] = (
            aws_sdk_cloudwatch_logs.types.anomaly_detector_status.serialize_aws_json_1_1(
                value["anomaly_detector_status"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    out["creationTimeStamp"] = value.get("creation_time_stamp", 0)
    out["lastModifiedTimeStamp"] = value.get("last_modified_time_stamp", 0)
    if "anomaly_visibility_time" in value:
        out["anomalyVisibilityTime"] = value["anomaly_visibility_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogAnomalyDetectorResponse:
    out: GetLogAnomalyDetectorResponse = {}  # type: ignore[typeddict-item]
    if "detectorName" in data:
        out["detector_name"] = data["detectorName"]
    if "logGroupArnList" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_arn_list

        out["log_group_arn_list"] = (
            aws_sdk_cloudwatch_logs.types.log_group_arn_list.deserialize_aws_json_1_1(
                data["logGroupArnList"]
            )
        )
    if "evaluationFrequency" in data:
        import aws_sdk_cloudwatch_logs.types.evaluation_frequency

        out["evaluation_frequency"] = (
            aws_sdk_cloudwatch_logs.types.evaluation_frequency.deserialize_aws_json_1_1(
                data["evaluationFrequency"]
            )
        )
    if "filterPattern" in data:
        out["filter_pattern"] = data["filterPattern"]
    if "anomalyDetectorStatus" in data:
        import aws_sdk_cloudwatch_logs.types.anomaly_detector_status

        out["anomaly_detector_status"] = (
            aws_sdk_cloudwatch_logs.types.anomaly_detector_status.deserialize_aws_json_1_1(
                data["anomalyDetectorStatus"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "creationTimeStamp" in data:
        out["creation_time_stamp"] = data["creationTimeStamp"]
    else:
        out["creation_time_stamp"] = 0
    if "lastModifiedTimeStamp" in data:
        out["last_modified_time_stamp"] = data["lastModifiedTimeStamp"]
    else:
        out["last_modified_time_stamp"] = 0
    if "anomalyVisibilityTime" in data:
        out["anomaly_visibility_time"] = data["anomalyVisibilityTime"]
    return out
