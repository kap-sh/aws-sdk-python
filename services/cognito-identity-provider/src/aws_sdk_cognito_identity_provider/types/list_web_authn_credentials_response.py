"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListWebAuthnCredentialsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.pagination_key
    import aws_sdk_cognito_identity_provider.types.web_authn_credential_description_list_type


class ListWebAuthnCredentialsResponse(TypedDict):
    credentials: "aws_sdk_cognito_identity_provider.types.web_authn_credential_description_list_type.WebAuthnCredentialDescriptionListType"
    """<p>A list of registered passkeys for a user.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebAuthnCredentialsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.web_authn_credential_description_list_type

    out["Credentials"] = (
        aws_sdk_cognito_identity_provider.types.web_authn_credential_description_list_type.serialize_aws_json_1_1(
            value["credentials"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebAuthnCredentialsResponse:
    out: ListWebAuthnCredentialsResponse = {}  # type: ignore[typeddict-item]
    if "Credentials" in data:
        import aws_sdk_cognito_identity_provider.types.web_authn_credential_description_list_type

        out["credentials"] = (
            aws_sdk_cognito_identity_provider.types.web_authn_credential_description_list_type.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    else:
        raise DeserializationError(
            "ListWebAuthnCredentialsResponse.credentials required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
