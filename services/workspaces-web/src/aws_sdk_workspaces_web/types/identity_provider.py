"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IdentityProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.identity_provider_details
    import aws_sdk_workspaces_web.types.identity_provider_name
    import aws_sdk_workspaces_web.types.identity_provider_type
    import aws_sdk_workspaces_web.types.subresource_arn


class IdentityProvider(TypedDict):
    identity_provider_arn: "aws_sdk_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""
    identity_provider_name: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider_name.IdentityProviderName"
    ]
    """<p>The identity provider name.</p>"""
    identity_provider_type: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider_type.IdentityProviderType"
    ]
    """<p>The identity provider type.</p>"""
    identity_provider_details: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider_details.IdentityProviderDetails"
    ]
    """<p>The identity provider details. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by oidc_issuer key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by oidc_issuer key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by oidc_issuer key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by oidc_issuer key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProvider) -> dict:
    out: dict = {}
    out["identityProviderArn"] = value["identity_provider_arn"]
    if "identity_provider_name" in value:
        out["identityProviderName"] = value["identity_provider_name"]
    if "identity_provider_type" in value:
        out["identityProviderType"] = value["identity_provider_type"]
    if "identity_provider_details" in value:
        import aws_sdk_workspaces_web.types.identity_provider_details

        out["identityProviderDetails"] = (
            aws_sdk_workspaces_web.types.identity_provider_details.serialize_json(
                value["identity_provider_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> IdentityProvider:
    out: IdentityProvider = {}  # type: ignore[typeddict-item]
    if "identityProviderArn" in data:
        out["identity_provider_arn"] = data["identityProviderArn"]
    else:
        raise DeserializationError("IdentityProvider.identity_provider_arn required")
    if "identityProviderName" in data:
        out["identity_provider_name"] = data["identityProviderName"]
    if "identityProviderType" in data:
        out["identity_provider_type"] = data["identityProviderType"]
    if "identityProviderDetails" in data:
        import aws_sdk_workspaces_web.types.identity_provider_details

        out["identity_provider_details"] = (
            aws_sdk_workspaces_web.types.identity_provider_details.deserialize_json(
                data["identityProviderDetails"]
            )
        )
    return out
