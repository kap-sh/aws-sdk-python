"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelCopyJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_name
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.kms_key_id
    import aws_sdk_bedrock.types.model_arn
    import aws_sdk_bedrock.types.tag_list


class CreateModelCopyJobRequest(TypedDict):
    source_model_arn: "aws_sdk_bedrock.types.model_arn.ModelArn"
    """<p>The Amazon Resource Name (ARN) of the model to be copied.</p>"""
    target_model_name: "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    """<p>A name for the copied model.</p>"""
    model_kms_key_id: NotRequired["aws_sdk_bedrock.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key that you use to encrypt the model copy.</p>"""
    target_model_tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>Tags to associate with the target model. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html\">Tag resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelCopyJobRequest) -> dict:
    out: dict = {}
    out["sourceModelArn"] = value["source_model_arn"]
    out["targetModelName"] = value["target_model_name"]
    if "model_kms_key_id" in value:
        out["modelKmsKeyId"] = value["model_kms_key_id"]
    if "target_model_tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["targetModelTags"] = aws_sdk_bedrock.types.tag_list.serialize_json(
            value["target_model_tags"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateModelCopyJobRequest:
    out: CreateModelCopyJobRequest = {}  # type: ignore[typeddict-item]
    if "sourceModelArn" in data:
        out["source_model_arn"] = data["sourceModelArn"]
    else:
        raise DeserializationError(
            "CreateModelCopyJobRequest.source_model_arn required"
        )
    if "targetModelName" in data:
        out["target_model_name"] = data["targetModelName"]
    else:
        raise DeserializationError(
            "CreateModelCopyJobRequest.target_model_name required"
        )
    if "modelKmsKeyId" in data:
        out["model_kms_key_id"] = data["modelKmsKeyId"]
    if "targetModelTags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["target_model_tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(
            data["targetModelTags"]
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
