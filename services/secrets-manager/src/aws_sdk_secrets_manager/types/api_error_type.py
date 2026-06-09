"""Generated from Smithy shape ``com.amazonaws.secretsmanager#APIErrorType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_code
    import aws_sdk_secrets_manager.types.error_message
    import aws_sdk_secrets_manager.types.secret_id_type


class APIErrorType(TypedDict):
    secret_id: NotRequired["aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"]
    """<p>The ARN or name of the secret.</p>"""
    error_code: NotRequired["aws_sdk_secrets_manager.types.error_code.ErrorCode"]
    """<p>The error Secrets Manager encountered while retrieving an individual secret as part of <a>BatchGetSecretValue</a>, for example <code>ResourceNotFoundException</code>,<code>InvalidParameterException</code>, <code>InvalidRequestException</code>, <code>DecryptionFailure</code>, or <code>AccessDeniedException</code>.</p>"""
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]
    """<p>A message describing the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: APIErrorType) -> dict:
    out: dict = {}
    if "secret_id" in value:
        out["SecretId"] = value["secret_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> APIErrorType:
    out: APIErrorType = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
