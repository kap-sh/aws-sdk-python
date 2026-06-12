"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_experiment_description
    import aws_sdk_sagemaker.types.inference_experiment_name
    import aws_sdk_sagemaker.types.inference_experiment_schedule
    import aws_sdk_sagemaker.types.inference_experiment_status
    import aws_sdk_sagemaker.types.inference_experiment_status_reason
    import aws_sdk_sagemaker.types.inference_experiment_type
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp


class InferenceExperimentSummary(TypedDict):
    name: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name of the inference experiment.</p>"""
    type: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_type.InferenceExperimentType"
    ]
    """<p>The type of the inference experiment.</p>"""
    schedule: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_schedule.InferenceExperimentSchedule"
    ]
    """<p>The duration for which the inference experiment ran or will run.</p> <p>The maximum duration that you can set for an inference experiment is 30 days.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_status.InferenceExperimentStatus"
    ]
    """<p>The status of the inference experiment.</p>"""
    status_reason: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_status_reason.InferenceExperimentStatusReason"
    ]
    """<p>The error message for the inference experiment status result.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_description.InferenceExperimentDescription"
    ]
    """<p>The description of the inference experiment.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp at which the inference experiment was created.</p>"""
    completion_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp at which the inference experiment was completed.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when you last modified the inference experiment.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p> The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExperimentSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_sagemaker.types.inference_experiment_type

        out["Type"] = (
            aws_sdk_sagemaker.types.inference_experiment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "schedule" in value:
        import aws_sdk_sagemaker.types.inference_experiment_schedule

        out["Schedule"] = (
            aws_sdk_sagemaker.types.inference_experiment_schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "status" in value:
        import aws_sdk_sagemaker.types.inference_experiment_status

        out["Status"] = (
            aws_sdk_sagemaker.types.inference_experiment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "completion_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CompletionTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["completion_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceExperimentSummary:
    out: InferenceExperimentSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.inference_experiment_type

        out["type"] = (
            aws_sdk_sagemaker.types.inference_experiment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Schedule" in data:
        import aws_sdk_sagemaker.types.inference_experiment_schedule

        out["schedule"] = (
            aws_sdk_sagemaker.types.inference_experiment_schedule.deserialize_aws_json_1_1(
                data["Schedule"]
            )
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.inference_experiment_status

        out["status"] = (
            aws_sdk_sagemaker.types.inference_experiment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["completion_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
