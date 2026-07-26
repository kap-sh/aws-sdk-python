"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretVersionIdsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.secret_arn_type
    import capo_secrets_manager.types.secret_name_type
    import capo_secrets_manager.types.secret_versions_list_type


class ListSecretVersionIdsResponse(TypedDict, closed=True):
    versions: NotRequired[
        "capo_secrets_manager.types.secret_versions_list_type.SecretVersionsListType"
    ]
    """<p>A list of the versions of the secret.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call <code>ListSecretVersionIds</code> again with this value. </p>"""
    arn: NotRequired["capo_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["capo_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecretVersionIdsResponse) -> dict:
    out: dict = {}
    if "versions" in value:
        import capo_secrets_manager.types.secret_versions_list_type

        out["Versions"] = (
            capo_secrets_manager.types.secret_versions_list_type.serialize_aws_json_1_1(
                value["versions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecretVersionIdsResponse:
    out: ListSecretVersionIdsResponse = {}  # type: ignore[typeddict-item]
    if "Versions" in data:
        import capo_secrets_manager.types.secret_versions_list_type

        out["versions"] = (
            capo_secrets_manager.types.secret_versions_list_type.deserialize_aws_json_1_1(
                data["Versions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
