"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AuthenticateCognitoActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_authentication_request_extra_params
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_conditional_behavior_enum
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_scope
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_session_cookie_name
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_session_timeout
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_user_pool_arn
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_user_pool_client_id
    import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_user_pool_domain


class AuthenticateCognitoActionConfig(TypedDict, closed=True):
    user_pool_arn: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_user_pool_arn.AuthenticateCognitoActionUserPoolArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Cognito user pool.</p>"""
    user_pool_client_id: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_user_pool_client_id.AuthenticateCognitoActionUserPoolClientId"
    ]
    """<p>The ID of the Amazon Cognito user pool client.</p>"""
    user_pool_domain: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_user_pool_domain.AuthenticateCognitoActionUserPoolDomain"
    ]
    """<p>The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.</p>"""
    session_cookie_name: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_session_cookie_name.AuthenticateCognitoActionSessionCookieName"
    ]
    """<p>The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.</p>"""
    scope: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_scope.AuthenticateCognitoActionScope"
    ]
    """<p>The set of user claims to be requested from the IdP. The default is <code>openid</code>.</p> <p>To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.</p>"""
    session_timeout: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_session_timeout.AuthenticateCognitoActionSessionTimeout"
    ]
    """<p>The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).</p>"""
    authentication_request_extra_params: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_authentication_request_extra_params.AuthenticateCognitoActionAuthenticationRequestExtraParams"
    ]
    """<p>The query parameters (up to 10) to include in the redirect request to the authorization endpoint.</p>"""
    on_unauthenticated_request: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_conditional_behavior_enum.AuthenticateCognitoActionConditionalBehaviorEnum"
    ]
    """<p>The behavior if the user is not authenticated. The following are possible values:</p> <ul> <li> <p>deny<code></code> - Return an HTTP 401 Unauthorized error.</p> </li> <li> <p>allow<code></code> - Allow the request to be forwarded to the target.</p> </li> <li> <p>authenticate<code></code> - Redirect the request to the IdP authorization endpoint. This is the default value.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthenticateCognitoActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_pool_arn" in value:
        pairs.append((f"{prefix}.UserPoolArn", str(value["user_pool_arn"])))
    if "user_pool_client_id" in value:
        pairs.append((f"{prefix}.UserPoolClientId", str(value["user_pool_client_id"])))
    if "user_pool_domain" in value:
        pairs.append((f"{prefix}.UserPoolDomain", str(value["user_pool_domain"])))
    if "session_cookie_name" in value:
        pairs.append((f"{prefix}.SessionCookieName", str(value["session_cookie_name"])))
    if "scope" in value:
        pairs.append((f"{prefix}.Scope", str(value["scope"])))
    if "session_timeout" in value:
        pairs.append((f"{prefix}.SessionTimeout", str(value["session_timeout"])))
    if "authentication_request_extra_params" in value:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_authentication_request_extra_params

        aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_authentication_request_extra_params.serialize_query(
            value["authentication_request_extra_params"],
            pairs,
            f"{prefix}.AuthenticationRequestExtraParams",
        )
    if "on_unauthenticated_request" in value:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_conditional_behavior_enum

        aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_conditional_behavior_enum.serialize_query(
            value["on_unauthenticated_request"],
            pairs,
            f"{prefix}.OnUnauthenticatedRequest",
        )


def deserialize_query(el: Element) -> AuthenticateCognitoActionConfig:
    out: AuthenticateCognitoActionConfig = {}  # type: ignore[typeddict-item]
    child_user_pool_arn = el.find("UserPoolArn")
    if child_user_pool_arn is not None:
        out["user_pool_arn"] = str(child_user_pool_arn.text or "")
    child_user_pool_client_id = el.find("UserPoolClientId")
    if child_user_pool_client_id is not None:
        out["user_pool_client_id"] = str(child_user_pool_client_id.text or "")
    child_user_pool_domain = el.find("UserPoolDomain")
    if child_user_pool_domain is not None:
        out["user_pool_domain"] = str(child_user_pool_domain.text or "")
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
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_authentication_request_extra_params

        out["authentication_request_extra_params"] = (
            aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_authentication_request_extra_params.deserialize_query(
                child_authentication_request_extra_params
            )
        )
    child_on_unauthenticated_request = el.find("OnUnauthenticatedRequest")
    if child_on_unauthenticated_request is not None:
        import aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_conditional_behavior_enum

        out["on_unauthenticated_request"] = (
            aws_sdk_elastic_load_balancing_v2.types.authenticate_cognito_action_conditional_behavior_enum.deserialize_query(
                child_on_unauthenticated_request
            )
        )
    return out
