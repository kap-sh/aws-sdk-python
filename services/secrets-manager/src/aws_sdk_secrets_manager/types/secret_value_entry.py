"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretValueEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.created_date_type
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_binary_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_string_type
    import aws_sdk_secrets_manager.types.secret_version_id_type
    import aws_sdk_secrets_manager.types.secret_version_stages_type


class SecretValueEntry(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The Amazon Resource Name (ARN) of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The friendly name of the secret. </p>"""
    version_id: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType"
    ]
    """<p>The unique version identifier of this version of the secret.</p>"""
    secret_binary: NotRequired[
        "aws_sdk_secrets_manager.types.secret_binary_type.SecretBinaryType"
    ]
    """<p>The decrypted secret value, if the secret value was originally provided as binary data in the form of a byte array. The parameter represents the binary data as a <a href=\"https://tools.ietf.org/html/rfc4648#section-4\">base64-encoded</a> string.</p>"""
    secret_string: NotRequired[
        "aws_sdk_secrets_manager.types.secret_string_type.SecretStringType"
    ]
    """<p>The decrypted secret value, if the secret value was originally provided as a string or through the Secrets Manager console.</p>"""
    version_stages: NotRequired[
        "aws_sdk_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType"
    ]
    """<p>A list of all of the staging labels currently attached to this version of the secret.</p>"""
    created_date: NotRequired[
        "aws_sdk_secrets_manager.types.created_date_type.CreatedDateType"
    ]
    """<p>The date the secret was created.</p>"""
