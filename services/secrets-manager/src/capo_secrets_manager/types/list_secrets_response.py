"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.secret_list_type


class ListSecretsResponse(TypedDict, closed=True):
    secret_list: NotRequired[
        "capo_secrets_manager.types.secret_list_type.SecretListType"
    ]
    """<p>A list of the secrets in the account.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call <code>ListSecrets</code> again with this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecretsResponse) -> dict:
    out: dict = {}
    if "secret_list" in value:
        import capo_secrets_manager.types.secret_list_type

        out["SecretList"] = (
            capo_secrets_manager.types.secret_list_type.serialize_aws_json_1_1(
                value["secret_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecretsResponse:
    out: ListSecretsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SecretList") is not None:
        import capo_secrets_manager.types.secret_list_type

        out["secret_list"] = (
            capo_secrets_manager.types.secret_list_type.deserialize_aws_json_1_1(
                data["SecretList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
