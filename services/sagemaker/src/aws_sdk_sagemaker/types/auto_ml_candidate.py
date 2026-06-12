"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLCandidate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_container_definitions
    import aws_sdk_sagemaker.types.auto_ml_failure_reason
    import aws_sdk_sagemaker.types.auto_ml_inference_container_definitions
    import aws_sdk_sagemaker.types.candidate_name
    import aws_sdk_sagemaker.types.candidate_properties
    import aws_sdk_sagemaker.types.candidate_status
    import aws_sdk_sagemaker.types.candidate_steps
    import aws_sdk_sagemaker.types.final_auto_ml_job_objective_metric
    import aws_sdk_sagemaker.types.objective_status
    import aws_sdk_sagemaker.types.timestamp


class AutoMLCandidate(TypedDict):
    candidate_name: NotRequired["aws_sdk_sagemaker.types.candidate_name.CandidateName"]
    """<p>The name of the candidate.</p>"""
    final_auto_ml_job_objective_metric: NotRequired[
        "aws_sdk_sagemaker.types.final_auto_ml_job_objective_metric.FinalAutoMLJobObjectiveMetric"
    ]
    objective_status: NotRequired[
        "aws_sdk_sagemaker.types.objective_status.ObjectiveStatus"
    ]
    """<p>The objective's status.</p>"""
    candidate_steps: NotRequired[
        "aws_sdk_sagemaker.types.candidate_steps.CandidateSteps"
    ]
    """<p>Information about the candidate's steps.</p>"""
    candidate_status: NotRequired[
        "aws_sdk_sagemaker.types.candidate_status.CandidateStatus"
    ]
    """<p>The candidate's status.</p>"""
    inference_containers: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_container_definitions.AutoMLContainerDefinitions"
    ]
    """<p>Information about the recommended inference container definitions.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end time.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last modified time.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_failure_reason.AutoMLFailureReason"
    ]
    """<p>The failure reason.</p>"""
    candidate_properties: NotRequired[
        "aws_sdk_sagemaker.types.candidate_properties.CandidateProperties"
    ]
    """<p>The properties of an AutoML candidate job.</p>"""
    inference_container_definitions: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_inference_container_definitions.AutoMLInferenceContainerDefinitions"
    ]
    """<p>The mapping of all supported processing unit (CPU, GPU, etc...) to inference container definitions for the candidate. This field is populated for the AutoML jobs V2 (for example, for jobs created by calling <code>CreateAutoMLJobV2</code>) related to image or text classification problem types only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLCandidate) -> dict:
    out: dict = {}
    if "candidate_name" in value:
        out["CandidateName"] = value["candidate_name"]
    if "final_auto_ml_job_objective_metric" in value:
        import aws_sdk_sagemaker.types.final_auto_ml_job_objective_metric

        out["FinalAutoMLJobObjectiveMetric"] = (
            aws_sdk_sagemaker.types.final_auto_ml_job_objective_metric.serialize_aws_json_1_1(
                value["final_auto_ml_job_objective_metric"]
            )
        )
    if "objective_status" in value:
        import aws_sdk_sagemaker.types.objective_status

        out["ObjectiveStatus"] = (
            aws_sdk_sagemaker.types.objective_status.serialize_aws_json_1_1(
                value["objective_status"]
            )
        )
    if "candidate_steps" in value:
        import aws_sdk_sagemaker.types.candidate_steps

        out["CandidateSteps"] = (
            aws_sdk_sagemaker.types.candidate_steps.serialize_aws_json_1_1(
                value["candidate_steps"]
            )
        )
    if "candidate_status" in value:
        import aws_sdk_sagemaker.types.candidate_status

        out["CandidateStatus"] = (
            aws_sdk_sagemaker.types.candidate_status.serialize_aws_json_1_1(
                value["candidate_status"]
            )
        )
    if "inference_containers" in value:
        import aws_sdk_sagemaker.types.auto_ml_container_definitions

        out["InferenceContainers"] = (
            aws_sdk_sagemaker.types.auto_ml_container_definitions.serialize_aws_json_1_1(
                value["inference_containers"]
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
    if "candidate_properties" in value:
        import aws_sdk_sagemaker.types.candidate_properties

        out["CandidateProperties"] = (
            aws_sdk_sagemaker.types.candidate_properties.serialize_aws_json_1_1(
                value["candidate_properties"]
            )
        )
    if "inference_container_definitions" in value:
        import aws_sdk_sagemaker.types.auto_ml_inference_container_definitions

        out["InferenceContainerDefinitions"] = (
            aws_sdk_sagemaker.types.auto_ml_inference_container_definitions.serialize_aws_json_1_1(
                value["inference_container_definitions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLCandidate:
    out: AutoMLCandidate = {}  # type: ignore[typeddict-item]
    if "CandidateName" in data:
        out["candidate_name"] = data["CandidateName"]
    if "FinalAutoMLJobObjectiveMetric" in data:
        import aws_sdk_sagemaker.types.final_auto_ml_job_objective_metric

        out["final_auto_ml_job_objective_metric"] = (
            aws_sdk_sagemaker.types.final_auto_ml_job_objective_metric.deserialize_aws_json_1_1(
                data["FinalAutoMLJobObjectiveMetric"]
            )
        )
    if "ObjectiveStatus" in data:
        import aws_sdk_sagemaker.types.objective_status

        out["objective_status"] = (
            aws_sdk_sagemaker.types.objective_status.deserialize_aws_json_1_1(
                data["ObjectiveStatus"]
            )
        )
    if "CandidateSteps" in data:
        import aws_sdk_sagemaker.types.candidate_steps

        out["candidate_steps"] = (
            aws_sdk_sagemaker.types.candidate_steps.deserialize_aws_json_1_1(
                data["CandidateSteps"]
            )
        )
    if "CandidateStatus" in data:
        import aws_sdk_sagemaker.types.candidate_status

        out["candidate_status"] = (
            aws_sdk_sagemaker.types.candidate_status.deserialize_aws_json_1_1(
                data["CandidateStatus"]
            )
        )
    if "InferenceContainers" in data:
        import aws_sdk_sagemaker.types.auto_ml_container_definitions

        out["inference_containers"] = (
            aws_sdk_sagemaker.types.auto_ml_container_definitions.deserialize_aws_json_1_1(
                data["InferenceContainers"]
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
    if "CandidateProperties" in data:
        import aws_sdk_sagemaker.types.candidate_properties

        out["candidate_properties"] = (
            aws_sdk_sagemaker.types.candidate_properties.deserialize_aws_json_1_1(
                data["CandidateProperties"]
            )
        )
    if "InferenceContainerDefinitions" in data:
        import aws_sdk_sagemaker.types.auto_ml_inference_container_definitions

        out["inference_container_definitions"] = (
            aws_sdk_sagemaker.types.auto_ml_inference_container_definitions.deserialize_aws_json_1_1(
                data["InferenceContainerDefinitions"]
            )
        )
    return out
