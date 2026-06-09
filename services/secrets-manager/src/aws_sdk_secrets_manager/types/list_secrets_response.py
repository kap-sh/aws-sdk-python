"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.next_token_type
    import aws_sdk_secrets_manager.types.secret_list_type


class ListSecretsResponse(TypedDict):
    secret_list: NotRequired[
        "aws_sdk_secrets_manager.types.secret_list_type.SecretListType"
    ]
    """<p>A list of the secrets in the account.</p>"""
    next_token: NotRequired[
        "aws_sdk_secrets_manager.types.next_token_type.NextTokenType"
    ]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call <code>ListSecrets</code> again with this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecretsResponse) -> dict:
    out: dict = {}
    if "secret_list" in value:
        import aws_sdk_secrets_manager.types.secret_list_type

        out["SecretList"] = (
            aws_sdk_secrets_manager.types.secret_list_type.serialize_aws_json_1_1(
                value["secret_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecretsResponse:
    out: ListSecretsResponse = {}  # type: ignore[typeddict-item]
    if "SecretList" in data:
        import aws_sdk_secrets_manager.types.secret_list_type

        out["secret_list"] = (
            aws_sdk_secrets_manager.types.secret_list_type.deserialize_aws_json_1_1(
                data["SecretList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
