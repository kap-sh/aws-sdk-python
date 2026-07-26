"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnAuthenticatorTransportsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.web_authn_authenticator_transport_type

WebAuthnAuthenticatorTransportsList: TypeAlias = list[
    "capo_cognito_identity_provider.types.web_authn_authenticator_transport_type.WebAuthnAuthenticatorTransportType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnAuthenticatorTransportsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WebAuthnAuthenticatorTransportsList:
    return list(data)
