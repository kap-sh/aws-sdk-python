"""Generated from Smithy shape ``com.amazonaws.bedrock#GetEvaluationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.application_type
    import capo_bedrock.types.error_messages
    import capo_bedrock.types.evaluation_config
    import capo_bedrock.types.evaluation_inference_config
    import capo_bedrock.types.evaluation_job_arn
    import capo_bedrock.types.evaluation_job_description
    import capo_bedrock.types.evaluation_job_name
    import capo_bedrock.types.evaluation_job_status
    import capo_bedrock.types.evaluation_job_type
    import capo_bedrock.types.evaluation_output_data_config
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.timestamp


class GetEvaluationJobResponse(TypedDict, closed=True):
    job_name: "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
    """<p>The name for the evaluation job.</p>"""
    status: "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
    """<p>The current status of the evaluation job.</p>"""
    job_arn: "capo_bedrock.types.evaluation_job_arn.EvaluationJobArn"
    """<p>The Amazon Resource Name (ARN) of the evaluation job.</p>"""
    job_description: NotRequired[
        "capo_bedrock.types.evaluation_job_description.EvaluationJobDescription"
    ]
    """<p>The description of the evaluation job.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM service role used in the evaluation job.</p>"""
    customer_encryption_key_id: NotRequired["capo_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of the customer managed encryption key specified when the evaluation job was created.</p>"""
    job_type: "capo_bedrock.types.evaluation_job_type.EvaluationJobType"
    """<p>Specifies whether the evaluation job is automated or human-based.</p>"""
    application_type: NotRequired["capo_bedrock.types.application_type.ApplicationType"]
    """<p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>"""
    evaluation_config: "capo_bedrock.types.evaluation_config.EvaluationConfig"
    """<p>Contains the configuration details of either an automated or human-based evaluation job.</p>"""
    inference_config: (
        "capo_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig"
    )
    """<p>Contains the configuration details of the inference model used for the evaluation job. </p>"""
    output_data_config: (
        "capo_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig"
    )
    """<p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time the evaluation job was created.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time the evaluation job was last modified.</p>"""
    failure_messages: NotRequired["capo_bedrock.types.error_messages.ErrorMessages"]
    """<p>A list of strings that specify why the evaluation job failed to create.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluationJobResponse) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    import capo_bedrock.types.evaluation_job_status

    out["status"] = capo_bedrock.types.evaluation_job_status.serialize_json(
        value["status"]
    )
    out["jobArn"] = value["job_arn"]
    if "job_description" in value:
        out["jobDescription"] = value["job_description"]
    out["roleArn"] = value["role_arn"]
    if "customer_encryption_key_id" in value:
        out["customerEncryptionKeyId"] = value["customer_encryption_key_id"]
    import capo_bedrock.types.evaluation_job_type

    out["jobType"] = capo_bedrock.types.evaluation_job_type.serialize_json(
        value["job_type"]
    )
    if "application_type" in value:
        import capo_bedrock.types.application_type

        out["applicationType"] = capo_bedrock.types.application_type.serialize_json(
            value["application_type"]
        )
    import capo_bedrock.types.evaluation_config

    out["evaluationConfig"] = capo_bedrock.types.evaluation_config.serialize_json(
        value["evaluation_config"]
    )
    import capo_bedrock.types.evaluation_inference_config

    out["inferenceConfig"] = (
        capo_bedrock.types.evaluation_inference_config.serialize_json(
            value["inference_config"]
        )
    )
    import capo_bedrock.types.evaluation_output_data_config

    out["outputDataConfig"] = (
        capo_bedrock.types.evaluation_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "failure_messages" in value:
        import capo_bedrock.types.error_messages

        out["failureMessages"] = capo_bedrock.types.error_messages.serialize_json(
            value["failure_messages"]
        )
    return out


def deserialize_json(data: dict) -> GetEvaluationJobResponse:
    out: GetEvaluationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("GetEvaluationJobResponse.job_name required")
    if "status" in data:
        import capo_bedrock.types.evaluation_job_status

        out["status"] = capo_bedrock.types.evaluation_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetEvaluationJobResponse.status required")
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetEvaluationJobResponse.job_arn required")
    if "jobDescription" in data:
        out["job_description"] = data["jobDescription"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetEvaluationJobResponse.role_arn required")
    if "customerEncryptionKeyId" in data:
        out["customer_encryption_key_id"] = data["customerEncryptionKeyId"]
    if "jobType" in data:
        import capo_bedrock.types.evaluation_job_type

        out["job_type"] = capo_bedrock.types.evaluation_job_type.deserialize_json(
            data["jobType"]
        )
    else:
        raise DeserializationError("GetEvaluationJobResponse.job_type required")
    if "applicationType" in data:
        import capo_bedrock.types.application_type

        out["application_type"] = capo_bedrock.types.application_type.deserialize_json(
            data["applicationType"]
        )
    if "evaluationConfig" in data:
        import capo_bedrock.types.evaluation_config

        out["evaluation_config"] = (
            capo_bedrock.types.evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetEvaluationJobResponse.evaluation_config required"
        )
    if "inferenceConfig" in data:
        import capo_bedrock.types.evaluation_inference_config

        out["inference_config"] = (
            capo_bedrock.types.evaluation_inference_config.deserialize_json(
                data["inferenceConfig"]
            )
        )
    else:
        raise DeserializationError("GetEvaluationJobResponse.inference_config required")
    if "outputDataConfig" in data:
        import capo_bedrock.types.evaluation_output_data_config

        out["output_data_config"] = (
            capo_bedrock.types.evaluation_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetEvaluationJobResponse.output_data_config required"
        )
    if "creationTime" in data:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetEvaluationJobResponse.creation_time required")
    if "lastModifiedTime" in data:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if "failureMessages" in data:
        import capo_bedrock.types.error_messages

        out["failure_messages"] = capo_bedrock.types.error_messages.deserialize_json(
            data["failureMessages"]
        )
    return out
