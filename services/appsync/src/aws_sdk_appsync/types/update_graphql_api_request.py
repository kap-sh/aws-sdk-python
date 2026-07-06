"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateGraphqlApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.additional_authentication_providers
    import aws_sdk_appsync.types.authentication_type
    import aws_sdk_appsync.types.boolean
    import aws_sdk_appsync.types.enhanced_metrics_config
    import aws_sdk_appsync.types.graph_ql_api_introspection_config
    import aws_sdk_appsync.types.lambda_authorizer_config
    import aws_sdk_appsync.types.log_config
    import aws_sdk_appsync.types.open_id_connect_config
    import aws_sdk_appsync.types.query_depth_limit
    import aws_sdk_appsync.types.resolver_count_limit
    import aws_sdk_appsync.types.string
    import aws_sdk_appsync.types.user_pool_config


class UpdateGraphqlApiRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    name: "aws_sdk_appsync.types.string.String"
    """<p>The new name for the <code>GraphqlApi</code> object.</p>"""
    log_config: NotRequired["aws_sdk_appsync.types.log_config.LogConfig"]
    """<p>The Amazon CloudWatch Logs configuration for the <code>GraphqlApi</code> object.</p>"""
    authentication_type: "aws_sdk_appsync.types.authentication_type.AuthenticationType"
    """<p>The new authentication type for the <code>GraphqlApi</code> object.</p>"""
    user_pool_config: NotRequired[
        "aws_sdk_appsync.types.user_pool_config.UserPoolConfig"
    ]
    """<p>The new Amazon Cognito user pool configuration for the <code>~GraphqlApi</code> object.</p>"""
    open_id_connect_config: NotRequired[
        "aws_sdk_appsync.types.open_id_connect_config.OpenIDConnectConfig"
    ]
    """<p>The OpenID Connect configuration for the <code>GraphqlApi</code> object.</p>"""
    additional_authentication_providers: NotRequired[
        "aws_sdk_appsync.types.additional_authentication_providers.AdditionalAuthenticationProviders"
    ]
    """<p>A list of additional authentication providers for the <code>GraphqlApi</code> API.</p>"""
    xray_enabled: "aws_sdk_appsync.types.boolean.Boolean"
    """<p>A flag indicating whether to use X-Ray tracing for the <code>GraphqlApi</code>.</p>"""
    lambda_authorizer_config: NotRequired[
        "aws_sdk_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
    ]
    """<p>Configuration for Lambda function authorization.</p>"""
    merged_api_execution_role_arn: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the <code>AUTO_MERGE</code> to update the merged API endpoint with the source API changes automatically.</p>"""
    owner_contact: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The owner contact information for an API resource.</p> <p>This field accepts any string input with a length of 0 - 256 characters.</p>"""
    introspection_config: NotRequired[
        "aws_sdk_appsync.types.graph_ql_api_introspection_config.GraphQLApiIntrospectionConfig"
    ]
    r"""<p>Sets the value of the GraphQL API to enable (<code>ENABLED</code>) or disable (<code>DISABLED</code>) introspection. If no value is provided, the introspection configuration will be set to <code>ENABLED</code> by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.</p> <p>For more information about introspection, see <a href=\"https://graphql.org/learn/introspection/\">GraphQL introspection</a>.</p>"""
    query_depth_limit: "aws_sdk_appsync.types.query_depth_limit.QueryDepthLimit"
    """<p>The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is <code>0</code> (or unspecified), which indicates there's no depth limit. If you set a limit, it can be between <code>1</code> and <code>75</code> nested levels. This field will produce a limit error if the operation falls out of bounds.</p> <p>Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.</p>"""
    resolver_count_limit: (
        "aws_sdk_appsync.types.resolver_count_limit.ResolverCountLimit"
    )
    """<p>The maximum number of resolvers that can be invoked in a single request. The default value is <code>0</code> (or unspecified), which will set the limit to <code>10000</code>. When specified, the limit value can be between <code>1</code> and <code>10000</code>. This field will produce a limit error if the operation falls out of bounds.</p>"""
    enhanced_metrics_config: NotRequired[
        "aws_sdk_appsync.types.enhanced_metrics_config.EnhancedMetricsConfig"
    ]
    """<p>The <code>enhancedMetricsConfig</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGraphqlApiRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "log_config" in value:
        import aws_sdk_appsync.types.log_config

        out["logConfig"] = aws_sdk_appsync.types.log_config.serialize_json(
            value["log_config"]
        )
    import aws_sdk_appsync.types.authentication_type

    out["authenticationType"] = (
        aws_sdk_appsync.types.authentication_type.serialize_json(
            value["authentication_type"]
        )
    )
    if "user_pool_config" in value:
        import aws_sdk_appsync.types.user_pool_config

        out["userPoolConfig"] = aws_sdk_appsync.types.user_pool_config.serialize_json(
            value["user_pool_config"]
        )
    if "open_id_connect_config" in value:
        import aws_sdk_appsync.types.open_id_connect_config

        out["openIDConnectConfig"] = (
            aws_sdk_appsync.types.open_id_connect_config.serialize_json(
                value["open_id_connect_config"]
            )
        )
    if "additional_authentication_providers" in value:
        import aws_sdk_appsync.types.additional_authentication_providers

        out["additionalAuthenticationProviders"] = (
            aws_sdk_appsync.types.additional_authentication_providers.serialize_json(
                value["additional_authentication_providers"]
            )
        )
    out["xrayEnabled"] = value.get("xray_enabled", False)
    if "lambda_authorizer_config" in value:
        import aws_sdk_appsync.types.lambda_authorizer_config

        out["lambdaAuthorizerConfig"] = (
            aws_sdk_appsync.types.lambda_authorizer_config.serialize_json(
                value["lambda_authorizer_config"]
            )
        )
    if "merged_api_execution_role_arn" in value:
        out["mergedApiExecutionRoleArn"] = value["merged_api_execution_role_arn"]
    if "owner_contact" in value:
        out["ownerContact"] = value["owner_contact"]
    if "introspection_config" in value:
        import aws_sdk_appsync.types.graph_ql_api_introspection_config

        out["introspectionConfig"] = (
            aws_sdk_appsync.types.graph_ql_api_introspection_config.serialize_json(
                value["introspection_config"]
            )
        )
    out["queryDepthLimit"] = value.get("query_depth_limit", 0)
    out["resolverCountLimit"] = value.get("resolver_count_limit", 0)
    if "enhanced_metrics_config" in value:
        import aws_sdk_appsync.types.enhanced_metrics_config

        out["enhancedMetricsConfig"] = (
            aws_sdk_appsync.types.enhanced_metrics_config.serialize_json(
                value["enhanced_metrics_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGraphqlApiRequest:
    out: UpdateGraphqlApiRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGraphqlApiRequest.name required")
    if "logConfig" in data:
        import aws_sdk_appsync.types.log_config

        out["log_config"] = aws_sdk_appsync.types.log_config.deserialize_json(
            data["logConfig"]
        )
    if "authenticationType" in data:
        import aws_sdk_appsync.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appsync.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateGraphqlApiRequest.authentication_type required"
        )
    if "userPoolConfig" in data:
        import aws_sdk_appsync.types.user_pool_config

        out["user_pool_config"] = (
            aws_sdk_appsync.types.user_pool_config.deserialize_json(
                data["userPoolConfig"]
            )
        )
    if "openIDConnectConfig" in data:
        import aws_sdk_appsync.types.open_id_connect_config

        out["open_id_connect_config"] = (
            aws_sdk_appsync.types.open_id_connect_config.deserialize_json(
                data["openIDConnectConfig"]
            )
        )
    if "additionalAuthenticationProviders" in data:
        import aws_sdk_appsync.types.additional_authentication_providers

        out["additional_authentication_providers"] = (
            aws_sdk_appsync.types.additional_authentication_providers.deserialize_json(
                data["additionalAuthenticationProviders"]
            )
        )
    if "xrayEnabled" in data:
        out["xray_enabled"] = data["xrayEnabled"]
    else:
        out["xray_enabled"] = False
    if "lambdaAuthorizerConfig" in data:
        import aws_sdk_appsync.types.lambda_authorizer_config

        out["lambda_authorizer_config"] = (
            aws_sdk_appsync.types.lambda_authorizer_config.deserialize_json(
                data["lambdaAuthorizerConfig"]
            )
        )
    if "mergedApiExecutionRoleArn" in data:
        out["merged_api_execution_role_arn"] = data["mergedApiExecutionRoleArn"]
    if "ownerContact" in data:
        out["owner_contact"] = data["ownerContact"]
    if "introspectionConfig" in data:
        import aws_sdk_appsync.types.graph_ql_api_introspection_config

        out["introspection_config"] = (
            aws_sdk_appsync.types.graph_ql_api_introspection_config.deserialize_json(
                data["introspectionConfig"]
            )
        )
    if "queryDepthLimit" in data:
        out["query_depth_limit"] = data["queryDepthLimit"]
    else:
        out["query_depth_limit"] = 0
    if "resolverCountLimit" in data:
        out["resolver_count_limit"] = data["resolverCountLimit"]
    else:
        out["resolver_count_limit"] = 0
    if "enhancedMetricsConfig" in data:
        import aws_sdk_appsync.types.enhanced_metrics_config

        out["enhanced_metrics_config"] = (
            aws_sdk_appsync.types.enhanced_metrics_config.deserialize_json(
                data["enhancedMetricsConfig"]
            )
        )
    return out
