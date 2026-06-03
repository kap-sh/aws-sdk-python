"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretVersionIdsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.next_token_type
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_versions_list_type


class ListSecretVersionIdsResponse(TypedDict):
    versions: NotRequired[
        "aws_sdk_secrets_manager.types.secret_versions_list_type.SecretVersionsListType"
    ]
    """<p>A list of the versions of the secret.</p>"""
    next_token: NotRequired[
        "aws_sdk_secrets_manager.types.next_token_type.NextTokenType"
    ]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call <code>ListSecretVersionIds</code> again with this value. </p>"""
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""
