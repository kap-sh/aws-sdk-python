"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetSecretValueRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_id_type
    import aws_sdk_secrets_manager.types.secret_version_id_type
    import aws_sdk_secrets_manager.types.secret_version_stage_type


class GetSecretValueRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to retrieve. To retrieve a secret from another account, you must use an ARN.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen\">Finding a secret from a partial ARN</a>.</p>"""
    version_id: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique identifier of the version of the secret to retrieve. If you include both this parameter and <code>VersionStage</code>, the two parameters must refer to the same secret version. If you don't specify either a <code>VersionStage</code> or <code>VersionId</code>, then Secrets Manager returns the <code>AWSCURRENT</code> version.</p> <p>This value is typically a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID-type</a> value with 32 hexadecimal digits.</p>"""
    version_stage: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_stage_type.SecretVersionStageType"
    ]
    """<p>The staging label of the version of the secret to retrieve. </p> <p>Secrets Manager uses staging labels to keep track of different versions during the rotation process. If you include both this parameter and <code>VersionId</code>, the two parameters must refer to the same secret version. If you don't specify either a <code>VersionStage</code> or <code>VersionId</code>, Secrets Manager returns the <code>AWSCURRENT</code> version.</p>"""
