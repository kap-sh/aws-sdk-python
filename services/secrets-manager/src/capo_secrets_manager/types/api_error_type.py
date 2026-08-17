"""Generated from Smithy shape ``com.amazonaws.secretsmanager#APIErrorType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.error_code
    import capo_secrets_manager.types.error_message
    import capo_secrets_manager.types.secret_id_type


class APIErrorType(TypedDict, closed=True):
    secret_id: NotRequired["capo_secrets_manager.types.secret_id_type.SecretIdType"]
    """<p>The ARN or name of the secret.</p>"""
    error_code: NotRequired["capo_secrets_manager.types.error_code.ErrorCode"]
    """<p>The error Secrets Manager encountered while retrieving an individual secret as part of <a>BatchGetSecretValue</a>, for example <code>ResourceNotFoundException</code>,<code>InvalidParameterException</code>, <code>InvalidRequestException</code>, <code>DecryptionFailure</code>, or <code>AccessDeniedException</code>.</p>"""
    message: NotRequired["capo_secrets_manager.types.error_message.ErrorMessage"]
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
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
