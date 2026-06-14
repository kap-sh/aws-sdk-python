"""Generated from Smithy shape ``com.amazonaws.drs#ElasticDisasterRecoveryService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_drs._auth._signers
import aws_sdk_drs._auth._sigv4
from aws_sdk_drs._auth._identity import Credentials
from aws_sdk_drs._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_drs._auth._zapros_handler import AuthMiddleware
from aws_sdk_drs._pagination import resolve_path as _resolve_path
from aws_sdk_drs._resources.elastic_disaster_recovery_service.account_resource import (
    AsyncAccountResource,
)
from aws_sdk_drs._resources.elastic_disaster_recovery_service.job_resource import (
    AsyncJobResource,
)
from aws_sdk_drs._resources.elastic_disaster_recovery_service.launch_configuration_template_resource import (
    AsyncLaunchConfigurationTemplateResource,
)
from aws_sdk_drs._resources.elastic_disaster_recovery_service.recovery_instance_resource import (
    AsyncRecoveryInstanceResource,
)
from aws_sdk_drs._resources.elastic_disaster_recovery_service.replication_configuration_template_resource import (
    AsyncReplicationConfigurationTemplateResource,
)
from aws_sdk_drs._resources.elastic_disaster_recovery_service.source_network_resource import (
    AsyncSourceNetworkResource,
)
from aws_sdk_drs._resources.elastic_disaster_recovery_service.source_server_resource import (
    AsyncSourceServerResource,
)
from aws_sdk_drs._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_drs.types.account
    import aws_sdk_drs.types.account_id
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.create_extended_source_server_request
    import aws_sdk_drs.types.create_extended_source_server_response
    import aws_sdk_drs.types.delete_launch_action_request
    import aws_sdk_drs.types.delete_launch_action_response
    import aws_sdk_drs.types.initialize_service_request
    import aws_sdk_drs.types.initialize_service_response
    import aws_sdk_drs.types.launch_action
    import aws_sdk_drs.types.launch_action_category
    import aws_sdk_drs.types.launch_action_description
    import aws_sdk_drs.types.launch_action_id
    import aws_sdk_drs.types.launch_action_name
    import aws_sdk_drs.types.launch_action_order
    import aws_sdk_drs.types.launch_action_parameters
    import aws_sdk_drs.types.launch_action_resource_id
    import aws_sdk_drs.types.launch_action_version
    import aws_sdk_drs.types.launch_actions_request_filters
    import aws_sdk_drs.types.list_extensible_source_servers_request
    import aws_sdk_drs.types.list_extensible_source_servers_response
    import aws_sdk_drs.types.list_launch_actions_request
    import aws_sdk_drs.types.list_launch_actions_response
    import aws_sdk_drs.types.list_staging_accounts_request
    import aws_sdk_drs.types.list_staging_accounts_response
    import aws_sdk_drs.types.list_tags_for_resource_request
    import aws_sdk_drs.types.list_tags_for_resource_response
    import aws_sdk_drs.types.max_results_replicating_source_servers
    import aws_sdk_drs.types.max_results_type
    import aws_sdk_drs.types.pagination_token
    import aws_sdk_drs.types.put_launch_action_request
    import aws_sdk_drs.types.put_launch_action_response
    import aws_sdk_drs.types.source_server_arn
    import aws_sdk_drs.types.ssm_document_name
    import aws_sdk_drs.types.staging_source_server
    import aws_sdk_drs.types.tag_keys
    import aws_sdk_drs.types.tag_resource_request
    import aws_sdk_drs.types.tags_map
    import aws_sdk_drs.types.untag_resource_request


class AsyncdrsClientConfig(TypedDict, total=False):
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


class AsyncdrsClient:
    """A client for the ``drs`` service.

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
        self.config = AsyncdrsClientConfig(
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
        # resources
        self.account_resource = AsyncAccountResource(self)
        self.job_resource = AsyncJobResource(self)
        self.launch_configuration_template_resource = (
            AsyncLaunchConfigurationTemplateResource(self)
        )
        self.recovery_instance_resource = AsyncRecoveryInstanceResource(self)
        self.replication_configuration_template_resource = (
            AsyncReplicationConfigurationTemplateResource(self)
        )
        self.source_network_resource = AsyncSourceNetworkResource(self)
        self.source_server_resource = AsyncSourceServerResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncdrsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncdrsClientConfig = config_overrides or {}
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

    async def create_extended_source_server(
        self,
        source_server_arn: "aws_sdk_drs.types.source_server_arn.SourceServerARN",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        tags: Optional["aws_sdk_drs.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_drs.types.create_extended_source_server_response.CreateExtendedSourceServerResponse":
        """<p>Create an extended source server in the target Account based on the source server in staging account.</p>

        Args:
            source_server_arn: <p>This defines the ARN of the source server in staging Account based on which you want to create an extended source server.</p>
            tags: <p>A list of tags associated with the extended source server.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.create_extended_source_server_request.CreateExtendedSourceServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.create_extended_source_server_response.CreateExtendedSourceServerResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.create_extended_source_server

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.create_extended_source_server.async_create_extended_source_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.create_extended_source_server_request.CreateExtendedSourceServerRequest = {}  # type: ignore[typeddict-item]
        input_["source_server_arn"] = source_server_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_launch_action(
        self,
        resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId",
        action_id: "aws_sdk_drs.types.launch_action_id.LaunchActionId",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "aws_sdk_drs.types.delete_launch_action_response.DeleteLaunchActionResponse":
        """<p>Deletes a resource launch action.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.delete_launch_action_request.DeleteLaunchActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.delete_launch_action_response.DeleteLaunchActionResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_launch_action

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.delete_launch_action.async_delete_launch_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.delete_launch_action_request.DeleteLaunchActionRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        input_["action_id"] = action_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def initialize_service(
        self, *, config_overrides: Optional[AsyncdrsClientConfig] = None
    ) -> "aws_sdk_drs.types.initialize_service_response.InitializeServiceResponse":
        """<p>Initialize Elastic Disaster Recovery.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.initialize_service_request.InitializeServiceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.initialize_service_response.InitializeServiceResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.initialize_service

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.initialize_service.async_initialize_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.initialize_service_request.InitializeServiceRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_extensible_source_servers(
        self,
        staging_account_id: "aws_sdk_drs.types.account_id.AccountID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_drs.types.max_results_replicating_source_servers.MaxResultsReplicatingSourceServers"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.list_extensible_source_servers_response.ListExtensibleSourceServersResponse":
        """<p>Returns a list of source servers on a staging account that are extensible, which means that: a. The source server is not already extended into this Account. b. The source server on the Account we’re reading from is not an extension of another source server. </p>

        Args:
            staging_account_id: <p>The Id of the staging Account to retrieve extensible source servers from.</p>
            max_results: <p>The maximum number of extensible source servers to retrieve.</p>
            next_token: <p>The token of the next extensible source server to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.list_extensible_source_servers_request.ListExtensibleSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.list_extensible_source_servers_response.ListExtensibleSourceServersResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.list_extensible_source_servers

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.list_extensible_source_servers.async_list_extensible_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.list_extensible_source_servers_request.ListExtensibleSourceServersRequest = {}  # type: ignore[typeddict-item]
        input_["staging_account_id"] = staging_account_id
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

    async def iter_list_extensible_source_servers(
        self,
        staging_account_id: "aws_sdk_drs.types.account_id.AccountID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_drs.types.max_results_replicating_source_servers.MaxResultsReplicatingSourceServers"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_drs.types.staging_source_server.StagingSourceServer]":
        _token = next_token
        while True:
            _response = await self.list_extensible_source_servers(
                staging_account_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_launch_actions(
        self,
        resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.launch_actions_request_filters.LaunchActionsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.list_launch_actions_response.ListLaunchActionsResponse":
        """<p>Lists resource launch actions.</p>

        Args:
            filters: <p>Filters to apply when listing resource launch actions.</p>
            max_results: <p>Maximum amount of items to return when listing resource launch actions.</p>
            next_token: <p>Next token to use when listing resource launch actions.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.list_launch_actions_request.ListLaunchActionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.list_launch_actions_response.ListLaunchActionsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.list_launch_actions

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.list_launch_actions.async_list_launch_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.list_launch_actions_request.ListLaunchActionsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
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

    async def iter_list_launch_actions(
        self,
        resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "aws_sdk_drs.types.launch_actions_request_filters.LaunchActionsRequestFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_drs.types.max_results_type.MaxResultsType"
        ] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_drs.types.launch_action.LaunchAction]":
        _token = next_token
        while True:
            _response = await self.list_launch_actions(
                resource_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_staging_accounts(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_drs.types.list_staging_accounts_response.ListStagingAccountsResponse":
        """<p>Returns an array of staging accounts for existing extended source servers.</p>

        Args:
            max_results: <p>The maximum number of staging Accounts to retrieve.</p>
            next_token: <p>The token of the next staging Account to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.list_staging_accounts_request.ListStagingAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.list_staging_accounts_response.ListStagingAccountsResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.list_staging_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.list_staging_accounts.async_list_staging_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.list_staging_accounts_request.ListStagingAccountsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_staging_accounts(
        self,
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "aws_sdk_drs.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_drs.types.account.Account]":
        _token = next_token
        while True:
            _response = await self.list_staging_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_drs.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> (
        "aws_sdk_drs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>List all tags for your Elastic Disaster Recovery resources.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags should be returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_launch_action(
        self,
        resource_id: "aws_sdk_drs.types.launch_action_resource_id.LaunchActionResourceId",
        action_code: "aws_sdk_drs.types.ssm_document_name.SsmDocumentName",
        order: "aws_sdk_drs.types.launch_action_order.LaunchActionOrder",
        action_id: "aws_sdk_drs.types.launch_action_id.LaunchActionId",
        optional: bool,
        active: bool,
        name: "aws_sdk_drs.types.launch_action_name.LaunchActionName",
        action_version: "aws_sdk_drs.types.launch_action_version.LaunchActionVersion",
        category: "aws_sdk_drs.types.launch_action_category.LaunchActionCategory",
        description: "aws_sdk_drs.types.launch_action_description.LaunchActionDescription",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        parameters: Optional[
            "aws_sdk_drs.types.launch_action_parameters.LaunchActionParameters"
        ] = None,
    ) -> "aws_sdk_drs.types.put_launch_action_response.PutLaunchActionResponse":
        """<p>Puts a resource launch action.</p>

        Args:
            action_code: <p>Launch action code.</p>
            optional: <p>Whether the launch will not be marked as failed if this action fails.</p>
            active: <p>Whether the launch action is active.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.put_launch_action_request.PutLaunchActionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_drs.types.put_launch_action_response.PutLaunchActionResponse"
        ]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.put_launch_action

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.put_launch_action.async_put_launch_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.put_launch_action_request.PutLaunchActionRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        input_["action_code"] = action_code
        input_["order"] = order
        input_["action_id"] = action_id
        input_["optional"] = optional
        input_["active"] = active
        input_["name"] = name
        input_["action_version"] = action_version
        input_["category"] = category
        if parameters is not None:
            input_["parameters"] = parameters
        input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_drs.types.arn.ARN",
        tags: "aws_sdk_drs.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Adds or overwrites only the specified tags for the specified Elastic Disaster Recovery resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be added or updated.</p>
            tags: <p>Array of tags to be added or updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_drs.types.arn.ARN",
        tag_keys: "aws_sdk_drs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified set of tags from the specified set of Elastic Disaster Recovery resources.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be removed.</p>
            tag_keys: <p>Array of tags to be removed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_drs.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_drs._operations.elastic_disaster_recovery_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_drs._operations.elastic_disaster_recovery_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_drs.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
