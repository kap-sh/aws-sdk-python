"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AuthenticateOidcActionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_extra_params
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authorization_endpoint
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_client_id
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_client_secret
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_conditional_behavior_enum
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_issuer
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_scope
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_session_cookie_name
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_session_timeout
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_token_endpoint
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_use_existing_client_secret
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_user_info_endpoint


class AuthenticateOidcActionConfig(TypedDict):
    issuer: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_issuer.AuthenticateOidcActionIssuer"
    ]
    """<p>The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.</p>"""
    authorization_endpoint: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authorization_endpoint.AuthenticateOidcActionAuthorizationEndpoint"
    ]
    """<p>The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.</p>"""
    token_endpoint: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_token_endpoint.AuthenticateOidcActionTokenEndpoint"
    ]
    """<p>The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.</p>"""
    user_info_endpoint: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_user_info_endpoint.AuthenticateOidcActionUserInfoEndpoint"
    ]
    """<p>The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.</p>"""
    client_id: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_client_id.AuthenticateOidcActionClientId"
    ]
    """<p>The OAuth 2.0 client identifier.</p>"""
    client_secret: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_client_secret.AuthenticateOidcActionClientSecret"
    ]
    """<p>The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set <code>UseExistingClientSecret</code> to true.</p>"""
    session_cookie_name: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_session_cookie_name.AuthenticateOidcActionSessionCookieName"
    ]
    """<p>The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.</p>"""
    scope: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_scope.AuthenticateOidcActionScope"
    ]
    """<p>The set of user claims to be requested from the IdP. The default is <code>openid</code>.</p> <p>To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.</p>"""
    session_timeout: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_session_timeout.AuthenticateOidcActionSessionTimeout"
    ]
    """<p>The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).</p>"""
    authentication_request_extra_params: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_extra_params.AuthenticateOidcActionAuthenticationRequestExtraParams"
    ]
    """<p>The query parameters (up to 10) to include in the redirect request to the authorization endpoint.</p>"""
    on_unauthenticated_request: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_conditional_behavior_enum.AuthenticateOidcActionConditionalBehaviorEnum"
    ]
    """<p>The behavior if the user is not authenticated. The following are possible values:</p> <ul> <li> <p>deny<code></code> - Return an HTTP 401 Unauthorized error.</p> </li> <li> <p>allow<code></code> - Allow the request to be forwarded to the target.</p> </li> <li> <p>authenticate<code></code> - Redirect the request to the IdP authorization endpoint. This is the default value.</p> </li> </ul>"""
    use_existing_client_secret: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_use_existing_client_secret.AuthenticateOidcActionUseExistingClientSecret"
    ]
    """<p>Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthenticateOidcActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "issuer" in value:
        pairs.append((f"{prefix}.Issuer", str(value["issuer"])))
    if "authorization_endpoint" in value:
        pairs.append(
            (f"{prefix}.AuthorizationEndpoint", str(value["authorization_endpoint"]))
        )
    if "token_endpoint" in value:
        pairs.append((f"{prefix}.TokenEndpoint", str(value["token_endpoint"])))
    if "user_info_endpoint" in value:
        pairs.append((f"{prefix}.UserInfoEndpoint", str(value["user_info_endpoint"])))
    if "client_id" in value:
        pairs.append((f"{prefix}.ClientId", str(value["client_id"])))
    if "client_secret" in value:
        pairs.append((f"{prefix}.ClientSecret", str(value["client_secret"])))
    if "session_cookie_name" in value:
        pairs.append((f"{prefix}.SessionCookieName", str(value["session_cookie_name"])))
    if "scope" in value:
        pairs.append((f"{prefix}.Scope", str(value["scope"])))
    if "session_timeout" in value:
        pairs.append((f"{prefix}.SessionTimeout", str(value["session_timeout"])))
    if "authentication_request_extra_params" in value:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_extra_params

        aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_extra_params.serialize_query(
            value["authentication_request_extra_params"],
            pairs,
            f"{prefix}.AuthenticationRequestExtraParams",
        )
    if "on_unauthenticated_request" in value:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_conditional_behavior_enum

        aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_conditional_behavior_enum.serialize_query(
            value["on_unauthenticated_request"],
            pairs,
            f"{prefix}.OnUnauthenticatedRequest",
        )
    if "use_existing_client_secret" in value:
        pairs.append(
            (
                f"{prefix}.UseExistingClientSecret",
                "true" if value["use_existing_client_secret"] else "false",
            )
        )


def deserialize_query(el: Element) -> AuthenticateOidcActionConfig:
    out: AuthenticateOidcActionConfig = {}  # type: ignore[typeddict-item]
    child_issuer = el.find("Issuer")
    if child_issuer is not None:
        out["issuer"] = str(child_issuer.text or "")
    child_authorization_endpoint = el.find("AuthorizationEndpoint")
    if child_authorization_endpoint is not None:
        out["authorization_endpoint"] = str(child_authorization_endpoint.text or "")
    child_token_endpoint = el.find("TokenEndpoint")
    if child_token_endpoint is not None:
        out["token_endpoint"] = str(child_token_endpoint.text or "")
    child_user_info_endpoint = el.find("UserInfoEndpoint")
    if child_user_info_endpoint is not None:
        out["user_info_endpoint"] = str(child_user_info_endpoint.text or "")
    child_client_id = el.find("ClientId")
    if child_client_id is not None:
        out["client_id"] = str(child_client_id.text or "")
    child_client_secret = el.find("ClientSecret")
    if child_client_secret is not None:
        out["client_secret"] = str(child_client_secret.text or "")
    child_session_cookie_name = el.find("SessionCookieName")
    if child_session_cookie_name is not None:
        out["session_cookie_name"] = str(child_session_cookie_name.text or "")
    child_scope = el.find("Scope")
    if child_scope is not None:
        out["scope"] = str(child_scope.text or "")
    child_session_timeout = el.find("SessionTimeout")
    if child_session_timeout is not None:
        out["session_timeout"] = int(child_session_timeout.text or "")
    child_authentication_request_extra_params = el.find(
        "AuthenticationRequestExtraParams"
    )
    if child_authentication_request_extra_params is not None:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_extra_params

        out["authentication_request_extra_params"] = (
            aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_authentication_request_extra_params.deserialize_query(
                child_authentication_request_extra_params
            )
        )
    child_on_unauthenticated_request = el.find("OnUnauthenticatedRequest")
    if child_on_unauthenticated_request is not None:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_conditional_behavior_enum

        out["on_unauthenticated_request"] = (
            aws_sdk_elastic_load_balancing_v2.types.authenticate_oidc_action_conditional_behavior_enum.deserialize_query(
                child_on_unauthenticated_request
            )
        )
    child_use_existing_client_secret = el.find("UseExistingClientSecret")
    if child_use_existing_client_secret is not None:
        out["use_existing_client_secret"] = (
            child_use_existing_client_secret.text or ""
        ).lower() == "true"
    return out
