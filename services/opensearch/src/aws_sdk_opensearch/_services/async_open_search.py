"""Generated from Smithy shape ``com.amazonaws.opensearch#AmazonOpenSearchService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_opensearch._auth._signers
import aws_sdk_opensearch._auth._sigv4
from aws_sdk_opensearch._auth._identity import Credentials
from aws_sdk_opensearch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_opensearch._auth._zapros_handler import AuthMiddleware
from aws_sdk_opensearch._pagination import resolve_path as _resolve_path
from aws_sdk_opensearch._services._aws_config import aaws_config
from aws_sdk_opensearch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.accept_inbound_connection_request
    import aws_sdk_opensearch.types.accept_inbound_connection_response
    import aws_sdk_opensearch.types.action_type
    import aws_sdk_opensearch.types.add_data_source_request
    import aws_sdk_opensearch.types.add_data_source_response
    import aws_sdk_opensearch.types.add_direct_query_data_source_request
    import aws_sdk_opensearch.types.add_direct_query_data_source_response
    import aws_sdk_opensearch.types.add_tags_request
    import aws_sdk_opensearch.types.advanced_options
    import aws_sdk_opensearch.types.advanced_security_options_input
    import aws_sdk_opensearch.types.aiml_options_input
    import aws_sdk_opensearch.types.app_configs
    import aws_sdk_opensearch.types.application_id
    import aws_sdk_opensearch.types.application_name
    import aws_sdk_opensearch.types.application_statuses
    import aws_sdk_opensearch.types.application_summary
    import aws_sdk_opensearch.types.arn
    import aws_sdk_opensearch.types.associate_package_request
    import aws_sdk_opensearch.types.associate_package_response
    import aws_sdk_opensearch.types.associate_packages_request
    import aws_sdk_opensearch.types.associate_packages_response
    import aws_sdk_opensearch.types.authorize_vpc_endpoint_access_request
    import aws_sdk_opensearch.types.authorize_vpc_endpoint_access_response
    import aws_sdk_opensearch.types.auto_tune_options
    import aws_sdk_opensearch.types.auto_tune_options_input
    import aws_sdk_opensearch.types.automated_snapshot_pause_request_options
    import aws_sdk_opensearch.types.aws_account
    import aws_sdk_opensearch.types.aws_service_principal
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.cancel_domain_config_change_request
    import aws_sdk_opensearch.types.cancel_domain_config_change_response
    import aws_sdk_opensearch.types.cancel_service_software_update_request
    import aws_sdk_opensearch.types.cancel_service_software_update_response
    import aws_sdk_opensearch.types.capability_base_request_config
    import aws_sdk_opensearch.types.capability_name
    import aws_sdk_opensearch.types.client_token
    import aws_sdk_opensearch.types.cluster_config
    import aws_sdk_opensearch.types.cognito_options
    import aws_sdk_opensearch.types.commit_message
    import aws_sdk_opensearch.types.connection_alias
    import aws_sdk_opensearch.types.connection_id
    import aws_sdk_opensearch.types.connection_mode
    import aws_sdk_opensearch.types.connection_properties
    import aws_sdk_opensearch.types.create_application_request
    import aws_sdk_opensearch.types.create_application_response
    import aws_sdk_opensearch.types.create_domain_request
    import aws_sdk_opensearch.types.create_domain_response
    import aws_sdk_opensearch.types.create_index_request
    import aws_sdk_opensearch.types.create_index_response
    import aws_sdk_opensearch.types.create_outbound_connection_request
    import aws_sdk_opensearch.types.create_outbound_connection_response
    import aws_sdk_opensearch.types.create_package_request
    import aws_sdk_opensearch.types.create_package_response
    import aws_sdk_opensearch.types.create_vpc_endpoint_request
    import aws_sdk_opensearch.types.create_vpc_endpoint_response
    import aws_sdk_opensearch.types.data_source_description
    import aws_sdk_opensearch.types.data_source_name
    import aws_sdk_opensearch.types.data_source_status
    import aws_sdk_opensearch.types.data_source_type
    import aws_sdk_opensearch.types.data_sources
    import aws_sdk_opensearch.types.delete_application_request
    import aws_sdk_opensearch.types.delete_application_response
    import aws_sdk_opensearch.types.delete_data_source_request
    import aws_sdk_opensearch.types.delete_data_source_response
    import aws_sdk_opensearch.types.delete_direct_query_data_source_request
    import aws_sdk_opensearch.types.delete_domain_request
    import aws_sdk_opensearch.types.delete_domain_response
    import aws_sdk_opensearch.types.delete_inbound_connection_request
    import aws_sdk_opensearch.types.delete_inbound_connection_response
    import aws_sdk_opensearch.types.delete_index_request
    import aws_sdk_opensearch.types.delete_index_response
    import aws_sdk_opensearch.types.delete_outbound_connection_request
    import aws_sdk_opensearch.types.delete_outbound_connection_response
    import aws_sdk_opensearch.types.delete_package_request
    import aws_sdk_opensearch.types.delete_package_response
    import aws_sdk_opensearch.types.delete_vpc_endpoint_request
    import aws_sdk_opensearch.types.delete_vpc_endpoint_response
    import aws_sdk_opensearch.types.deployment_strategy_options
    import aws_sdk_opensearch.types.deregister_capability_request
    import aws_sdk_opensearch.types.deregister_capability_response
    import aws_sdk_opensearch.types.describe_domain_auto_tunes_request
    import aws_sdk_opensearch.types.describe_domain_auto_tunes_response
    import aws_sdk_opensearch.types.describe_domain_change_progress_request
    import aws_sdk_opensearch.types.describe_domain_change_progress_response
    import aws_sdk_opensearch.types.describe_domain_config_request
    import aws_sdk_opensearch.types.describe_domain_config_response
    import aws_sdk_opensearch.types.describe_domain_health_request
    import aws_sdk_opensearch.types.describe_domain_health_response
    import aws_sdk_opensearch.types.describe_domain_nodes_request
    import aws_sdk_opensearch.types.describe_domain_nodes_response
    import aws_sdk_opensearch.types.describe_domain_request
    import aws_sdk_opensearch.types.describe_domain_response
    import aws_sdk_opensearch.types.describe_domains_request
    import aws_sdk_opensearch.types.describe_domains_response
    import aws_sdk_opensearch.types.describe_dry_run_progress_request
    import aws_sdk_opensearch.types.describe_dry_run_progress_response
    import aws_sdk_opensearch.types.describe_inbound_connections_request
    import aws_sdk_opensearch.types.describe_inbound_connections_response
    import aws_sdk_opensearch.types.describe_insight_details_request
    import aws_sdk_opensearch.types.describe_insight_details_response
    import aws_sdk_opensearch.types.describe_instance_type_limits_request
    import aws_sdk_opensearch.types.describe_instance_type_limits_response
    import aws_sdk_opensearch.types.describe_outbound_connections_request
    import aws_sdk_opensearch.types.describe_outbound_connections_response
    import aws_sdk_opensearch.types.describe_packages_filter_list
    import aws_sdk_opensearch.types.describe_packages_request
    import aws_sdk_opensearch.types.describe_packages_response
    import aws_sdk_opensearch.types.describe_reserved_instance_offerings_request
    import aws_sdk_opensearch.types.describe_reserved_instance_offerings_response
    import aws_sdk_opensearch.types.describe_reserved_instances_request
    import aws_sdk_opensearch.types.describe_reserved_instances_response
    import aws_sdk_opensearch.types.describe_vpc_endpoints_request
    import aws_sdk_opensearch.types.describe_vpc_endpoints_response
    import aws_sdk_opensearch.types.direct_query_data_source_description
    import aws_sdk_opensearch.types.direct_query_data_source_name
    import aws_sdk_opensearch.types.direct_query_data_source_type
    import aws_sdk_opensearch.types.direct_query_open_search_arn_list
    import aws_sdk_opensearch.types.dissociate_package_request
    import aws_sdk_opensearch.types.dissociate_package_response
    import aws_sdk_opensearch.types.dissociate_packages_request
    import aws_sdk_opensearch.types.dissociate_packages_response
    import aws_sdk_opensearch.types.domain_arn
    import aws_sdk_opensearch.types.domain_endpoint_options
    import aws_sdk_opensearch.types.domain_information_container
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.domain_name_list
    import aws_sdk_opensearch.types.dry_run
    import aws_sdk_opensearch.types.dry_run_mode
    import aws_sdk_opensearch.types.ebs_options
    import aws_sdk_opensearch.types.encryption_at_rest_options
    import aws_sdk_opensearch.types.engine_type
    import aws_sdk_opensearch.types.engine_version
    import aws_sdk_opensearch.types.filter_list
    import aws_sdk_opensearch.types.get_application_request
    import aws_sdk_opensearch.types.get_application_response
    import aws_sdk_opensearch.types.get_capability_request
    import aws_sdk_opensearch.types.get_capability_response
    import aws_sdk_opensearch.types.get_compatible_versions_request
    import aws_sdk_opensearch.types.get_compatible_versions_response
    import aws_sdk_opensearch.types.get_data_source_request
    import aws_sdk_opensearch.types.get_data_source_response
    import aws_sdk_opensearch.types.get_default_application_setting_request
    import aws_sdk_opensearch.types.get_default_application_setting_response
    import aws_sdk_opensearch.types.get_direct_query_data_source_request
    import aws_sdk_opensearch.types.get_direct_query_data_source_response
    import aws_sdk_opensearch.types.get_domain_maintenance_status_request
    import aws_sdk_opensearch.types.get_domain_maintenance_status_response
    import aws_sdk_opensearch.types.get_index_request
    import aws_sdk_opensearch.types.get_index_response
    import aws_sdk_opensearch.types.get_package_version_history_request
    import aws_sdk_opensearch.types.get_package_version_history_response
    import aws_sdk_opensearch.types.get_upgrade_history_request
    import aws_sdk_opensearch.types.get_upgrade_history_response
    import aws_sdk_opensearch.types.get_upgrade_status_request
    import aws_sdk_opensearch.types.get_upgrade_status_response
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.iam_identity_center_options_input
    import aws_sdk_opensearch.types.id
    import aws_sdk_opensearch.types.identity_center_options_input
    import aws_sdk_opensearch.types.index_name
    import aws_sdk_opensearch.types.index_schema
    import aws_sdk_opensearch.types.insight_entity
    import aws_sdk_opensearch.types.insight_page_size
    import aws_sdk_opensearch.types.insight_sort_order
    import aws_sdk_opensearch.types.insight_time_range
    import aws_sdk_opensearch.types.instance_count
    import aws_sdk_opensearch.types.instance_type_string
    import aws_sdk_opensearch.types.ip_address_type
    import aws_sdk_opensearch.types.kms_key_arn
    import aws_sdk_opensearch.types.list_applications_request
    import aws_sdk_opensearch.types.list_applications_response
    import aws_sdk_opensearch.types.list_data_sources_request
    import aws_sdk_opensearch.types.list_data_sources_response
    import aws_sdk_opensearch.types.list_direct_query_data_sources_request
    import aws_sdk_opensearch.types.list_direct_query_data_sources_response
    import aws_sdk_opensearch.types.list_domain_maintenances_request
    import aws_sdk_opensearch.types.list_domain_maintenances_response
    import aws_sdk_opensearch.types.list_domain_names_request
    import aws_sdk_opensearch.types.list_domain_names_response
    import aws_sdk_opensearch.types.list_domains_for_package_request
    import aws_sdk_opensearch.types.list_domains_for_package_response
    import aws_sdk_opensearch.types.list_insights_request
    import aws_sdk_opensearch.types.list_insights_response
    import aws_sdk_opensearch.types.list_instance_type_details_request
    import aws_sdk_opensearch.types.list_instance_type_details_response
    import aws_sdk_opensearch.types.list_packages_for_domain_request
    import aws_sdk_opensearch.types.list_packages_for_domain_response
    import aws_sdk_opensearch.types.list_scheduled_actions_request
    import aws_sdk_opensearch.types.list_scheduled_actions_response
    import aws_sdk_opensearch.types.list_tags_request
    import aws_sdk_opensearch.types.list_tags_response
    import aws_sdk_opensearch.types.list_versions_request
    import aws_sdk_opensearch.types.list_versions_response
    import aws_sdk_opensearch.types.list_vpc_endpoint_access_request
    import aws_sdk_opensearch.types.list_vpc_endpoint_access_response
    import aws_sdk_opensearch.types.list_vpc_endpoints_for_domain_request
    import aws_sdk_opensearch.types.list_vpc_endpoints_for_domain_response
    import aws_sdk_opensearch.types.list_vpc_endpoints_request
    import aws_sdk_opensearch.types.list_vpc_endpoints_response
    import aws_sdk_opensearch.types.log_publishing_options
    import aws_sdk_opensearch.types.long
    import aws_sdk_opensearch.types.maintenance_status
    import aws_sdk_opensearch.types.maintenance_type
    import aws_sdk_opensearch.types.max_results
    import aws_sdk_opensearch.types.next_token
    import aws_sdk_opensearch.types.node_id
    import aws_sdk_opensearch.types.node_to_node_encryption_options
    import aws_sdk_opensearch.types.off_peak_window_options
    import aws_sdk_opensearch.types.open_search_partition_instance_type
    import aws_sdk_opensearch.types.package_association_configuration
    import aws_sdk_opensearch.types.package_configuration
    import aws_sdk_opensearch.types.package_description
    import aws_sdk_opensearch.types.package_details_for_association_list
    import aws_sdk_opensearch.types.package_encryption_options
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_id_list
    import aws_sdk_opensearch.types.package_name
    import aws_sdk_opensearch.types.package_scope_operation_enum
    import aws_sdk_opensearch.types.package_source
    import aws_sdk_opensearch.types.package_type
    import aws_sdk_opensearch.types.package_user_list
    import aws_sdk_opensearch.types.package_vending_options
    import aws_sdk_opensearch.types.policy_document
    import aws_sdk_opensearch.types.purchase_reserved_instance_offering_request
    import aws_sdk_opensearch.types.purchase_reserved_instance_offering_response
    import aws_sdk_opensearch.types.put_default_application_setting_request
    import aws_sdk_opensearch.types.put_default_application_setting_response
    import aws_sdk_opensearch.types.register_capability_request
    import aws_sdk_opensearch.types.register_capability_response
    import aws_sdk_opensearch.types.reject_inbound_connection_request
    import aws_sdk_opensearch.types.reject_inbound_connection_response
    import aws_sdk_opensearch.types.remove_tags_request
    import aws_sdk_opensearch.types.request_id
    import aws_sdk_opensearch.types.reservation_token
    import aws_sdk_opensearch.types.revoke_vpc_endpoint_access_request
    import aws_sdk_opensearch.types.revoke_vpc_endpoint_access_response
    import aws_sdk_opensearch.types.rollback_service_software_update_request
    import aws_sdk_opensearch.types.rollback_service_software_update_response
    import aws_sdk_opensearch.types.schedule_at
    import aws_sdk_opensearch.types.service_options
    import aws_sdk_opensearch.types.snapshot_options
    import aws_sdk_opensearch.types.software_update_options
    import aws_sdk_opensearch.types.start_domain_maintenance_request
    import aws_sdk_opensearch.types.start_domain_maintenance_response
    import aws_sdk_opensearch.types.start_service_software_update_request
    import aws_sdk_opensearch.types.start_service_software_update_response
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.string_list
    import aws_sdk_opensearch.types.tag_list
    import aws_sdk_opensearch.types.update_application_request
    import aws_sdk_opensearch.types.update_application_response
    import aws_sdk_opensearch.types.update_data_source_request
    import aws_sdk_opensearch.types.update_data_source_response
    import aws_sdk_opensearch.types.update_direct_query_data_source_request
    import aws_sdk_opensearch.types.update_direct_query_data_source_response
    import aws_sdk_opensearch.types.update_domain_config_request
    import aws_sdk_opensearch.types.update_domain_config_response
    import aws_sdk_opensearch.types.update_index_request
    import aws_sdk_opensearch.types.update_index_response
    import aws_sdk_opensearch.types.update_package_request
    import aws_sdk_opensearch.types.update_package_response
    import aws_sdk_opensearch.types.update_package_scope_request
    import aws_sdk_opensearch.types.update_package_scope_response
    import aws_sdk_opensearch.types.update_scheduled_action_request
    import aws_sdk_opensearch.types.update_scheduled_action_response
    import aws_sdk_opensearch.types.update_vpc_endpoint_request
    import aws_sdk_opensearch.types.update_vpc_endpoint_response
    import aws_sdk_opensearch.types.upgrade_domain_request
    import aws_sdk_opensearch.types.upgrade_domain_response
    import aws_sdk_opensearch.types.version_string
    import aws_sdk_opensearch.types.vpc_endpoint_id
    import aws_sdk_opensearch.types.vpc_endpoint_id_list
    import aws_sdk_opensearch.types.vpc_options


class AsyncOpenSearchClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncOpenSearchClient:
    """A client for the ``OpenSearch`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncOpenSearchClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncOpenSearchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncOpenSearchClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def accept_inbound_connection(
        self,
        connection_id: "aws_sdk_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.accept_inbound_connection_response.AcceptInboundConnectionResponse":
        r"""<p>Allows the destination Amazon OpenSearch Service domain owner to accept an inbound cross-cluster search connection request. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            connection_id: <p>The ID of the inbound connection to accept.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.accept_inbound_connection_request.AcceptInboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.accept_inbound_connection_response.AcceptInboundConnectionResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.accept_inbound_connection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.accept_inbound_connection.async_accept_inbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.accept_inbound_connection_request.AcceptInboundConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_data_source(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        name: "aws_sdk_opensearch.types.data_source_name.DataSourceName",
        data_source_type: "aws_sdk_opensearch.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearch.types.data_source_description.DataSourceDescription"
        ] = None,
    ) -> "aws_sdk_opensearch.types.add_data_source_response.AddDataSourceResponse":
        r"""<p>Creates a new direct-query data source to the specified domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html\">Creating Amazon OpenSearch Service data source integrations with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain to add the data source to.</p>
            name: <p>A name for the data source.</p>
            data_source_type: <p>The type of data source.</p>
            description: <p>A description of the data source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.add_data_source_request.AddDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.add_data_source_response.AddDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.add_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.add_data_source.async_add_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.add_data_source_request.AddDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["name"] = name
        input_["data_source_type"] = data_source_type
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_direct_query_data_source(
        self,
        data_source_name: "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        data_source_type: "aws_sdk_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
        ] = None,
        open_search_arns: Optional[
            "aws_sdk_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
        ] = None,
        data_source_access_policy: Optional[
            "aws_sdk_opensearch.types.policy_document.PolicyDocument"
        ] = None,
        tag_list: Optional["aws_sdk_opensearch.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_opensearch.types.add_direct_query_data_source_response.AddDirectQueryDataSourceResponse":
        """<p> Adds a new data source in Amazon OpenSearch Service so that you can perform direct queries on external data. </p>

        Args:
            data_source_name: <p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>
            data_source_type: <p> The supported Amazon Web Services service that you want to use as the source for direct queries in OpenSearch Service. </p>
            description: <p> An optional text field for providing additional context and details about the data source. </p>
            open_search_arns: <p> An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types. </p>
            data_source_access_policy: <p> An optional IAM access policy document that defines the permissions for accessing the data source. The policy document must be in valid JSON format and follow IAM policy syntax.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.add_direct_query_data_source_request.AddDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.add_direct_query_data_source_response.AddDirectQueryDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.add_direct_query_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.add_direct_query_data_source.async_add_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.add_direct_query_data_source_request.AddDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_name"] = data_source_name
        input_["data_source_type"] = data_source_type
        if description is not None:
            input_["description"] = description
        if open_search_arns is not None:
            input_["open_search_arns"] = open_search_arns
        if data_source_access_policy is not None:
            input_["data_source_access_policy"] = data_source_access_policy
        if tag_list is not None:
            input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_tags(
        self,
        arn: "aws_sdk_opensearch.types.arn.ARN",
        tag_list: "aws_sdk_opensearch.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> None:
        r"""<p>Attaches tags to an existing Amazon OpenSearch Service domain, data source, or application. </p> <p>Tags are a set of case-sensitive key-value pairs. A domain, data source, or application can have up to 10 tags. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html\">Tagging Amazon OpenSearch Service resources</a>. </p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the OpenSearch Service domain, data source, or application to which you want to attach resource tags.</p>
            tag_list: <p>List of resource tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.add_tags_request.AddTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.add_tags

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.add_tags.async_add_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.add_tags_request.AddTagsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_package(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        prerequisite_package_id_list: Optional[
            "aws_sdk_opensearch.types.package_id_list.PackageIDList"
        ] = None,
        association_configuration: Optional[
            "aws_sdk_opensearch.types.package_association_configuration.PackageAssociationConfiguration"
        ] = None,
    ) -> "aws_sdk_opensearch.types.associate_package_response.AssociatePackageResponse":
        r"""<p>Associates a package with an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>Internal ID of the package to associate with a domain. Use <code>DescribePackages</code> to find this value. </p>
            domain_name: <p>Name of the domain to associate the package with.</p>
            prerequisite_package_id_list: <p>A list of package IDs that must be associated with the domain before the package specified in the request can be associated.</p>
            association_configuration: <p>The configuration for associating a package with an Amazon OpenSearch Service domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.associate_package_request.AssociatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.associate_package_response.AssociatePackageResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.associate_package

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.associate_package.async_associate_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.associate_package_request.AssociatePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        input_["domain_name"] = domain_name
        if prerequisite_package_id_list is not None:
            input_["prerequisite_package_id_list"] = prerequisite_package_id_list
        if association_configuration is not None:
            input_["association_configuration"] = association_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_packages(
        self,
        package_list: "aws_sdk_opensearch.types.package_details_for_association_list.PackageDetailsForAssociationList",
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "aws_sdk_opensearch.types.associate_packages_response.AssociatePackagesResponse"
    ):
        """<p>Operation in the Amazon OpenSearch Service API for associating multiple packages with a domain simultaneously.</p>

        Args:
            package_list: <p>A list of packages and their prerequisites to be associated with a domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.associate_packages_request.AssociatePackagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.associate_packages_response.AssociatePackagesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.associate_packages

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.associate_packages.async_associate_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.associate_packages_request.AssociatePackagesRequest = {}  # type: ignore[typeddict-item]
        input_["package_list"] = package_list
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def authorize_vpc_endpoint_access(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        account: Optional["aws_sdk_opensearch.types.aws_account.AWSAccount"] = None,
        service: Optional[
            "aws_sdk_opensearch.types.aws_service_principal.AWSServicePrincipal"
        ] = None,
        service_options: Optional[
            "aws_sdk_opensearch.types.service_options.ServiceOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse":
        """<p>Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to provide access to.</p>
            account: <p>The Amazon Web Services account ID to grant access to.</p>
            service: <p>The Amazon Web Services service SP to grant access to.</p>
            service_options: <p>The options for the service, including the supported Regions for the endpoint access.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.authorize_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.authorize_vpc_endpoint_access.async_authorize_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if account is not None:
            input_["account"] = account
        if service is not None:
            input_["service"] = service
        if service_options is not None:
            input_["service_options"] = service_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_domain_config_change(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        dry_run: Optional["aws_sdk_opensearch.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_opensearch.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse":
        """<p>Cancels a pending configuration change on an Amazon OpenSearch Service domain.</p>

        Args:
            dry_run: <p>When set to <code>True</code>, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.cancel_domain_config_change

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.cancel_domain_config_change.async_cancel_domain_config_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_service_software_update(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.cancel_service_software_update_response.CancelServiceSoftwareUpdateResponse":
        r"""<p>Cancels a scheduled service software update for an Amazon OpenSearch Service domain. You can only perform this operation before the <code>AutomatedUpdateDate</code> and when the domain's <code>UpdateStatus</code> is <code>PENDING_UPDATE</code>. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\">Service software updates in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain that you want to cancel the service software update on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.cancel_service_software_update_request.CancelServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.cancel_service_software_update_response.CancelServiceSoftwareUpdateResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.cancel_service_software_update

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.cancel_service_software_update.async_cancel_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.cancel_service_software_update_request.CancelServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_application(
        self,
        name: "aws_sdk_opensearch.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearch.types.client_token.ClientToken"
        ] = None,
        data_sources: Optional[
            "aws_sdk_opensearch.types.data_sources.DataSources"
        ] = None,
        iam_identity_center_options: Optional[
            "aws_sdk_opensearch.types.iam_identity_center_options_input.IamIdentityCenterOptionsInput"
        ] = None,
        app_configs: Optional["aws_sdk_opensearch.types.app_configs.AppConfigs"] = None,
        tag_list: Optional["aws_sdk_opensearch.types.tag_list.TagList"] = None,
        kms_key_arn: Optional["aws_sdk_opensearch.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> (
        "aws_sdk_opensearch.types.create_application_response.CreateApplicationResponse"
    ):
        r"""<p>Creates an OpenSearch UI application. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html\">Using the OpenSearch user interface in Amazon OpenSearch Service</a>.</p>

        Args:
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
            name: <p>The unique name of the OpenSearch application. Names must be unique within an Amazon Web Services Region for each account.</p>
            data_sources: <p>The data sources to link to the OpenSearch application.</p>
            iam_identity_center_options: <p>Configuration settings for integrating Amazon Web Services IAM Identity Center with the OpenSearch application.</p>
            app_configs: <p>Configuration settings for the OpenSearch application, including administrative options.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the application's data at rest. If provided, the application uses your customer-managed key for encryption. If omitted, the application uses an AWS-managed key. The KMS key must be in the same region as the application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.create_application_response.CreateApplicationResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.create_application

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["name"] = name
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if iam_identity_center_options is not None:
            input_["iam_identity_center_options"] = iam_identity_center_options
        if app_configs is not None:
            input_["app_configs"] = app_configs
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_domain(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        engine_version: Optional[
            "aws_sdk_opensearch.types.version_string.VersionString"
        ] = None,
        cluster_config: Optional[
            "aws_sdk_opensearch.types.cluster_config.ClusterConfig"
        ] = None,
        ebs_options: Optional["aws_sdk_opensearch.types.ebs_options.EBSOptions"] = None,
        access_policies: Optional[
            "aws_sdk_opensearch.types.policy_document.PolicyDocument"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_opensearch.types.ip_address_type.IPAddressType"
        ] = None,
        snapshot_options: Optional[
            "aws_sdk_opensearch.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional["aws_sdk_opensearch.types.vpc_options.VPCOptions"] = None,
        cognito_options: Optional[
            "aws_sdk_opensearch.types.cognito_options.CognitoOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "aws_sdk_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        node_to_node_encryption_options: Optional[
            "aws_sdk_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        advanced_options: Optional[
            "aws_sdk_opensearch.types.advanced_options.AdvancedOptions"
        ] = None,
        log_publishing_options: Optional[
            "aws_sdk_opensearch.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "aws_sdk_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        advanced_security_options: Optional[
            "aws_sdk_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        identity_center_options: Optional[
            "aws_sdk_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
        ] = None,
        tag_list: Optional["aws_sdk_opensearch.types.tag_list.TagList"] = None,
        auto_tune_options: Optional[
            "aws_sdk_opensearch.types.auto_tune_options_input.AutoTuneOptionsInput"
        ] = None,
        off_peak_window_options: Optional[
            "aws_sdk_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
        ] = None,
        software_update_options: Optional[
            "aws_sdk_opensearch.types.software_update_options.SoftwareUpdateOptions"
        ] = None,
        aiml_options: Optional[
            "aws_sdk_opensearch.types.aiml_options_input.AIMLOptionsInput"
        ] = None,
        deployment_strategy_options: Optional[
            "aws_sdk_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "aws_sdk_opensearch.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.create_domain_response.CreateDomainResponse":
        r"""<p>Creates an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html\">Creating and managing Amazon OpenSearch Service domains</a>.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain to create. Domain names are unique across the domains owned by an account within an Amazon Web Services Region.</p>
            engine_version: <p>String of format Elasticsearch_X.Y or OpenSearch_X.Y to specify the engine version for the OpenSearch Service domain. For example, <code>OpenSearch_1.0</code> or <code>Elasticsearch_7.9</code>. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains\">Creating and managing Amazon OpenSearch Service domains</a>.</p>
            cluster_config: <p>Container for the cluster configuration of a domain.</p>
            ebs_options: <p>Container for the parameters required to enable EBS-based storage for an OpenSearch Service domain.</p>
            access_policies: <p>Identity and Access Management (IAM) policy document specifying the access policies for the new domain.</p>
            ip_address_type: <p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.</p>
            snapshot_options: <p>DEPRECATED. Container for the parameters required to configure automated snapshots of domain indexes.</p>
            vpc_options: <p>Container for the values required to configure VPC access domains. If you don't specify these values, OpenSearch Service creates the domain with a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html\">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>
            cognito_options: <p>Key-value pairs to configure Amazon Cognito authentication. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html\">Configuring Amazon Cognito authentication for OpenSearch Dashboards</a>.</p>
            encryption_at_rest_options: <p>Key-value pairs to enable encryption at rest.</p>
            node_to_node_encryption_options: <p>Enables node-to-node encryption.</p>
            advanced_options: <p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>\"rest.action.multi.allow_explicit_index\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>\"indices.fielddata.cache.size\": \"80\" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>\"indices.query.bool.max_clause_count\": \"1024\"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> <li> <p> <code>\"override_main_response_version\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\">Advanced cluster parameters</a>.</p>
            log_publishing_options: <p>Key-value pairs to configure log publishing.</p>
            domain_endpoint_options: <p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>
            advanced_security_options: <p>Options for fine-grained access control.</p>
            identity_center_options: <p>Configuration options for enabling and managing IAM Identity Center integration within a domain.</p>
            tag_list: <p>List of tags to add to the domain upon creation.</p>
            auto_tune_options: <p>Options for Auto-Tune.</p>
            off_peak_window_options: <p>Specifies a daily 10-hour time block during which OpenSearch Service can perform configuration changes on the domain, including service software updates and Auto-Tune enhancements that require a blue/green deployment. If no options are specified, the default start time of 10:00 P.M. local time (for the Region that the domain is created in) is used.</p>
            software_update_options: <p>Software update options for the domain.</p>
            aiml_options: <p>Options for all machine learning features for the specified domain.</p>
            deployment_strategy_options: <p>Specifies the deployment strategy options for the domain.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.create_domain_response.CreateDomainResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.create_domain

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.create_domain_request.CreateDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if cluster_config is not None:
            input_["cluster_config"] = cluster_config
        if ebs_options is not None:
            input_["ebs_options"] = ebs_options
        if access_policies is not None:
            input_["access_policies"] = access_policies
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if snapshot_options is not None:
            input_["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if cognito_options is not None:
            input_["cognito_options"] = cognito_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if node_to_node_encryption_options is not None:
            input_["node_to_node_encryption_options"] = node_to_node_encryption_options
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if domain_endpoint_options is not None:
            input_["domain_endpoint_options"] = domain_endpoint_options
        if advanced_security_options is not None:
            input_["advanced_security_options"] = advanced_security_options
        if identity_center_options is not None:
            input_["identity_center_options"] = identity_center_options
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if auto_tune_options is not None:
            input_["auto_tune_options"] = auto_tune_options
        if off_peak_window_options is not None:
            input_["off_peak_window_options"] = off_peak_window_options
        if software_update_options is not None:
            input_["software_update_options"] = software_update_options
        if aiml_options is not None:
            input_["aiml_options"] = aiml_options
        if deployment_strategy_options is not None:
            input_["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input_["automated_snapshot_pause_options"] = (
                automated_snapshot_pause_options
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_index(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        index_name: "aws_sdk_opensearch.types.index_name.IndexName",
        index_schema: "aws_sdk_opensearch.types.index_schema.IndexSchema",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.create_index_response.CreateIndexResponse":
        r"""<p>Creates an OpenSearch index with optional automatic semantic enrichment for specified text fields. Automatic semantic enrichment enables semantic search capabilities without requiring machine learning expertise, improving search relevance by up to 20% by understanding search intent and contextual meaning beyond keyword matching. The semantic enrichment process has zero impact on search latency as sparse encodings are stored directly within the index during indexing. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-semantic-enrichment.html\">Automatic semantic enrichment</a>.</p>

        Args:
            index_name: <p>The name of the index to create. Must be between 1 and 255 characters and follow OpenSearch naming conventions.</p>
            index_schema: <p>The JSON schema defining index mappings, settings, and semantic enrichment configuration. The schema specifies which text fields should be automatically enriched for semantic search capabilities and includes OpenSearch index configuration parameters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.create_index_request.CreateIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.create_index_response.CreateIndexResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.create_index

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.create_index.async_create_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.create_index_request.CreateIndexRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["index_name"] = index_name
        input_["index_schema"] = index_schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_outbound_connection(
        self,
        local_domain_info: "aws_sdk_opensearch.types.domain_information_container.DomainInformationContainer",
        remote_domain_info: "aws_sdk_opensearch.types.domain_information_container.DomainInformationContainer",
        connection_alias: "aws_sdk_opensearch.types.connection_alias.ConnectionAlias",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        connection_mode: Optional[
            "aws_sdk_opensearch.types.connection_mode.ConnectionMode"
        ] = None,
        connection_properties: Optional[
            "aws_sdk_opensearch.types.connection_properties.ConnectionProperties"
        ] = None,
    ) -> "aws_sdk_opensearch.types.create_outbound_connection_response.CreateOutboundConnectionResponse":
        r"""<p>Creates a new cross-cluster search connection from a source Amazon OpenSearch Service domain to a destination domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            local_domain_info: <p>Name and Region of the source (local) domain.</p>
            remote_domain_info: <p>Name and Region of the destination (remote) domain.</p>
            connection_alias: <p>Name of the connection.</p>
            connection_mode: <p>The connection mode.</p>
            connection_properties: <p>The <code>ConnectionProperties</code> for the outbound connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.create_outbound_connection_request.CreateOutboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.create_outbound_connection_response.CreateOutboundConnectionResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.create_outbound_connection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.create_outbound_connection.async_create_outbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.create_outbound_connection_request.CreateOutboundConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["local_domain_info"] = local_domain_info
        input_["remote_domain_info"] = remote_domain_info
        input_["connection_alias"] = connection_alias
        if connection_mode is not None:
            input_["connection_mode"] = connection_mode
        if connection_properties is not None:
            input_["connection_properties"] = connection_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_package(
        self,
        package_name: "aws_sdk_opensearch.types.package_name.PackageName",
        package_type: "aws_sdk_opensearch.types.package_type.PackageType",
        package_source: "aws_sdk_opensearch.types.package_source.PackageSource",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        package_description: Optional[
            "aws_sdk_opensearch.types.package_description.PackageDescription"
        ] = None,
        package_configuration: Optional[
            "aws_sdk_opensearch.types.package_configuration.PackageConfiguration"
        ] = None,
        engine_version: Optional[
            "aws_sdk_opensearch.types.engine_version.EngineVersion"
        ] = None,
        package_vending_options: Optional[
            "aws_sdk_opensearch.types.package_vending_options.PackageVendingOptions"
        ] = None,
        package_encryption_options: Optional[
            "aws_sdk_opensearch.types.package_encryption_options.PackageEncryptionOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.create_package_response.CreatePackageResponse":
        r"""<p>Creates a package for use with Amazon OpenSearch Service domains. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_name: <p>Unique name for the package.</p>
            package_type: <p>The type of package.</p>
            package_description: <p>Description of the package.</p>
            package_source: <p>The Amazon S3 location from which to import the package.</p>
            package_configuration: <p> The configuration parameters for the package being created.</p>
            engine_version: <p>The version of the Amazon OpenSearch Service engine for which is compatible with the package. This can only be specified for package type <code>ZIP-PLUGIN</code> </p>
            package_vending_options: <p> The vending options for the package being created. They determine if the package can be vended to other users.</p>
            package_encryption_options: <p>The encryption parameters for the package being created.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.create_package_request.CreatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.create_package_response.CreatePackageResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.create_package

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.create_package.async_create_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.create_package_request.CreatePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_name"] = package_name
        input_["package_type"] = package_type
        if package_description is not None:
            input_["package_description"] = package_description
        input_["package_source"] = package_source
        if package_configuration is not None:
            input_["package_configuration"] = package_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if package_vending_options is not None:
            input_["package_vending_options"] = package_vending_options
        if package_encryption_options is not None:
            input_["package_encryption_options"] = package_encryption_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_vpc_endpoint(
        self,
        domain_arn: "aws_sdk_opensearch.types.domain_arn.DomainArn",
        vpc_options: "aws_sdk_opensearch.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearch.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearch.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an Amazon OpenSearch Service-managed VPC endpoint.</p>

        Args:
            domain_arn: <p>The Amazon Resource Name (ARN) of the domain to create the endpoint for.</p>
            vpc_options: <p>Options to specify the subnets and security groups for the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.create_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.create_vpc_endpoint.async_create_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["domain_arn"] = domain_arn
        input_["vpc_options"] = vpc_options
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_application(
        self,
        id: "aws_sdk_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "aws_sdk_opensearch.types.delete_application_response.DeleteApplicationResponse"
    ):
        """<p>Deletes a specified OpenSearch application.</p>

        Args:
            id: <p>The unique identifier of the OpenSearch application to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_application

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_data_source(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        name: "aws_sdk_opensearch.types.data_source_name.DataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "aws_sdk_opensearch.types.delete_data_source_response.DeleteDataSourceResponse"
    ):
        r"""<p>Deletes a direct-query data source. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-delete.html\">Deleting an Amazon OpenSearch Service data source with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            name: <p>The name of the data source to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_data_source.async_delete_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_data_source_request.DeleteDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_direct_query_data_source(
        self,
        data_source_name: "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> None:
        """<p> Deletes a previously configured direct query data source from Amazon OpenSearch Service. </p>

        Args:
            data_source_name: <p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_direct_query_data_source_request.DeleteDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_direct_query_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_direct_query_data_source.async_delete_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_direct_query_data_source_request.DeleteDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_name"] = data_source_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_domain(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes an Amazon OpenSearch Service domain and all of its data. You can't recover a domain after you delete it.</p>

        Args:
            domain_name: <p>The name of the domain you want to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_domain

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_domain_request.DeleteDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_inbound_connection(
        self,
        connection_id: "aws_sdk_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.delete_inbound_connection_response.DeleteInboundConnectionResponse":
        r"""<p>Allows the destination Amazon OpenSearch Service domain owner to delete an existing inbound cross-cluster search connection. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            connection_id: <p>The ID of the inbound connection to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_inbound_connection_request.DeleteInboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_inbound_connection_response.DeleteInboundConnectionResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_inbound_connection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_inbound_connection.async_delete_inbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_inbound_connection_request.DeleteInboundConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_index(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        index_name: "aws_sdk_opensearch.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.delete_index_response.DeleteIndexResponse":
        """<p>Deletes an OpenSearch index. This operation permanently removes the index and cannot be undone.</p>

        Args:
            index_name: <p>The name of the index to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_index_request.DeleteIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_index_response.DeleteIndexResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_index

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_index.async_delete_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_index_request.DeleteIndexRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["index_name"] = index_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_outbound_connection(
        self,
        connection_id: "aws_sdk_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.delete_outbound_connection_response.DeleteOutboundConnectionResponse":
        r"""<p>Allows the source Amazon OpenSearch Service domain owner to delete an existing outbound cross-cluster search connection. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            connection_id: <p>The ID of the outbound connection you want to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_outbound_connection_request.DeleteOutboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_outbound_connection_response.DeleteOutboundConnectionResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_outbound_connection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_outbound_connection.async_delete_outbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_outbound_connection_request.DeleteOutboundConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_package(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.delete_package_response.DeletePackageResponse":
        r"""<p>Deletes an Amazon OpenSearch Service package. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The internal ID of the package you want to delete. Use <code>DescribePackages</code> to find this value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_package_request.DeletePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_package_response.DeletePackageResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_package

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_package.async_delete_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_package_request.DeletePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_vpc_endpoint(
        self,
        vpc_endpoint_id: "aws_sdk_opensearch.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>The unique identifier of the endpoint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.delete_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.delete_vpc_endpoint.async_delete_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_endpoint_id"] = vpc_endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deregister_capability(
        self,
        application_id: "aws_sdk_opensearch.types.application_id.ApplicationId",
        capability_name: "aws_sdk_opensearch.types.capability_name.CapabilityName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.deregister_capability_response.DeregisterCapabilityResponse":
        """<p>Deregisters a capability from an OpenSearch UI application. This operation removes the capability and its associated configuration.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch UI application to deregister the capability from.</p>
            capability_name: <p>The name of the capability to deregister.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.deregister_capability_request.DeregisterCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.deregister_capability_response.DeregisterCapabilityResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.deregister_capability

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.deregister_capability.async_deregister_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.deregister_capability_request.DeregisterCapabilityRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["capability_name"] = capability_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.describe_domain_response.DescribeDomainResponse":
        """<p>Describes the domain configuration for the specified Amazon OpenSearch Service domain, including the domain ID, domain service endpoint, and domain ARN.</p>

        Args:
            domain_name: <p>The name of the domain that you want information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domain_request.DescribeDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domain_response.DescribeDomainResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain.async_describe_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domain_request.DescribeDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_auto_tunes(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse":
        r"""<p>Returns the list of optimizations that Auto-Tune has made to an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html\">Auto-Tune for Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>Name of the domain that you want Auto-Tune details about.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeDomainAutoTunes</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeDomainAutoTunes</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_auto_tunes

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_auto_tunes.async_describe_domain_auto_tunes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_change_progress(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        change_id: Optional["aws_sdk_opensearch.types.guid.GUID"] = None,
    ) -> "aws_sdk_opensearch.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse":
        r"""<p>Returns information about the current blue/green deployment happening on an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html\">Making configuration changes in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain to get progress information for.</p>
            change_id: <p>The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_change_progress

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_change_progress.async_describe_domain_change_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if change_id is not None:
            input_["change_id"] = change_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_config(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.describe_domain_config_response.DescribeDomainConfigResponse":
        """<p>Returns the configuration of an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain configuration that you want to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domain_config_request.DescribeDomainConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domain_config_response.DescribeDomainConfigResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_config

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_config.async_describe_domain_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domain_config_request.DescribeDomainConfigRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_health(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.describe_domain_health_response.DescribeDomainHealthResponse":
        """<p>Returns information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domain_health_request.DescribeDomainHealthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domain_health_response.DescribeDomainHealthResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_health

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_health.async_describe_domain_health(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domain_health_request.DescribeDomainHealthRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_nodes(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.describe_domain_nodes_response.DescribeDomainNodesResponse":
        """<p>Returns information about domain and nodes, including data nodes, master nodes, ultrawarm nodes, Availability Zone(s), standby nodes, node configurations, and node states.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domain_nodes_request.DescribeDomainNodesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domain_nodes_response.DescribeDomainNodesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_nodes

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domain_nodes.async_describe_domain_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domain_nodes_request.DescribeDomainNodesRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domains(
        self,
        domain_names: "aws_sdk_opensearch.types.domain_name_list.DomainNameList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.describe_domains_response.DescribeDomainsResponse":
        """<p>Returns domain configuration information about the specified Amazon OpenSearch Service domains.</p>

        Args:
            domain_names: <p>Array of OpenSearch Service domain names that you want information about. You must specify at least one domain name.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_domains_request.DescribeDomainsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_domains_response.DescribeDomainsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_domains

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_domains.async_describe_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_domains_request.DescribeDomainsRequest = {}  # type: ignore[typeddict-item]
        input_["domain_names"] = domain_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_dry_run_progress(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        dry_run_id: Optional["aws_sdk_opensearch.types.guid.GUID"] = None,
        load_dry_run_config: Optional[
            "aws_sdk_opensearch.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_opensearch.types.describe_dry_run_progress_response.DescribeDryRunProgressResponse":
        r"""<p>Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#dryrun\">Determining whether a change will cause a blue/green deployment</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            dry_run_id: <p>The unique identifier of the dry run.</p>
            load_dry_run_config: <p>Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you're planning to make on the domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_dry_run_progress_request.DescribeDryRunProgressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_dry_run_progress_response.DescribeDryRunProgressResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_dry_run_progress

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_dry_run_progress.async_describe_dry_run_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_dry_run_progress_request.DescribeDryRunProgressRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if dry_run_id is not None:
            input_["dry_run_id"] = dry_run_id
        if load_dry_run_config is not None:
            input_["load_dry_run_config"] = load_dry_run_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_inbound_connections(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional["aws_sdk_opensearch.types.filter_list.FilterList"] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.describe_inbound_connections_response.DescribeInboundConnectionsResponse":
        r"""<p>Lists all the inbound cross-cluster search connections for a destination (remote) Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            filters: <p> A list of filters used to match properties for inbound cross-cluster connections.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeInboundConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeInboundConnections</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_inbound_connections_request.DescribeInboundConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_inbound_connections_response.DescribeInboundConnectionsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_inbound_connections

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_inbound_connections.async_describe_inbound_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_inbound_connections_request.DescribeInboundConnectionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_insight_details(
        self,
        entity: "aws_sdk_opensearch.types.insight_entity.InsightEntity",
        insight_id: "aws_sdk_opensearch.types.guid.GUID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        show_html_content: Optional["aws_sdk_opensearch.types.boolean.Boolean"] = None,
    ) -> "aws_sdk_opensearch.types.describe_insight_details_response.DescribeInsightDetailsResponse":
        """<p>Describes the details of an existing insight for an Amazon OpenSearch Service domain. Returns detailed fields associated with the specified insight, such as text descriptions and metric data.</p>

        Args:
            entity: <p>The entity for which to retrieve insight details. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>
            insight_id: <p>The unique identifier of the insight to describe.</p>
            show_html_content: <p>Specifies whether to show response with HTML content in response or not.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_insight_details_request.DescribeInsightDetailsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_insight_details_response.DescribeInsightDetailsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_insight_details

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_insight_details.async_describe_insight_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_insight_details_request.DescribeInsightDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["entity"] = entity
        input_["insight_id"] = insight_id
        if show_html_content is not None:
            input_["show_html_content"] = show_html_content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_instance_type_limits(
        self,
        instance_type: "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType",
        engine_version: "aws_sdk_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["aws_sdk_opensearch.types.domain_name.DomainName"] = None,
    ) -> "aws_sdk_opensearch.types.describe_instance_type_limits_response.DescribeInstanceTypeLimitsResponse":
        """<p>Describes the instance count, storage, and master node limits for a given OpenSearch or Elasticsearch version and instance type.</p>

        Args:
            domain_name: <p>The name of the domain. Only specify if you need the limits for an existing domain.</p>
            instance_type: <p>The OpenSearch Service instance type for which you need limit information.</p>
            engine_version: <p>Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_instance_type_limits_request.DescribeInstanceTypeLimitsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_instance_type_limits_response.DescribeInstanceTypeLimitsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_instance_type_limits

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_instance_type_limits.async_describe_instance_type_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_instance_type_limits_request.DescribeInstanceTypeLimitsRequest = {}  # type: ignore[typeddict-item]
        if domain_name is not None:
            input_["domain_name"] = domain_name
        input_["instance_type"] = instance_type
        input_["engine_version"] = engine_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_outbound_connections(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional["aws_sdk_opensearch.types.filter_list.FilterList"] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.describe_outbound_connections_response.DescribeOutboundConnectionsResponse":
        r"""<p>Lists all the outbound cross-cluster connections for a local (source) Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html\">Cross-cluster search for Amazon OpenSearch Service</a>.</p>

        Args:
            filters: <p>List of filter names and values that you can use for requests.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeOutboundConnections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeOutboundConnections</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_outbound_connections_request.DescribeOutboundConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_outbound_connections_response.DescribeOutboundConnectionsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_outbound_connections

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_outbound_connections.async_describe_outbound_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_outbound_connections_request.DescribeOutboundConnectionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_packages(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        filters: Optional[
            "aws_sdk_opensearch.types.describe_packages_filter_list.DescribePackagesFilterList"
        ] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.describe_packages_response.DescribePackagesResponse":
        r"""<p>Describes all packages available to OpenSearch Service. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            filters: <p>Only returns packages that match the <code>DescribePackagesFilterList</code> values.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribePackageFilters</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribePackageFilters</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_packages_request.DescribePackagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_packages_response.DescribePackagesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_packages

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_packages.async_describe_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_packages_request.DescribePackagesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_reserved_instance_offerings(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        reserved_instance_offering_id: Optional[
            "aws_sdk_opensearch.types.guid.GUID"
        ] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.describe_reserved_instance_offerings_response.DescribeReservedInstanceOfferingsResponse":
        r"""<p>Describes the available Amazon OpenSearch Service Reserved Instance offerings for a given Region. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html\">Reserved Instances in Amazon OpenSearch Service</a>.</p>

        Args:
            reserved_instance_offering_id: <p>The Reserved Instance identifier filter value. Use this parameter to show only the available instance types that match the specified reservation identifier.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeReservedInstanceOfferings</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstanceOfferings</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_reserved_instance_offerings_request.DescribeReservedInstanceOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_reserved_instance_offerings_response.DescribeReservedInstanceOfferingsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_reserved_instance_offerings

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_reserved_instance_offerings.async_describe_reserved_instance_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_reserved_instance_offerings_request.DescribeReservedInstanceOfferingsRequest = {}  # type: ignore[typeddict-item]
        if reserved_instance_offering_id is not None:
            input_["reserved_instance_offering_id"] = reserved_instance_offering_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_reserved_instances(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        reserved_instance_id: Optional["aws_sdk_opensearch.types.guid.GUID"] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.describe_reserved_instances_response.DescribeReservedInstancesResponse":
        r"""<p>Describes the Amazon OpenSearch Service instances that you have reserved in a given Region. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html\">Reserved Instances in Amazon OpenSearch Service</a>.</p>

        Args:
            reserved_instance_id: <p>The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved OpenSearch instance ID.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>DescribeReservedInstances</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>DescribeReservedInstances</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_reserved_instances_request.DescribeReservedInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_reserved_instances_response.DescribeReservedInstancesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_reserved_instances

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_reserved_instances.async_describe_reserved_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_reserved_instances_request.DescribeReservedInstancesRequest = {}  # type: ignore[typeddict-item]
        if reserved_instance_id is not None:
            input_["reserved_instance_id"] = reserved_instance_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_vpc_endpoints(
        self,
        vpc_endpoint_ids: "aws_sdk_opensearch.types.vpc_endpoint_id_list.VpcEndpointIdList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse":
        """<p>Describes one or more Amazon OpenSearch Service-managed VPC endpoints.</p>

        Args:
            vpc_endpoint_ids: <p>The unique identifiers of the endpoints to get information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.describe_vpc_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.describe_vpc_endpoints.async_describe_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_endpoint_ids"] = vpc_endpoint_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def dissociate_package(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "aws_sdk_opensearch.types.dissociate_package_response.DissociatePackageResponse"
    ):
        r"""<p>Removes a package from the specified Amazon OpenSearch Service domain. The package can't be in use with any OpenSearch index for the dissociation to succeed. The package is still available in OpenSearch Service for association later. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>Internal ID of the package to dissociate from the domain. Use <code>ListPackagesForDomain</code> to find this value.</p>
            domain_name: <p>Name of the domain to dissociate the package from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.dissociate_package_request.DissociatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.dissociate_package_response.DissociatePackageResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.dissociate_package

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.dissociate_package.async_dissociate_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.dissociate_package_request.DissociatePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def dissociate_packages(
        self,
        package_list: "aws_sdk_opensearch.types.package_id_list.PackageIDList",
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.dissociate_packages_response.DissociatePackagesResponse":
        """<p>Dissociates multiple packages from a domain simultaneously.</p>

        Args:
            package_list: <p>A list of package IDs to be dissociated from a domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.dissociate_packages_request.DissociatePackagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.dissociate_packages_response.DissociatePackagesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.dissociate_packages

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.dissociate_packages.async_dissociate_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.dissociate_packages_request.DissociatePackagesRequest = {}  # type: ignore[typeddict-item]
        input_["package_list"] = package_list
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_application(
        self,
        id: "aws_sdk_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves the configuration and status of an existing OpenSearch application.</p>

        Args:
            id: <p>The unique identifier of the OpenSearch application to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_application_response.GetApplicationResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_application

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_application_request.GetApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_capability(
        self,
        application_id: "aws_sdk_opensearch.types.application_id.ApplicationId",
        capability_name: "aws_sdk_opensearch.types.capability_name.CapabilityName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.get_capability_response.GetCapabilityResponse":
        """<p>Retrieves information about a registered capability for an OpenSearch UI application, including its configuration and current status.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch UI application.</p>
            capability_name: <p>The name of the capability to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_capability_request.GetCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_capability_response.GetCapabilityResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_capability

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_capability.async_get_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_capability_request.GetCapabilityRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["capability_name"] = capability_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_compatible_versions(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["aws_sdk_opensearch.types.domain_name.DomainName"] = None,
    ) -> "aws_sdk_opensearch.types.get_compatible_versions_response.GetCompatibleVersionsResponse":
        """<p>Returns a map of OpenSearch or Elasticsearch versions and the versions you can upgrade them to.</p>

        Args:
            domain_name: <p>The name of an existing domain. Provide this parameter to limit the results to a single domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_compatible_versions_request.GetCompatibleVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_compatible_versions_response.GetCompatibleVersionsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_compatible_versions

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_compatible_versions.async_get_compatible_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_compatible_versions_request.GetCompatibleVersionsRequest = {}  # type: ignore[typeddict-item]
        if domain_name is not None:
            input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_source(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        name: "aws_sdk_opensearch.types.data_source_name.DataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.get_data_source_response.GetDataSourceResponse":
        """<p>Retrieves information about a direct query data source.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            name: <p>The name of the data source to get information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_data_source_request.GetDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_data_source.async_get_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_data_source_request.GetDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_default_application_setting(
        self, *, config_overrides: Optional[AsyncOpenSearchClientConfig] = None
    ) -> "aws_sdk_opensearch.types.get_default_application_setting_response.GetDefaultApplicationSettingResponse":
        """<p>Gets the ARN of the current default application.</p> <p> If the default application isn't set, the operation returns a resource not found error.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_default_application_setting_request.GetDefaultApplicationSettingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_default_application_setting_response.GetDefaultApplicationSettingResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_default_application_setting

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_default_application_setting.async_get_default_application_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_default_application_setting_request.GetDefaultApplicationSettingRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_direct_query_data_source(
        self,
        data_source_name: "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.get_direct_query_data_source_response.GetDirectQueryDataSourceResponse":
        """<p> Returns detailed configuration information for a specific direct query data source in Amazon OpenSearch Service. </p>

        Args:
            data_source_name: <p> A unique, user-defined label that identifies the data source within your OpenSearch Service environment. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_direct_query_data_source_request.GetDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_direct_query_data_source_response.GetDirectQueryDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_direct_query_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_direct_query_data_source.async_get_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_direct_query_data_source_request.GetDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_name"] = data_source_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_domain_maintenance_status(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        maintenance_id: "aws_sdk_opensearch.types.request_id.RequestId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.get_domain_maintenance_status_response.GetDomainMaintenanceStatusResponse":
        """<p>The status of the maintenance action.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            maintenance_id: <p>The request ID of the maintenance action.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_domain_maintenance_status_request.GetDomainMaintenanceStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_domain_maintenance_status_response.GetDomainMaintenanceStatusResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_domain_maintenance_status

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_domain_maintenance_status.async_get_domain_maintenance_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_domain_maintenance_status_request.GetDomainMaintenanceStatusRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["maintenance_id"] = maintenance_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_index(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        index_name: "aws_sdk_opensearch.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.get_index_response.GetIndexResponse":
        """<p>Retrieves information about an OpenSearch index including its schema and semantic enrichment configuration. Use this operation to view the current index structure and semantic search settings.</p>

        Args:
            index_name: <p>The name of the index to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_index_request.GetIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_index_response.GetIndexResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_index

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_index.async_get_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_index_request.GetIndexRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["index_name"] = index_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_package_version_history(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.get_package_version_history_response.GetPackageVersionHistoryResponse":
        r"""<p>Returns a list of Amazon OpenSearch Service package versions, along with their creation time, commit message, and plugin properties (if the package is a zip plugin package). For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The unique identifier of the package.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>GetPackageVersionHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetPackageVersionHistory</code> operations, which returns results in the next page. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_package_version_history_request.GetPackageVersionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_package_version_history_response.GetPackageVersionHistoryResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_package_version_history

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_package_version_history.async_get_package_version_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_package_version_history_request.GetPackageVersionHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_upgrade_history(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.get_upgrade_history_response.GetUpgradeHistoryResponse":
        """<p>Retrieves the complete history of the last 10 upgrades performed on an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>The name of an existing domain.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>GetUpgradeHistory</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>GetUpgradeHistory</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_upgrade_history_request.GetUpgradeHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_upgrade_history_response.GetUpgradeHistoryResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_upgrade_history

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_upgrade_history.async_get_upgrade_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_upgrade_history_request.GetUpgradeHistoryRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_upgrade_status(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> (
        "aws_sdk_opensearch.types.get_upgrade_status_response.GetUpgradeStatusResponse"
    ):
        """<p>Returns the most recent status of the last upgrade or upgrade eligibility check performed on an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>The domain of the domain to get upgrade status information for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.get_upgrade_status_request.GetUpgradeStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.get_upgrade_status_response.GetUpgradeStatusResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.get_upgrade_status

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.get_upgrade_status.async_get_upgrade_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.get_upgrade_status_request.GetUpgradeStatusRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
        statuses: Optional[
            "aws_sdk_opensearch.types.application_statuses.ApplicationStatuses"
        ] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_opensearch.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists all OpenSearch applications under your account.</p>

        Args:
            statuses: <p>Filters the list of OpenSearch applications by status. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_applications

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if statuses is not None:
            input_["statuses"] = statuses
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
        statuses: Optional[
            "aws_sdk_opensearch.types.application_statuses.ApplicationStatuses"
        ] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[aws_sdk_opensearch.types.application_summary.ApplicationSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                statuses=statuses,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_sources(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.list_data_sources_response.ListDataSourcesResponse":
        r"""<p>Lists direct-query data sources for a specific domain. For more information, see For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3.html\">Working with Amazon OpenSearch Service direct queries with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_data_sources

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_data_sources.async_list_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_data_sources_request.ListDataSourcesRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_direct_query_data_sources(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_direct_query_data_sources_response.ListDirectQueryDataSourcesResponse":
        """<p> Lists an inventory of all the direct query data sources that you have configured within Amazon OpenSearch Service. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_direct_query_data_sources_request.ListDirectQueryDataSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_direct_query_data_sources_response.ListDirectQueryDataSourcesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_direct_query_data_sources

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_direct_query_data_sources.async_list_direct_query_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_direct_query_data_sources_request.ListDirectQueryDataSourcesRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domain_maintenances(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        action: Optional[
            "aws_sdk_opensearch.types.maintenance_type.MaintenanceType"
        ] = None,
        status: Optional[
            "aws_sdk_opensearch.types.maintenance_status.MaintenanceStatus"
        ] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_domain_maintenances_response.ListDomainMaintenancesResponse":
        """<p>A list of maintenance actions for the domain.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            action: <p>The name of the action.</p>
            status: <p>The status of the action.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListDomainMaintenances</code> operation returns a <code>nextToken</code>, include the returned <code>nextToken</code> in subsequent <code>ListDomainMaintenances</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_domain_maintenances_request.ListDomainMaintenancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_domain_maintenances_response.ListDomainMaintenancesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_domain_maintenances

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_domain_maintenances.async_list_domain_maintenances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_domain_maintenances_request.ListDomainMaintenancesRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if action is not None:
            input_["action"] = action
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domain_names(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        engine_type: Optional["aws_sdk_opensearch.types.engine_type.EngineType"] = None,
    ) -> "aws_sdk_opensearch.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Returns the names of all Amazon OpenSearch Service domains owned by the current user in the active Region.</p>

        Args:
            engine_type: <p>Filters the output by domain engine type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_domain_names_request.ListDomainNamesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_domain_names

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_domain_names.async_list_domain_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_domain_names_request.ListDomainNamesRequest = {}  # type: ignore[typeddict-item]
        if engine_type is not None:
            input_["engine_type"] = engine_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domains_for_package(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_domains_for_package_response.ListDomainsForPackageResponse":
        r"""<p>Lists all Amazon OpenSearch Service domains associated with a given package. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The unique identifier of the package for which to list associated domains.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListDomainsForPackage</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListDomainsForPackage</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_domains_for_package_request.ListDomainsForPackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_domains_for_package_response.ListDomainsForPackageResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_domains_for_package

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_domains_for_package.async_list_domains_for_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_domains_for_package_request.ListDomainsForPackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_insights(
        self,
        entity: "aws_sdk_opensearch.types.insight_entity.InsightEntity",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        time_range: Optional[
            "aws_sdk_opensearch.types.insight_time_range.InsightTimeRange"
        ] = None,
        sort_order: Optional[
            "aws_sdk_opensearch.types.insight_sort_order.InsightSortOrder"
        ] = None,
        max_results: Optional[
            "aws_sdk_opensearch.types.insight_page_size.InsightPageSize"
        ] = None,
        next_token: Optional["aws_sdk_opensearch.types.string.String"] = None,
    ) -> "aws_sdk_opensearch.types.list_insights_response.ListInsightsResponse":
        """<p>Lists insights for an Amazon OpenSearch Service domain or Amazon Web Services account. Returns a paginated list of insights based on the specified entity, filters, time range, and sort order.</p>

        Args:
            entity: <p>The entity for which to list insights. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.</p>
            time_range: <p>The time range for filtering insights, specified as epoch millisecond timestamps.</p>
            sort_order: <p>The sort order for the results. Possible values are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>NextToken</code> to get the next page of results. Valid values are 1 to 500.</p>
            next_token: <p>If your initial <code>ListInsights</code> operation returns a <code>NextToken</code>, include the returned <code>NextToken</code> in subsequent <code>ListInsights</code> operations to retrieve the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_insights_request.ListInsightsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_insights_response.ListInsightsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_insights

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_insights.async_list_insights(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_insights_request.ListInsightsRequest = {}  # type: ignore[typeddict-item]
        input_["entity"] = entity
        if time_range is not None:
            input_["time_range"] = time_range
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_instance_type_details(
        self,
        engine_version: "aws_sdk_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        domain_name: Optional["aws_sdk_opensearch.types.domain_name.DomainName"] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
        retrieve_a_zs: Optional["aws_sdk_opensearch.types.boolean.Boolean"] = None,
        instance_type: Optional[
            "aws_sdk_opensearch.types.instance_type_string.InstanceTypeString"
        ] = None,
    ) -> "aws_sdk_opensearch.types.list_instance_type_details_response.ListInstanceTypeDetailsResponse":
        """<p>Lists all instance types and available features for a given OpenSearch or Elasticsearch version.</p>

        Args:
            engine_version: <p>The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>
            domain_name: <p>The name of the domain.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListInstanceTypeDetails</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListInstanceTypeDetails</code> operations, which returns results in the next page.</p>
            retrieve_a_zs: <p>An optional parameter that specifies the Availability Zones for the domain.</p>
            instance_type: <p>An optional parameter that lists information for a given instance type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_instance_type_details_request.ListInstanceTypeDetailsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_instance_type_details_response.ListInstanceTypeDetailsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_instance_type_details

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_instance_type_details.async_list_instance_type_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_instance_type_details_request.ListInstanceTypeDetailsRequest = {}  # type: ignore[typeddict-item]
        input_["engine_version"] = engine_version
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if retrieve_a_zs is not None:
            input_["retrieve_a_zs"] = retrieve_a_zs
        if instance_type is not None:
            input_["instance_type"] = instance_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_packages_for_domain(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_packages_for_domain_response.ListPackagesForDomainResponse":
        r"""<p>Lists all packages associated with an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain for which you want to list associated packages.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListPackagesForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListPackagesForDomain</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_packages_for_domain_request.ListPackagesForDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_packages_for_domain_response.ListPackagesForDomainResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_packages_for_domain

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_packages_for_domain.async_list_packages_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_packages_for_domain_request.ListPackagesForDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_scheduled_actions(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_scheduled_actions_response.ListScheduledActionsResponse":
        r"""<p>Retrieves a list of configuration changes that are scheduled for a domain. These changes can be <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\">service software updates</a> or <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\">blue/green Auto-Tune enhancements</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListScheduledActions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListScheduledActions</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_scheduled_actions_request.ListScheduledActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_scheduled_actions_response.ListScheduledActionsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_scheduled_actions

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_scheduled_actions.async_list_scheduled_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_scheduled_actions_request.ListScheduledActionsRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags(
        self,
        arn: "aws_sdk_opensearch.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.list_tags_response.ListTagsResponse":
        r"""<p>Returns all resource tags for an Amazon OpenSearch Service domain, data source, or application. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-awsresourcetagging.html\">Tagging Amazon OpenSearch Service resources</a>.</p>

        Args:
            arn: <p>Amazon Resource Name (ARN) for the domain, data source, or application to view tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_tags_response.ListTagsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_tags

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_versions(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        max_results: Optional["aws_sdk_opensearch.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_versions_response.ListVersionsResponse":
        """<p>Lists all versions of OpenSearch and Elasticsearch that Amazon OpenSearch Service supports.</p>

        Args:
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>
            next_token: <p>If your initial <code>ListVersions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVersions</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_versions_request.ListVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_versions_response.ListVersionsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_versions

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_versions.async_list_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_versions_request.ListVersionsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vpc_endpoint_access(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse":
        """<p>Retrieves information about each Amazon Web Services principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to retrieve access information for.</p>
            next_token: <p>If your initial <code>ListVpcEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpointAccess</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_vpc_endpoint_access.async_list_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vpc_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> (
        "aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
    ):
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current Amazon Web Services account and Region.</p>

        Args:
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_vpc_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_vpc_endpoints.async_list_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vpc_endpoints_for_domain(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        next_token: Optional["aws_sdk_opensearch.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_opensearch.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.</p>

        Args:
            domain_name: <p>The name of the domain to list associated VPC endpoints for.</p>
            next_token: <p>If your initial <code>ListEndpointsForDomain</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListEndpointsForDomain</code> operations, which returns results in the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.list_vpc_endpoints_for_domain

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.list_vpc_endpoints_for_domain.async_list_vpc_endpoints_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def purchase_reserved_instance_offering(
        self,
        reserved_instance_offering_id: "aws_sdk_opensearch.types.guid.GUID",
        reservation_name: "aws_sdk_opensearch.types.reservation_token.ReservationToken",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        instance_count: Optional[
            "aws_sdk_opensearch.types.instance_count.InstanceCount"
        ] = None,
    ) -> "aws_sdk_opensearch.types.purchase_reserved_instance_offering_response.PurchaseReservedInstanceOfferingResponse":
        """<p>Allows you to purchase Amazon OpenSearch Service Reserved Instances.</p>

        Args:
            reserved_instance_offering_id: <p>The ID of the Reserved Instance offering to purchase.</p>
            reservation_name: <p>A customer-specified identifier to track this reservation.</p>
            instance_count: <p>The number of OpenSearch instances to reserve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.purchase_reserved_instance_offering_request.PurchaseReservedInstanceOfferingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.purchase_reserved_instance_offering_response.PurchaseReservedInstanceOfferingResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.purchase_reserved_instance_offering

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.purchase_reserved_instance_offering.async_purchase_reserved_instance_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.purchase_reserved_instance_offering_request.PurchaseReservedInstanceOfferingRequest = {}  # type: ignore[typeddict-item]
        input_["reserved_instance_offering_id"] = reserved_instance_offering_id
        input_["reservation_name"] = reservation_name
        if instance_count is not None:
            input_["instance_count"] = instance_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_default_application_setting(
        self,
        application_arn: "aws_sdk_opensearch.types.arn.ARN",
        set_as_default: "aws_sdk_opensearch.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.put_default_application_setting_response.PutDefaultApplicationSettingResponse":
        """<p>Sets the default application to the application with the specified ARN.</p> <p> To remove the default application, use the <code>GetDefaultApplicationSetting</code> operation to get the current default and then call the <code>PutDefaultApplicationSetting</code> with the current applications ARN and the <code>setAsDefault</code> parameter set to <code>false</code>.</p>

        Args:
            set_as_default: <p>Set to true to set the specified ARN as the default application. Set to false to clear the default application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.put_default_application_setting_request.PutDefaultApplicationSettingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.put_default_application_setting_response.PutDefaultApplicationSettingResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.put_default_application_setting

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.put_default_application_setting.async_put_default_application_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.put_default_application_setting_request.PutDefaultApplicationSettingRequest = {}  # type: ignore[typeddict-item]
        input_["application_arn"] = application_arn
        input_["set_as_default"] = set_as_default

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_capability(
        self,
        application_id: "aws_sdk_opensearch.types.application_id.ApplicationId",
        capability_name: "aws_sdk_opensearch.types.capability_name.CapabilityName",
        capability_config: "aws_sdk_opensearch.types.capability_base_request_config.CapabilityBaseRequestConfig",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.register_capability_response.RegisterCapabilityResponse":
        r"""<p>Registers a capability for an OpenSearch UI application. Use this operation to enable specific capabilities, such as AI features, for a given application. The capability configuration defines the type and settings of the capability to register. For more information about the AI features, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-ai-assistant.html\">Agentic AI for OpenSearch UI</a>.</p>

        Args:
            application_id: <p>The unique identifier of the OpenSearch UI application to register the capability for.</p>
            capability_name: <p>The name of the capability to register. Must be between 3 and 30 characters and contain only alphanumeric characters and hyphens. This identifies the type of capability being enabled for the application. For registering AI Assistant capability, use <code>ai-capability</code> </p>
            capability_config: <p>The configuration settings for the capability being registered. This includes capability-specific settings such as AI configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.register_capability_request.RegisterCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.register_capability_response.RegisterCapabilityResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.register_capability

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.register_capability.async_register_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.register_capability_request.RegisterCapabilityRequest = {}  # type: ignore[typeddict-item]
        input_["application_id"] = application_id
        input_["capability_name"] = capability_name
        input_["capability_config"] = capability_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reject_inbound_connection(
        self,
        connection_id: "aws_sdk_opensearch.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.reject_inbound_connection_response.RejectInboundConnectionResponse":
        """<p>Allows the remote Amazon OpenSearch Service domain owner to reject an inbound cross-cluster connection request.</p>

        Args:
            connection_id: <p>The unique identifier of the inbound connection to reject.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.reject_inbound_connection_request.RejectInboundConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.reject_inbound_connection_response.RejectInboundConnectionResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.reject_inbound_connection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.reject_inbound_connection.async_reject_inbound_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.reject_inbound_connection_request.RejectInboundConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["connection_id"] = connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_tags(
        self,
        arn: "aws_sdk_opensearch.types.arn.ARN",
        tag_keys: "aws_sdk_opensearch.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> None:
        r"""<p>Removes the specified set of tags from an Amazon OpenSearch Service domain, data source, or application. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains.html#managedomains-awsresorcetagging\"> Tagging Amazon OpenSearch Service resources</a>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the domain, data source, or application from which you want to delete the specified tags.</p>
            tag_keys: <p>The list of tag keys to remove from the domain, data source, or application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.remove_tags_request.RemoveTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.remove_tags

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.remove_tags.async_remove_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.remove_tags_request.RemoveTagsRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def revoke_vpc_endpoint_access(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        account: Optional["aws_sdk_opensearch.types.aws_account.AWSAccount"] = None,
        service: Optional[
            "aws_sdk_opensearch.types.aws_service_principal.AWSServicePrincipal"
        ] = None,
        service_options: Optional[
            "aws_sdk_opensearch.types.service_options.ServiceOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse":
        """<p>Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain.</p>
            account: <p>The account ID to revoke access from.</p>
            service: <p>The service SP to revoke access from.</p>
            service_options: <p>The options for the service, including the supported Regions for the endpoint access.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.revoke_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.revoke_vpc_endpoint_access.async_revoke_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if account is not None:
            input_["account"] = account
        if service is not None:
            input_["service"] = service
        if service_options is not None:
            input_["service_options"] = service_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def rollback_service_software_update(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.rollback_service_software_update_response.RollbackServiceSoftwareUpdateResponse":
        r"""<p>Rolls back a service software update for a domain to the previous version. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\">Service software updates in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain to roll back the service software update on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.rollback_service_software_update_request.RollbackServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.rollback_service_software_update_response.RollbackServiceSoftwareUpdateResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.rollback_service_software_update

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.rollback_service_software_update.async_rollback_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.rollback_service_software_update_request.RollbackServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_domain_maintenance(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        action: "aws_sdk_opensearch.types.maintenance_type.MaintenanceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        node_id: Optional["aws_sdk_opensearch.types.node_id.NodeId"] = None,
    ) -> "aws_sdk_opensearch.types.start_domain_maintenance_response.StartDomainMaintenanceResponse":
        """<p>Starts the node maintenance process on the data node. These processes can include a node reboot, an Opensearch or Elasticsearch process restart, or a Dashboard or Kibana restart.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            action: <p>The name of the action.</p>
            node_id: <p>The ID of the data node.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.start_domain_maintenance_request.StartDomainMaintenanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.start_domain_maintenance_response.StartDomainMaintenanceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.start_domain_maintenance

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.start_domain_maintenance.async_start_domain_maintenance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.start_domain_maintenance_request.StartDomainMaintenanceRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["action"] = action
        if node_id is not None:
            input_["node_id"] = node_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_service_software_update(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        schedule_at: Optional["aws_sdk_opensearch.types.schedule_at.ScheduleAt"] = None,
        desired_start_time: Optional["aws_sdk_opensearch.types.long.Long"] = None,
    ) -> "aws_sdk_opensearch.types.start_service_software_update_response.StartServiceSoftwareUpdateResponse":
        r"""<p>Schedules a service software update for an Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\">Service software updates in Amazon OpenSearch Service</a>.</p>

        Args:
            domain_name: <p>The name of the domain that you want to update to the latest service software.</p>
            schedule_at: <p>When to start the service software update.</p> <ul> <li> <p> <code>NOW</code> - Immediately schedules the update to happen in the current hour if there's capacity available.</p> </li> <li> <p> <code>TIMESTAMP</code> - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for <code>DesiredStartTime</code>.</p> </li> <li> <p> <code>OFF_PEAK_WINDOW</code> - Marks the update to be picked up during an upcoming off-peak window. There's no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days.</p> </li> </ul> <p>Default: <code>NOW</code> if you don't specify a value for <code>DesiredStartTime</code>, and <code>TIMESTAMP</code> if you do.</p>
            desired_start_time: <p>The Epoch timestamp when you want the service software update to start. You only need to specify this parameter if you set <code>ScheduleAt</code> to <code>TIMESTAMP</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.start_service_software_update_request.StartServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.start_service_software_update_response.StartServiceSoftwareUpdateResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.start_service_software_update

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.start_service_software_update.async_start_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.start_service_software_update_request.StartServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if schedule_at is not None:
            input_["schedule_at"] = schedule_at
        if desired_start_time is not None:
            input_["desired_start_time"] = desired_start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_application(
        self,
        id: "aws_sdk_opensearch.types.id.Id",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        data_sources: Optional[
            "aws_sdk_opensearch.types.data_sources.DataSources"
        ] = None,
        app_configs: Optional["aws_sdk_opensearch.types.app_configs.AppConfigs"] = None,
    ) -> (
        "aws_sdk_opensearch.types.update_application_response.UpdateApplicationResponse"
    ):
        """<p>Updates the configuration and settings of an existing OpenSearch application.</p>

        Args:
            id: <p>The unique identifier for the OpenSearch application to be updated.</p>
            data_sources: <p>The data sources to associate with the OpenSearch application.</p>
            app_configs: <p>The configuration settings to modify for the OpenSearch application.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_application_response.UpdateApplicationResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_application

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if app_configs is not None:
            input_["app_configs"] = app_configs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_data_source(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        name: "aws_sdk_opensearch.types.data_source_name.DataSourceName",
        data_source_type: "aws_sdk_opensearch.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearch.types.data_source_description.DataSourceDescription"
        ] = None,
        status: Optional[
            "aws_sdk_opensearch.types.data_source_status.DataSourceStatus"
        ] = None,
    ) -> (
        "aws_sdk_opensearch.types.update_data_source_response.UpdateDataSourceResponse"
    ):
        r"""<p>Updates a direct-query data source. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html\">Working with Amazon OpenSearch Service data source integrations with Amazon S3</a>.</p>

        Args:
            domain_name: <p>The name of the domain.</p>
            name: <p>The name of the data source to modify.</p>
            data_source_type: <p>The type of data source.</p>
            description: <p>A new description of the data source.</p>
            status: <p>The status of the data source update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_data_source.async_update_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_data_source_request.UpdateDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["name"] = name
        input_["data_source_type"] = data_source_type
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_direct_query_data_source(
        self,
        data_source_name: "aws_sdk_opensearch.types.direct_query_data_source_name.DirectQueryDataSourceName",
        data_source_type: "aws_sdk_opensearch.types.direct_query_data_source_type.DirectQueryDataSourceType",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        description: Optional[
            "aws_sdk_opensearch.types.direct_query_data_source_description.DirectQueryDataSourceDescription"
        ] = None,
        open_search_arns: Optional[
            "aws_sdk_opensearch.types.direct_query_open_search_arn_list.DirectQueryOpenSearchARNList"
        ] = None,
        data_source_access_policy: Optional[
            "aws_sdk_opensearch.types.policy_document.PolicyDocument"
        ] = None,
    ) -> "aws_sdk_opensearch.types.update_direct_query_data_source_response.UpdateDirectQueryDataSourceResponse":
        """<p> Updates the configuration or properties of an existing direct query data source in Amazon OpenSearch Service. </p>

        Args:
            data_source_name: <p> A unique, user-defined label to identify the data source within your OpenSearch Service environment. </p>
            data_source_type: <p> The supported Amazon Web Services service that you want to use as the source for direct queries in OpenSearch Service. </p>
            description: <p> An optional text field for providing additional context and details about the data source. </p>
            open_search_arns: <p> An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types. </p>
            data_source_access_policy: <p> An optional IAM access policy document that defines the updated permissions for accessing the direct query data source. The policy document must be in valid JSON format and follow IAM policy syntax. If not specified, the existing access policy if present remains unchanged. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_direct_query_data_source_request.UpdateDirectQueryDataSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_direct_query_data_source_response.UpdateDirectQueryDataSourceResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_direct_query_data_source

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_direct_query_data_source.async_update_direct_query_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_direct_query_data_source_request.UpdateDirectQueryDataSourceRequest = {}  # type: ignore[typeddict-item]
        input_["data_source_name"] = data_source_name
        input_["data_source_type"] = data_source_type
        if description is not None:
            input_["description"] = description
        if open_search_arns is not None:
            input_["open_search_arns"] = open_search_arns
        if data_source_access_policy is not None:
            input_["data_source_access_policy"] = data_source_access_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_domain_config(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        cluster_config: Optional[
            "aws_sdk_opensearch.types.cluster_config.ClusterConfig"
        ] = None,
        ebs_options: Optional["aws_sdk_opensearch.types.ebs_options.EBSOptions"] = None,
        snapshot_options: Optional[
            "aws_sdk_opensearch.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional["aws_sdk_opensearch.types.vpc_options.VPCOptions"] = None,
        cognito_options: Optional[
            "aws_sdk_opensearch.types.cognito_options.CognitoOptions"
        ] = None,
        advanced_options: Optional[
            "aws_sdk_opensearch.types.advanced_options.AdvancedOptions"
        ] = None,
        access_policies: Optional[
            "aws_sdk_opensearch.types.policy_document.PolicyDocument"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_opensearch.types.ip_address_type.IPAddressType"
        ] = None,
        log_publishing_options: Optional[
            "aws_sdk_opensearch.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "aws_sdk_opensearch.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "aws_sdk_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        node_to_node_encryption_options: Optional[
            "aws_sdk_opensearch.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        advanced_security_options: Optional[
            "aws_sdk_opensearch.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        identity_center_options: Optional[
            "aws_sdk_opensearch.types.identity_center_options_input.IdentityCenterOptionsInput"
        ] = None,
        auto_tune_options: Optional[
            "aws_sdk_opensearch.types.auto_tune_options.AutoTuneOptions"
        ] = None,
        dry_run: Optional["aws_sdk_opensearch.types.dry_run.DryRun"] = None,
        dry_run_mode: Optional[
            "aws_sdk_opensearch.types.dry_run_mode.DryRunMode"
        ] = None,
        off_peak_window_options: Optional[
            "aws_sdk_opensearch.types.off_peak_window_options.OffPeakWindowOptions"
        ] = None,
        software_update_options: Optional[
            "aws_sdk_opensearch.types.software_update_options.SoftwareUpdateOptions"
        ] = None,
        aiml_options: Optional[
            "aws_sdk_opensearch.types.aiml_options_input.AIMLOptionsInput"
        ] = None,
        deployment_strategy_options: Optional[
            "aws_sdk_opensearch.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "aws_sdk_opensearch.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.update_domain_config_response.UpdateDomainConfigResponse":
        r"""<p>Modifies the cluster configuration of the specified Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>The name of the domain that you're updating.</p>
            cluster_config: <p>Changes that you want to make to the cluster configuration, such as the instance type and number of EC2 instances.</p>
            ebs_options: <p>The type and size of the EBS volume to attach to instances in the domain.</p>
            snapshot_options: <p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>
            vpc_options: <p>Options to specify the subnets and security groups for a VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html\">Launching your Amazon OpenSearch Service domains using a VPC</a>.</p>
            cognito_options: <p>Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.</p>
            advanced_options: <p>Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:</p> <ul> <li> <p> <code>\"rest.action.multi.allow_explicit_index\": \"true\" | \"false\"</code> - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.</p> </li> <li> <p> <code>\"indices.fielddata.cache.size\": \"80\" </code> - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.</p> </li> <li> <p> <code>\"indices.query.bool.max_clause_count\": \"1024\"</code> - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a <code>TooManyClauses</code> error.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options\">Advanced cluster parameters</a>.</p>
            access_policies: <p>Identity and Access Management (IAM) access policy as a JSON-formatted string.</p>
            ip_address_type: <p>Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If your IP address type is currently set to dual stack, you can't change it. </p>
            log_publishing_options: <p>Options to publish OpenSearch logs to Amazon CloudWatch Logs.</p>
            encryption_at_rest_options: <p>Encryption at rest options for the domain.</p>
            domain_endpoint_options: <p>Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.</p>
            node_to_node_encryption_options: <p>Node-to-node encryption options for the domain.</p>
            advanced_security_options: <p>Options for fine-grained access control.</p>
            auto_tune_options: <p>Options for Auto-Tune.</p>
            dry_run: <p>This flag, when set to True, specifies whether the <code>UpdateDomain</code> request should return the results of a dry run analysis without actually applying the change. A dry run determines what type of deployment the update will cause.</p>
            dry_run_mode: <p>The type of dry run to perform.</p> <ul> <li> <p> <code>Basic</code> only returns the type of deployment (blue/green or dynamic) that the update will cause.</p> </li> <li> <p> <code>Verbose</code> runs an additional check to validate the changes you're making. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check\">Validating a domain update</a>.</p> </li> </ul>
            off_peak_window_options: <p>Off-peak window options for the domain.</p>
            software_update_options: <p>Service software update options for the domain.</p>
            aiml_options: <p>Options for all machine learning features for the specified domain.</p>
            deployment_strategy_options: <p>Specifies the deployment strategy options for the domain.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_domain_config_request.UpdateDomainConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_domain_config_response.UpdateDomainConfigResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_domain_config

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_domain_config.async_update_domain_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_domain_config_request.UpdateDomainConfigRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        if cluster_config is not None:
            input_["cluster_config"] = cluster_config
        if ebs_options is not None:
            input_["ebs_options"] = ebs_options
        if snapshot_options is not None:
            input_["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input_["vpc_options"] = vpc_options
        if cognito_options is not None:
            input_["cognito_options"] = cognito_options
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options
        if access_policies is not None:
            input_["access_policies"] = access_policies
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if log_publishing_options is not None:
            input_["log_publishing_options"] = log_publishing_options
        if encryption_at_rest_options is not None:
            input_["encryption_at_rest_options"] = encryption_at_rest_options
        if domain_endpoint_options is not None:
            input_["domain_endpoint_options"] = domain_endpoint_options
        if node_to_node_encryption_options is not None:
            input_["node_to_node_encryption_options"] = node_to_node_encryption_options
        if advanced_security_options is not None:
            input_["advanced_security_options"] = advanced_security_options
        if identity_center_options is not None:
            input_["identity_center_options"] = identity_center_options
        if auto_tune_options is not None:
            input_["auto_tune_options"] = auto_tune_options
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if dry_run_mode is not None:
            input_["dry_run_mode"] = dry_run_mode
        if off_peak_window_options is not None:
            input_["off_peak_window_options"] = off_peak_window_options
        if software_update_options is not None:
            input_["software_update_options"] = software_update_options
        if aiml_options is not None:
            input_["aiml_options"] = aiml_options
        if deployment_strategy_options is not None:
            input_["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input_["automated_snapshot_pause_options"] = (
                automated_snapshot_pause_options
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_index(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        index_name: "aws_sdk_opensearch.types.index_name.IndexName",
        index_schema: "aws_sdk_opensearch.types.index_schema.IndexSchema",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.update_index_response.UpdateIndexResponse":
        """<p>Updates an existing OpenSearch index schema and semantic enrichment configuration. This operation allows modification of field mappings and semantic search settings for text fields. Changes to semantic enrichment configuration will apply to newly ingested documents.</p>

        Args:
            index_name: <p>The name of the index to update.</p>
            index_schema: <p>The updated JSON schema for the index including any changes to mappings, settings, and semantic enrichment configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_index_request.UpdateIndexRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_index_response.UpdateIndexResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_index

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_index.async_update_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_index_request.UpdateIndexRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["index_name"] = index_name
        input_["index_schema"] = index_schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_package(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        package_source: "aws_sdk_opensearch.types.package_source.PackageSource",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        package_description: Optional[
            "aws_sdk_opensearch.types.package_description.PackageDescription"
        ] = None,
        commit_message: Optional[
            "aws_sdk_opensearch.types.commit_message.CommitMessage"
        ] = None,
        package_configuration: Optional[
            "aws_sdk_opensearch.types.package_configuration.PackageConfiguration"
        ] = None,
        package_encryption_options: Optional[
            "aws_sdk_opensearch.types.package_encryption_options.PackageEncryptionOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.update_package_response.UpdatePackageResponse":
        r"""<p>Updates a package for use with Amazon OpenSearch Service domains. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html\">Custom packages for Amazon OpenSearch Service</a>.</p>

        Args:
            package_id: <p>The unique identifier for the package.</p>
            package_source: <p>Amazon S3 bucket and key for the package.</p>
            package_description: <p>A new description of the package.</p>
            commit_message: <p>Commit message for the updated file, which is shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>
            package_configuration: <p>The updated configuration details for a package.</p>
            package_encryption_options: <p>Encryption options for a package.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_package_request.UpdatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_package_response.UpdatePackageResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_package

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_package.async_update_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_package_request.UpdatePackageRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        input_["package_source"] = package_source
        if package_description is not None:
            input_["package_description"] = package_description
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if package_configuration is not None:
            input_["package_configuration"] = package_configuration
        if package_encryption_options is not None:
            input_["package_encryption_options"] = package_encryption_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_package_scope(
        self,
        package_id: "aws_sdk_opensearch.types.package_id.PackageID",
        operation: "aws_sdk_opensearch.types.package_scope_operation_enum.PackageScopeOperationEnum",
        package_user_list: "aws_sdk_opensearch.types.package_user_list.PackageUserList",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.update_package_scope_response.UpdatePackageScopeResponse":
        """<p>Updates the scope of a package. Scope of the package defines users who can view and associate a package.</p>

        Args:
            package_id: <p>ID of the package whose scope is being updated.</p>
            operation: <p> The operation to perform on the package scope (e.g., add/remove/override users).</p>
            package_user_list: <p> List of users to be added or removed from the package scope.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_package_scope_request.UpdatePackageScopeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_package_scope_response.UpdatePackageScopeResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_package_scope

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_package_scope.async_update_package_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_package_scope_request.UpdatePackageScopeRequest = {}  # type: ignore[typeddict-item]
        input_["package_id"] = package_id
        input_["operation"] = operation
        input_["package_user_list"] = package_user_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_scheduled_action(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        action_id: "aws_sdk_opensearch.types.string.String",
        action_type: "aws_sdk_opensearch.types.action_type.ActionType",
        schedule_at: "aws_sdk_opensearch.types.schedule_at.ScheduleAt",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        desired_start_time: Optional["aws_sdk_opensearch.types.long.Long"] = None,
    ) -> "aws_sdk_opensearch.types.update_scheduled_action_response.UpdateScheduledActionResponse":
        r"""<p>Reschedules a planned domain configuration change for a later time. This change can be a scheduled <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html\">service software update</a> or a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html#auto-tune-types\">blue/green Auto-Tune enhancement</a>.</p>

        Args:
            domain_name: <p>The name of the domain to reschedule an action for.</p>
            action_id: <p>The unique identifier of the action to reschedule. To retrieve this ID, send a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html\">ListScheduledActions</a> request.</p>
            action_type: <p>The type of action to reschedule. Can be one of <code>SERVICE_SOFTWARE_UPDATE</code>, <code>JVM_HEAP_SIZE_TUNING</code>, or <code>JVM_YOUNG_GEN_TUNING</code>. To retrieve this value, send a <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html\">ListScheduledActions</a> request.</p>
            schedule_at: <p>When to schedule the action.</p> <ul> <li> <p> <code>NOW</code> - Immediately schedules the update to happen in the current hour if there's capacity available.</p> </li> <li> <p> <code>TIMESTAMP</code> - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for <code>DesiredStartTime</code>.</p> </li> <li> <p> <code>OFF_PEAK_WINDOW</code> - Marks the action to be picked up during an upcoming off-peak window. There's no guarantee that the change will be implemented during the next immediate window. Depending on capacity, it might happen in subsequent days.</p> </li> </ul>
            desired_start_time: <p>The time to implement the change, in Coordinated Universal Time (UTC). Only specify this parameter if you set <code>ScheduleAt</code> to <code>TIMESTAMP</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_scheduled_action_request.UpdateScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_scheduled_action_response.UpdateScheduledActionResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_scheduled_action

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_scheduled_action.async_update_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_scheduled_action_request.UpdateScheduledActionRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["action_id"] = action_id
        input_["action_type"] = action_type
        input_["schedule_at"] = schedule_at
        if desired_start_time is not None:
            input_["desired_start_time"] = desired_start_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_vpc_endpoint(
        self,
        vpc_endpoint_id: "aws_sdk_opensearch.types.vpc_endpoint_id.VpcEndpointId",
        vpc_options: "aws_sdk_opensearch.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
    ) -> "aws_sdk_opensearch.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        """<p>Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>The unique identifier of the endpoint.</p>
            vpc_options: <p>The security groups and/or subnets to add, remove, or modify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.update_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.update_vpc_endpoint.async_update_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_endpoint_id"] = vpc_endpoint_id
        input_["vpc_options"] = vpc_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_domain(
        self,
        domain_name: "aws_sdk_opensearch.types.domain_name.DomainName",
        target_version: "aws_sdk_opensearch.types.version_string.VersionString",
        *,
        config_overrides: Optional[AsyncOpenSearchClientConfig] = None,
        perform_check_only: Optional["aws_sdk_opensearch.types.boolean.Boolean"] = None,
        advanced_options: Optional[
            "aws_sdk_opensearch.types.advanced_options.AdvancedOptions"
        ] = None,
    ) -> "aws_sdk_opensearch.types.upgrade_domain_response.UpgradeDomainResponse":
        """<p>Allows you to either upgrade your Amazon OpenSearch Service domain or perform an upgrade eligibility check to a compatible version of OpenSearch or Elasticsearch.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain that you want to upgrade.</p>
            target_version: <p>OpenSearch or Elasticsearch version to which you want to upgrade, in the format Opensearch_X.Y or Elasticsearch_X.Y.</p>
            perform_check_only: <p>When true, indicates that an upgrade eligibility check needs to be performed. Does not actually perform the upgrade.</p>
            advanced_options: <p>Only supports the <code>override_main_response_version</code> parameter and not other advanced options. You can only include this option when upgrading to an OpenSearch version. Specifies whether the domain reports its version as 7.10 so that it continues to work with Elasticsearch OSS clients and plugins.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearch.types.upgrade_domain_request.UpgradeDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearch.types.upgrade_domain_response.UpgradeDomainResponse"
        ]:
            import aws_sdk_opensearch._operations.amazon_open_search_service.upgrade_domain

            (
                output,
                http_response,
            ) = await aws_sdk_opensearch._operations.amazon_open_search_service.upgrade_domain.async_upgrade_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_opensearch.types.upgrade_domain_request.UpgradeDomainRequest = {}  # type: ignore[typeddict-item]
        input_["domain_name"] = domain_name
        input_["target_version"] = target_version
        if perform_check_only is not None:
            input_["perform_check_only"] = perform_check_only
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
