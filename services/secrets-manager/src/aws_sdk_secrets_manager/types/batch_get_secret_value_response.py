"""Generated from Smithy shape ``com.amazonaws.secretsmanager#BatchGetSecretValueResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.api_error_list_type
    import aws_sdk_secrets_manager.types.next_token_type
    import aws_sdk_secrets_manager.types.secret_values_type


class BatchGetSecretValueResponse(TypedDict):
    secret_values: NotRequired[
        "aws_sdk_secrets_manager.types.secret_values_type.SecretValuesType"
    ]
    """<p>A list of secret values.</p>"""
    next_token: NotRequired[
        "aws_sdk_secrets_manager.types.next_token_type.NextTokenType"
    ]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call <code>BatchGetSecretValue</code> again with this value.</p>"""
    errors: NotRequired[
        "aws_sdk_secrets_manager.types.api_error_list_type.APIErrorListType"
    ]
    """<p>A list of errors Secrets Manager encountered while attempting to retrieve individual secrets.</p>"""
