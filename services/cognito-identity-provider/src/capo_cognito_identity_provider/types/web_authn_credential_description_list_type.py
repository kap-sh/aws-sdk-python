"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnCredentialDescriptionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.web_authn_credential_description

WebAuthnCredentialDescriptionListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.web_authn_credential_description.WebAuthnCredentialDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnCredentialDescriptionListType) -> list:
    import capo_cognito_identity_provider.types.web_authn_credential_description

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.web_authn_credential_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WebAuthnCredentialDescriptionListType:
    import capo_cognito_identity_provider.types.web_authn_credential_description

    out: WebAuthnCredentialDescriptionListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.web_authn_credential_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
