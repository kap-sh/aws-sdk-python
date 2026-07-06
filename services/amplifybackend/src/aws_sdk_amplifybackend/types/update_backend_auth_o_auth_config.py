"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthOAuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.list_of__string
    import aws_sdk_amplifybackend.types.list_of_o_auth_scopes_element
    import aws_sdk_amplifybackend.types.o_auth_grant_type
    import aws_sdk_amplifybackend.types.social_provider_settings


class UpdateBackendAuthOAuthConfig(TypedDict, closed=True):
    domain_prefix: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The Amazon Cognito domain prefix used to create a hosted UI for authentication.</p>"""
    o_auth_grant_type: NotRequired[
        "aws_sdk_amplifybackend.types.o_auth_grant_type.OAuthGrantType"
    ]
    """<p>The OAuth grant type to allow app users to authenticate from your Amplify app.</p>"""
    o_auth_scopes: NotRequired[
        "aws_sdk_amplifybackend.types.list_of_o_auth_scopes_element.ListOfOAuthScopesElement"
    ]
    """<p>The list of OAuth-related flows that can allow users to authenticate from your Amplify app.</p>"""
    redirect_sign_in_ur_is: NotRequired[
        "aws_sdk_amplifybackend.types.list_of__string.ListOf__string"
    ]
    """<p>Redirect URLs that OAuth uses when a user signs in to an Amplify app.</p>"""
    redirect_sign_out_ur_is: NotRequired[
        "aws_sdk_amplifybackend.types.list_of__string.ListOf__string"
    ]
    """<p>Redirect URLs that OAuth uses when a user signs out of an Amplify app.</p>"""
    social_provider_settings: NotRequired[
        "aws_sdk_amplifybackend.types.social_provider_settings.SocialProviderSettings"
    ]
    """<p>Describes third-party social federation configurations for allowing your users to sign in with OAuth.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthOAuthConfig) -> dict:
    out: dict = {}
    if "domain_prefix" in value:
        out["domainPrefix"] = value["domain_prefix"]
    if "o_auth_grant_type" in value:
        import aws_sdk_amplifybackend.types.o_auth_grant_type

        out["oAuthGrantType"] = (
            aws_sdk_amplifybackend.types.o_auth_grant_type.serialize_json(
                value["o_auth_grant_type"]
            )
        )
    if "o_auth_scopes" in value:
        import aws_sdk_amplifybackend.types.list_of_o_auth_scopes_element

        out["oAuthScopes"] = (
            aws_sdk_amplifybackend.types.list_of_o_auth_scopes_element.serialize_json(
                value["o_auth_scopes"]
            )
        )
    if "redirect_sign_in_ur_is" in value:
        import aws_sdk_amplifybackend.types.list_of__string

        out["redirectSignInURIs"] = (
            aws_sdk_amplifybackend.types.list_of__string.serialize_json(
                value["redirect_sign_in_ur_is"]
            )
        )
    if "redirect_sign_out_ur_is" in value:
        import aws_sdk_amplifybackend.types.list_of__string

        out["redirectSignOutURIs"] = (
            aws_sdk_amplifybackend.types.list_of__string.serialize_json(
                value["redirect_sign_out_ur_is"]
            )
        )
    if "social_provider_settings" in value:
        import aws_sdk_amplifybackend.types.social_provider_settings

        out["socialProviderSettings"] = (
            aws_sdk_amplifybackend.types.social_provider_settings.serialize_json(
                value["social_provider_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthOAuthConfig:
    out: UpdateBackendAuthOAuthConfig = {}  # type: ignore[typeddict-item]
    if "domainPrefix" in data:
        out["domain_prefix"] = data["domainPrefix"]
    if "oAuthGrantType" in data:
        import aws_sdk_amplifybackend.types.o_auth_grant_type

        out["o_auth_grant_type"] = (
            aws_sdk_amplifybackend.types.o_auth_grant_type.deserialize_json(
                data["oAuthGrantType"]
            )
        )
    if "oAuthScopes" in data:
        import aws_sdk_amplifybackend.types.list_of_o_auth_scopes_element

        out["o_auth_scopes"] = (
            aws_sdk_amplifybackend.types.list_of_o_auth_scopes_element.deserialize_json(
                data["oAuthScopes"]
            )
        )
    if "redirectSignInURIs" in data:
        import aws_sdk_amplifybackend.types.list_of__string

        out["redirect_sign_in_ur_is"] = (
            aws_sdk_amplifybackend.types.list_of__string.deserialize_json(
                data["redirectSignInURIs"]
            )
        )
    if "redirectSignOutURIs" in data:
        import aws_sdk_amplifybackend.types.list_of__string

        out["redirect_sign_out_ur_is"] = (
            aws_sdk_amplifybackend.types.list_of__string.deserialize_json(
                data["redirectSignOutURIs"]
            )
        )
    if "socialProviderSettings" in data:
        import aws_sdk_amplifybackend.types.social_provider_settings

        out["social_provider_settings"] = (
            aws_sdk_amplifybackend.types.social_provider_settings.deserialize_json(
                data["socialProviderSettings"]
            )
        )
    return out
