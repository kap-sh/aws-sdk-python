"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCopyJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_id
    import aws_sdk_bedrock.types.custom_model_arn
    import aws_sdk_bedrock.types.custom_model_name
    import aws_sdk_bedrock.types.error_message
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.model_arn
    import aws_sdk_bedrock.types.model_copy_job_arn
    import aws_sdk_bedrock.types.model_copy_job_status
    import aws_sdk_bedrock.types.tag_list
    import aws_sdk_bedrock.types.timestamp


class ModelCopyJobSummary(TypedDict, closed=True):
    job_arn: "aws_sdk_bedrock.types.model_copy_job_arn.ModelCopyJobArn"
    """<p>The Amazon Resoource Name (ARN) of the model copy job.</p>"""
    status: "aws_sdk_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
    """<p>The status of the model copy job.</p>"""
    creation_time: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The time that the model copy job was created.</p>"""
    target_model_arn: "aws_sdk_bedrock.types.custom_model_arn.CustomModelArn"
    """<p>The Amazon Resource Name (ARN) of the copied model.</p>"""
    target_model_name: NotRequired[
        "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>The name of the copied model.</p>"""
    source_account_id: "aws_sdk_bedrock.types.account_id.AccountId"
    """<p>The unique identifier of the account that the model being copied originated from.</p>"""
    source_model_arn: "aws_sdk_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the original model being copied.</p>"""
    target_model_kms_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the copied model.</p>"""
    target_model_tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>Tags associated with the copied model.</p>"""
    failure_message: NotRequired["aws_sdk_bedrock.types.error_message.ErrorMessage"]
    """<p>If a model fails to be copied, a message describing why the job failed is included here.</p>"""
    source_model_name: NotRequired[
        "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>The name of the original model being copied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelCopyJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    import aws_sdk_bedrock.types.model_copy_job_status

    out["status"] = aws_sdk_bedrock.types.model_copy_job_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    out["targetModelArn"] = value["target_model_arn"]
    if "target_model_name" in value:
        out["targetModelName"] = value["target_model_name"]
    out["sourceAccountId"] = value["source_account_id"]
    out["sourceModelArn"] = value["source_model_arn"]
    if "target_model_kms_key_arn" in value:
        out["targetModelKmsKeyArn"] = value["target_model_kms_key_arn"]
    if "target_model_tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["targetModelTags"] = aws_sdk_bedrock.types.tag_list.serialize_json(
            value["target_model_tags"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "source_model_name" in value:
        out["sourceModelName"] = value["source_model_name"]
    return out


def deserialize_json(data: dict) -> ModelCopyJobSummary:
    out: ModelCopyJobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("ModelCopyJobSummary.job_arn required")
    if "status" in data:
        import aws_sdk_bedrock.types.model_copy_job_status

        out["status"] = aws_sdk_bedrock.types.model_copy_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ModelCopyJobSummary.status required")
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ModelCopyJobSummary.creation_time required")
    if "targetModelArn" in data:
        out["target_model_arn"] = data["targetModelArn"]
    else:
        raise DeserializationError("ModelCopyJobSummary.target_model_arn required")
    if "targetModelName" in data:
        out["target_model_name"] = data["targetModelName"]
    if "sourceAccountId" in data:
        out["source_account_id"] = data["sourceAccountId"]
    else:
        raise DeserializationError("ModelCopyJobSummary.source_account_id required")
    if "sourceModelArn" in data:
        out["source_model_arn"] = data["sourceModelArn"]
    else:
        raise DeserializationError("ModelCopyJobSummary.source_model_arn required")
    if "targetModelKmsKeyArn" in data:
        out["target_model_kms_key_arn"] = data["targetModelKmsKeyArn"]
    if "targetModelTags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["target_model_tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(
            data["targetModelTags"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "sourceModelName" in data:
        out["source_model_name"] = data["sourceModelName"]
    return out
