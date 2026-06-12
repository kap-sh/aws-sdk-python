"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ApiGatewayV2``."""

from aws_sdk_apigatewayv2._auth._signers import SigV4Signer
from aws_sdk_apigatewayv2._auth._sigv4 import presign_sigv4
from collections.abc import AsyncIterator
from aws_sdk_apigatewayv2._pagination import resolve_path as _resolve_path
from typing import Any, Iterable, TypedDict, Unpack, TYPE_CHECKING
from typing_extensions import Self
from typing import Optional
from zapros import URL, AsyncBaseHandler, AsyncClient
from aws_sdk_apigatewayv2._auth._zapros_handler import AuthMiddleware
from aws_sdk_apigatewayv2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from aws_sdk_apigatewayv2._async import anysleep
import time
from aws_sdk_apigatewayv2.errors import (
    ServiceError,
    WaiterFailedError,
    WaiterTimeoutError,
)
import warnings
import aws_sdk_apigatewayv2._auth._signers
import aws_sdk_apigatewayv2._auth._sigv4
from aws_sdk_apigatewayv2._auth._identity import Credentials
from aws_sdk_apigatewayv2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean
    import aws_sdk_apigatewayv2.types.__list_of__string
    import aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_action
    import aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition
    import aws_sdk_apigatewayv2.types.__string
    import aws_sdk_apigatewayv2.types.__string_min0_max1024
    import aws_sdk_apigatewayv2.types.__string_min0_max1092
    import aws_sdk_apigatewayv2.types.__string_min0_max255
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.__string_min1_max307200
    import aws_sdk_apigatewayv2.types.access_log_settings
    import aws_sdk_apigatewayv2.types.arn
    import aws_sdk_apigatewayv2.types.authorization
    import aws_sdk_apigatewayv2.types.authorization_scopes
    import aws_sdk_apigatewayv2.types.authorization_type
    import aws_sdk_apigatewayv2.types.authorizer_type
    import aws_sdk_apigatewayv2.types.connection_type
    import aws_sdk_apigatewayv2.types.content_handling_strategy
    import aws_sdk_apigatewayv2.types.cors
    import aws_sdk_apigatewayv2.types.create_api_mapping_request
    import aws_sdk_apigatewayv2.types.create_api_mapping_response
    import aws_sdk_apigatewayv2.types.create_api_request
    import aws_sdk_apigatewayv2.types.create_api_response
    import aws_sdk_apigatewayv2.types.create_authorizer_request
    import aws_sdk_apigatewayv2.types.create_authorizer_response
    import aws_sdk_apigatewayv2.types.create_deployment_request
    import aws_sdk_apigatewayv2.types.create_deployment_response
    import aws_sdk_apigatewayv2.types.create_domain_name_request
    import aws_sdk_apigatewayv2.types.create_domain_name_response
    import aws_sdk_apigatewayv2.types.create_integration_request
    import aws_sdk_apigatewayv2.types.create_integration_response_request
    import aws_sdk_apigatewayv2.types.create_integration_response_response
    import aws_sdk_apigatewayv2.types.create_integration_result
    import aws_sdk_apigatewayv2.types.create_model_request
    import aws_sdk_apigatewayv2.types.create_model_response
    import aws_sdk_apigatewayv2.types.create_portal_product_request
    import aws_sdk_apigatewayv2.types.create_portal_product_response
    import aws_sdk_apigatewayv2.types.create_portal_request
    import aws_sdk_apigatewayv2.types.create_portal_response
    import aws_sdk_apigatewayv2.types.create_product_page_request
    import aws_sdk_apigatewayv2.types.create_product_page_response
    import aws_sdk_apigatewayv2.types.create_product_rest_endpoint_page_request
    import aws_sdk_apigatewayv2.types.create_product_rest_endpoint_page_response
    import aws_sdk_apigatewayv2.types.create_route_request
    import aws_sdk_apigatewayv2.types.create_route_response_request
    import aws_sdk_apigatewayv2.types.create_route_response_response
    import aws_sdk_apigatewayv2.types.create_route_result
    import aws_sdk_apigatewayv2.types.create_routing_rule_request
    import aws_sdk_apigatewayv2.types.create_routing_rule_response
    import aws_sdk_apigatewayv2.types.create_stage_request
    import aws_sdk_apigatewayv2.types.create_stage_response
    import aws_sdk_apigatewayv2.types.create_vpc_link_request
    import aws_sdk_apigatewayv2.types.create_vpc_link_response
    import aws_sdk_apigatewayv2.types.delete_access_log_settings_request
    import aws_sdk_apigatewayv2.types.delete_api_mapping_request
    import aws_sdk_apigatewayv2.types.delete_api_request
    import aws_sdk_apigatewayv2.types.delete_authorizer_request
    import aws_sdk_apigatewayv2.types.delete_cors_configuration_request
    import aws_sdk_apigatewayv2.types.delete_deployment_request
    import aws_sdk_apigatewayv2.types.delete_domain_name_request
    import aws_sdk_apigatewayv2.types.delete_integration_request
    import aws_sdk_apigatewayv2.types.delete_integration_response_request
    import aws_sdk_apigatewayv2.types.delete_model_request
    import aws_sdk_apigatewayv2.types.delete_portal_product_request
    import aws_sdk_apigatewayv2.types.delete_portal_product_sharing_policy_request
    import aws_sdk_apigatewayv2.types.delete_portal_request
    import aws_sdk_apigatewayv2.types.delete_product_page_request
    import aws_sdk_apigatewayv2.types.delete_product_rest_endpoint_page_request
    import aws_sdk_apigatewayv2.types.delete_route_request
    import aws_sdk_apigatewayv2.types.delete_route_request_parameter_request
    import aws_sdk_apigatewayv2.types.delete_route_response_request
    import aws_sdk_apigatewayv2.types.delete_route_settings_request
    import aws_sdk_apigatewayv2.types.delete_routing_rule_request
    import aws_sdk_apigatewayv2.types.delete_stage_request
    import aws_sdk_apigatewayv2.types.delete_vpc_link_request
    import aws_sdk_apigatewayv2.types.delete_vpc_link_response
    import aws_sdk_apigatewayv2.types.disable_portal_request
    import aws_sdk_apigatewayv2.types.display_content
    import aws_sdk_apigatewayv2.types.display_order
    import aws_sdk_apigatewayv2.types.domain_name_configurations
    import aws_sdk_apigatewayv2.types.endpoint_configuration_request
    import aws_sdk_apigatewayv2.types.endpoint_display_content
    import aws_sdk_apigatewayv2.types.export_api_request
    import aws_sdk_apigatewayv2.types.export_api_response
    import aws_sdk_apigatewayv2.types.get_api_mapping_request
    import aws_sdk_apigatewayv2.types.get_api_mapping_response
    import aws_sdk_apigatewayv2.types.get_api_mappings_request
    import aws_sdk_apigatewayv2.types.get_api_mappings_response
    import aws_sdk_apigatewayv2.types.get_api_request
    import aws_sdk_apigatewayv2.types.get_api_response
    import aws_sdk_apigatewayv2.types.get_apis_request
    import aws_sdk_apigatewayv2.types.get_apis_response
    import aws_sdk_apigatewayv2.types.get_authorizer_request
    import aws_sdk_apigatewayv2.types.get_authorizer_response
    import aws_sdk_apigatewayv2.types.get_authorizers_request
    import aws_sdk_apigatewayv2.types.get_authorizers_response
    import aws_sdk_apigatewayv2.types.get_deployment_request
    import aws_sdk_apigatewayv2.types.get_deployment_response
    import aws_sdk_apigatewayv2.types.get_deployments_request
    import aws_sdk_apigatewayv2.types.get_deployments_response
    import aws_sdk_apigatewayv2.types.get_domain_name_request
    import aws_sdk_apigatewayv2.types.get_domain_name_response
    import aws_sdk_apigatewayv2.types.get_domain_names_request
    import aws_sdk_apigatewayv2.types.get_domain_names_response
    import aws_sdk_apigatewayv2.types.get_integration_request
    import aws_sdk_apigatewayv2.types.get_integration_response_request
    import aws_sdk_apigatewayv2.types.get_integration_response_response
    import aws_sdk_apigatewayv2.types.get_integration_responses_request
    import aws_sdk_apigatewayv2.types.get_integration_responses_response
    import aws_sdk_apigatewayv2.types.get_integration_result
    import aws_sdk_apigatewayv2.types.get_integrations_request
    import aws_sdk_apigatewayv2.types.get_integrations_response
    import aws_sdk_apigatewayv2.types.get_model_request
    import aws_sdk_apigatewayv2.types.get_model_response
    import aws_sdk_apigatewayv2.types.get_model_template_request
    import aws_sdk_apigatewayv2.types.get_model_template_response
    import aws_sdk_apigatewayv2.types.get_models_request
    import aws_sdk_apigatewayv2.types.get_models_response
    import aws_sdk_apigatewayv2.types.get_portal_product_request
    import aws_sdk_apigatewayv2.types.get_portal_product_response
    import aws_sdk_apigatewayv2.types.get_portal_product_sharing_policy_request
    import aws_sdk_apigatewayv2.types.get_portal_product_sharing_policy_response
    import aws_sdk_apigatewayv2.types.get_portal_request
    import aws_sdk_apigatewayv2.types.get_portal_response
    import aws_sdk_apigatewayv2.types.get_product_page_request
    import aws_sdk_apigatewayv2.types.get_product_page_response
    import aws_sdk_apigatewayv2.types.get_product_rest_endpoint_page_request
    import aws_sdk_apigatewayv2.types.get_product_rest_endpoint_page_response
    import aws_sdk_apigatewayv2.types.get_route_request
    import aws_sdk_apigatewayv2.types.get_route_response_request
    import aws_sdk_apigatewayv2.types.get_route_response_response
    import aws_sdk_apigatewayv2.types.get_route_responses_request
    import aws_sdk_apigatewayv2.types.get_route_responses_response
    import aws_sdk_apigatewayv2.types.get_route_result
    import aws_sdk_apigatewayv2.types.get_routes_request
    import aws_sdk_apigatewayv2.types.get_routes_response
    import aws_sdk_apigatewayv2.types.get_routing_rule_request
    import aws_sdk_apigatewayv2.types.get_routing_rule_response
    import aws_sdk_apigatewayv2.types.get_stage_request
    import aws_sdk_apigatewayv2.types.get_stage_response
    import aws_sdk_apigatewayv2.types.get_stages_request
    import aws_sdk_apigatewayv2.types.get_stages_response
    import aws_sdk_apigatewayv2.types.get_tags_request
    import aws_sdk_apigatewayv2.types.get_tags_response
    import aws_sdk_apigatewayv2.types.get_vpc_link_request
    import aws_sdk_apigatewayv2.types.get_vpc_link_response
    import aws_sdk_apigatewayv2.types.get_vpc_links_request
    import aws_sdk_apigatewayv2.types.get_vpc_links_response
    import aws_sdk_apigatewayv2.types.id
    import aws_sdk_apigatewayv2.types.identity_source_list
    import aws_sdk_apigatewayv2.types.import_api_request
    import aws_sdk_apigatewayv2.types.import_api_response
    import aws_sdk_apigatewayv2.types.integer_with_length_between0_and3600
    import aws_sdk_apigatewayv2.types.integer_with_length_between50_and30000
    import aws_sdk_apigatewayv2.types.integration_parameters
    import aws_sdk_apigatewayv2.types.integration_type
    import aws_sdk_apigatewayv2.types.ip_address_type
    import aws_sdk_apigatewayv2.types.jwt_configuration
    import aws_sdk_apigatewayv2.types.list_portal_products_request
    import aws_sdk_apigatewayv2.types.list_portal_products_response
    import aws_sdk_apigatewayv2.types.list_portals_request
    import aws_sdk_apigatewayv2.types.list_portals_response
    import aws_sdk_apigatewayv2.types.list_product_pages_request
    import aws_sdk_apigatewayv2.types.list_product_pages_response
    import aws_sdk_apigatewayv2.types.list_product_rest_endpoint_pages_request
    import aws_sdk_apigatewayv2.types.list_product_rest_endpoint_pages_response
    import aws_sdk_apigatewayv2.types.list_routing_rules_request
    import aws_sdk_apigatewayv2.types.list_routing_rules_response
    import aws_sdk_apigatewayv2.types.max_results
    import aws_sdk_apigatewayv2.types.mutual_tls_authentication_input
    import aws_sdk_apigatewayv2.types.passthrough_behavior
    import aws_sdk_apigatewayv2.types.portal_content
    import aws_sdk_apigatewayv2.types.preview_portal_request
    import aws_sdk_apigatewayv2.types.preview_portal_response
    import aws_sdk_apigatewayv2.types.protocol_type
    import aws_sdk_apigatewayv2.types.publish_portal_request
    import aws_sdk_apigatewayv2.types.publish_portal_response
    import aws_sdk_apigatewayv2.types.put_portal_product_sharing_policy_request
    import aws_sdk_apigatewayv2.types.put_portal_product_sharing_policy_response
    import aws_sdk_apigatewayv2.types.put_routing_rule_request
    import aws_sdk_apigatewayv2.types.put_routing_rule_response
    import aws_sdk_apigatewayv2.types.reimport_api_request
    import aws_sdk_apigatewayv2.types.reimport_api_response
    import aws_sdk_apigatewayv2.types.reset_authorizers_cache_request
    import aws_sdk_apigatewayv2.types.response_parameters
    import aws_sdk_apigatewayv2.types.rest_endpoint_identifier
    import aws_sdk_apigatewayv2.types.route_models
    import aws_sdk_apigatewayv2.types.route_parameters
    import aws_sdk_apigatewayv2.types.route_settings
    import aws_sdk_apigatewayv2.types.route_settings_map
    import aws_sdk_apigatewayv2.types.routing_mode
    import aws_sdk_apigatewayv2.types.routing_rule
    import aws_sdk_apigatewayv2.types.routing_rule_priority
    import aws_sdk_apigatewayv2.types.security_group_id_list
    import aws_sdk_apigatewayv2.types.selection_expression
    import aws_sdk_apigatewayv2.types.selection_key
    import aws_sdk_apigatewayv2.types.stage_variables_map
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and1024
    import aws_sdk_apigatewayv2.types.string_with_length_between0_and32_k
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and1024
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and128
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and256
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and512
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64
    import aws_sdk_apigatewayv2.types.subnet_id_list
    import aws_sdk_apigatewayv2.types.tag_resource_request
    import aws_sdk_apigatewayv2.types.tag_resource_response
    import aws_sdk_apigatewayv2.types.tags
    import aws_sdk_apigatewayv2.types.template_map
    import aws_sdk_apigatewayv2.types.tls_config_input
    import aws_sdk_apigatewayv2.types.try_it_state
    import aws_sdk_apigatewayv2.types.untag_resource_request
    import aws_sdk_apigatewayv2.types.update_api_mapping_request
    import aws_sdk_apigatewayv2.types.update_api_mapping_response
    import aws_sdk_apigatewayv2.types.update_api_request
    import aws_sdk_apigatewayv2.types.update_api_response
    import aws_sdk_apigatewayv2.types.update_authorizer_request
    import aws_sdk_apigatewayv2.types.update_authorizer_response
    import aws_sdk_apigatewayv2.types.update_deployment_request
    import aws_sdk_apigatewayv2.types.update_deployment_response
    import aws_sdk_apigatewayv2.types.update_domain_name_request
    import aws_sdk_apigatewayv2.types.update_domain_name_response
    import aws_sdk_apigatewayv2.types.update_integration_request
    import aws_sdk_apigatewayv2.types.update_integration_response_request
    import aws_sdk_apigatewayv2.types.update_integration_response_response
    import aws_sdk_apigatewayv2.types.update_integration_result
    import aws_sdk_apigatewayv2.types.update_model_request
    import aws_sdk_apigatewayv2.types.update_model_response
    import aws_sdk_apigatewayv2.types.update_portal_product_request
    import aws_sdk_apigatewayv2.types.update_portal_product_response
    import aws_sdk_apigatewayv2.types.update_portal_request
    import aws_sdk_apigatewayv2.types.update_portal_response
    import aws_sdk_apigatewayv2.types.update_product_page_request
    import aws_sdk_apigatewayv2.types.update_product_page_response
    import aws_sdk_apigatewayv2.types.update_product_rest_endpoint_page_request
    import aws_sdk_apigatewayv2.types.update_product_rest_endpoint_page_response
    import aws_sdk_apigatewayv2.types.update_route_request
    import aws_sdk_apigatewayv2.types.update_route_response_request
    import aws_sdk_apigatewayv2.types.update_route_response_response
    import aws_sdk_apigatewayv2.types.update_route_result
    import aws_sdk_apigatewayv2.types.update_stage_request
    import aws_sdk_apigatewayv2.types.update_stage_response
    import aws_sdk_apigatewayv2.types.update_vpc_link_request
    import aws_sdk_apigatewayv2.types.update_vpc_link_response
    import aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048


class AsyncApiGatewayV2ClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncApiGatewayV2Client:
    """A client for the ``ApiGatewayV2`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = AsyncApiGatewayV2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncApiGatewayV2ClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_api(
        self,
        name: "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128",
        protocol_type: "aws_sdk_apigatewayv2.types.protocol_type.ProtocolType",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        api_key_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        cors_configuration: Optional["aws_sdk_apigatewayv2.types.cors.Cors"] = None,
        credentials_arn: Optional["aws_sdk_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        disable_schema_validation: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        disable_execute_api_endpoint: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_apigatewayv2.types.ip_address_type.IpAddressType"
        ] = None,
        route_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
        target: Optional[
            "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        version: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_api_response.CreateApiResponse":
        """<p>Creates an Api resource.</p>

        Args:
            api_key_selection_expression: <p>An API key selection expression. Supported only for WebSocket APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\">API Key Selection Expressions</a>.</p>
            cors_configuration: <p>A CORS configuration. Supported only for HTTP APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html\">Configuring CORS</a> for more information.</p>
            credentials_arn: <p>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null. Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.</p>
            description: <p>The description of the API.</p>
            disable_schema_validation: <p>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</p>
            disable_execute_api_endpoint: <p>Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>
            ip_address_type: <p>The IP address types that can invoke the API.</p>
            name: <p>The name of the API.</p>
            protocol_type: <p>The API protocol.</p>
            route_key: <p>This property is part of quick create. If you don't specify a routeKey, a default route of $default is created. The $default route acts as a catch-all for any request made to your API, for a particular stage. The $default route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.</p>
            route_selection_expression: <p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>
            target: <p>This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.</p>
            version: <p>A version identifier for the API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_api_request.CreateApiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_api_response.CreateApiResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_api.async_create_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_api_request.CreateApiRequest = {}  # type: ignore[typeddict-item]
        if api_key_selection_expression is not None:
            input["api_key_selection_expression"] = api_key_selection_expression
        if cors_configuration is not None:
            input["cors_configuration"] = cors_configuration
        if credentials_arn is not None:
            input["credentials_arn"] = credentials_arn
        if description is not None:
            input["description"] = description
        if disable_schema_validation is not None:
            input["disable_schema_validation"] = disable_schema_validation
        if disable_execute_api_endpoint is not None:
            input["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        input["name"] = name
        input["protocol_type"] = protocol_type
        if route_key is not None:
            input["route_key"] = route_key
        if route_selection_expression is not None:
            input["route_selection_expression"] = route_selection_expression
        if tags is not None:
            input["tags"] = tags
        if target is not None:
            input["target"] = target
        if version is not None:
            input["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_api_mapping(
        self,
        api_id: "aws_sdk_apigatewayv2.types.id.Id",
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        stage: "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        api_mapping_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_api_mapping_response.CreateApiMappingResponse":
        """<p>Creates an API mapping.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_mapping_key: The API mapping key.
            domain_name: <p>The domain name.</p>
            stage: <p>The API stage.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_api_mapping_request.CreateApiMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_api_mapping_response.CreateApiMappingResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_api_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_api_mapping.async_create_api_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_api_mapping_request.CreateApiMappingRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if api_mapping_key is not None:
            input["api_mapping_key"] = api_mapping_key
        input["domain_name"] = domain_name
        input["stage"] = stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_authorizer(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        authorizer_type: "aws_sdk_apigatewayv2.types.authorizer_type.AuthorizerType",
        identity_source: "aws_sdk_apigatewayv2.types.identity_source_list.IdentitySourceList",
        name: "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        authorizer_credentials_arn: Optional[
            "aws_sdk_apigatewayv2.types.arn.Arn"
        ] = None,
        authorizer_payload_format_version: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        authorizer_result_ttl_in_seconds: Optional[
            "aws_sdk_apigatewayv2.types.integer_with_length_between0_and3600.IntegerWithLengthBetween0And3600"
        ] = None,
        authorizer_uri: Optional[
            "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        enable_simple_responses: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        identity_validation_expression: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        jwt_configuration: Optional[
            "aws_sdk_apigatewayv2.types.jwt_configuration.JWTConfiguration"
        ] = None,
    ) -> (
        "aws_sdk_apigatewayv2.types.create_authorizer_response.CreateAuthorizerResponse"
    ):
        """<p>Creates an Authorizer for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_credentials_arn: <p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter. Supported only for REQUEST authorizers.</p>
            authorizer_payload_format_version: <p>Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are 1.0 and 2.0. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\">Working with AWS Lambda authorizers for HTTP APIs</a>.</p>
            authorizer_result_ttl_in_seconds: <p>The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.</p>
            authorizer_type: <p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>
            authorizer_uri: <p>The authorizer's Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:<replaceable>{account_id}</replaceable>:function:<replaceable>{lambda_function_name}</replaceable>/invocations. In general, the URI has this form: arn:aws:apigateway:<replaceable>{region}</replaceable>:lambda:path/<replaceable>{service_api}</replaceable> , where <replaceable></replaceable>{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.</p>
            enable_simple_responses: <p>Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\">Working with AWS Lambda authorizers for HTTP APIs</a></p>
            identity_source: <p>The identity source for which authorization is requested.</p> <p>For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with $, for example, $request.header.Auth, $request.querystring.Name. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\">Working with AWS Lambda authorizers for HTTP APIs</a>.</p> <p>For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example $request.header.Authorization.</p>
            identity_validation_expression: <p>This parameter is not used.</p>
            jwt_configuration: <p>Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.</p>
            name: <p>The name of the authorizer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_authorizer_request.CreateAuthorizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_authorizer_response.CreateAuthorizerResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_authorizer

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_authorizer.async_create_authorizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_authorizer_request.CreateAuthorizerRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if authorizer_credentials_arn is not None:
            input["authorizer_credentials_arn"] = authorizer_credentials_arn
        if authorizer_payload_format_version is not None:
            input["authorizer_payload_format_version"] = (
                authorizer_payload_format_version
            )
        if authorizer_result_ttl_in_seconds is not None:
            input["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        input["authorizer_type"] = authorizer_type
        if authorizer_uri is not None:
            input["authorizer_uri"] = authorizer_uri
        if enable_simple_responses is not None:
            input["enable_simple_responses"] = enable_simple_responses
        input["identity_source"] = identity_source
        if identity_validation_expression is not None:
            input["identity_validation_expression"] = identity_validation_expression
        if jwt_configuration is not None:
            input["jwt_configuration"] = jwt_configuration
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_deployment(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        stage_name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> (
        "aws_sdk_apigatewayv2.types.create_deployment_response.CreateDeploymentResponse"
    ):
        """<p>Creates a Deployment for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            description: <p>The description for the deployment resource.</p>
            stage_name: <p>The name of the Stage resource for the Deployment resource to create.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_deployment_request.CreateDeploymentRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if description is not None:
            input["description"] = description
        if stage_name is not None:
            input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_domain_name(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.string_with_length_between1_and512.StringWithLengthBetween1And512",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_configurations: Optional[
            "aws_sdk_apigatewayv2.types.domain_name_configurations.DomainNameConfigurations"
        ] = None,
        mutual_tls_authentication: Optional[
            "aws_sdk_apigatewayv2.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
        ] = None,
        routing_mode: Optional[
            "aws_sdk_apigatewayv2.types.routing_mode.RoutingMode"
        ] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_domain_name_response.CreateDomainNameResponse":
        """<p>Creates a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_configurations: <p>The domain name configurations.</p>
            mutual_tls_authentication: <p>The mutual TLS authentication configuration for a custom domain name.</p>
            routing_mode: <p>The routing mode.</p>
            tags: <p>The collection of tags associated with a domain name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_domain_name_request.CreateDomainNameRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_domain_name_response.CreateDomainNameResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_domain_name

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_domain_name.async_create_domain_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_domain_name_request.CreateDomainNameRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if domain_name_configurations is not None:
            input["domain_name_configurations"] = domain_name_configurations
        if mutual_tls_authentication is not None:
            input["mutual_tls_authentication"] = mutual_tls_authentication
        if routing_mode is not None:
            input["routing_mode"] = routing_mode
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_integration(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_type: "aws_sdk_apigatewayv2.types.integration_type.IntegrationType",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        connection_id: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and1024.StringWithLengthBetween1And1024"
        ] = None,
        connection_type: Optional[
            "aws_sdk_apigatewayv2.types.connection_type.ConnectionType"
        ] = None,
        content_handling_strategy: Optional[
            "aws_sdk_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        credentials_arn: Optional["aws_sdk_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        integration_method: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        integration_subtype: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        integration_uri: Optional[
            "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        passthrough_behavior: Optional[
            "aws_sdk_apigatewayv2.types.passthrough_behavior.PassthroughBehavior"
        ] = None,
        payload_format_version: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_parameters: Optional[
            "aws_sdk_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        request_templates: Optional[
            "aws_sdk_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        response_parameters: Optional[
            "aws_sdk_apigatewayv2.types.response_parameters.ResponseParameters"
        ] = None,
        template_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        timeout_in_millis: Optional[
            "aws_sdk_apigatewayv2.types.integer_with_length_between50_and30000.IntegerWithLengthBetween50And30000"
        ] = None,
        tls_config: Optional[
            "aws_sdk_apigatewayv2.types.tls_config_input.TlsConfigInput"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_integration_result.CreateIntegrationResult":
        """<p>Creates an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            connection_id: <p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>
            connection_type: <p>The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.</p>
            content_handling_strategy: <p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            credentials_arn: <p>Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.</p>
            description: <p>The description of the integration.</p>
            integration_method: <p>Specifies the integration's HTTP method type.</p>
            integration_subtype: <p>Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html\">Integration subtype reference</a>.</p>
            integration_type: <p>The integration type of an integration. One of the following:</p> <p>AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.</p> <p>AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.</p> <p>HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.</p> <p>HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.</p> <p>MOCK: for integrating the route or method request with API Gateway as a \"loopback\" endpoint without invoking any backend. Supported only for WebSocket APIs.</p>
            integration_uri: <p>For a Lambda integration, specify the URI of a Lambda function.</p> <p>For an HTTP integration, specify a fully-qualified URL.</p> <p>For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html\">DiscoverInstances</a>. For private integrations, all resources must be owned by the same AWS account.</p>
            passthrough_behavior: <p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.</p> <p>WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.</p> <p>NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.</p> <p>WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.</p>
            payload_format_version: <p>Specifies the format of the payload sent to an integration. Required for HTTP APIs. Supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html\">Working with AWS Lambda proxy integrations for HTTP APIs</a>.</p>
            request_parameters: <p>For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.<replaceable>{location}</replaceable>.<replaceable>{name}</replaceable> , where <replaceable>{location}</replaceable> is querystring, path, or header; and <replaceable>{name}</replaceable> must be a valid and unique method request parameter name.</p> <p>For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html\">Working with AWS service integrations for HTTP APIs</a>.</p> <p>For HTTP API integrations without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern &lt;action&gt;:&lt;header|querystring|path&gt;.&lt;location&gt; where action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html\">Transforming API requests and responses</a>.</p>
            request_templates: <p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.</p>
            response_parameters: <p>Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match pattern &lt;action&gt;:&lt;header&gt;.&lt;location&gt; or overwrite.statuscode. The action can be append, overwrite or remove. The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html\">Transforming API requests and responses</a>.</p>
            template_selection_expression: <p>The template selection expression for the integration.</p>
            timeout_in_millis: <p>Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.</p>
            tls_config: <p>The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_integration_request.CreateIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_integration_result.CreateIntegrationResult"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_integration

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_integration_request.CreateIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if connection_id is not None:
            input["connection_id"] = connection_id
        if connection_type is not None:
            input["connection_type"] = connection_type
        if content_handling_strategy is not None:
            input["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None:
            input["credentials_arn"] = credentials_arn
        if description is not None:
            input["description"] = description
        if integration_method is not None:
            input["integration_method"] = integration_method
        if integration_subtype is not None:
            input["integration_subtype"] = integration_subtype
        input["integration_type"] = integration_type
        if integration_uri is not None:
            input["integration_uri"] = integration_uri
        if passthrough_behavior is not None:
            input["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None:
            input["payload_format_version"] = payload_format_version
        if request_parameters is not None:
            input["request_parameters"] = request_parameters
        if request_templates is not None:
            input["request_templates"] = request_templates
        if response_parameters is not None:
            input["response_parameters"] = response_parameters
        if template_selection_expression is not None:
            input["template_selection_expression"] = template_selection_expression
        if timeout_in_millis is not None:
            input["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            input["tls_config"] = tls_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_integration_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_response_key: "aws_sdk_apigatewayv2.types.selection_key.SelectionKey",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        content_handling_strategy: Optional[
            "aws_sdk_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        response_parameters: Optional[
            "aws_sdk_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        response_templates: Optional[
            "aws_sdk_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        template_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_integration_response_response.CreateIntegrationResponseResponse":
        """<p>Creates an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_handling_strategy: <p>Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_key: <p>The integration response key.</p>
            response_parameters: <p>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where {name} is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where {name} is a valid and unique response header name and {JSON-expression} is a valid JSON expression without the $ prefix.</p>
            response_templates: <p>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>
            template_selection_expression: <p>The template selection expression for the integration response. Supported only for WebSocket APIs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_integration_response_request.CreateIntegrationResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_integration_response_response.CreateIntegrationResponseResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_integration_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_integration_response.async_create_integration_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_integration_response_request.CreateIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if content_handling_strategy is not None:
            input["content_handling_strategy"] = content_handling_strategy
        input["integration_id"] = integration_id
        input["integration_response_key"] = integration_response_key
        if response_parameters is not None:
            input["response_parameters"] = response_parameters
        if response_templates is not None:
            input["response_templates"] = response_templates
        if template_selection_expression is not None:
            input["template_selection_expression"] = template_selection_expression

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_model(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        name: "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128",
        schema: "aws_sdk_apigatewayv2.types.string_with_length_between0_and32_k.StringWithLengthBetween0And32K",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        content_type: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and256.StringWithLengthBetween1And256"
        ] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_model_response.CreateModelResponse":
        """<p>Creates a Model for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_type: <p>The content-type for the model, for example, \"application/json\".</p>
            description: <p>The description of the model.</p>
            name: <p>The name of the model. Must be alphanumeric.</p>
            schema: <p>The schema for the model. For application/json models, this should be JSON schema draft 4 model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_model_request.CreateModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_model_response.CreateModelResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_model

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_model.async_create_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_model_request.CreateModelRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if content_type is not None:
            input["content_type"] = content_type
        if description is not None:
            input["description"] = description
        input["name"] = name
        input["schema"] = schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_portal(
        self,
        authorization: "aws_sdk_apigatewayv2.types.authorization.Authorization",
        endpoint_configuration: "aws_sdk_apigatewayv2.types.endpoint_configuration_request.EndpointConfigurationRequest",
        portal_content: "aws_sdk_apigatewayv2.types.portal_content.PortalContent",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        included_portal_product_arns: Optional[
            "aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
        ] = None,
        logo_uri: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max1092.__stringMin0Max1092"
        ] = None,
        rum_app_monitor_name: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
        ] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_portal_response.CreatePortalResponse":
        """<p>Creates a portal.</p>

        Args:
            authorization: <p>The authentication configuration for the portal.</p>
            endpoint_configuration: <p>The domain configuration for the portal. Use a default domain provided by API Gateway or provide a fully-qualified domain name that you own.</p>
            included_portal_product_arns: <p>The ARNs of the portal products included in the portal.</p>
            logo_uri: <p>The URI for the portal logo image that is displayed in the portal header.</p>
            portal_content: <p>The content of the portal.</p>
            rum_app_monitor_name: <p>The name of the Amazon CloudWatch RUM app monitor for the portal.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_portal_request.CreatePortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_portal_response.CreatePortalResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_portal.async_create_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_portal_request.CreatePortalRequest = {}  # type: ignore[typeddict-item]
        input["authorization"] = authorization
        input["endpoint_configuration"] = endpoint_configuration
        if included_portal_product_arns is not None:
            input["included_portal_product_arns"] = included_portal_product_arns
        if logo_uri is not None:
            input["logo_uri"] = logo_uri
        input["portal_content"] = portal_content
        if rum_app_monitor_name is not None:
            input["rum_app_monitor_name"] = rum_app_monitor_name
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_portal_product(
        self,
        display_name: "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_portal_product_response.CreatePortalProductResponse":
        """<p>Creates a new portal product.</p>

        Args:
            description: <p>A description of the portal product.</p>
            display_name: <p>The name of the portal product as it appears in a published portal.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_portal_product_request.CreatePortalProductRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_portal_product_response.CreatePortalProductResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_portal_product

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_portal_product.async_create_portal_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_portal_product_request.CreatePortalProductRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input["description"] = description
        input["display_name"] = display_name
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_product_page(
        self,
        display_content: "aws_sdk_apigatewayv2.types.display_content.DisplayContent",
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_product_page_response.CreateProductPageResponse":
        """<p>Creates a new product page for a portal product.</p>

        Args:
            display_content: <p>The content of the product page.</p>
            portal_product_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_product_page_request.CreateProductPageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_product_page_response.CreateProductPageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_product_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_product_page.async_create_product_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_product_page_request.CreateProductPageRequest = {}  # type: ignore[typeddict-item]
        input["display_content"] = display_content
        input["portal_product_id"] = portal_product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_product_rest_endpoint_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        rest_endpoint_identifier: "aws_sdk_apigatewayv2.types.rest_endpoint_identifier.RestEndpointIdentifier",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "aws_sdk_apigatewayv2.types.endpoint_display_content.EndpointDisplayContent"
        ] = None,
        try_it_state: Optional[
            "aws_sdk_apigatewayv2.types.try_it_state.TryItState"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_product_rest_endpoint_page_response.CreateProductRestEndpointPageResponse":
        """<p>Creates a product REST endpoint page for a portal product.</p>

        Args:
            display_content: <p>The content of the product REST endpoint page.</p>
            portal_product_id: <p>The portal product identifier.</p>
            rest_endpoint_identifier: <p>The REST endpoint identifier.</p>
            try_it_state: <p>The try it state of the product REST endpoint page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_product_rest_endpoint_page_request.CreateProductRestEndpointPageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_product_rest_endpoint_page_response.CreateProductRestEndpointPageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_product_rest_endpoint_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_product_rest_endpoint_page.async_create_product_rest_endpoint_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_product_rest_endpoint_page_request.CreateProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
        if display_content is not None:
            input["display_content"] = display_content
        input["portal_product_id"] = portal_product_id
        input["rest_endpoint_identifier"] = rest_endpoint_identifier
        if try_it_state is not None:
            input["try_it_state"] = try_it_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_route(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_key: "aws_sdk_apigatewayv2.types.selection_key.SelectionKey",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        api_key_required: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        authorization_scopes: Optional[
            "aws_sdk_apigatewayv2.types.authorization_scopes.AuthorizationScopes"
        ] = None,
        authorization_type: Optional[
            "aws_sdk_apigatewayv2.types.authorization_type.AuthorizationType"
        ] = None,
        authorizer_id: Optional["aws_sdk_apigatewayv2.types.id.Id"] = None,
        model_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        operation_name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_models: Optional[
            "aws_sdk_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        request_parameters: Optional[
            "aws_sdk_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_response_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        target: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_route_result.CreateRouteResult":
        """<p>Creates a Route for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_key_required: <p>Specifies whether an API key is required for the route. Supported only for WebSocket APIs.</p>
            authorization_scopes: <p>The authorization scopes supported by this route.</p>
            authorization_type: <p>The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer.</p>
            authorizer_id: <p>The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.</p>
            model_selection_expression: <p>The model selection expression for the route. Supported only for WebSocket APIs.</p>
            operation_name: <p>The operation name for the route.</p>
            request_models: <p>The request models for the route. Supported only for WebSocket APIs.</p>
            request_parameters: <p>The request parameters for the route. Supported only for WebSocket APIs.</p>
            route_key: <p>The route key for the route.</p>
            route_response_selection_expression: <p>The route response selection expression for the route. Supported only for WebSocket APIs.</p>
            target: <p>The target for the route.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_route_request.CreateRouteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_route_result.CreateRouteResult"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_route

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_route.async_create_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_route_request.CreateRouteRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if api_key_required is not None:
            input["api_key_required"] = api_key_required
        if authorization_scopes is not None:
            input["authorization_scopes"] = authorization_scopes
        if authorization_type is not None:
            input["authorization_type"] = authorization_type
        if authorizer_id is not None:
            input["authorizer_id"] = authorizer_id
        if model_selection_expression is not None:
            input["model_selection_expression"] = model_selection_expression
        if operation_name is not None:
            input["operation_name"] = operation_name
        if request_models is not None:
            input["request_models"] = request_models
        if request_parameters is not None:
            input["request_parameters"] = request_parameters
        input["route_key"] = route_key
        if route_response_selection_expression is not None:
            input["route_response_selection_expression"] = (
                route_response_selection_expression
            )
        if target is not None:
            input["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_route_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_response_key: "aws_sdk_apigatewayv2.types.selection_key.SelectionKey",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        model_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        response_models: Optional[
            "aws_sdk_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        response_parameters: Optional[
            "aws_sdk_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_route_response_response.CreateRouteResponseResponse":
        """<p>Creates a RouteResponse for a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_selection_expression: <p>The model selection expression for the route response. Supported only for WebSocket APIs.</p>
            response_models: <p>The response models for the route response.</p>
            response_parameters: <p>The route response parameters.</p>
            route_id: <p>The route ID.</p>
            route_response_key: <p>The route response key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_route_response_request.CreateRouteResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_route_response_response.CreateRouteResponseResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_route_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_route_response.async_create_route_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_route_response_request.CreateRouteResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if model_selection_expression is not None:
            input["model_selection_expression"] = model_selection_expression
        if response_models is not None:
            input["response_models"] = response_models
        if response_parameters is not None:
            input["response_parameters"] = response_parameters
        input["route_id"] = route_id
        input["route_response_key"] = route_response_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_routing_rule(
        self,
        actions: "aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction",
        conditions: "aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition",
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        priority: "aws_sdk_apigatewayv2.types.routing_rule_priority.RoutingRulePriority",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_routing_rule_response.CreateRoutingRuleResponse":
        """<p>Creates a RoutingRule.</p>

        Args:
            actions: <p>Represents a routing rule action. The only supported action is invokeApi.</p>
            conditions: <p>Represents a condition. Conditions can contain up to two matchHeaders conditions and one matchBasePaths conditions. API Gateway evaluates header conditions and base path conditions together. You can only use AND between header and base path conditions.</p>
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            priority: Represents the priority of the routing rule.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_routing_rule_request.CreateRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_routing_rule_response.CreateRoutingRuleResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_routing_rule

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_routing_rule.async_create_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_routing_rule_request.CreateRoutingRuleRequest = {}  # type: ignore[typeddict-item]
        input["actions"] = actions
        input["conditions"] = conditions
        input["domain_name"] = domain_name
        if domain_name_id is not None:
            input["domain_name_id"] = domain_name_id
        input["priority"] = priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_stage(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        access_log_settings: Optional[
            "aws_sdk_apigatewayv2.types.access_log_settings.AccessLogSettings"
        ] = None,
        auto_deploy: Optional["aws_sdk_apigatewayv2.types.__boolean.__boolean"] = None,
        client_certificate_id: Optional["aws_sdk_apigatewayv2.types.id.Id"] = None,
        default_route_settings: Optional[
            "aws_sdk_apigatewayv2.types.route_settings.RouteSettings"
        ] = None,
        deployment_id: Optional["aws_sdk_apigatewayv2.types.id.Id"] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        route_settings: Optional[
            "aws_sdk_apigatewayv2.types.route_settings_map.RouteSettingsMap"
        ] = None,
        stage_variables: Optional[
            "aws_sdk_apigatewayv2.types.stage_variables_map.StageVariablesMap"
        ] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_stage_response.CreateStageResponse":
        """<p>Creates a Stage for an API.</p>

        Args:
            access_log_settings: <p>Settings for logging access in this stage.</p>
            api_id: <p>The API identifier.</p>
            auto_deploy: <p>Specifies whether updates to an API automatically trigger a new deployment. The default value is false.</p>
            client_certificate_id: <p>The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.</p>
            default_route_settings: <p>The default route settings for the stage.</p>
            deployment_id: <p>The deployment identifier of the API stage.</p>
            description: <p>The description for the API stage.</p>
            route_settings: <p>Route settings for the stage, by routeKey.</p>
            stage_name: <p>The name of the stage.</p>
            stage_variables: <p>A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&amp;=,]+.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_stage_request.CreateStageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_stage_response.CreateStageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_stage

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_stage.async_create_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_stage_request.CreateStageRequest = {}  # type: ignore[typeddict-item]
        if access_log_settings is not None:
            input["access_log_settings"] = access_log_settings
        input["api_id"] = api_id
        if auto_deploy is not None:
            input["auto_deploy"] = auto_deploy
        if client_certificate_id is not None:
            input["client_certificate_id"] = client_certificate_id
        if default_route_settings is not None:
            input["default_route_settings"] = default_route_settings
        if deployment_id is not None:
            input["deployment_id"] = deployment_id
        if description is not None:
            input["description"] = description
        if route_settings is not None:
            input["route_settings"] = route_settings
        input["stage_name"] = stage_name
        if stage_variables is not None:
            input["stage_variables"] = stage_variables
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_vpc_link(
        self,
        name: "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128",
        subnet_ids: "aws_sdk_apigatewayv2.types.subnet_id_list.SubnetIdList",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        security_group_ids: Optional[
            "aws_sdk_apigatewayv2.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
    ) -> "aws_sdk_apigatewayv2.types.create_vpc_link_response.CreateVpcLinkResponse":
        """<p>Creates a VPC link.</p>

        Args:
            name: <p>The name of the VPC link.</p>
            security_group_ids: <p>A list of security group IDs for the VPC link.</p>
            subnet_ids: <p>A list of subnet IDs to include in the VPC link.</p>
            tags: <p>A list of tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.create_vpc_link_request.CreateVpcLinkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.create_vpc_link_response.CreateVpcLinkResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.create_vpc_link

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.create_vpc_link.async_create_vpc_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.create_vpc_link_request.CreateVpcLinkRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids
        input["subnet_ids"] = subnet_ids
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_access_log_settings(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the AccessLogSettings for a Stage. To disable access logging for a Stage, delete its AccessLogSettings.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_access_log_settings_request.DeleteAccessLogSettingsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_access_log_settings

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_access_log_settings.async_delete_access_log_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_access_log_settings_request.DeleteAccessLogSettingsRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_api(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_api_request.DeleteApiRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_api.async_delete_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_api_request.DeleteApiRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_api_mapping(
        self,
        api_mapping_id: "aws_sdk_apigatewayv2.types.__string.__string",
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an API mapping.</p>

        Args:
            api_mapping_id: <p>The API mapping identifier.</p>
            domain_name: <p>The domain name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_api_mapping_request.DeleteApiMappingRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_api_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_api_mapping.async_delete_api_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_api_mapping_request.DeleteApiMappingRequest = {}  # type: ignore[typeddict-item]
        input["api_mapping_id"] = api_mapping_id
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_authorizer(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        authorizer_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an Authorizer.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_id: <p>The authorizer identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_authorizer_request.DeleteAuthorizerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_authorizer

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_authorizer.async_delete_authorizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_authorizer_request.DeleteAuthorizerRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["authorizer_id"] = authorizer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_cors_configuration(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a CORS configuration.</p>

        Args:
            api_id: <p>The API identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_cors_configuration_request.DeleteCorsConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_cors_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_cors_configuration.async_delete_cors_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_cors_configuration_request.DeleteCorsConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_deployment(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        deployment_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Deployment.</p>

        Args:
            api_id: <p>The API identifier.</p>
            deployment_id: <p>The deployment ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_deployment_request.DeleteDeploymentRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_deployment_request.DeleteDeploymentRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_domain_name(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_domain_name_request.DeleteDomainNameRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_domain_name

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_domain_name.async_delete_domain_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_domain_name_request.DeleteDomainNameRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_integration(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_integration_request.DeleteIntegrationRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_integration

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_integration_request.DeleteIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["integration_id"] = integration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_integration_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_response_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_id: <p>The integration response ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_integration_response_request.DeleteIntegrationResponseRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_integration_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_integration_response.async_delete_integration_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_integration_response_request.DeleteIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["integration_id"] = integration_id
        input["integration_response_id"] = integration_response_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_model(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        model_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Model.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_id: <p>The model ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_model_request.DeleteModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_model

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_model.async_delete_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_model_request.DeleteModelRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["model_id"] = model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_portal(
        self,
        portal_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a portal.</p>

        Args:
            portal_id: <p>The portal identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_portal_request.DeletePortalRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_portal.async_delete_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_portal_request.DeletePortalRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_portal_product(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_portal_product_request.DeletePortalProductRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_portal_product

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_portal_product.async_delete_portal_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_portal_product_request.DeletePortalProductRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_portal_product_sharing_policy(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the sharing policy for a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_portal_product_sharing_policy_request.DeletePortalProductSharingPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_portal_product_sharing_policy

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_portal_product_sharing_policy.async_delete_portal_product_sharing_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_portal_product_sharing_policy_request.DeletePortalProductSharingPolicyRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_product_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        product_page_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a product page of a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            product_page_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_product_page_request.DeleteProductPageRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_product_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_product_page.async_delete_product_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_product_page_request.DeleteProductPageRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id
        input["product_page_id"] = product_page_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_product_rest_endpoint_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        product_rest_endpoint_page_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a product REST endpoint page.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            product_rest_endpoint_page_id: <p>The product REST endpoint identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_product_rest_endpoint_page_request.DeleteProductRestEndpointPageRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_product_rest_endpoint_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_product_rest_endpoint_page.async_delete_product_rest_endpoint_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_product_rest_endpoint_page_request.DeleteProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id
        input["product_rest_endpoint_page_id"] = product_rest_endpoint_page_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_route(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_route_request.DeleteRouteRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route.async_delete_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_route_request.DeleteRouteRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["route_id"] = route_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_route_request_parameter(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        request_parameter_key: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a route request parameter. Supported only for WebSocket APIs.</p>

        Args:
            api_id: <p>The API identifier.</p>
            request_parameter_key: <p>The route request parameter key.</p>
            route_id: <p>The route ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_route_request_parameter_request.DeleteRouteRequestParameterRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route_request_parameter

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route_request_parameter.async_delete_route_request_parameter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_route_request_parameter_request.DeleteRouteRequestParameterRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["request_parameter_key"] = request_parameter_key
        input["route_id"] = route_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_route_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_response_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a RouteResponse.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>
            route_response_id: <p>The route response ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_route_response_request.DeleteRouteResponseRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route_response.async_delete_route_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_route_response_request.DeleteRouteResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["route_id"] = route_id
        input["route_response_id"] = route_response_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_route_settings(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_key: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the RouteSettings for a stage.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_key: <p>The route key.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_route_settings_request.DeleteRouteSettingsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route_settings

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_route_settings.async_delete_route_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_route_settings_request.DeleteRouteSettingsRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["route_key"] = route_key
        input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_routing_rule(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        routing_rule_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> None:
        """<p>Deletes a routing rule.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            routing_rule_id: <p>The routing rule ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_routing_rule_request.DeleteRoutingRuleRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_routing_rule

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_routing_rule.async_delete_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_routing_rule_request.DeleteRoutingRuleRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if domain_name_id is not None:
            input["domain_name_id"] = domain_name_id
        input["routing_rule_id"] = routing_rule_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_stage(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Stage.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_stage_request.DeleteStageRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_stage

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_stage.async_delete_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_stage_request.DeleteStageRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_vpc_link(
        self,
        vpc_link_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse":
        """<p>Deletes a VPC link.</p>

        Args:
            vpc_link_id: <p>The ID of the VPC link.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_vpc_link

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.delete_vpc_link.async_delete_vpc_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest = {}  # type: ignore[typeddict-item]
        input["vpc_link_id"] = vpc_link_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_portal(
        self,
        portal_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the publication of a portal portal.</p>

        Args:
            portal_id: <p>The portal identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.disable_portal_request.DisablePortalRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.disable_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.disable_portal.async_disable_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.disable_portal_request.DisablePortalRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def export_api(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        output_type: "aws_sdk_apigatewayv2.types.__string.__string",
        specification: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        export_version: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        include_extensions: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        stage_name: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.export_api_response.ExportApiResponse":
        """export_api

        Args:
            api_id: <p>The API identifier.</p>
            export_version: <p>The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is 1.0.</p>
            include_extensions: <p>Specifies whether to include <a href=\"https://docs.aws.amazon.com//apigateway/latest/developerguide/api-gateway-swagger-extensions.html\">API Gateway extensions</a> in the exported API definition. API Gateway extensions are included by default.</p>
            output_type: <p>The output type of the exported definition file. Valid values are JSON and YAML.</p>
            specification: <p>The version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value.</p>
            stage_name: <p>The name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.export_api_request.ExportApiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.export_api_response.ExportApiResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.export_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.export_api.async_export_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.export_api_request.ExportApiRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if export_version is not None:
            input["export_version"] = export_version
        if include_extensions is not None:
            input["include_extensions"] = include_extensions
        input["output_type"] = output_type
        input["specification"] = specification
        if stage_name is not None:
            input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_api(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_api_response.GetApiResponse":
        """<p>Gets an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_api_request.GetApiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_api_response.GetApiResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_api.async_get_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_api_request.GetApiRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_api_mapping(
        self,
        api_mapping_id: "aws_sdk_apigatewayv2.types.__string.__string",
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_api_mapping_response.GetApiMappingResponse":
        """<p>Gets an API mapping.</p>

        Args:
            api_mapping_id: <p>The API mapping identifier.</p>
            domain_name: <p>The domain name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_api_mapping_request.GetApiMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_api_mapping_response.GetApiMappingResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_api_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_api_mapping.async_get_api_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_api_mapping_request.GetApiMappingRequest = {}  # type: ignore[typeddict-item]
        input["api_mapping_id"] = api_mapping_id
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_api_mappings(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_api_mappings_response.GetApiMappingsResponse":
        """<p>Gets API mappings.</p>

        Args:
            domain_name: <p>The domain name.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_api_mappings_request.GetApiMappingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_api_mappings_response.GetApiMappingsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_api_mappings

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_api_mappings.async_get_api_mappings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_api_mappings_request.GetApiMappingsRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_apis(
        self,
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_apis_response.GetApisResponse":
        """<p>Gets a collection of Api resources.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_apis_request.GetApisRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_apis_response.GetApisResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_apis

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_apis.async_get_apis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_apis_request.GetApisRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_authorizer(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        authorizer_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_authorizer_response.GetAuthorizerResponse":
        """<p>Gets an Authorizer.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_id: <p>The authorizer identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_authorizer_request.GetAuthorizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_authorizer_response.GetAuthorizerResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_authorizer

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_authorizer.async_get_authorizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_authorizer_request.GetAuthorizerRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["authorizer_id"] = authorizer_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_authorizers(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_authorizers_response.GetAuthorizersResponse":
        """<p>Gets the Authorizers for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_authorizers_request.GetAuthorizersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_authorizers_response.GetAuthorizersResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_authorizers

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_authorizers.async_get_authorizers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_authorizers_request.GetAuthorizersRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_deployment(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        deployment_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_deployment_response.GetDeploymentResponse":
        """<p>Gets a Deployment.</p>

        Args:
            api_id: <p>The API identifier.</p>
            deployment_id: <p>The deployment ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_deployment_request.GetDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_deployment_response.GetDeploymentResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_deployment_request.GetDeploymentRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_deployments(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_deployments_response.GetDeploymentsResponse":
        """<p>Gets the Deployments for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_deployments_request.GetDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_deployments_response.GetDeploymentsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_deployments

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_deployments.async_get_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_deployments_request.GetDeploymentsRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_domain_name(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_domain_name_response.GetDomainNameResponse":
        """<p>Gets a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_domain_name_request.GetDomainNameRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_domain_name_response.GetDomainNameResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_domain_name

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_domain_name.async_get_domain_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_domain_name_request.GetDomainNameRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_domain_names(
        self,
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_domain_names_response.GetDomainNamesResponse":
        """<p>Gets the domain names for an AWS account.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_domain_names_request.GetDomainNamesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_domain_names_response.GetDomainNamesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_domain_names

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_domain_names.async_get_domain_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_domain_names_request.GetDomainNamesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_integration(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_integration_result.GetIntegrationResult":
        """<p>Gets an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_integration_request.GetIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_integration_result.GetIntegrationResult"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integration

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integration.async_get_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_integration_request.GetIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["integration_id"] = integration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_integration_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_response_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_integration_response_response.GetIntegrationResponseResponse":
        """<p>Gets an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_id: <p>The integration response ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_integration_response_request.GetIntegrationResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_integration_response_response.GetIntegrationResponseResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integration_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integration_response.async_get_integration_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_integration_response_request.GetIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["integration_id"] = integration_id
        input["integration_response_id"] = integration_response_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_integration_responses(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_integration_responses_response.GetIntegrationResponsesResponse":
        """<p>Gets the IntegrationResponses for an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_integration_responses_request.GetIntegrationResponsesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_integration_responses_response.GetIntegrationResponsesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integration_responses

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integration_responses.async_get_integration_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_integration_responses_request.GetIntegrationResponsesRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["integration_id"] = integration_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_integrations(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_integrations_response.GetIntegrationsResponse":
        """<p>Gets the Integrations for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_integrations_request.GetIntegrationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_integrations_response.GetIntegrationsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integrations

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_integrations.async_get_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_integrations_request.GetIntegrationsRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_model(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        model_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_model_response.GetModelResponse":
        """<p>Gets a Model.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_id: <p>The model ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_model_request.GetModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_model_response.GetModelResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_model

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_model.async_get_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_model_request.GetModelRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["model_id"] = model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_models(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_models_response.GetModelsResponse":
        """<p>Gets the Models for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_models_request.GetModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_models_response.GetModelsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_models

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_models.async_get_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_models_request.GetModelsRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_model_template(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        model_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_model_template_response.GetModelTemplateResponse":
        """<p>Gets a model template.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_id: <p>The model ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_model_template_request.GetModelTemplateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_model_template_response.GetModelTemplateResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_model_template

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_model_template.async_get_model_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_model_template_request.GetModelTemplateRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["model_id"] = model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_portal(
        self,
        portal_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_portal_response.GetPortalResponse":
        """<p>Gets a portal.</p>

        Args:
            portal_id: <p>The portal identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_portal_request.GetPortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_portal_response.GetPortalResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_portal.async_get_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_portal_request.GetPortalRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_portal_product(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        resource_owner_account_id: Optional[
            "aws_sdk_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_portal_product_response.GetPortalProductResponse":
        """<p>Gets a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_portal_product_request.GetPortalProductRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_portal_product_response.GetPortalProductResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_portal_product

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_portal_product.async_get_portal_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_portal_product_request.GetPortalProductRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id
        if resource_owner_account_id is not None:
            input["resource_owner_account_id"] = resource_owner_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_portal_product_sharing_policy(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_portal_product_sharing_policy_response.GetPortalProductSharingPolicyResponse":
        """<p>Gets the sharing policy for a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_portal_product_sharing_policy_request.GetPortalProductSharingPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_portal_product_sharing_policy_response.GetPortalProductSharingPolicyResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_portal_product_sharing_policy

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_portal_product_sharing_policy.async_get_portal_product_sharing_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_portal_product_sharing_policy_request.GetPortalProductSharingPolicyRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_product_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        product_page_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        resource_owner_account_id: Optional[
            "aws_sdk_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_product_page_response.GetProductPageResponse":
        """<p>Gets a product page of a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            product_page_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_product_page_request.GetProductPageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_product_page_response.GetProductPageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_product_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_product_page.async_get_product_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_product_page_request.GetProductPageRequest = {}  # type: ignore[typeddict-item]
        input["portal_product_id"] = portal_product_id
        input["product_page_id"] = product_page_id
        if resource_owner_account_id is not None:
            input["resource_owner_account_id"] = resource_owner_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_product_rest_endpoint_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        product_rest_endpoint_page_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        include_raw_display_content: Optional[
            "aws_sdk_apigatewayv2.types.__string.__string"
        ] = None,
        resource_owner_account_id: Optional[
            "aws_sdk_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_product_rest_endpoint_page_response.GetProductRestEndpointPageResponse":
        """<p>Gets a product REST endpoint page.</p>

        Args:
            include_raw_display_content: <p>The query parameter to include raw display content.</p>
            portal_product_id: <p>The portal product identifier.</p>
            product_rest_endpoint_page_id: <p>The product REST endpoint identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_product_rest_endpoint_page_request.GetProductRestEndpointPageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_product_rest_endpoint_page_response.GetProductRestEndpointPageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_product_rest_endpoint_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_product_rest_endpoint_page.async_get_product_rest_endpoint_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_product_rest_endpoint_page_request.GetProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
        if include_raw_display_content is not None:
            input["include_raw_display_content"] = include_raw_display_content
        input["portal_product_id"] = portal_product_id
        input["product_rest_endpoint_page_id"] = product_rest_endpoint_page_id
        if resource_owner_account_id is not None:
            input["resource_owner_account_id"] = resource_owner_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_route(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_route_result.GetRouteResult":
        """<p>Gets a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_route_request.GetRouteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_route_result.GetRouteResult"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_route

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_route.async_get_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_route_request.GetRouteRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["route_id"] = route_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_route_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_response_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_route_response_response.GetRouteResponseResponse":
        """<p>Gets a RouteResponse.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>
            route_response_id: <p>The route response ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_route_response_request.GetRouteResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_route_response_response.GetRouteResponseResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_route_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_route_response.async_get_route_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_route_response_request.GetRouteResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["route_id"] = route_id
        input["route_response_id"] = route_response_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_route_responses(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_route_responses_response.GetRouteResponsesResponse":
        """<p>Gets the RouteResponses for a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            route_id: <p>The route ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_route_responses_request.GetRouteResponsesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_route_responses_response.GetRouteResponsesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_route_responses

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_route_responses.async_get_route_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_route_responses_request.GetRouteResponsesRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["route_id"] = route_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_routes(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_routes_response.GetRoutesResponse":
        """<p>Gets the Routes for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_routes_request.GetRoutesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_routes_response.GetRoutesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_routes

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_routes.async_get_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_routes_request.GetRoutesRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_routing_rule(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        routing_rule_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_routing_rule_response.GetRoutingRuleResponse":
        """<p>Gets a routing rule.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            routing_rule_id: <p>The routing rule ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_routing_rule_request.GetRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_routing_rule_response.GetRoutingRuleResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_routing_rule

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_routing_rule.async_get_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_routing_rule_request.GetRoutingRuleRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if domain_name_id is not None:
            input["domain_name_id"] = domain_name_id
        input["routing_rule_id"] = routing_rule_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_stage(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_stage_response.GetStageResponse":
        """<p>Gets a Stage.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_stage_request.GetStageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_stage_response.GetStageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_stage

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_stage.async_get_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_stage_request.GetStageRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_stages(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_stages_response.GetStagesResponse":
        """<p>Gets the Stages for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_stages_request.GetStagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_stages_response.GetStagesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_stages

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_stages.async_get_stages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_stages_request.GetStagesRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_tags(
        self,
        resource_arn: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_tags_response.GetTagsResponse":
        """<p>Gets a collection of Tag resources.</p>

        Args:
            resource_arn: <p>The resource ARN for the tag.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_tags_request.GetTagsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_tags_response.GetTagsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_tags

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_tags.async_get_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_tags_request.GetTagsRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_vpc_link(
        self,
        vpc_link_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_vpc_link_response.GetVpcLinkResponse":
        """<p>Gets a VPC link.</p>

        Args:
            vpc_link_id: <p>The ID of the VPC link.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_vpc_link_request.GetVpcLinkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_vpc_link_response.GetVpcLinkResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_vpc_link

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_vpc_link.async_get_vpc_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_vpc_link_request.GetVpcLinkRequest = {}  # type: ignore[typeddict-item]
        input["vpc_link_id"] = vpc_link_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_vpc_links(
        self,
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.get_vpc_links_response.GetVpcLinksResponse":
        """<p>Gets a collection of VPC links.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.get_vpc_links_request.GetVpcLinksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.get_vpc_links_response.GetVpcLinksResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.get_vpc_links

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.get_vpc_links.async_get_vpc_links(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.get_vpc_links_request.GetVpcLinksRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_api(
        self,
        body: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        basepath: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        fail_on_warnings: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.import_api_response.ImportApiResponse":
        """<p>Imports an API.</p>

        Args:
            basepath: <p>Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.</p>
            body: <p>The OpenAPI definition. Supported only for HTTP APIs.</p>
            fail_on_warnings: <p>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.import_api_request.ImportApiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.import_api_response.ImportApiResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.import_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.import_api.async_import_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.import_api_request.ImportApiRequest = {}  # type: ignore[typeddict-item]
        if basepath is not None:
            input["basepath"] = basepath
        input["body"] = body
        if fail_on_warnings is not None:
            input["fail_on_warnings"] = fail_on_warnings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_portal_products(
        self,
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        resource_owner: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.list_portal_products_response.ListPortalProductsResponse":
        """<p>Lists portal products.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            resource_owner: <p>The resource owner of the portal product.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.list_portal_products_request.ListPortalProductsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.list_portal_products_response.ListPortalProductsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.list_portal_products

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.list_portal_products.async_list_portal_products(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.list_portal_products_request.ListPortalProductsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if resource_owner is not None:
            input["resource_owner"] = resource_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_portals(
        self,
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.list_portals_response.ListPortalsResponse":
        """<p>Lists portals.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.list_portals_request.ListPortalsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.list_portals_response.ListPortalsResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.list_portals

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.list_portals.async_list_portals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.list_portals_request.ListPortalsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_product_pages(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        resource_owner_account_id: Optional[
            "aws_sdk_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.list_product_pages_response.ListProductPagesResponse":
        """<p>Lists the product pages for a portal product.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            portal_product_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.list_product_pages_request.ListProductPagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.list_product_pages_response.ListProductPagesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.list_product_pages

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.list_product_pages.async_list_product_pages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.list_product_pages_request.ListProductPagesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["portal_product_id"] = portal_product_id
        if resource_owner_account_id is not None:
            input["resource_owner_account_id"] = resource_owner_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_product_rest_endpoint_pages(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        max_results: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        resource_owner_account_id: Optional[
            "aws_sdk_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.list_product_rest_endpoint_pages_response.ListProductRestEndpointPagesResponse":
        """<p>Lists the product REST endpoint pages of a portal product.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            portal_product_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.list_product_rest_endpoint_pages_request.ListProductRestEndpointPagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.list_product_rest_endpoint_pages_response.ListProductRestEndpointPagesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.list_product_rest_endpoint_pages

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.list_product_rest_endpoint_pages.async_list_product_rest_endpoint_pages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.list_product_rest_endpoint_pages_request.ListProductRestEndpointPagesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["portal_product_id"] = portal_product_id
        if resource_owner_account_id is not None:
            input["resource_owner_account_id"] = resource_owner_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_routing_rules(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_apigatewayv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.list_routing_rules_response.ListRoutingRulesResponse":
        """<p>Lists routing rules.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.list_routing_rules_request.ListRoutingRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.list_routing_rules_response.ListRoutingRulesResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.list_routing_rules

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.list_routing_rules.async_list_routing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.list_routing_rules_request.ListRoutingRulesRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if domain_name_id is not None:
            input["domain_name_id"] = domain_name_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_routing_rules(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        max_results: Optional[
            "aws_sdk_apigatewayv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "AsyncIterator[aws_sdk_apigatewayv2.types.routing_rule.RoutingRule]":
        _token = next_token
        while True:
            _response = await self.list_routing_rules(
                domain_name,
                config_overrides=config_overrides,
                domain_name_id=domain_name_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("routing_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def preview_portal(
        self,
        portal_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.preview_portal_response.PreviewPortalResponse":
        """<p>Creates a portal preview.</p>

        Args:
            portal_id: <p>The portal identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.preview_portal_request.PreviewPortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.preview_portal_response.PreviewPortalResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.preview_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.preview_portal.async_preview_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.preview_portal_request.PreviewPortalRequest = {}  # type: ignore[typeddict-item]
        input["portal_id"] = portal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def publish_portal(
        self,
        portal_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.publish_portal_response.PublishPortalResponse":
        """<p>Publishes a portal.</p>

        Args:
            description: <p>The description of the portal. When the portal is published, this description becomes the last published description.</p>
            portal_id: <p>The portal identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.publish_portal_request.PublishPortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.publish_portal_response.PublishPortalResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.publish_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.publish_portal.async_publish_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.publish_portal_request.PublishPortalRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input["description"] = description
        input["portal_id"] = portal_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_portal_product_sharing_policy(
        self,
        policy_document: "aws_sdk_apigatewayv2.types.__string_min1_max307200.__stringMin1Max307200",
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> "aws_sdk_apigatewayv2.types.put_portal_product_sharing_policy_response.PutPortalProductSharingPolicyResponse":
        """<p>Updates the sharing policy for a portal product.</p>

        Args:
            policy_document: <p>The product sharing policy.</p>
            portal_product_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.put_portal_product_sharing_policy_request.PutPortalProductSharingPolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.put_portal_product_sharing_policy_response.PutPortalProductSharingPolicyResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.put_portal_product_sharing_policy

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.put_portal_product_sharing_policy.async_put_portal_product_sharing_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.put_portal_product_sharing_policy_request.PutPortalProductSharingPolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_document"] = policy_document
        input["portal_product_id"] = portal_product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_routing_rule(
        self,
        actions: "aws_sdk_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction",
        conditions: "aws_sdk_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition",
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        priority: "aws_sdk_apigatewayv2.types.routing_rule_priority.RoutingRulePriority",
        routing_rule_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
    ) -> "aws_sdk_apigatewayv2.types.put_routing_rule_response.PutRoutingRuleResponse":
        """<p>Updates a routing rule.</p>

        Args:
            actions: <p>The routing rule action.</p>
            conditions: <p>The routing rule condition.</p>
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            priority: <p>The routing rule priority.</p>
            routing_rule_id: <p>The routing rule ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.put_routing_rule_request.PutRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.put_routing_rule_response.PutRoutingRuleResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.put_routing_rule

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.put_routing_rule.async_put_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.put_routing_rule_request.PutRoutingRuleRequest = {}  # type: ignore[typeddict-item]
        input["actions"] = actions
        input["conditions"] = conditions
        input["domain_name"] = domain_name
        if domain_name_id is not None:
            input["domain_name_id"] = domain_name_id
        input["priority"] = priority
        input["routing_rule_id"] = routing_rule_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reimport_api(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        body: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        basepath: Optional["aws_sdk_apigatewayv2.types.__string.__string"] = None,
        fail_on_warnings: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.reimport_api_response.ReimportApiResponse":
        """<p>Puts an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>
            basepath: <p>Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html\">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.</p>
            body: <p>The OpenAPI definition. Supported only for HTTP APIs.</p>
            fail_on_warnings: <p>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.reimport_api_request.ReimportApiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.reimport_api_response.ReimportApiResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.reimport_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.reimport_api.async_reimport_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.reimport_api_request.ReimportApiRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if basepath is not None:
            input["basepath"] = basepath
        input["body"] = body
        if fail_on_warnings is not None:
            input["fail_on_warnings"] = fail_on_warnings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_authorizers_cache(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Resets all authorizer cache entries on a stage. Supported only for HTTP APIs.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.reset_authorizers_cache_request.ResetAuthorizersCacheRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.reset_authorizers_cache

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.reset_authorizers_cache.async_reset_authorizers_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.reset_authorizers_cache_request.ResetAuthorizersCacheRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["stage_name"] = stage_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        tags: Optional["aws_sdk_apigatewayv2.types.tags.Tags"] = None,
    ) -> "aws_sdk_apigatewayv2.types.tag_resource_response.TagResourceResponse":
        """<p>Creates a new Tag resource to represent a tag.</p>

        Args:
            resource_arn: <p>The resource ARN for the tag.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_apigatewayv2.types.__string.__string",
        tag_keys: "aws_sdk_apigatewayv2.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Tag.</p>

        Args:
            resource_arn: <p>The resource ARN for the tag.</p>
            tag_keys: <p>The Tag keys to delete</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_api(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        api_key_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        cors_configuration: Optional["aws_sdk_apigatewayv2.types.cors.Cors"] = None,
        credentials_arn: Optional["aws_sdk_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        disable_schema_validation: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        disable_execute_api_endpoint: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_apigatewayv2.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        route_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        target: Optional[
            "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        version: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_api_response.UpdateApiResponse":
        """<p>Updates an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_key_selection_expression: <p>An API key selection expression. Supported only for WebSocket APIs. See <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions\">API Key Selection Expressions</a>.</p>
            cors_configuration: <p>A CORS configuration. Supported only for HTTP APIs.</p>
            credentials_arn: <p>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, don't specify this parameter. Currently, this property is not used for HTTP integrations. If provided, this value replaces the credentials associated with the quick create integration. Supported only for HTTP APIs.</p>
            description: <p>The description of the API.</p>
            disable_schema_validation: <p>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</p>
            disable_execute_api_endpoint: <p>Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>
            ip_address_type: <p>The IP address types that can invoke your API or domain name.</p>
            name: <p>The name of the API.</p>
            route_key: <p>This property is part of quick create. If not specified, the route created using quick create is kept. Otherwise, this value replaces the route key of the quick create route. Additional routes may still be added after the API is updated. Supported only for HTTP APIs.</p>
            route_selection_expression: <p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>
            target: <p>This property is part of quick create. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. The value provided updates the integration URI and integration type. You can update a quick-created target, but you can't remove it from an API. Supported only for HTTP APIs.</p>
            version: <p>A version identifier for the API.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_api_request.UpdateApiRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_api_response.UpdateApiResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_api

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_api.async_update_api(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_api_request.UpdateApiRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if api_key_selection_expression is not None:
            input["api_key_selection_expression"] = api_key_selection_expression
        if cors_configuration is not None:
            input["cors_configuration"] = cors_configuration
        if credentials_arn is not None:
            input["credentials_arn"] = credentials_arn
        if description is not None:
            input["description"] = description
        if disable_schema_validation is not None:
            input["disable_schema_validation"] = disable_schema_validation
        if disable_execute_api_endpoint is not None:
            input["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if name is not None:
            input["name"] = name
        if route_key is not None:
            input["route_key"] = route_key
        if route_selection_expression is not None:
            input["route_selection_expression"] = route_selection_expression
        if target is not None:
            input["target"] = target
        if version is not None:
            input["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_api_mapping(
        self,
        api_id: "aws_sdk_apigatewayv2.types.id.Id",
        api_mapping_id: "aws_sdk_apigatewayv2.types.__string.__string",
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        api_mapping_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        stage: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_api_mapping_response.UpdateApiMappingResponse":
        """<p>The API mapping.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_mapping_id: <p>The API mapping identifier.</p>
            api_mapping_key: <p>The API mapping key.</p>
            domain_name: <p>The domain name.</p>
            stage: <p>The API stage.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_api_mapping_request.UpdateApiMappingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_api_mapping_response.UpdateApiMappingResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_api_mapping

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_api_mapping.async_update_api_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_api_mapping_request.UpdateApiMappingRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["api_mapping_id"] = api_mapping_id
        if api_mapping_key is not None:
            input["api_mapping_key"] = api_mapping_key
        input["domain_name"] = domain_name
        if stage is not None:
            input["stage"] = stage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_authorizer(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        authorizer_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        authorizer_credentials_arn: Optional[
            "aws_sdk_apigatewayv2.types.arn.Arn"
        ] = None,
        authorizer_payload_format_version: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        authorizer_result_ttl_in_seconds: Optional[
            "aws_sdk_apigatewayv2.types.integer_with_length_between0_and3600.IntegerWithLengthBetween0And3600"
        ] = None,
        authorizer_type: Optional[
            "aws_sdk_apigatewayv2.types.authorizer_type.AuthorizerType"
        ] = None,
        authorizer_uri: Optional[
            "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        enable_simple_responses: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        identity_source: Optional[
            "aws_sdk_apigatewayv2.types.identity_source_list.IdentitySourceList"
        ] = None,
        identity_validation_expression: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        jwt_configuration: Optional[
            "aws_sdk_apigatewayv2.types.jwt_configuration.JWTConfiguration"
        ] = None,
        name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> (
        "aws_sdk_apigatewayv2.types.update_authorizer_response.UpdateAuthorizerResponse"
    ):
        """<p>Updates an Authorizer.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_credentials_arn: <p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter.</p>
            authorizer_id: <p>The authorizer identifier.</p>
            authorizer_payload_format_version: <p>Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are 1.0 and 2.0. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\">Working with AWS Lambda authorizers for HTTP APIs</a>.</p>
            authorizer_result_ttl_in_seconds: <p>The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.</p>
            authorizer_type: <p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>
            authorizer_uri: <p>The authorizer's Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:<replaceable>{account_id}</replaceable>:function:<replaceable>{lambda_function_name}</replaceable>/invocations. In general, the URI has this form: arn:aws:apigateway:<replaceable>{region}</replaceable>:lambda:path/<replaceable>{service_api}</replaceable> , where <replaceable></replaceable>{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.</p>
            enable_simple_responses: <p>Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\">Working with AWS Lambda authorizers for HTTP APIs</a></p>
            identity_source: <p>The identity source for which authorization is requested.</p> <p>For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with $, for example, $request.header.Auth, $request.querystring.Name. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\">Working with AWS Lambda authorizers for HTTP APIs</a>.</p> <p>For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example $request.header.Authorization.</p>
            identity_validation_expression: <p>This parameter is not used.</p>
            jwt_configuration: <p>Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.</p>
            name: <p>The name of the authorizer.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_authorizer_request.UpdateAuthorizerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_authorizer_response.UpdateAuthorizerResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_authorizer

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_authorizer.async_update_authorizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_authorizer_request.UpdateAuthorizerRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if authorizer_credentials_arn is not None:
            input["authorizer_credentials_arn"] = authorizer_credentials_arn
        input["authorizer_id"] = authorizer_id
        if authorizer_payload_format_version is not None:
            input["authorizer_payload_format_version"] = (
                authorizer_payload_format_version
            )
        if authorizer_result_ttl_in_seconds is not None:
            input["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if authorizer_type is not None:
            input["authorizer_type"] = authorizer_type
        if authorizer_uri is not None:
            input["authorizer_uri"] = authorizer_uri
        if enable_simple_responses is not None:
            input["enable_simple_responses"] = enable_simple_responses
        if identity_source is not None:
            input["identity_source"] = identity_source
        if identity_validation_expression is not None:
            input["identity_validation_expression"] = identity_validation_expression
        if jwt_configuration is not None:
            input["jwt_configuration"] = jwt_configuration
        if name is not None:
            input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_deployment(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        deployment_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
    ) -> (
        "aws_sdk_apigatewayv2.types.update_deployment_response.UpdateDeploymentResponse"
    ):
        """<p>Updates a Deployment.</p>

        Args:
            api_id: <p>The API identifier.</p>
            deployment_id: <p>The deployment ID.</p>
            description: <p>The description for the deployment resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_deployment_request.UpdateDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_deployment_response.UpdateDeploymentResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_deployment.async_update_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_deployment_request.UpdateDeploymentRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        input["deployment_id"] = deployment_id
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_domain_name(
        self,
        domain_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        domain_name_configurations: Optional[
            "aws_sdk_apigatewayv2.types.domain_name_configurations.DomainNameConfigurations"
        ] = None,
        mutual_tls_authentication: Optional[
            "aws_sdk_apigatewayv2.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
        ] = None,
        routing_mode: Optional[
            "aws_sdk_apigatewayv2.types.routing_mode.RoutingMode"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_domain_name_response.UpdateDomainNameResponse":
        """<p>Updates a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_configurations: <p>The domain name configurations.</p>
            mutual_tls_authentication: <p>The mutual TLS authentication configuration for a custom domain name.</p>
            routing_mode: <p>The routing mode.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_domain_name_request.UpdateDomainNameRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_domain_name_response.UpdateDomainNameResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_domain_name

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_domain_name.async_update_domain_name(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_domain_name_request.UpdateDomainNameRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if domain_name_configurations is not None:
            input["domain_name_configurations"] = domain_name_configurations
        if mutual_tls_authentication is not None:
            input["mutual_tls_authentication"] = mutual_tls_authentication
        if routing_mode is not None:
            input["routing_mode"] = routing_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_integration(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        connection_id: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and1024.StringWithLengthBetween1And1024"
        ] = None,
        connection_type: Optional[
            "aws_sdk_apigatewayv2.types.connection_type.ConnectionType"
        ] = None,
        content_handling_strategy: Optional[
            "aws_sdk_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        credentials_arn: Optional["aws_sdk_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        integration_method: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        integration_subtype: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        integration_type: Optional[
            "aws_sdk_apigatewayv2.types.integration_type.IntegrationType"
        ] = None,
        integration_uri: Optional[
            "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        passthrough_behavior: Optional[
            "aws_sdk_apigatewayv2.types.passthrough_behavior.PassthroughBehavior"
        ] = None,
        payload_format_version: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_parameters: Optional[
            "aws_sdk_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        request_templates: Optional[
            "aws_sdk_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        response_parameters: Optional[
            "aws_sdk_apigatewayv2.types.response_parameters.ResponseParameters"
        ] = None,
        template_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        timeout_in_millis: Optional[
            "aws_sdk_apigatewayv2.types.integer_with_length_between50_and30000.IntegerWithLengthBetween50And30000"
        ] = None,
        tls_config: Optional[
            "aws_sdk_apigatewayv2.types.tls_config_input.TlsConfigInput"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_integration_result.UpdateIntegrationResult":
        """<p>Updates an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            connection_id: <p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>
            connection_type: <p>The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.</p>
            content_handling_strategy: <p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            credentials_arn: <p>Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.</p>
            description: <p>The description of the integration</p>
            integration_id: <p>The integration ID.</p>
            integration_method: <p>Specifies the integration's HTTP method type.</p>
            integration_subtype: <p>Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html\">Integration subtype reference</a>.</p>
            integration_type: <p>The integration type of an integration. One of the following:</p> <p>AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.</p> <p>AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.</p> <p>HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.</p> <p>HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.</p> <p>MOCK: for integrating the route or method request with API Gateway as a \"loopback\" endpoint without invoking any backend. Supported only for WebSocket APIs.</p>
            integration_uri: <p>For a Lambda integration, specify the URI of a Lambda function.</p> <p>For an HTTP integration, specify a fully-qualified URL.</p> <p>For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html\">DiscoverInstances</a>. For private integrations, all resources must be owned by the same AWS account.</p>
            passthrough_behavior: <p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.</p> <p>WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.</p> <p>NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.</p> <p>WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.</p>
            payload_format_version: <p>Specifies the format of the payload sent to an integration. Required for HTTP APIs. Supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html\">Working with AWS Lambda proxy integrations for HTTP APIs</a>.</p>
            request_parameters: <p>For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.<replaceable>{location}</replaceable>.<replaceable>{name}</replaceable> , where <replaceable>{location}</replaceable> is querystring, path, or header; and <replaceable>{name}</replaceable> must be a valid and unique method request parameter name.</p> <p>For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html\">Working with AWS service integrations for HTTP APIs</a>.</p> <p>For HTTP API integrations, without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern &lt;action&gt;:&lt;header|querystring|path&gt;.&lt;location&gt; where action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html\">Transforming API requests and responses</a>.</p>
            request_templates: <p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.</p>
            response_parameters: <p>Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match pattern &lt;action&gt;:&lt;header&gt;.&lt;location&gt; or overwrite.statuscode. The action can be append, overwrite or remove. The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href=\"https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html\">Transforming API requests and responses</a>.</p>
            template_selection_expression: <p>The template selection expression for the integration.</p>
            timeout_in_millis: <p>Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.</p>
            tls_config: <p>The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_integration_request.UpdateIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_integration_result.UpdateIntegrationResult"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_integration

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_integration_request.UpdateIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if connection_id is not None:
            input["connection_id"] = connection_id
        if connection_type is not None:
            input["connection_type"] = connection_type
        if content_handling_strategy is not None:
            input["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None:
            input["credentials_arn"] = credentials_arn
        if description is not None:
            input["description"] = description
        input["integration_id"] = integration_id
        if integration_method is not None:
            input["integration_method"] = integration_method
        if integration_subtype is not None:
            input["integration_subtype"] = integration_subtype
        if integration_type is not None:
            input["integration_type"] = integration_type
        if integration_uri is not None:
            input["integration_uri"] = integration_uri
        if passthrough_behavior is not None:
            input["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None:
            input["payload_format_version"] = payload_format_version
        if request_parameters is not None:
            input["request_parameters"] = request_parameters
        if request_templates is not None:
            input["request_templates"] = request_templates
        if response_parameters is not None:
            input["response_parameters"] = response_parameters
        if template_selection_expression is not None:
            input["template_selection_expression"] = template_selection_expression
        if timeout_in_millis is not None:
            input["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            input["tls_config"] = tls_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_integration_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_id: "aws_sdk_apigatewayv2.types.__string.__string",
        integration_response_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        content_handling_strategy: Optional[
            "aws_sdk_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        integration_response_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        response_parameters: Optional[
            "aws_sdk_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        response_templates: Optional[
            "aws_sdk_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        template_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_integration_response_response.UpdateIntegrationResponseResponse":
        """<p>Updates an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_handling_strategy: <p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_id: <p>The integration response ID.</p>
            integration_response_key: <p>The integration response key.</p>
            response_parameters: <p>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.<replaceable>{name}</replaceable> , where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.<replaceable>{name}</replaceable> or integration.response.body.<replaceable>{JSON-expression}</replaceable> , where <replaceable>{name}</replaceable> is a valid and unique response header name and <replaceable>{JSON-expression}</replaceable> is a valid JSON expression without the $ prefix.</p>
            response_templates: <p>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>
            template_selection_expression: <p>The template selection expression for the integration response. Supported only for WebSocket APIs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_integration_response_request.UpdateIntegrationResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_integration_response_response.UpdateIntegrationResponseResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_integration_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_integration_response.async_update_integration_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_integration_response_request.UpdateIntegrationResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if content_handling_strategy is not None:
            input["content_handling_strategy"] = content_handling_strategy
        input["integration_id"] = integration_id
        input["integration_response_id"] = integration_response_id
        if integration_response_key is not None:
            input["integration_response_key"] = integration_response_key
        if response_parameters is not None:
            input["response_parameters"] = response_parameters
        if response_templates is not None:
            input["response_templates"] = response_templates
        if template_selection_expression is not None:
            input["template_selection_expression"] = template_selection_expression

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_model(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        model_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        content_type: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and256.StringWithLengthBetween1And256"
        ] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        schema: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and32_k.StringWithLengthBetween0And32K"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_model_response.UpdateModelResponse":
        """<p>Updates a Model.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_type: <p>The content-type for the model, for example, \"application/json\".</p>
            description: <p>The description of the model.</p>
            model_id: <p>The model ID.</p>
            name: <p>The name of the model.</p>
            schema: <p>The schema for the model. For application/json models, this should be JSON schema draft 4 model.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_model_request.UpdateModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_model_response.UpdateModelResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_model

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_model.async_update_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_model_request.UpdateModelRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if content_type is not None:
            input["content_type"] = content_type
        if description is not None:
            input["description"] = description
        input["model_id"] = model_id
        if name is not None:
            input["name"] = name
        if schema is not None:
            input["schema"] = schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_portal(
        self,
        portal_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        authorization: Optional[
            "aws_sdk_apigatewayv2.types.authorization.Authorization"
        ] = None,
        endpoint_configuration: Optional[
            "aws_sdk_apigatewayv2.types.endpoint_configuration_request.EndpointConfigurationRequest"
        ] = None,
        included_portal_product_arns: Optional[
            "aws_sdk_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
        ] = None,
        logo_uri: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max1092.__stringMin0Max1092"
        ] = None,
        portal_content: Optional[
            "aws_sdk_apigatewayv2.types.portal_content.PortalContent"
        ] = None,
        rum_app_monitor_name: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_portal_response.UpdatePortalResponse":
        """<p>Updates a portal.</p>

        Args:
            authorization: <p>The authorization of the portal.</p>
            endpoint_configuration: <p>Represents an endpoint configuration.</p>
            included_portal_product_arns: <p>The ARNs of the portal products included in the portal.</p>
            logo_uri: <p>The logo URI.</p>
            portal_content: <p>Contains the content that is visible to portal consumers including the themes, display names, and description.</p>
            portal_id: <p>The portal identifier.</p>
            rum_app_monitor_name: <p>The CloudWatch RUM app monitor name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_portal_request.UpdatePortalRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_portal_response.UpdatePortalResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_portal

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_portal.async_update_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_portal_request.UpdatePortalRequest = {}  # type: ignore[typeddict-item]
        if authorization is not None:
            input["authorization"] = authorization
        if endpoint_configuration is not None:
            input["endpoint_configuration"] = endpoint_configuration
        if included_portal_product_arns is not None:
            input["included_portal_product_arns"] = included_portal_product_arns
        if logo_uri is not None:
            input["logo_uri"] = logo_uri
        if portal_content is not None:
            input["portal_content"] = portal_content
        input["portal_id"] = portal_id
        if rum_app_monitor_name is not None:
            input["rum_app_monitor_name"] = rum_app_monitor_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_portal_product(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        display_name: Optional[
            "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
        ] = None,
        display_order: Optional[
            "aws_sdk_apigatewayv2.types.display_order.DisplayOrder"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_portal_product_response.UpdatePortalProductResponse":
        """<p>Updates the portal product.</p>

        Args:
            description: <p>The description.</p>
            display_name: <p>The displayName.</p>
            display_order: <p>The display order.</p>
            portal_product_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_portal_product_request.UpdatePortalProductRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_portal_product_response.UpdatePortalProductResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_portal_product

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_portal_product.async_update_portal_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_portal_product_request.UpdatePortalProductRequest = {}  # type: ignore[typeddict-item]
        if description is not None:
            input["description"] = description
        if display_name is not None:
            input["display_name"] = display_name
        if display_order is not None:
            input["display_order"] = display_order
        input["portal_product_id"] = portal_product_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_product_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        product_page_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "aws_sdk_apigatewayv2.types.display_content.DisplayContent"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_product_page_response.UpdateProductPageResponse":
        """<p>Updates a product page of a portal product.</p>

        Args:
            display_content: <p>The content of the product page.</p>
            portal_product_id: <p>The portal product identifier.</p>
            product_page_id: <p>The portal product identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_product_page_request.UpdateProductPageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_product_page_response.UpdateProductPageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_product_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_product_page.async_update_product_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_product_page_request.UpdateProductPageRequest = {}  # type: ignore[typeddict-item]
        if display_content is not None:
            input["display_content"] = display_content
        input["portal_product_id"] = portal_product_id
        input["product_page_id"] = product_page_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_product_rest_endpoint_page(
        self,
        portal_product_id: "aws_sdk_apigatewayv2.types.__string.__string",
        product_rest_endpoint_page_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "aws_sdk_apigatewayv2.types.endpoint_display_content.EndpointDisplayContent"
        ] = None,
        try_it_state: Optional[
            "aws_sdk_apigatewayv2.types.try_it_state.TryItState"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_product_rest_endpoint_page_response.UpdateProductRestEndpointPageResponse":
        """<p>Updates a product REST endpoint page.</p>

        Args:
            display_content: <p>The display content.</p>
            portal_product_id: <p>The portal product identifier.</p>
            product_rest_endpoint_page_id: <p>The product REST endpoint identifier.</p>
            try_it_state: <p>The try it state of a product REST endpoint page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_product_rest_endpoint_page_request.UpdateProductRestEndpointPageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_product_rest_endpoint_page_response.UpdateProductRestEndpointPageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_product_rest_endpoint_page

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_product_rest_endpoint_page.async_update_product_rest_endpoint_page(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_product_rest_endpoint_page_request.UpdateProductRestEndpointPageRequest = {}  # type: ignore[typeddict-item]
        if display_content is not None:
            input["display_content"] = display_content
        input["portal_product_id"] = portal_product_id
        input["product_rest_endpoint_page_id"] = product_rest_endpoint_page_id
        if try_it_state is not None:
            input["try_it_state"] = try_it_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_route(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        api_key_required: Optional[
            "aws_sdk_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        authorization_scopes: Optional[
            "aws_sdk_apigatewayv2.types.authorization_scopes.AuthorizationScopes"
        ] = None,
        authorization_type: Optional[
            "aws_sdk_apigatewayv2.types.authorization_type.AuthorizationType"
        ] = None,
        authorizer_id: Optional["aws_sdk_apigatewayv2.types.id.Id"] = None,
        model_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        operation_name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_models: Optional[
            "aws_sdk_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        request_parameters: Optional[
            "aws_sdk_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_response_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        target: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_route_result.UpdateRouteResult":
        """<p>Updates a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_key_required: <p>Specifies whether an API key is required for the route. Supported only for WebSocket APIs.</p>
            authorization_scopes: <p>The authorization scopes supported by this route.</p>
            authorization_type: <p>The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer.</p>
            authorizer_id: <p>The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.</p>
            model_selection_expression: <p>The model selection expression for the route. Supported only for WebSocket APIs.</p>
            operation_name: <p>The operation name for the route.</p>
            request_models: <p>The request models for the route. Supported only for WebSocket APIs.</p>
            request_parameters: <p>The request parameters for the route. Supported only for WebSocket APIs.</p>
            route_id: <p>The route ID.</p>
            route_key: <p>The route key for the route.</p>
            route_response_selection_expression: <p>The route response selection expression for the route. Supported only for WebSocket APIs.</p>
            target: <p>The target for the route.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_route_request.UpdateRouteRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_route_result.UpdateRouteResult"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_route

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_route.async_update_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_route_request.UpdateRouteRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if api_key_required is not None:
            input["api_key_required"] = api_key_required
        if authorization_scopes is not None:
            input["authorization_scopes"] = authorization_scopes
        if authorization_type is not None:
            input["authorization_type"] = authorization_type
        if authorizer_id is not None:
            input["authorizer_id"] = authorizer_id
        if model_selection_expression is not None:
            input["model_selection_expression"] = model_selection_expression
        if operation_name is not None:
            input["operation_name"] = operation_name
        if request_models is not None:
            input["request_models"] = request_models
        if request_parameters is not None:
            input["request_parameters"] = request_parameters
        input["route_id"] = route_id
        if route_key is not None:
            input["route_key"] = route_key
        if route_response_selection_expression is not None:
            input["route_response_selection_expression"] = (
                route_response_selection_expression
            )
        if target is not None:
            input["target"] = target

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_route_response(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_id: "aws_sdk_apigatewayv2.types.__string.__string",
        route_response_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        model_selection_expression: Optional[
            "aws_sdk_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        response_models: Optional[
            "aws_sdk_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        response_parameters: Optional[
            "aws_sdk_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_response_key: Optional[
            "aws_sdk_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_route_response_response.UpdateRouteResponseResponse":
        """<p>Updates a RouteResponse.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_selection_expression: <p>The model selection expression for the route response. Supported only for WebSocket APIs.</p>
            response_models: <p>The response models for the route response.</p>
            response_parameters: <p>The route response parameters.</p>
            route_id: <p>The route ID.</p>
            route_response_id: <p>The route response ID.</p>
            route_response_key: <p>The route response key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_route_response_request.UpdateRouteResponseRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_route_response_response.UpdateRouteResponseResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_route_response

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_route_response.async_update_route_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_route_response_request.UpdateRouteResponseRequest = {}  # type: ignore[typeddict-item]
        input["api_id"] = api_id
        if model_selection_expression is not None:
            input["model_selection_expression"] = model_selection_expression
        if response_models is not None:
            input["response_models"] = response_models
        if response_parameters is not None:
            input["response_parameters"] = response_parameters
        input["route_id"] = route_id
        input["route_response_id"] = route_response_id
        if route_response_key is not None:
            input["route_response_key"] = route_response_key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_stage(
        self,
        api_id: "aws_sdk_apigatewayv2.types.__string.__string",
        stage_name: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        access_log_settings: Optional[
            "aws_sdk_apigatewayv2.types.access_log_settings.AccessLogSettings"
        ] = None,
        auto_deploy: Optional["aws_sdk_apigatewayv2.types.__boolean.__boolean"] = None,
        client_certificate_id: Optional["aws_sdk_apigatewayv2.types.id.Id"] = None,
        default_route_settings: Optional[
            "aws_sdk_apigatewayv2.types.route_settings.RouteSettings"
        ] = None,
        deployment_id: Optional["aws_sdk_apigatewayv2.types.id.Id"] = None,
        description: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        route_settings: Optional[
            "aws_sdk_apigatewayv2.types.route_settings_map.RouteSettingsMap"
        ] = None,
        stage_variables: Optional[
            "aws_sdk_apigatewayv2.types.stage_variables_map.StageVariablesMap"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_stage_response.UpdateStageResponse":
        """<p>Updates a Stage.</p>

        Args:
            access_log_settings: <p>Settings for logging access in this stage.</p>
            api_id: <p>The API identifier.</p>
            auto_deploy: <p>Specifies whether updates to an API automatically trigger a new deployment. The default value is false.</p>
            client_certificate_id: <p>The identifier of a client certificate for a Stage.</p>
            default_route_settings: <p>The default route settings for the stage.</p>
            deployment_id: <p>The deployment identifier for the API stage. Can't be updated if autoDeploy is enabled.</p>
            description: <p>The description for the API stage.</p>
            route_settings: <p>Route settings for the stage.</p>
            stage_name: <p>The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.</p>
            stage_variables: <p>A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&amp;=,]+.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_stage_request.UpdateStageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_stage_response.UpdateStageResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_stage

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_stage.async_update_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_stage_request.UpdateStageRequest = {}  # type: ignore[typeddict-item]
        if access_log_settings is not None:
            input["access_log_settings"] = access_log_settings
        input["api_id"] = api_id
        if auto_deploy is not None:
            input["auto_deploy"] = auto_deploy
        if client_certificate_id is not None:
            input["client_certificate_id"] = client_certificate_id
        if default_route_settings is not None:
            input["default_route_settings"] = default_route_settings
        if deployment_id is not None:
            input["deployment_id"] = deployment_id
        if description is not None:
            input["description"] = description
        if route_settings is not None:
            input["route_settings"] = route_settings
        input["stage_name"] = stage_name
        if stage_variables is not None:
            input["stage_variables"] = stage_variables

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_vpc_link(
        self,
        vpc_link_id: "aws_sdk_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[AsyncApiGatewayV2ClientConfig] = None,
        name: Optional[
            "aws_sdk_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "aws_sdk_apigatewayv2.types.update_vpc_link_response.UpdateVpcLinkResponse":
        """<p>Updates a VPC link.</p>

        Args:
            name: <p>The name of the VPC link.</p>
            vpc_link_id: <p>The ID of the VPC link.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_apigatewayv2.types.update_vpc_link_request.UpdateVpcLinkRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_apigatewayv2.types.update_vpc_link_response.UpdateVpcLinkResponse"
        ]:
            import aws_sdk_apigatewayv2._operations.api_gateway_v2.update_vpc_link

            (
                output,
                http_response,
            ) = await aws_sdk_apigatewayv2._operations.api_gateway_v2.update_vpc_link.async_update_vpc_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_apigatewayv2.types.update_vpc_link_request.UpdateVpcLinkRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input["name"] = name
        input["vpc_link_id"] = vpc_link_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
