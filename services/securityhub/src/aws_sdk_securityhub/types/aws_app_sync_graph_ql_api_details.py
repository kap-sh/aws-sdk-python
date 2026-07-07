"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_list
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_log_config_details
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details
    import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsAppSyncGraphQlApiDetails(TypedDict, closed=True):
    api_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The unique identifier for the API. </p>"""
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for the API.</p>"""
    open_id_connect_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details.AwsAppSyncGraphQlApiOpenIdConnectConfigDetails"
    ]
    """<p> Specifies the authorization configuration for using an OpenID Connect compliant service with an AppSync GraphQL API endpoint. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The API name. </p>"""
    lambda_authorizer_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details.AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails"
    ]
    """<p> Specifies the configuration for Lambda function authorization. </p>"""
    xray_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether to use X-Ray tracing for the GraphQL API. </p>"""
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the API. </p>"""
    user_pool_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details.AwsAppSyncGraphQlApiUserPoolConfigDetails"
    ]
    """<p> The Amazon Cognito user pools configuration. </p>"""
    authentication_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The type of security configuration for your GraphQL API: API key, Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or Lambda. </p>"""
    log_config: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_log_config_details.AwsAppSyncGraphQlApiLogConfigDetails"
    ]
    """<p> The Amazon CloudWatch Logs configuration. </p>"""
    additional_authentication_providers: NotRequired[
        "aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_list.AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersList"
    ]
    """<p> A list of additional authentication providers for the GraphQL API. </p>"""
    waf_web_acl_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the WAF web access control list (web ACL) associated with this GraphQL API, if one exists. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAppSyncGraphQlApiDetails) -> dict:
    out: dict = {}
    if "api_id" in value:
        out["ApiId"] = value["api_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "open_id_connect_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details

        out["OpenIdConnectConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details.serialize_json(
                value["open_id_connect_config"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "lambda_authorizer_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details

        out["LambdaAuthorizerConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details.serialize_json(
                value["lambda_authorizer_config"]
            )
        )
    if "xray_enabled" in value:
        out["XrayEnabled"] = value["xray_enabled"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "user_pool_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details

        out["UserPoolConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details.serialize_json(
                value["user_pool_config"]
            )
        )
    if "authentication_type" in value:
        out["AuthenticationType"] = value["authentication_type"]
    if "log_config" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_log_config_details

        out["LogConfig"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_log_config_details.serialize_json(
                value["log_config"]
            )
        )
    if "additional_authentication_providers" in value:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_list

        out["AdditionalAuthenticationProviders"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_list.serialize_json(
                value["additional_authentication_providers"]
            )
        )
    if "waf_web_acl_arn" in value:
        out["WafWebAclArn"] = value["waf_web_acl_arn"]
    return out


def deserialize_json(data: dict) -> AwsAppSyncGraphQlApiDetails:
    out: AwsAppSyncGraphQlApiDetails = {}  # type: ignore[typeddict-item]
    if "ApiId" in data:
        out["api_id"] = data["ApiId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "OpenIdConnectConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details

        out["open_id_connect_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_open_id_connect_config_details.deserialize_json(
                data["OpenIdConnectConfig"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "LambdaAuthorizerConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details

        out["lambda_authorizer_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_lambda_authorizer_config_details.deserialize_json(
                data["LambdaAuthorizerConfig"]
            )
        )
    if "XrayEnabled" in data:
        out["xray_enabled"] = data["XrayEnabled"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "UserPoolConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details

        out["user_pool_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_user_pool_config_details.deserialize_json(
                data["UserPoolConfig"]
            )
        )
    if "AuthenticationType" in data:
        out["authentication_type"] = data["AuthenticationType"]
    if "LogConfig" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_log_config_details

        out["log_config"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_log_config_details.deserialize_json(
                data["LogConfig"]
            )
        )
    if "AdditionalAuthenticationProviders" in data:
        import aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_list

        out["additional_authentication_providers"] = (
            aws_sdk_securityhub.types.aws_app_sync_graph_ql_api_additional_authentication_providers_list.deserialize_json(
                data["AdditionalAuthenticationProviders"]
            )
        )
    if "WafWebAclArn" in data:
        out["waf_web_acl_arn"] = data["WafWebAclArn"]
    return out
