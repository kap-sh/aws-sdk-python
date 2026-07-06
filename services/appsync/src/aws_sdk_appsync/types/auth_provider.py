"""Generated from Smithy shape ``com.amazonaws.appsync#AuthProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.authentication_type
    import aws_sdk_appsync.types.cognito_config
    import aws_sdk_appsync.types.lambda_authorizer_config
    import aws_sdk_appsync.types.open_id_connect_config


class AuthProvider(TypedDict, closed=True):
    auth_type: "aws_sdk_appsync.types.authentication_type.AuthenticationType"
    """<p>The authorization type.</p>"""
    cognito_config: NotRequired["aws_sdk_appsync.types.cognito_config.CognitoConfig"]
    """<p>Describes an Amazon Cognito user pool configuration.</p>"""
    open_id_connect_config: NotRequired[
        "aws_sdk_appsync.types.open_id_connect_config.OpenIDConnectConfig"
    ]
    lambda_authorizer_config: NotRequired[
        "aws_sdk_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AuthProvider) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.authentication_type

    out["authType"] = aws_sdk_appsync.types.authentication_type.serialize_json(
        value["auth_type"]
    )
    if "cognito_config" in value:
        import aws_sdk_appsync.types.cognito_config

        out["cognitoConfig"] = aws_sdk_appsync.types.cognito_config.serialize_json(
            value["cognito_config"]
        )
    if "open_id_connect_config" in value:
        import aws_sdk_appsync.types.open_id_connect_config

        out["openIDConnectConfig"] = (
            aws_sdk_appsync.types.open_id_connect_config.serialize_json(
                value["open_id_connect_config"]
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


def deserialize_json(data: dict) -> AuthProvider:
    out: AuthProvider = {}  # type: ignore[typeddict-item]
    if "authType" in data:
        import aws_sdk_appsync.types.authentication_type

        out["auth_type"] = aws_sdk_appsync.types.authentication_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError("AuthProvider.auth_type required")
    if "cognitoConfig" in data:
        import aws_sdk_appsync.types.cognito_config

        out["cognito_config"] = aws_sdk_appsync.types.cognito_config.deserialize_json(
            data["cognitoConfig"]
        )
    if "openIDConnectConfig" in data:
        import aws_sdk_appsync.types.open_id_connect_config

        out["open_id_connect_config"] = (
            aws_sdk_appsync.types.open_id_connect_config.deserialize_json(
                data["openIDConnectConfig"]
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
