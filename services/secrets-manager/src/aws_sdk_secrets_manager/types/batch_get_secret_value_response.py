"""Generated from Smithy shape ``com.amazonaws.secretsmanager#BatchGetSecretValueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.api_error_list_type
    import aws_sdk_secrets_manager.types.next_token_type
    import aws_sdk_secrets_manager.types.secret_values_type


class BatchGetSecretValueResponse(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSecretValueResponse) -> dict:
    out: dict = {}
    if "secret_values" in value:
        import aws_sdk_secrets_manager.types.secret_values_type

        out["SecretValues"] = (
            aws_sdk_secrets_manager.types.secret_values_type.serialize_aws_json_1_1(
                value["secret_values"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "errors" in value:
        import aws_sdk_secrets_manager.types.api_error_list_type

        out["Errors"] = (
            aws_sdk_secrets_manager.types.api_error_list_type.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSecretValueResponse:
    out: BatchGetSecretValueResponse = {}  # type: ignore[typeddict-item]
    if "SecretValues" in data:
        import aws_sdk_secrets_manager.types.secret_values_type

        out["secret_values"] = (
            aws_sdk_secrets_manager.types.secret_values_type.deserialize_aws_json_1_1(
                data["SecretValues"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Errors" in data:
        import aws_sdk_secrets_manager.types.api_error_list_type

        out["errors"] = (
            aws_sdk_secrets_manager.types.api_error_list_type.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
