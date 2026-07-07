"""Generated from Smithy shape ``com.amazonaws.sagemaker#OidcConfigForResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.authentication_request_extra_params
    import aws_sdk_sagemaker.types.client_id
    import aws_sdk_sagemaker.types.oidc_endpoint
    import aws_sdk_sagemaker.types.scope


class OidcConfigForResponse(TypedDict, closed=True):
    client_id: NotRequired["aws_sdk_sagemaker.types.client_id.ClientId"]
    """<p>The OIDC IdP client ID used to configure your private workforce.</p>"""
    issuer: NotRequired["aws_sdk_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP issuer used to configure your private workforce.</p>"""
    authorization_endpoint: NotRequired[
        "aws_sdk_sagemaker.types.oidc_endpoint.OidcEndpoint"
    ]
    """<p>The OIDC IdP authorization endpoint used to configure your private workforce.</p>"""
    token_endpoint: NotRequired["aws_sdk_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP token endpoint used to configure your private workforce.</p>"""
    user_info_endpoint: NotRequired[
        "aws_sdk_sagemaker.types.oidc_endpoint.OidcEndpoint"
    ]
    """<p>The OIDC IdP user information endpoint used to configure your private workforce.</p>"""
    logout_endpoint: NotRequired["aws_sdk_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP logout endpoint used to configure your private workforce.</p>"""
    jwks_uri: NotRequired["aws_sdk_sagemaker.types.oidc_endpoint.OidcEndpoint"]
    """<p>The OIDC IdP JSON Web Key Set (Jwks) URI used to configure your private workforce.</p>"""
    scope: NotRequired["aws_sdk_sagemaker.types.scope.Scope"]
    """<p>An array of string identifiers used to refer to the specific pieces of user data or claims that the client application wants to access.</p>"""
    authentication_request_extra_params: NotRequired[
        "aws_sdk_sagemaker.types.authentication_request_extra_params.AuthenticationRequestExtraParams"
    ]
    """<p>A string to string map of identifiers specific to the custom identity provider (IdP) being used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OidcConfigForResponse) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "authorization_endpoint" in value:
        out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    if "token_endpoint" in value:
        out["TokenEndpoint"] = value["token_endpoint"]
    if "user_info_endpoint" in value:
        out["UserInfoEndpoint"] = value["user_info_endpoint"]
    if "logout_endpoint" in value:
        out["LogoutEndpoint"] = value["logout_endpoint"]
    if "jwks_uri" in value:
        out["JwksUri"] = value["jwks_uri"]
    if "scope" in value:
        out["Scope"] = value["scope"]
    if "authentication_request_extra_params" in value:
        import aws_sdk_sagemaker.types.authentication_request_extra_params

        out["AuthenticationRequestExtraParams"] = (
            aws_sdk_sagemaker.types.authentication_request_extra_params.serialize_aws_json_1_1(
                value["authentication_request_extra_params"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OidcConfigForResponse:
    out: OidcConfigForResponse = {}  # type: ignore[typeddict-item]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    if "AuthorizationEndpoint" in data:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    if "TokenEndpoint" in data:
        out["token_endpoint"] = data["TokenEndpoint"]
    if "UserInfoEndpoint" in data:
        out["user_info_endpoint"] = data["UserInfoEndpoint"]
    if "LogoutEndpoint" in data:
        out["logout_endpoint"] = data["LogoutEndpoint"]
    if "JwksUri" in data:
        out["jwks_uri"] = data["JwksUri"]
    if "Scope" in data:
        out["scope"] = data["Scope"]
    if "AuthenticationRequestExtraParams" in data:
        import aws_sdk_sagemaker.types.authentication_request_extra_params

        out["authentication_request_extra_params"] = (
            aws_sdk_sagemaker.types.authentication_request_extra_params.deserialize_aws_json_1_1(
                data["AuthenticationRequestExtraParams"]
            )
        )
    return out
