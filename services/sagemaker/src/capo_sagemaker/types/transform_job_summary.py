"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.transform_job_arn
    import capo_sagemaker.types.transform_job_name
    import capo_sagemaker.types.transform_job_status


class TransformJobSummary(TypedDict, closed=True):
    transform_job_name: NotRequired[
        "capo_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the transform job.</p>"""
    transform_job_arn: NotRequired[
        "capo_sagemaker.types.transform_job_arn.TransformJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transform job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the transform Job was created.</p>"""
    transform_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job ends on compute instances. For successful jobs and stopped jobs, this is the exact time recorded after the results are uploaded. For failed jobs, this is when Amazon SageMaker detected that the job failed.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Indicates when the transform job was last modified.</p>"""
    transform_job_status: NotRequired[
        "capo_sagemaker.types.transform_job_status.TransformJobStatus"
    ]
    """<p>The status of the transform job.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the transform job failed, the reason it failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformJobSummary) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
    if "transform_job_arn" in value:
        out["TransformJobArn"] = value["transform_job_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "transform_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["TransformEndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["transform_end_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "transform_job_status" in value:
        import capo_sagemaker.types.transform_job_status

        out["TransformJobStatus"] = (
            capo_sagemaker.types.transform_job_status.serialize_aws_json_1_1(
                value["transform_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformJobSummary:
    out: TransformJobSummary = {}  # type: ignore[typeddict-item]
    if "TransformJobName" in data:
        out["transform_job_name"] = data["TransformJobName"]
    if "TransformJobArn" in data:
        out["transform_job_arn"] = data["TransformJobArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "TransformEndTime" in data:
        import capo_sagemaker.types.timestamp

        out["transform_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TransformEndTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "TransformJobStatus" in data:
        import capo_sagemaker.types.transform_job_status

        out["transform_job_status"] = (
            capo_sagemaker.types.transform_job_status.deserialize_aws_json_1_1(
                data["TransformJobStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
