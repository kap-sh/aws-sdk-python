"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails(TypedDict):
    authentication_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of security configuration for your GraphQL API: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda. </p>"""
    lambda_authorizer_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails"
    ]
    """<p> The configuration for Lambda function authorization. </p>"""
    open_id_connect_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details.AwsAppSyncGraphQlApiOpenIdConnectConfigDetails"
    ]
    """<p> The OpenID Connect configuration. </p>"""
    user_pool_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details.AwsAppSyncGraphQlApiUserPoolConfigDetails"
    ]
    """<p> The Amazon Cognito user pools configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails,
) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        out["AuthenticationType"] = value["authentication_type"]
    if "lambda_authorizer_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details

        out["LambdaAuthorizerConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details.serialize_json(
                value["lambda_authorizer_config"]
            )
        )
    if "open_id_connect_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details

        out["OpenIdConnectConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details.serialize_json(
                value["open_id_connect_config"]
            )
        )
    if "user_pool_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details

        out["UserPoolConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details.serialize_json(
                value["user_pool_config"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails:
    out: AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        out["authentication_type"] = data["AuthenticationType"]
    if "LambdaAuthorizerConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details

        out["lambda_authorizer_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details.deserialize_json(
                data["LambdaAuthorizerConfig"]
            )
        )
    if "OpenIdConnectConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details

        out["open_id_connect_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details.deserialize_json(
                data["OpenIdConnectConfig"]
            )
        )
    if "UserPoolConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details

        out["user_pool_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details.deserialize_json(
                data["UserPoolConfig"]
            )
        )
    return out
