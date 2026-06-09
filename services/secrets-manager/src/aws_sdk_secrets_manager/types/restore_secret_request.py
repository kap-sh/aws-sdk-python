"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RestoreSecretRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_id_type


class RestoreSecretRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to restore.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen\">Finding a secret from a partial ARN</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreSecretRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreSecretRequest:
    out: RestoreSecretRequest = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("RestoreSecretRequest.secret_id required")
    return out
