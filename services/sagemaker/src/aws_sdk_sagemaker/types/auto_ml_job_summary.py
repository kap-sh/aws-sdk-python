"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_failure_reason
    import aws_sdk_sagemaker.types.auto_ml_job_arn
    import aws_sdk_sagemaker.types.auto_ml_job_name
    import aws_sdk_sagemaker.types.auto_ml_job_secondary_status
    import aws_sdk_sagemaker.types.auto_ml_job_status
    import aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons
    import aws_sdk_sagemaker.types.timestamp


class AutoMLJobSummary(TypedDict, closed=True):
    auto_ml_job_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_name.AutoMLJobName"
    ]
    """<p>The name of the AutoML job you are requesting.</p>"""
    auto_ml_job_arn: NotRequired["aws_sdk_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The ARN of the AutoML job.</p>"""
    auto_ml_job_status: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_status.AutoMLJobStatus"
    ]
    """<p>The status of the AutoML job.</p>"""
    auto_ml_job_secondary_status: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_secondary_status.AutoMLJobSecondaryStatus"
    ]
    """<p>The secondary status of the AutoML job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the AutoML job was created.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end time of an AutoML job.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>When the AutoML job was last modified.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_failure_reason.AutoMLFailureReason"
    ]
    """<p>The failure reason of an AutoML job.</p>"""
    partial_failure_reasons: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons.AutoMLPartialFailureReasons"
    ]
    """<p>The list of reasons for partial failures within an AutoML job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobSummary) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    if "auto_ml_job_status" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_status

        out["AutoMLJobStatus"] = (
            aws_sdk_sagemaker.types.auto_ml_job_status.serialize_aws_json_1_1(
                value["auto_ml_job_status"]
            )
        )
    if "auto_ml_job_secondary_status" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_secondary_status

        out["AutoMLJobSecondaryStatus"] = (
            aws_sdk_sagemaker.types.auto_ml_job_secondary_status.serialize_aws_json_1_1(
                value["auto_ml_job_secondary_status"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "partial_failure_reasons" in value:
        import aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons

        out["PartialFailureReasons"] = (
            aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons.serialize_aws_json_1_1(
                value["partial_failure_reasons"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobSummary:
    out: AutoMLJobSummary = {}  # type: ignore[typeddict-item]
    if "AutoMLJobName" in data:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    if "AutoMLJobStatus" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_status

        out["auto_ml_job_status"] = (
            aws_sdk_sagemaker.types.auto_ml_job_status.deserialize_aws_json_1_1(
                data["AutoMLJobStatus"]
            )
        )
    if "AutoMLJobSecondaryStatus" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_secondary_status

        out["auto_ml_job_secondary_status"] = (
            aws_sdk_sagemaker.types.auto_ml_job_secondary_status.deserialize_aws_json_1_1(
                data["AutoMLJobSecondaryStatus"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "PartialFailureReasons" in data:
        import aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons

        out["partial_failure_reasons"] = (
            aws_sdk_sagemaker.types.auto_ml_partial_failure_reasons.deserialize_aws_json_1_1(
                data["PartialFailureReasons"]
            )
        )
    return out
