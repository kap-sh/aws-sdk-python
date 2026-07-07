"""Generated from Smithy shape ``com.amazonaws.appsync#AdditionalAuthenticationProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.authentication_type
    import aws_sdk_appsync.types.cognito_user_pool_config
    import aws_sdk_appsync.types.lambda_authorizer_config
    import aws_sdk_appsync.types.open_id_connect_config


class AdditionalAuthenticationProvider(TypedDict, closed=True):
    authentication_type: NotRequired[
        "aws_sdk_appsync.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda.</p>"""
    open_id_connect_config: NotRequired[
        "aws_sdk_appsync.types.open_id_connect_config.OpenIDConnectConfig"
    ]
    """<p>The OIDC configuration.</p>"""
    user_pool_config: NotRequired[
        "aws_sdk_appsync.types.cognito_user_pool_config.CognitoUserPoolConfig"
    ]
    """<p>The Amazon Cognito user pool configuration.</p>"""
    lambda_authorizer_config: NotRequired[
        "aws_sdk_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
    ]
    """<p>Configuration for Lambda function authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalAuthenticationProvider) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import aws_sdk_appsync.types.authentication_type

        out["authenticationType"] = (
            aws_sdk_appsync.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "open_id_connect_config" in value:
        import aws_sdk_appsync.types.open_id_connect_config

        out["openIDConnectConfig"] = (
            aws_sdk_appsync.types.open_id_connect_config.serialize_json(
                value["open_id_connect_config"]
            )
        )
    if "user_pool_config" in value:
        import aws_sdk_appsync.types.cognito_user_pool_config

        out["userPoolConfig"] = (
            aws_sdk_appsync.types.cognito_user_pool_config.serialize_json(
                value["user_pool_config"]
            )
        )
    if "lambda_authorizer_config" in value:
        import aws_sdk_appsync.types.lambda_authorizer_config

        out["lambdaAuthorizerConfig"] = (
            aws_sdk_appsync.types.lambda_authorizer_config.serialize_json(
                value["lambda_authorizer_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdditionalAuthenticationProvider:
    out: AdditionalAuthenticationProvider = {}  # type: ignore[typeddict-item]
    if "authenticationType" in data:
        import aws_sdk_appsync.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appsync.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    if "openIDConnectConfig" in data:
        import aws_sdk_appsync.types.open_id_connect_config

        out["open_id_connect_config"] = (
            aws_sdk_appsync.types.open_id_connect_config.deserialize_json(
                data["openIDConnectConfig"]
            )
        )
    if "userPoolConfig" in data:
        import aws_sdk_appsync.types.cognito_user_pool_config

        out["user_pool_config"] = (
            aws_sdk_appsync.types.cognito_user_pool_config.deserialize_json(
                data["userPoolConfig"]
            )
        )
    if "lambdaAuthorizerConfig" in data:
        import aws_sdk_appsync.types.lambda_authorizer_config

        out["lambda_authorizer_config"] = (
            aws_sdk_appsync.types.lambda_authorizer_config.deserialize_json(
                data["lambdaAuthorizerConfig"]
            )
        )
    return out
