"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListUserPoolClientSecretsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_list_type
    import aws_sdk_cognito_identity_provider.types.pagination_key


class ListUserPoolClientSecretsResponse(TypedDict):
    client_secrets: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_secret_descriptor_list_type.ClientSecretDescriptorListType"
    ]
    """<p>A list of client secret descriptors containing the identifier and creation date for each secret. For security reasons, the response never reveals the actual secret value in ClientSecretValue.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUserPoolClientSecretsResponse) -> dict:
    out: dict = {}
    if "client_secrets" in value:
        import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_list_type

        out["ClientSecrets"] = (
            aws_sdk_cognito_identity_provider.types.client_secret_descriptor_list_type.serialize_aws_json_1_1(
                value["client_secrets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUserPoolClientSecretsResponse:
    out: ListUserPoolClientSecretsResponse = {}  # type: ignore[typeddict-item]
    if "ClientSecrets" in data:
        import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_list_type

        out["client_secrets"] = (
            aws_sdk_cognito_identity_provider.types.client_secret_descriptor_list_type.deserialize_aws_json_1_1(
                data["ClientSecrets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
