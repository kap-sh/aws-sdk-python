"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AmazonElasticsearchService2015``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_elasticsearch_service._auth._signers
import aws_sdk_elasticsearch_service._auth._sigv4
from aws_sdk_elasticsearch_service._auth._identity import Credentials
from aws_sdk_elasticsearch_service._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_elasticsearch_service._auth._zapros_handler import AuthMiddleware
from aws_sdk_elasticsearch_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_request
    import aws_sdk_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_response
    import aws_sdk_elasticsearch_service.types.add_tags_request
    import aws_sdk_elasticsearch_service.types.advanced_options
    import aws_sdk_elasticsearch_service.types.advanced_security_options_input
    import aws_sdk_elasticsearch_service.types.arn
    import aws_sdk_elasticsearch_service.types.associate_package_request
    import aws_sdk_elasticsearch_service.types.associate_package_response
    import aws_sdk_elasticsearch_service.types.authorize_vpc_endpoint_access_request
    import aws_sdk_elasticsearch_service.types.authorize_vpc_endpoint_access_response
    import aws_sdk_elasticsearch_service.types.auto_tune_options
    import aws_sdk_elasticsearch_service.types.auto_tune_options_input
    import aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options
    import aws_sdk_elasticsearch_service.types.aws_account
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.cancel_domain_config_change_request
    import aws_sdk_elasticsearch_service.types.cancel_domain_config_change_response
    import aws_sdk_elasticsearch_service.types.cancel_elasticsearch_service_software_update_request
    import aws_sdk_elasticsearch_service.types.cancel_elasticsearch_service_software_update_response
    import aws_sdk_elasticsearch_service.types.client_token
    import aws_sdk_elasticsearch_service.types.cognito_options
    import aws_sdk_elasticsearch_service.types.commit_message
    import aws_sdk_elasticsearch_service.types.connection_alias
    import aws_sdk_elasticsearch_service.types.create_elasticsearch_domain_request
    import aws_sdk_elasticsearch_service.types.create_elasticsearch_domain_response
    import aws_sdk_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_request
    import aws_sdk_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_response
    import aws_sdk_elasticsearch_service.types.create_package_request
    import aws_sdk_elasticsearch_service.types.create_package_response
    import aws_sdk_elasticsearch_service.types.create_vpc_endpoint_request
    import aws_sdk_elasticsearch_service.types.create_vpc_endpoint_response
    import aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id
    import aws_sdk_elasticsearch_service.types.delete_elasticsearch_domain_request
    import aws_sdk_elasticsearch_service.types.delete_elasticsearch_domain_response
    import aws_sdk_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_request
    import aws_sdk_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_response
    import aws_sdk_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_request
    import aws_sdk_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_response
    import aws_sdk_elasticsearch_service.types.delete_package_request
    import aws_sdk_elasticsearch_service.types.delete_package_response
    import aws_sdk_elasticsearch_service.types.delete_vpc_endpoint_request
    import aws_sdk_elasticsearch_service.types.delete_vpc_endpoint_response
    import aws_sdk_elasticsearch_service.types.deployment_strategy_options
    import aws_sdk_elasticsearch_service.types.describe_domain_auto_tunes_request
    import aws_sdk_elasticsearch_service.types.describe_domain_auto_tunes_response
    import aws_sdk_elasticsearch_service.types.describe_domain_change_progress_request
    import aws_sdk_elasticsearch_service.types.describe_domain_change_progress_response
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_config_request
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_config_response
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_request
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_response
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_domains_request
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_domains_response
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_request
    import aws_sdk_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_response
    import aws_sdk_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_request
    import aws_sdk_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response
    import aws_sdk_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_request
    import aws_sdk_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response
    import aws_sdk_elasticsearch_service.types.describe_packages_filter_list
    import aws_sdk_elasticsearch_service.types.describe_packages_request
    import aws_sdk_elasticsearch_service.types.describe_packages_response
    import aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_request
    import aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response
    import aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instances_request
    import aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response
    import aws_sdk_elasticsearch_service.types.describe_vpc_endpoints_request
    import aws_sdk_elasticsearch_service.types.describe_vpc_endpoints_response
    import aws_sdk_elasticsearch_service.types.dissociate_package_request
    import aws_sdk_elasticsearch_service.types.dissociate_package_response
    import aws_sdk_elasticsearch_service.types.domain_arn
    import aws_sdk_elasticsearch_service.types.domain_endpoint_options
    import aws_sdk_elasticsearch_service.types.domain_information
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.domain_name_list
    import aws_sdk_elasticsearch_service.types.dry_run
    import aws_sdk_elasticsearch_service.types.ebs_options
    import aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_string
    import aws_sdk_elasticsearch_service.types.encryption_at_rest_options
    import aws_sdk_elasticsearch_service.types.engine_type
    import aws_sdk_elasticsearch_service.types.es_partition_instance_type
    import aws_sdk_elasticsearch_service.types.filter_list
    import aws_sdk_elasticsearch_service.types.get_compatible_elasticsearch_versions_request
    import aws_sdk_elasticsearch_service.types.get_compatible_elasticsearch_versions_response
    import aws_sdk_elasticsearch_service.types.get_package_version_history_request
    import aws_sdk_elasticsearch_service.types.get_package_version_history_response
    import aws_sdk_elasticsearch_service.types.get_upgrade_history_request
    import aws_sdk_elasticsearch_service.types.get_upgrade_history_response
    import aws_sdk_elasticsearch_service.types.get_upgrade_status_request
    import aws_sdk_elasticsearch_service.types.get_upgrade_status_response
    import aws_sdk_elasticsearch_service.types.guid
    import aws_sdk_elasticsearch_service.types.instance_count
    import aws_sdk_elasticsearch_service.types.list_domain_names_request
    import aws_sdk_elasticsearch_service.types.list_domain_names_response
    import aws_sdk_elasticsearch_service.types.list_domains_for_package_request
    import aws_sdk_elasticsearch_service.types.list_domains_for_package_response
    import aws_sdk_elasticsearch_service.types.list_elasticsearch_instance_types_request
    import aws_sdk_elasticsearch_service.types.list_elasticsearch_instance_types_response
    import aws_sdk_elasticsearch_service.types.list_elasticsearch_versions_request
    import aws_sdk_elasticsearch_service.types.list_elasticsearch_versions_response
    import aws_sdk_elasticsearch_service.types.list_packages_for_domain_request
    import aws_sdk_elasticsearch_service.types.list_packages_for_domain_response
    import aws_sdk_elasticsearch_service.types.list_tags_request
    import aws_sdk_elasticsearch_service.types.list_tags_response
    import aws_sdk_elasticsearch_service.types.list_vpc_endpoint_access_request
    import aws_sdk_elasticsearch_service.types.list_vpc_endpoint_access_response
    import aws_sdk_elasticsearch_service.types.list_vpc_endpoints_for_domain_request
    import aws_sdk_elasticsearch_service.types.list_vpc_endpoints_for_domain_response
    import aws_sdk_elasticsearch_service.types.list_vpc_endpoints_request
    import aws_sdk_elasticsearch_service.types.list_vpc_endpoints_response
    import aws_sdk_elasticsearch_service.types.log_publishing_options
    import aws_sdk_elasticsearch_service.types.max_results
    import aws_sdk_elasticsearch_service.types.next_token
    import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options
    import aws_sdk_elasticsearch_service.types.package_description
    import aws_sdk_elasticsearch_service.types.package_id
    import aws_sdk_elasticsearch_service.types.package_name
    import aws_sdk_elasticsearch_service.types.package_source
    import aws_sdk_elasticsearch_service.types.package_type
    import aws_sdk_elasticsearch_service.types.policy_document
    import aws_sdk_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_request
    import aws_sdk_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_response
    import aws_sdk_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_request
    import aws_sdk_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_response
    import aws_sdk_elasticsearch_service.types.remove_tags_request
    import aws_sdk_elasticsearch_service.types.reservation_token
    import aws_sdk_elasticsearch_service.types.revoke_vpc_endpoint_access_request
    import aws_sdk_elasticsearch_service.types.revoke_vpc_endpoint_access_response
    import aws_sdk_elasticsearch_service.types.snapshot_options
    import aws_sdk_elasticsearch_service.types.start_elasticsearch_service_software_update_request
    import aws_sdk_elasticsearch_service.types.start_elasticsearch_service_software_update_response
    import aws_sdk_elasticsearch_service.types.string_list
    import aws_sdk_elasticsearch_service.types.tag_list
    import aws_sdk_elasticsearch_service.types.update_elasticsearch_domain_config_request
    import aws_sdk_elasticsearch_service.types.update_elasticsearch_domain_config_response
    import aws_sdk_elasticsearch_service.types.update_package_request
    import aws_sdk_elasticsearch_service.types.update_package_response
    import aws_sdk_elasticsearch_service.types.update_vpc_endpoint_request
    import aws_sdk_elasticsearch_service.types.update_vpc_endpoint_response
    import aws_sdk_elasticsearch_service.types.upgrade_elasticsearch_domain_request
    import aws_sdk_elasticsearch_service.types.upgrade_elasticsearch_domain_response
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_id
    import aws_sdk_elasticsearch_service.types.vpc_endpoint_id_list
    import aws_sdk_elasticsearch_service.types.vpc_options


class AsyncElasticsearchServiceClientConfig(TypedDict, total=False):
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


class AsyncElasticsearchServiceClient:
    """A client for the ``ElasticsearchService`` service.

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
        self.config = AsyncElasticsearchServiceClientConfig(
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
        self, config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncElasticsearchServiceClientConfig = config_overrides or {}
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

    async def accept_inbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_response.AcceptInboundCrossClusterSearchConnectionResponse":
        """<p>Allows the destination domain owner to accept an inbound cross-cluster search connection request.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the inbound connection that you want to accept.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_request.AcceptInboundCrossClusterSearchConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_response.AcceptInboundCrossClusterSearchConnectionResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.accept_inbound_cross_cluster_search_connection

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.accept_inbound_cross_cluster_search_connection.async_accept_inbound_cross_cluster_search_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.accept_inbound_cross_cluster_search_connection_request.AcceptInboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
        input["cross_cluster_search_connection_id"] = cross_cluster_search_connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def add_tags(
        self,
        arn: "aws_sdk_elasticsearch_service.types.arn.ARN",
        tag_list: "aws_sdk_elasticsearch_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> None:
        """<p>Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-awsresorcetagging\" target=\"_blank\"> Tagging Amazon Elasticsearch Service Domains for more information.</a></p>

        Args:
            arn: <p> Specify the <code>ARN</code> for which you want to add the tags.</p>
            tag_list: <p> List of <code>Tag</code> that need to be added for the Elasticsearch domain. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.add_tags_request.AddTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.add_tags

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.add_tags.async_add_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.add_tags_request.AddTagsRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["tag_list"] = tag_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_package(
        self,
        package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID",
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.associate_package_response.AssociatePackageResponse":
        """<p>Associates a package with an Amazon ES domain.</p>

        Args:
            package_id: <p>Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.</p>
            domain_name: <p>Name of the domain that you want to associate the package with.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.associate_package_request.AssociatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.associate_package_response.AssociatePackageResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.associate_package

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.associate_package.async_associate_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.associate_package_request.AssociatePackageRequest = {}  # type: ignore[typeddict-item]
        input["package_id"] = package_id
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def authorize_vpc_endpoint_access(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        account: "aws_sdk_elasticsearch_service.types.aws_account.AWSAccount",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse":
        """<p>Provides access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to provide access to.</p>
            account: <p>The account ID to grant access to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.authorize_vpc_endpoint_access_response.AuthorizeVpcEndpointAccessResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.authorize_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.authorize_vpc_endpoint_access.async_authorize_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.authorize_vpc_endpoint_access_request.AuthorizeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["account"] = account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_domain_config_change(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        dry_run: Optional["aws_sdk_elasticsearch_service.types.dry_run.DryRun"] = None,
    ) -> "aws_sdk_elasticsearch_service.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse":
        """<p>Cancels a pending configuration change on an Amazon OpenSearch Service domain.</p>

        Args:
            domain_name: <p>Name of the OpenSearch Service domain configuration request to cancel.</p>
            dry_run: <p>When set to <b>True</b>, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.cancel_domain_config_change_response.CancelDomainConfigChangeResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_domain_config_change

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_domain_config_change.async_cancel_domain_config_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.cancel_domain_config_change_request.CancelDomainConfigChangeRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_elasticsearch_service_software_update(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.cancel_elasticsearch_service_software_update_response.CancelElasticsearchServiceSoftwareUpdateResponse":
        """<p>Cancels a scheduled service software update for an Amazon ES domain. You can only perform this operation before the <code>AutomatedUpdateDate</code> and when the <code>UpdateStatus</code> is in the <code>PENDING_UPDATE</code> state.</p>

        Args:
            domain_name: <p>The name of the domain that you want to stop the latest service software update on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.cancel_elasticsearch_service_software_update_request.CancelElasticsearchServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.cancel_elasticsearch_service_software_update_response.CancelElasticsearchServiceSoftwareUpdateResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_elasticsearch_service_software_update

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.cancel_elasticsearch_service_software_update.async_cancel_elasticsearch_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.cancel_elasticsearch_service_software_update_request.CancelElasticsearchServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_elasticsearch_domain(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        elasticsearch_version: Optional[
            "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
        ] = None,
        elasticsearch_cluster_config: Optional[
            "aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
        ] = None,
        ebs_options: Optional[
            "aws_sdk_elasticsearch_service.types.ebs_options.EBSOptions"
        ] = None,
        access_policies: Optional[
            "aws_sdk_elasticsearch_service.types.policy_document.PolicyDocument"
        ] = None,
        snapshot_options: Optional[
            "aws_sdk_elasticsearch_service.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional[
            "aws_sdk_elasticsearch_service.types.vpc_options.VPCOptions"
        ] = None,
        cognito_options: Optional[
            "aws_sdk_elasticsearch_service.types.cognito_options.CognitoOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "aws_sdk_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        node_to_node_encryption_options: Optional[
            "aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        advanced_options: Optional[
            "aws_sdk_elasticsearch_service.types.advanced_options.AdvancedOptions"
        ] = None,
        log_publishing_options: Optional[
            "aws_sdk_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "aws_sdk_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        advanced_security_options: Optional[
            "aws_sdk_elasticsearch_service.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        auto_tune_options: Optional[
            "aws_sdk_elasticsearch_service.types.auto_tune_options_input.AutoTuneOptionsInput"
        ] = None,
        tag_list: Optional[
            "aws_sdk_elasticsearch_service.types.tag_list.TagList"
        ] = None,
        deployment_strategy_options: Optional[
            "aws_sdk_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.create_elasticsearch_domain_response.CreateElasticsearchDomainResponse":
        """<p>Creates a new Elasticsearch domain. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains\" target=\"_blank\">Creating Elasticsearch Domains</a> in the <i>Amazon Elasticsearch Service Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain that you are creating. Domain names are unique across the domains owned by an account within an AWS region. Domain names must start with a lowercase letter and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).</p>
            elasticsearch_version: <p>String of format X.Y to specify version for the Elasticsearch domain eg. \"1.5\" or \"2.3\". For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains\" target=\"_blank\">Creating Elasticsearch Domains</a> in the <i>Amazon Elasticsearch Service Developer Guide</i>.</p>
            elasticsearch_cluster_config: <p>Configuration options for an Elasticsearch domain. Specifies the instance type and number of instances in the domain cluster. </p>
            ebs_options: <p>Options to enable, disable and specify the type and size of EBS storage volumes. </p>
            access_policies: <p> IAM access policy as a JSON-formatted string.</p>
            snapshot_options: <p>Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours. </p>
            vpc_options: <p>Options to specify the subnets and security groups for VPC endpoint. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc\" target=\"_blank\">Creating a VPC</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i></p>
            cognito_options: <p>Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html\" target=\"_blank\">Amazon Cognito Authentication for Kibana</a>.</p>
            encryption_at_rest_options: <p>Specifies the Encryption At Rest Options.</p>
            node_to_node_encryption_options: <p>Specifies the NodeToNodeEncryptionOptions.</p>
            advanced_options: <p> Option to allow references to indices in an HTTP request body. Must be <code>false</code> when configuring access to individual sub-resources. By default, the value is <code>true</code>. See <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options\" target=\"_blank\">Configuration Advanced Options</a> for more information.</p>
            log_publishing_options: <p>Map of <code>LogType</code> and <code>LogPublishingOption</code>, each containing options to publish a given type of Elasticsearch log.</p>
            domain_endpoint_options: <p>Options to specify configuration that will be applied to the domain endpoint.</p>
            advanced_security_options: <p>Specifies advanced security options.</p>
            auto_tune_options: <p>Specifies Auto-Tune options.</p>
            tag_list: <p>A list of <code>Tag</code> added during domain creation.</p>
            deployment_strategy_options: <p>Specifies the deployment strategy options.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.create_elasticsearch_domain_request.CreateElasticsearchDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.create_elasticsearch_domain_response.CreateElasticsearchDomainResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_elasticsearch_domain

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_elasticsearch_domain.async_create_elasticsearch_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.create_elasticsearch_domain_request.CreateElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if elasticsearch_version is not None:
            input["elasticsearch_version"] = elasticsearch_version
        if elasticsearch_cluster_config is not None:
            input["elasticsearch_cluster_config"] = elasticsearch_cluster_config
        if ebs_options is not None:
            input["ebs_options"] = ebs_options
        if access_policies is not None:
            input["access_policies"] = access_policies
        if snapshot_options is not None:
            input["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input["vpc_options"] = vpc_options
        if cognito_options is not None:
            input["cognito_options"] = cognito_options
        if encryption_at_rest_options is not None:
            input["encryption_at_rest_options"] = encryption_at_rest_options
        if node_to_node_encryption_options is not None:
            input["node_to_node_encryption_options"] = node_to_node_encryption_options
        if advanced_options is not None:
            input["advanced_options"] = advanced_options
        if log_publishing_options is not None:
            input["log_publishing_options"] = log_publishing_options
        if domain_endpoint_options is not None:
            input["domain_endpoint_options"] = domain_endpoint_options
        if advanced_security_options is not None:
            input["advanced_security_options"] = advanced_security_options
        if auto_tune_options is not None:
            input["auto_tune_options"] = auto_tune_options
        if tag_list is not None:
            input["tag_list"] = tag_list
        if deployment_strategy_options is not None:
            input["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input["automated_snapshot_pause_options"] = automated_snapshot_pause_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_outbound_cross_cluster_search_connection(
        self,
        source_domain_info: "aws_sdk_elasticsearch_service.types.domain_information.DomainInformation",
        destination_domain_info: "aws_sdk_elasticsearch_service.types.domain_information.DomainInformation",
        connection_alias: "aws_sdk_elasticsearch_service.types.connection_alias.ConnectionAlias",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_response.CreateOutboundCrossClusterSearchConnectionResponse":
        """<p>Creates a new cross-cluster search connection from a source domain to a destination domain.</p>

        Args:
            source_domain_info: <p>Specifies the <code><a>DomainInformation</a></code> for the source Elasticsearch domain.</p>
            destination_domain_info: <p>Specifies the <code><a>DomainInformation</a></code> for the destination Elasticsearch domain.</p>
            connection_alias: <p>Specifies the connection alias that will be used by the customer for this connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_request.CreateOutboundCrossClusterSearchConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_response.CreateOutboundCrossClusterSearchConnectionResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_outbound_cross_cluster_search_connection

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_outbound_cross_cluster_search_connection.async_create_outbound_cross_cluster_search_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.create_outbound_cross_cluster_search_connection_request.CreateOutboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
        input["source_domain_info"] = source_domain_info
        input["destination_domain_info"] = destination_domain_info
        input["connection_alias"] = connection_alias

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_package(
        self,
        package_name: "aws_sdk_elasticsearch_service.types.package_name.PackageName",
        package_type: "aws_sdk_elasticsearch_service.types.package_type.PackageType",
        package_source: "aws_sdk_elasticsearch_service.types.package_source.PackageSource",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        package_description: Optional[
            "aws_sdk_elasticsearch_service.types.package_description.PackageDescription"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.create_package_response.CreatePackageResponse":
        """<p>Create a package for use with Amazon ES domains.</p>

        Args:
            package_name: <p>Unique identifier for the package.</p>
            package_type: <p>Type of package. Currently supports only TXT-DICTIONARY.</p>
            package_description: <p>Description of the package.</p>
            package_source: <p>The customer S3 location <code>PackageSource</code> for importing the package.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.create_package_request.CreatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.create_package_response.CreatePackageResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_package

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_package.async_create_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.create_package_request.CreatePackageRequest = {}  # type: ignore[typeddict-item]
        input["package_name"] = package_name
        input["package_type"] = package_type
        if package_description is not None:
            input["package_description"] = package_description
        input["package_source"] = package_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_vpc_endpoint(
        self,
        domain_arn: "aws_sdk_elasticsearch_service.types.domain_arn.DomainArn",
        vpc_options: "aws_sdk_elasticsearch_service.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        client_token: Optional[
            "aws_sdk_elasticsearch_service.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an Amazon OpenSearch Service-managed VPC endpoint.</p>

        Args:
            domain_arn: <p>The Amazon Resource Name (ARN) of the domain to grant access to.</p>
            vpc_options: <p>Options to specify the subnets and security groups for the endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.create_vpc_endpoint.async_create_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input["domain_arn"] = domain_arn
        input["vpc_options"] = vpc_options
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_elasticsearch_domain(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.delete_elasticsearch_domain_response.DeleteElasticsearchDomainResponse":
        """<p>Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.</p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain that you want to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.delete_elasticsearch_domain_request.DeleteElasticsearchDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.delete_elasticsearch_domain_response.DeleteElasticsearchDomainResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_domain

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_domain.async_delete_elasticsearch_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.delete_elasticsearch_domain_request.DeleteElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_elasticsearch_service_role(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> None:
        """<p>Deletes the service-linked role that Elasticsearch Service uses to manage and maintain VPC domains. Role deletion will fail if any existing VPC domains use the role. You must delete any such Elasticsearch domains before deleting the role. See <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-enabling-slr\" target=\"_blank\">Deleting Elasticsearch Service Role</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_service_role

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_elasticsearch_service_role.async_delete_elasticsearch_service_role(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_inbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_response.DeleteInboundCrossClusterSearchConnectionResponse":
        """<p>Allows the destination domain owner to delete an existing inbound cross-cluster search connection.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the inbound connection that you want to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_request.DeleteInboundCrossClusterSearchConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_response.DeleteInboundCrossClusterSearchConnectionResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_inbound_cross_cluster_search_connection

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_inbound_cross_cluster_search_connection.async_delete_inbound_cross_cluster_search_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.delete_inbound_cross_cluster_search_connection_request.DeleteInboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
        input["cross_cluster_search_connection_id"] = cross_cluster_search_connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_outbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_response.DeleteOutboundCrossClusterSearchConnectionResponse":
        """<p>Allows the source domain owner to delete an existing outbound cross-cluster search connection.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the outbound connection that you want to permanently delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_request.DeleteOutboundCrossClusterSearchConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_response.DeleteOutboundCrossClusterSearchConnectionResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_outbound_cross_cluster_search_connection

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_outbound_cross_cluster_search_connection.async_delete_outbound_cross_cluster_search_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.delete_outbound_cross_cluster_search_connection_request.DeleteOutboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
        input["cross_cluster_search_connection_id"] = cross_cluster_search_connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_package(
        self,
        package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.delete_package_response.DeletePackageResponse":
        """<p>Delete the package.</p>

        Args:
            package_id: <p>Internal ID of the package that you want to delete. Use <code>DescribePackages</code> to find this value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.delete_package_request.DeletePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.delete_package_response.DeletePackageResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_package

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_package.async_delete_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.delete_package_request.DeletePackageRequest = {}  # type: ignore[typeddict-item]
        input["package_id"] = package_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_vpc_endpoint(
        self,
        vpc_endpoint_id: "aws_sdk_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>The unique identifier of the endpoint to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.delete_vpc_endpoint.async_delete_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input["vpc_endpoint_id"] = vpc_endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_domain_auto_tunes(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse":
        """<p>Provides scheduled Auto-Tune action details for the Elasticsearch domain, such as Auto-Tune action type, description, severity, and scheduled date.</p>

        Args:
            domain_name: <p>Specifies the domain name for which you want Auto-Tune action details.</p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p>NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_domain_auto_tunes_response.DescribeDomainAutoTunesResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_auto_tunes

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_auto_tunes.async_describe_domain_auto_tunes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_domain_auto_tunes_request.DescribeDomainAutoTunesRequest = {}  # type: ignore[typeddict-item]
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

    async def describe_domain_change_progress(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        change_id: Optional["aws_sdk_elasticsearch_service.types.guid.GUID"] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse":
        """<p>Returns information about the current blue/green deployment happening on a domain, including a change ID, status, and progress stages.</p>

        Args:
            domain_name: <p>The domain you want to get the progress information about.</p>
            change_id: <p>The specific change ID for which you want to get progress information. This is an optional parameter. If omitted, the service returns information about the most recent configuration change. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_domain_change_progress_response.DescribeDomainChangeProgressResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_change_progress

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_domain_change_progress.async_describe_domain_change_progress(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_domain_change_progress_request.DescribeDomainChangeProgressRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if change_id is not None:
            input["change_id"] = change_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_elasticsearch_domain(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_response.DescribeElasticsearchDomainResponse":
        """<p>Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.</p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain for which you want information.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_request.DescribeElasticsearchDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_response.DescribeElasticsearchDomainResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain.async_describe_elasticsearch_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_request.DescribeElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_elasticsearch_domain_config(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_config_response.DescribeElasticsearchDomainConfigResponse":
        """<p>Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.</p>

        Args:
            domain_name: <p>The Elasticsearch domain that you want to get information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_config_request.DescribeElasticsearchDomainConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_config_response.DescribeElasticsearchDomainConfigResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain_config

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domain_config.async_describe_elasticsearch_domain_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_elasticsearch_domain_config_request.DescribeElasticsearchDomainConfigRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_elasticsearch_domains(
        self,
        domain_names: "aws_sdk_elasticsearch_service.types.domain_name_list.DomainNameList",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_elasticsearch_domains_response.DescribeElasticsearchDomainsResponse":
        """<p>Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.</p>

        Args:
            domain_names: <p>The Elasticsearch domains for which you want information.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_elasticsearch_domains_request.DescribeElasticsearchDomainsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_elasticsearch_domains_response.DescribeElasticsearchDomainsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domains

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_domains.async_describe_elasticsearch_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_elasticsearch_domains_request.DescribeElasticsearchDomainsRequest = {}  # type: ignore[typeddict-item]
        input["domain_names"] = domain_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_elasticsearch_instance_type_limits(
        self,
        instance_type: "aws_sdk_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType",
        elasticsearch_version: "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_response.DescribeElasticsearchInstanceTypeLimitsResponse":
        """<p> Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the <code> <a>DomainName</a> </code> to know what Limits are supported for modifying. </p>

        Args:
            domain_name: <p> DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch <code> <a>Limits</a> </code> for existing domain. </p>
            instance_type: <p> The instance type for an Elasticsearch cluster for which Elasticsearch <code> <a>Limits</a> </code> are needed. </p>
            elasticsearch_version: <p> Version of Elasticsearch for which <code> <a>Limits</a> </code> are needed. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_request.DescribeElasticsearchInstanceTypeLimitsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_response.DescribeElasticsearchInstanceTypeLimitsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_instance_type_limits

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_elasticsearch_instance_type_limits.async_describe_elasticsearch_instance_type_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_elasticsearch_instance_type_limits_request.DescribeElasticsearchInstanceTypeLimitsRequest = {}  # type: ignore[typeddict-item]
        if domain_name is not None:
            input["domain_name"] = domain_name
        input["instance_type"] = instance_type
        input["elasticsearch_version"] = elasticsearch_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_inbound_cross_cluster_search_connections(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "aws_sdk_elasticsearch_service.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response.DescribeInboundCrossClusterSearchConnectionsResponse":
        """<p>Lists all the inbound cross-cluster search connections for a destination domain.</p>

        Args:
            filters: <p> A list of filters used to match properties for inbound cross-cluster search connection. Available <code><a>Filter</a></code> names for this operation are: <ul> <li>cross-cluster-search-connection-id</li> <li>source-domain-info.domain-name</li> <li>source-domain-info.owner-id</li> <li>source-domain-info.region</li> <li>destination-domain-info.domain-name</li> </ul> </p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p> NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_request.DescribeInboundCrossClusterSearchConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_response.DescribeInboundCrossClusterSearchConnectionsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_inbound_cross_cluster_search_connections

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_inbound_cross_cluster_search_connections.async_describe_inbound_cross_cluster_search_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_inbound_cross_cluster_search_connections_request.DescribeInboundCrossClusterSearchConnectionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
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

    async def describe_outbound_cross_cluster_search_connections(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "aws_sdk_elasticsearch_service.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response.DescribeOutboundCrossClusterSearchConnectionsResponse":
        """<p>Lists all the outbound cross-cluster search connections for a source domain.</p>

        Args:
            filters: <p> A list of filters used to match properties for outbound cross-cluster search connection. Available <code><a>Filter</a></code> names for this operation are: <ul> <li>cross-cluster-search-connection-id</li> <li>destination-domain-info.domain-name</li> <li>destination-domain-info.owner-id</li> <li>destination-domain-info.region</li> <li>source-domain-info.domain-name</li> </ul> </p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p> NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_request.DescribeOutboundCrossClusterSearchConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_response.DescribeOutboundCrossClusterSearchConnectionsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_outbound_cross_cluster_search_connections

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_outbound_cross_cluster_search_connections.async_describe_outbound_cross_cluster_search_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_outbound_cross_cluster_search_connections_request.DescribeOutboundCrossClusterSearchConnectionsRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
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

    async def describe_packages(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        filters: Optional[
            "aws_sdk_elasticsearch_service.types.describe_packages_filter_list.DescribePackagesFilterList"
        ] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_packages_response.DescribePackagesResponse":
        """<p>Describes all packages available to Amazon ES. Includes options for filtering, limiting the number of results, and pagination.</p>

        Args:
            filters: <p>Only returns packages that match the <code>DescribePackagesFilterList</code> values.</p>
            max_results: <p>Limits results to a maximum number of packages.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_packages_request.DescribePackagesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_packages_response.DescribePackagesResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_packages

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_packages.async_describe_packages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_packages_request.DescribePackagesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
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

    async def describe_reserved_elasticsearch_instance_offerings(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        reserved_elasticsearch_instance_offering_id: Optional[
            "aws_sdk_elasticsearch_service.types.guid.GUID"
        ] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response.DescribeReservedElasticsearchInstanceOfferingsResponse":
        """<p>Lists available reserved Elasticsearch instance offerings.</p>

        Args:
            reserved_elasticsearch_instance_offering_id: <p>The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.</p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_request.DescribeReservedElasticsearchInstanceOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_response.DescribeReservedElasticsearchInstanceOfferingsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instance_offerings

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instance_offerings.async_describe_reserved_elasticsearch_instance_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instance_offerings_request.DescribeReservedElasticsearchInstanceOfferingsRequest = {}  # type: ignore[typeddict-item]
        if reserved_elasticsearch_instance_offering_id is not None:
            input["reserved_elasticsearch_instance_offering_id"] = (
                reserved_elasticsearch_instance_offering_id
            )
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

    async def describe_reserved_elasticsearch_instances(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        reserved_elasticsearch_instance_id: Optional[
            "aws_sdk_elasticsearch_service.types.guid.GUID"
        ] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response.DescribeReservedElasticsearchInstancesResponse":
        """<p>Returns information about reserved Elasticsearch instances for this account.</p>

        Args:
            reserved_elasticsearch_instance_id: <p>The reserved instance identifier filter value. Use this parameter to show only the reservation that matches the specified reserved Elasticsearch instance ID.</p>
            max_results: <p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>
            next_token: <p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instances_request.DescribeReservedElasticsearchInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instances_response.DescribeReservedElasticsearchInstancesResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instances

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_reserved_elasticsearch_instances.async_describe_reserved_elasticsearch_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_reserved_elasticsearch_instances_request.DescribeReservedElasticsearchInstancesRequest = {}  # type: ignore[typeddict-item]
        if reserved_elasticsearch_instance_id is not None:
            input["reserved_elasticsearch_instance_id"] = (
                reserved_elasticsearch_instance_id
            )
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

    async def describe_vpc_endpoints(
        self,
        vpc_endpoint_ids: "aws_sdk_elasticsearch_service.types.vpc_endpoint_id_list.VpcEndpointIdList",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse":
        """<p>Describes one or more Amazon OpenSearch Service-managed VPC endpoints.</p>

        Args:
            vpc_endpoint_ids: <p>The unique identifiers of the endpoints to get information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.describe_vpc_endpoints_response.DescribeVpcEndpointsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_vpc_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.describe_vpc_endpoints.async_describe_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.describe_vpc_endpoints_request.DescribeVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
        input["vpc_endpoint_ids"] = vpc_endpoint_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def dissociate_package(
        self,
        package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID",
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.dissociate_package_response.DissociatePackageResponse":
        """<p>Dissociates a package from the Amazon ES domain.</p>

        Args:
            package_id: <p>Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.</p>
            domain_name: <p>Name of the domain that you want to associate the package with.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.dissociate_package_request.DissociatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.dissociate_package_response.DissociatePackageResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.dissociate_package

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.dissociate_package.async_dissociate_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.dissociate_package_request.DissociatePackageRequest = {}  # type: ignore[typeddict-item]
        input["package_id"] = package_id
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_compatible_elasticsearch_versions(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.get_compatible_elasticsearch_versions_response.GetCompatibleElasticsearchVersionsResponse":
        """<p> Returns a list of upgrade compatible Elastisearch versions. You can optionally pass a <code> <a>DomainName</a> </code> to get all upgrade compatible Elasticsearch versions for that specific domain. </p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.get_compatible_elasticsearch_versions_request.GetCompatibleElasticsearchVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.get_compatible_elasticsearch_versions_response.GetCompatibleElasticsearchVersionsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_compatible_elasticsearch_versions

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_compatible_elasticsearch_versions.async_get_compatible_elasticsearch_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.get_compatible_elasticsearch_versions_request.GetCompatibleElasticsearchVersionsRequest = {}  # type: ignore[typeddict-item]
        if domain_name is not None:
            input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_package_version_history(
        self,
        package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.get_package_version_history_response.GetPackageVersionHistoryResponse":
        """<p>Returns a list of versions of the package, along with their creation time and commit message.</p>

        Args:
            package_id: <p>Returns an audit history of versions of the package.</p>
            max_results: <p>Limits results to a maximum number of versions.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.get_package_version_history_request.GetPackageVersionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.get_package_version_history_response.GetPackageVersionHistoryResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_package_version_history

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_package_version_history.async_get_package_version_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.get_package_version_history_request.GetPackageVersionHistoryRequest = {}  # type: ignore[typeddict-item]
        input["package_id"] = package_id
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

    async def get_upgrade_history(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.get_upgrade_history_response.GetUpgradeHistoryResponse":
        """<p>Retrieves the complete history of the last 10 upgrades that were performed on the domain.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.get_upgrade_history_request.GetUpgradeHistoryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.get_upgrade_history_response.GetUpgradeHistoryResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_history

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_history.async_get_upgrade_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.get_upgrade_history_request.GetUpgradeHistoryRequest = {}  # type: ignore[typeddict-item]
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

    async def get_upgrade_status(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.get_upgrade_status_response.GetUpgradeStatusResponse":
        """<p>Retrieves the latest status of the last upgrade or upgrade eligibility check that was performed on the domain.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.get_upgrade_status_request.GetUpgradeStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.get_upgrade_status_response.GetUpgradeStatusResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_status

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.get_upgrade_status.async_get_upgrade_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.get_upgrade_status_request.GetUpgradeStatusRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domain_names(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        engine_type: Optional[
            "aws_sdk_elasticsearch_service.types.engine_type.EngineType"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Returns the name of all Elasticsearch domains owned by the current user's account. </p>

        Args:
            engine_type: <p> Optional parameter to filter the output by domain engine type. Acceptable values are 'Elasticsearch' and 'OpenSearch'. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_domain_names_request.ListDomainNamesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domain_names

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domain_names.async_list_domain_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_domain_names_request.ListDomainNamesRequest = {}  # type: ignore[typeddict-item]
        if engine_type is not None:
            input["engine_type"] = engine_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_domains_for_package(
        self,
        package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_domains_for_package_response.ListDomainsForPackageResponse":
        """<p>Lists all Amazon ES domains associated with the package.</p>

        Args:
            package_id: <p>The package for which to list domains.</p>
            max_results: <p>Limits results to a maximum number of domains.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_domains_for_package_request.ListDomainsForPackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_domains_for_package_response.ListDomainsForPackageResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domains_for_package

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_domains_for_package.async_list_domains_for_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_domains_for_package_request.ListDomainsForPackageRequest = {}  # type: ignore[typeddict-item]
        input["package_id"] = package_id
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

    async def list_elasticsearch_instance_types(
        self,
        elasticsearch_version: "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        domain_name: Optional[
            "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
        ] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_elasticsearch_instance_types_response.ListElasticsearchInstanceTypesResponse":
        """<p>List all Elasticsearch instance types that are supported for given ElasticsearchVersion</p>

        Args:
            elasticsearch_version: <p>Version of Elasticsearch for which list of supported elasticsearch instance types are needed. </p>
            domain_name: <p>DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. </p>
            max_results: <p> Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored. </p>
            next_token: <p>NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_elasticsearch_instance_types_request.ListElasticsearchInstanceTypesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_elasticsearch_instance_types_response.ListElasticsearchInstanceTypesResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_instance_types

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_instance_types.async_list_elasticsearch_instance_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_elasticsearch_instance_types_request.ListElasticsearchInstanceTypesRequest = {}  # type: ignore[typeddict-item]
        input["elasticsearch_version"] = elasticsearch_version
        if domain_name is not None:
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

    async def list_elasticsearch_versions(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_elasticsearch_versions_response.ListElasticsearchVersionsResponse":
        """<p>List all supported Elasticsearch versions</p>

        Args:
            max_results: <p> Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_elasticsearch_versions_request.ListElasticsearchVersionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_elasticsearch_versions_response.ListElasticsearchVersionsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_versions

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_elasticsearch_versions.async_list_elasticsearch_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_elasticsearch_versions_request.ListElasticsearchVersionsRequest = {}  # type: ignore[typeddict-item]
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

    async def list_packages_for_domain(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        max_results: Optional[
            "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_packages_for_domain_response.ListPackagesForDomainResponse":
        """<p>Lists all packages associated with the Amazon ES domain.</p>

        Args:
            domain_name: <p>The name of the domain for which you want to list associated packages.</p>
            max_results: <p>Limits results to a maximum number of packages.</p>
            next_token: <p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_packages_for_domain_request.ListPackagesForDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_packages_for_domain_response.ListPackagesForDomainResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_packages_for_domain

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_packages_for_domain.async_list_packages_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_packages_for_domain_request.ListPackagesForDomainRequest = {}  # type: ignore[typeddict-item]
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

    async def list_tags(
        self,
        arn: "aws_sdk_elasticsearch_service.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_tags_response.ListTagsResponse":
        """<p>Returns all tags for the given Elasticsearch domain.</p>

        Args:
            arn: <p> Specify the <code>ARN</code> for the Elasticsearch domain to which the tags are attached that you want to view.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_tags_request.ListTagsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_tags_response.ListTagsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_tags

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_tags.async_list_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vpc_endpoint_access(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse":
        """<p>Retrieves information about each principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain to retrieve access information for.</p>
            next_token: <p>Provides an identifier to allow retrieval of paginated results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_vpc_endpoint_access_response.ListVpcEndpointAccessResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoint_access.async_list_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_vpc_endpoint_access_request.ListVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vpc_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints in the current account and Region.</p>

        Args:
            next_token: <p>Identifier to allow retrieval of paginated results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints.async_list_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_vpc_endpoints_for_domain(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        next_token: Optional[
            "aws_sdk_elasticsearch_service.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse":
        """<p>Retrieves all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain.</p>

        Args:
            domain_name: <p>Name of the ElasticSearch domain whose VPC endpoints are to be listed.</p>
            next_token: <p>Provides an identifier to allow retrieval of paginated results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.list_vpc_endpoints_for_domain_response.ListVpcEndpointsForDomainResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints_for_domain

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.list_vpc_endpoints_for_domain.async_list_vpc_endpoints_for_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.list_vpc_endpoints_for_domain_request.ListVpcEndpointsForDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def purchase_reserved_elasticsearch_instance_offering(
        self,
        reserved_elasticsearch_instance_offering_id: "aws_sdk_elasticsearch_service.types.guid.GUID",
        reservation_name: "aws_sdk_elasticsearch_service.types.reservation_token.ReservationToken",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        instance_count: Optional[
            "aws_sdk_elasticsearch_service.types.instance_count.InstanceCount"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_response.PurchaseReservedElasticsearchInstanceOfferingResponse":
        """<p>Allows you to purchase reserved Elasticsearch instances.</p>

        Args:
            reserved_elasticsearch_instance_offering_id: <p>The ID of the reserved Elasticsearch instance offering to purchase.</p>
            reservation_name: <p>A customer-specified identifier to track this reservation.</p>
            instance_count: <p>The number of Elasticsearch instances to reserve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_request.PurchaseReservedElasticsearchInstanceOfferingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_response.PurchaseReservedElasticsearchInstanceOfferingResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.purchase_reserved_elasticsearch_instance_offering

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.purchase_reserved_elasticsearch_instance_offering.async_purchase_reserved_elasticsearch_instance_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.purchase_reserved_elasticsearch_instance_offering_request.PurchaseReservedElasticsearchInstanceOfferingRequest = {}  # type: ignore[typeddict-item]
        input["reserved_elasticsearch_instance_offering_id"] = (
            reserved_elasticsearch_instance_offering_id
        )
        input["reservation_name"] = reservation_name
        if instance_count is not None:
            input["instance_count"] = instance_count

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reject_inbound_cross_cluster_search_connection(
        self,
        cross_cluster_search_connection_id: "aws_sdk_elasticsearch_service.types.cross_cluster_search_connection_id.CrossClusterSearchConnectionId",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_response.RejectInboundCrossClusterSearchConnectionResponse":
        """<p>Allows the destination domain owner to reject an inbound cross-cluster search connection request.</p>

        Args:
            cross_cluster_search_connection_id: <p>The id of the inbound connection that you want to reject.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_request.RejectInboundCrossClusterSearchConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_response.RejectInboundCrossClusterSearchConnectionResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.reject_inbound_cross_cluster_search_connection

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.reject_inbound_cross_cluster_search_connection.async_reject_inbound_cross_cluster_search_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.reject_inbound_cross_cluster_search_connection_request.RejectInboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
        input["cross_cluster_search_connection_id"] = cross_cluster_search_connection_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_tags(
        self,
        arn: "aws_sdk_elasticsearch_service.types.arn.ARN",
        tag_keys: "aws_sdk_elasticsearch_service.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> None:
        """<p>Removes the specified set of tags from the specified Elasticsearch domain.</p>

        Args:
            arn: <p>Specifies the <code>ARN</code> for the Elasticsearch domain from which you want to delete the specified tags.</p>
            tag_keys: <p>Specifies the <code>TagKey</code> list which you want to remove from the Elasticsearch domain.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.remove_tags_request.RemoveTagsRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.remove_tags

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.remove_tags.async_remove_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.remove_tags_request.RemoveTagsRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def revoke_vpc_endpoint_access(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        account: "aws_sdk_elasticsearch_service.types.aws_account.AWSAccount",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse":
        """<p>Revokes access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint.</p>

        Args:
            domain_name: <p>The name of the OpenSearch Service domain.</p>
            account: <p>The account ID to revoke access from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.revoke_vpc_endpoint_access_response.RevokeVpcEndpointAccessResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.revoke_vpc_endpoint_access

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.revoke_vpc_endpoint_access.async_revoke_vpc_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.revoke_vpc_endpoint_access_request.RevokeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["account"] = account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_elasticsearch_service_software_update(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.start_elasticsearch_service_software_update_response.StartElasticsearchServiceSoftwareUpdateResponse":
        """<p>Schedules a service software update for an Amazon ES domain.</p>

        Args:
            domain_name: <p>The name of the domain that you want to update to the latest service software.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.start_elasticsearch_service_software_update_request.StartElasticsearchServiceSoftwareUpdateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.start_elasticsearch_service_software_update_response.StartElasticsearchServiceSoftwareUpdateResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.start_elasticsearch_service_software_update

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.start_elasticsearch_service_software_update.async_start_elasticsearch_service_software_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.start_elasticsearch_service_software_update_request.StartElasticsearchServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_elasticsearch_domain_config(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        elasticsearch_cluster_config: Optional[
            "aws_sdk_elasticsearch_service.types.elasticsearch_cluster_config.ElasticsearchClusterConfig"
        ] = None,
        ebs_options: Optional[
            "aws_sdk_elasticsearch_service.types.ebs_options.EBSOptions"
        ] = None,
        snapshot_options: Optional[
            "aws_sdk_elasticsearch_service.types.snapshot_options.SnapshotOptions"
        ] = None,
        vpc_options: Optional[
            "aws_sdk_elasticsearch_service.types.vpc_options.VPCOptions"
        ] = None,
        cognito_options: Optional[
            "aws_sdk_elasticsearch_service.types.cognito_options.CognitoOptions"
        ] = None,
        advanced_options: Optional[
            "aws_sdk_elasticsearch_service.types.advanced_options.AdvancedOptions"
        ] = None,
        access_policies: Optional[
            "aws_sdk_elasticsearch_service.types.policy_document.PolicyDocument"
        ] = None,
        log_publishing_options: Optional[
            "aws_sdk_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
        ] = None,
        domain_endpoint_options: Optional[
            "aws_sdk_elasticsearch_service.types.domain_endpoint_options.DomainEndpointOptions"
        ] = None,
        advanced_security_options: Optional[
            "aws_sdk_elasticsearch_service.types.advanced_security_options_input.AdvancedSecurityOptionsInput"
        ] = None,
        node_to_node_encryption_options: Optional[
            "aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
        ] = None,
        encryption_at_rest_options: Optional[
            "aws_sdk_elasticsearch_service.types.encryption_at_rest_options.EncryptionAtRestOptions"
        ] = None,
        auto_tune_options: Optional[
            "aws_sdk_elasticsearch_service.types.auto_tune_options.AutoTuneOptions"
        ] = None,
        dry_run: Optional["aws_sdk_elasticsearch_service.types.dry_run.DryRun"] = None,
        deployment_strategy_options: Optional[
            "aws_sdk_elasticsearch_service.types.deployment_strategy_options.DeploymentStrategyOptions"
        ] = None,
        automated_snapshot_pause_options: Optional[
            "aws_sdk_elasticsearch_service.types.automated_snapshot_pause_request_options.AutomatedSnapshotPauseRequestOptions"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse":
        """<p>Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances. </p>

        Args:
            domain_name: <p>The name of the Elasticsearch domain that you are updating. </p>
            elasticsearch_cluster_config: <p>The type and number of instances to instantiate for the domain cluster.</p>
            ebs_options: <p>Specify the type and size of the EBS volume that you want to use. </p>
            snapshot_options: <p>Option to set the time, in UTC format, for the daily automated snapshot. Default value is <code>0</code> hours. </p>
            vpc_options: <p>Options to specify the subnets and security groups for VPC endpoint. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc\" target=\"_blank\">Creating a VPC</a> in <i>VPC Endpoints for Amazon Elasticsearch Service Domains</i></p>
            cognito_options: <p>Options to specify the Cognito user and identity pools for Kibana authentication. For more information, see <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html\" target=\"_blank\">Amazon Cognito Authentication for Kibana</a>.</p>
            advanced_options: <p>Modifies the advanced option to allow references to indices in an HTTP request body. Must be <code>false</code> when configuring access to individual sub-resources. By default, the value is <code>true</code>. See <a href=\"http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options\" target=\"_blank\">Configuration Advanced Options</a> for more information.</p>
            access_policies: <p>IAM access policy as a JSON-formatted string.</p>
            log_publishing_options: <p>Map of <code>LogType</code> and <code>LogPublishingOption</code>, each containing options to publish a given type of Elasticsearch log.</p>
            domain_endpoint_options: <p>Options to specify configuration that will be applied to the domain endpoint.</p>
            advanced_security_options: <p>Specifies advanced security options.</p>
            node_to_node_encryption_options: <p>Specifies the NodeToNodeEncryptionOptions.</p>
            encryption_at_rest_options: <p>Specifies the Encryption At Rest Options.</p>
            auto_tune_options: <p>Specifies Auto-Tune options.</p>
            dry_run: <p> This flag, when set to True, specifies whether the <code>UpdateElasticsearchDomain</code> request should return the results of validation checks without actually applying the change. This flag, when set to True, specifies the deployment mechanism through which the update shall be applied on the domain. This will not actually perform the Update. </p>
            deployment_strategy_options: <p>Specifies the deployment strategy options.</p>
            automated_snapshot_pause_options: <p>Specifies the automated snapshot pause options for the domain.</p> <important> <p>Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.</p> </important> <p>Maximum suspension duration: 3 days.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.update_elasticsearch_domain_config_response.UpdateElasticsearchDomainConfigResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_elasticsearch_domain_config

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_elasticsearch_domain_config.async_update_elasticsearch_domain_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.update_elasticsearch_domain_config_request.UpdateElasticsearchDomainConfigRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        if elasticsearch_cluster_config is not None:
            input["elasticsearch_cluster_config"] = elasticsearch_cluster_config
        if ebs_options is not None:
            input["ebs_options"] = ebs_options
        if snapshot_options is not None:
            input["snapshot_options"] = snapshot_options
        if vpc_options is not None:
            input["vpc_options"] = vpc_options
        if cognito_options is not None:
            input["cognito_options"] = cognito_options
        if advanced_options is not None:
            input["advanced_options"] = advanced_options
        if access_policies is not None:
            input["access_policies"] = access_policies
        if log_publishing_options is not None:
            input["log_publishing_options"] = log_publishing_options
        if domain_endpoint_options is not None:
            input["domain_endpoint_options"] = domain_endpoint_options
        if advanced_security_options is not None:
            input["advanced_security_options"] = advanced_security_options
        if node_to_node_encryption_options is not None:
            input["node_to_node_encryption_options"] = node_to_node_encryption_options
        if encryption_at_rest_options is not None:
            input["encryption_at_rest_options"] = encryption_at_rest_options
        if auto_tune_options is not None:
            input["auto_tune_options"] = auto_tune_options
        if dry_run is not None:
            input["dry_run"] = dry_run
        if deployment_strategy_options is not None:
            input["deployment_strategy_options"] = deployment_strategy_options
        if automated_snapshot_pause_options is not None:
            input["automated_snapshot_pause_options"] = automated_snapshot_pause_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_package(
        self,
        package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID",
        package_source: "aws_sdk_elasticsearch_service.types.package_source.PackageSource",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        package_description: Optional[
            "aws_sdk_elasticsearch_service.types.package_description.PackageDescription"
        ] = None,
        commit_message: Optional[
            "aws_sdk_elasticsearch_service.types.commit_message.CommitMessage"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.update_package_response.UpdatePackageResponse":
        """<p>Updates a package for use with Amazon ES domains.</p>

        Args:
            package_id: <p>Unique identifier for the package.</p>
            package_description: <p>New description of the package.</p>
            commit_message: <p>An info message for the new version which will be shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.update_package_request.UpdatePackageRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.update_package_response.UpdatePackageResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_package

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_package.async_update_package(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.update_package_request.UpdatePackageRequest = {}  # type: ignore[typeddict-item]
        input["package_id"] = package_id
        input["package_source"] = package_source
        if package_description is not None:
            input["package_description"] = package_description
        if commit_message is not None:
            input["commit_message"] = commit_message

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_vpc_endpoint(
        self,
        vpc_endpoint_id: "aws_sdk_elasticsearch_service.types.vpc_endpoint_id.VpcEndpointId",
        vpc_options: "aws_sdk_elasticsearch_service.types.vpc_options.VPCOptions",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
    ) -> "aws_sdk_elasticsearch_service.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse":
        """<p>Modifies an Amazon OpenSearch Service-managed interface VPC endpoint.</p>

        Args:
            vpc_endpoint_id: <p>Unique identifier of the VPC endpoint to be updated.</p>
            vpc_options: <p>The security groups and/or subnets to add, remove, or modify.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.update_vpc_endpoint_response.UpdateVpcEndpointResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.update_vpc_endpoint.async_update_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.update_vpc_endpoint_request.UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input["vpc_endpoint_id"] = vpc_endpoint_id
        input["vpc_options"] = vpc_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def upgrade_elasticsearch_domain(
        self,
        domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName",
        target_version: "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString",
        *,
        config_overrides: Optional[AsyncElasticsearchServiceClientConfig] = None,
        perform_check_only: Optional[
            "aws_sdk_elasticsearch_service.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_elasticsearch_service.types.upgrade_elasticsearch_domain_response.UpgradeElasticsearchDomainResponse":
        """<p>Allows you to either upgrade your domain or perform an Upgrade eligibility check to a compatible Elasticsearch version.</p>

        Args:
            target_version: <p>The version of Elasticsearch that you intend to upgrade the domain to.</p>
            perform_check_only: <p> This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elasticsearch_service.types.upgrade_elasticsearch_domain_request.UpgradeElasticsearchDomainRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elasticsearch_service.types.upgrade_elasticsearch_domain_response.UpgradeElasticsearchDomainResponse"
        ]:
            import aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.upgrade_elasticsearch_domain

            (
                output,
                http_response,
            ) = await aws_sdk_elasticsearch_service._operations.amazon_elasticsearch_service2015.upgrade_elasticsearch_domain.async_upgrade_elasticsearch_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_elasticsearch_service.types.upgrade_elasticsearch_domain_request.UpgradeElasticsearchDomainRequest = {}  # type: ignore[typeddict-item]
        input["domain_name"] = domain_name
        input["target_version"] = target_version
        if perform_check_only is not None:
            input["perform_check_only"] = perform_check_only

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
