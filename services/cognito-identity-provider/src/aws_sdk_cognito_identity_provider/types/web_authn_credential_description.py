"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnCredentialDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.date_type
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.web_authn_authenticator_attachment_type
    import aws_sdk_cognito_identity_provider.types.web_authn_authenticator_transports_list


class WebAuthnCredentialDescription(TypedDict, closed=True):
    credential_id: "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    """<p>The unique identifier of the passkey credential.</p>"""
    friendly_credential_name: (
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    )
    """<p>An automatically-generated friendly name for the passkey credential.</p>"""
    relying_party_id: "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    """<p>The relying-party ID of the provider for the passkey credential.</p>"""
    authenticator_attachment: NotRequired[
        "aws_sdk_cognito_identity_provider.types.web_authn_authenticator_attachment_type.WebAuthnAuthenticatorAttachmentType"
    ]
    """<p>The general category of the passkey authenticator. Can be a platform, or on-device authenticator like a built-in fingerprint scanner, or a cross-platform device that's not attached to the device like a Bluetooth security key.</p>"""
    authenticator_transports: "aws_sdk_cognito_identity_provider.types.web_authn_authenticator_transports_list.WebAuthnAuthenticatorTransportsList"
    """<p>Information about the transport methods of the passkey credential, for example USB or Bluetooth Low Energy.</p>"""
    created_at: "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnCredentialDescription) -> dict:
    out: dict = {}
    out["CredentialId"] = value["credential_id"]
    out["FriendlyCredentialName"] = value["friendly_credential_name"]
    out["RelyingPartyId"] = value["relying_party_id"]
    if "authenticator_attachment" in value:
        out["AuthenticatorAttachment"] = value["authenticator_attachment"]
    import aws_sdk_cognito_identity_provider.types.web_authn_authenticator_transports_list

    out["AuthenticatorTransports"] = (
        aws_sdk_cognito_identity_provider.types.web_authn_authenticator_transports_list.serialize_aws_json_1_1(
            value["authenticator_transports"]
        )
    )
    import aws_sdk_cognito_identity_provider.types.date_type

    out["CreatedAt"] = (
        aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAuthnCredentialDescription:
    out: WebAuthnCredentialDescription = {}  # type: ignore[typeddict-item]
    if "CredentialId" in data:
        out["credential_id"] = data["CredentialId"]
    else:
        raise DeserializationError(
            "WebAuthnCredentialDescription.credential_id required"
        )
    if "FriendlyCredentialName" in data:
        out["friendly_credential_name"] = data["FriendlyCredentialName"]
    else:
        raise DeserializationError(
            "WebAuthnCredentialDescription.friendly_credential_name required"
        )
    if "RelyingPartyId" in data:
        out["relying_party_id"] = data["RelyingPartyId"]
    else:
        raise DeserializationError(
            "WebAuthnCredentialDescription.relying_party_id required"
        )
    if "AuthenticatorAttachment" in data:
        out["authenticator_attachment"] = data["AuthenticatorAttachment"]
    if "AuthenticatorTransports" in data:
        import aws_sdk_cognito_identity_provider.types.web_authn_authenticator_transports_list

        out["authenticator_transports"] = (
            aws_sdk_cognito_identity_provider.types.web_authn_authenticator_transports_list.deserialize_aws_json_1_1(
                data["AuthenticatorTransports"]
            )
        )
    else:
        raise DeserializationError(
            "WebAuthnCredentialDescription.authenticator_transports required"
        )
    if "CreatedAt" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["created_at"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("WebAuthnCredentialDescription.created_at required")
    return out
