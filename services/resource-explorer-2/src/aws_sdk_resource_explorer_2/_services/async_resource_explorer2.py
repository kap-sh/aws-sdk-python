"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ResourceExplorer``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_resource_explorer_2._auth._signers
import aws_sdk_resource_explorer_2._auth._sigv4
from aws_sdk_resource_explorer_2._auth._identity import Credentials
from aws_sdk_resource_explorer_2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_resource_explorer_2._auth._zapros_handler import AuthMiddleware
from aws_sdk_resource_explorer_2._pagination import resolve_path as _resolve_path
from aws_sdk_resource_explorer_2._resources.resource_explorer.cfn_index import (
    AsyncCfnIndex,
)
from aws_sdk_resource_explorer_2._resources.resource_explorer.cfn_view import (
    AsyncCfnView,
)
from aws_sdk_resource_explorer_2._resources.resource_explorer.default_view_association import (
    AsyncDefaultViewAssociation,
)
from aws_sdk_resource_explorer_2._services._aws_config import aaws_config
from aws_sdk_resource_explorer_2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.account_id_list
    import aws_sdk_resource_explorer_2.types.batch_get_view_input
    import aws_sdk_resource_explorer_2.types.batch_get_view_output
    import aws_sdk_resource_explorer_2.types.create_resource_explorer_setup_input
    import aws_sdk_resource_explorer_2.types.create_resource_explorer_setup_output
    import aws_sdk_resource_explorer_2.types.delete_resource_explorer_setup_input
    import aws_sdk_resource_explorer_2.types.delete_resource_explorer_setup_output
    import aws_sdk_resource_explorer_2.types.get_account_level_service_configuration_output
    import aws_sdk_resource_explorer_2.types.get_default_view_output
    import aws_sdk_resource_explorer_2.types.get_index_output
    import aws_sdk_resource_explorer_2.types.get_managed_view_input
    import aws_sdk_resource_explorer_2.types.get_managed_view_output
    import aws_sdk_resource_explorer_2.types.get_resource_explorer_setup_input
    import aws_sdk_resource_explorer_2.types.get_resource_explorer_setup_output
    import aws_sdk_resource_explorer_2.types.get_service_index_output
    import aws_sdk_resource_explorer_2.types.get_service_view_input
    import aws_sdk_resource_explorer_2.types.get_service_view_output
    import aws_sdk_resource_explorer_2.types.index
    import aws_sdk_resource_explorer_2.types.list_indexes_for_members_input
    import aws_sdk_resource_explorer_2.types.list_indexes_for_members_output
    import aws_sdk_resource_explorer_2.types.list_managed_views_input
    import aws_sdk_resource_explorer_2.types.list_managed_views_output
    import aws_sdk_resource_explorer_2.types.list_resources_input
    import aws_sdk_resource_explorer_2.types.list_resources_output
    import aws_sdk_resource_explorer_2.types.list_service_indexes_input
    import aws_sdk_resource_explorer_2.types.list_service_indexes_output
    import aws_sdk_resource_explorer_2.types.list_service_views_input
    import aws_sdk_resource_explorer_2.types.list_service_views_output
    import aws_sdk_resource_explorer_2.types.list_streaming_access_for_services_input
    import aws_sdk_resource_explorer_2.types.list_streaming_access_for_services_output
    import aws_sdk_resource_explorer_2.types.list_supported_resource_types_input
    import aws_sdk_resource_explorer_2.types.list_supported_resource_types_output
    import aws_sdk_resource_explorer_2.types.list_tags_for_resource_input
    import aws_sdk_resource_explorer_2.types.list_tags_for_resource_output
    import aws_sdk_resource_explorer_2.types.member_index
    import aws_sdk_resource_explorer_2.types.query_string
    import aws_sdk_resource_explorer_2.types.region_list
    import aws_sdk_resource_explorer_2.types.region_status
    import aws_sdk_resource_explorer_2.types.resource
    import aws_sdk_resource_explorer_2.types.search_filter
    import aws_sdk_resource_explorer_2.types.search_input
    import aws_sdk_resource_explorer_2.types.search_output
    import aws_sdk_resource_explorer_2.types.streaming_access_details
    import aws_sdk_resource_explorer_2.types.string_list
    import aws_sdk_resource_explorer_2.types.supported_resource_type
    import aws_sdk_resource_explorer_2.types.tag_map
    import aws_sdk_resource_explorer_2.types.tag_resource_input
    import aws_sdk_resource_explorer_2.types.tag_resource_output
    import aws_sdk_resource_explorer_2.types.untag_resource_input
    import aws_sdk_resource_explorer_2.types.untag_resource_output
    import aws_sdk_resource_explorer_2.types.view_arn_list


class AsyncResourceExplorer2ClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncResourceExplorer2Client:
    """A client for the ``ResourceExplorer2`` service.

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
        self._config = AsyncResourceExplorer2ClientConfig(
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

        # resources
        self.cfn_index = AsyncCfnIndex(self)
        self.cfn_view = AsyncCfnView(self)
        self.default_view_association = AsyncDefaultViewAssociation(self)

    def operation_options(
        self, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncResourceExplorer2ClientConfig = config_overrides or {}
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

    async def batch_get_view(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        view_arns: Optional[
            "aws_sdk_resource_explorer_2.types.view_arn_list.ViewArnList"
        ] = None,
    ) -> "aws_sdk_resource_explorer_2.types.batch_get_view_output.BatchGetViewOutput":
        r"""<p>Retrieves details about a list of views.</p>

        Args:
            view_arns: <p>A list of <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource names (ARNs)</a> that identify the views you want details for.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.batch_get_view_input.BatchGetViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.batch_get_view_output.BatchGetViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.batch_get_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.batch_get_view.async_batch_get_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.batch_get_view_input.BatchGetViewInput = {}  # type: ignore[typeddict-item]
        if view_arns is not None:
            input_["view_arns"] = view_arns

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_resource_explorer_setup(
        self,
        region_list: "aws_sdk_resource_explorer_2.types.region_list.RegionList",
        view_name: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        aggregator_regions: Optional[
            "aws_sdk_resource_explorer_2.types.region_list.RegionList"
        ] = None,
    ) -> "aws_sdk_resource_explorer_2.types.create_resource_explorer_setup_output.CreateResourceExplorerSetupOutput":
        """<p>Creates a Resource Explorer setup configuration across multiple Amazon Web Services Regions. This operation sets up indexes and views in the specified Regions. This operation can also be used to set an aggregator Region for cross-Region resource search.</p>

        Args:
            region_list: <p>A list of Amazon Web Services Regions where Resource Explorer should be configured. Each Region in the list will have a user-owned index created.</p>
            aggregator_regions: <p>A list of Amazon Web Services Regions that should be configured as aggregator Regions. Aggregator Regions receive replicated index information from all other Regions where there is a user-owned index.</p>
            view_name: <p>The name for the view to be created as part of the Resource Explorer setup. The view name must be unique within the Amazon Web Services account and Region.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.create_resource_explorer_setup_input.CreateResourceExplorerSetupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.create_resource_explorer_setup_output.CreateResourceExplorerSetupOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.create_resource_explorer_setup

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.create_resource_explorer_setup.async_create_resource_explorer_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.create_resource_explorer_setup_input.CreateResourceExplorerSetupInput = {}  # type: ignore[typeddict-item]
        input_["region_list"] = region_list
        if aggregator_regions is not None:
            input_["aggregator_regions"] = aggregator_regions
        input_["view_name"] = view_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_resource_explorer_setup(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        region_list: Optional[
            "aws_sdk_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        delete_in_all_regions: Optional[bool] = None,
    ) -> "aws_sdk_resource_explorer_2.types.delete_resource_explorer_setup_output.DeleteResourceExplorerSetupOutput":
        """<p>Deletes a Resource Explorer setup configuration. This operation removes indexes and views from the specified Regions or all Regions where Resource Explorer is configured.</p>

        Args:
            region_list: <p>A list of Amazon Web Services Regions from which to delete the Resource Explorer configuration. If not specified, the operation uses the <code>DeleteInAllRegions</code> parameter to determine scope.</p>
            delete_in_all_regions: <p>Specifies whether to delete Resource Explorer configuration from all Regions where it is currently enabled. If this parameter is set to <code>true</code>, a value for <code>RegionList</code> must not be provided. Otherwise, the operation fails with a <code>ValidationException</code> error.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.delete_resource_explorer_setup_input.DeleteResourceExplorerSetupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.delete_resource_explorer_setup_output.DeleteResourceExplorerSetupOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.delete_resource_explorer_setup

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.delete_resource_explorer_setup.async_delete_resource_explorer_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.delete_resource_explorer_setup_input.DeleteResourceExplorerSetupInput = {}  # type: ignore[typeddict-item]
        if region_list is not None:
            input_["region_list"] = region_list
        if delete_in_all_regions is not None:
            input_["delete_in_all_regions"] = delete_in_all_regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_default_view(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> None:
        """<p>After you call this operation, the affected Amazon Web Services Region no longer has a default view. All <a>Search</a> operations in that Region must explicitly specify a view or the operation fails. You can configure a new default by calling the <a>AssociateDefaultView</a> operation.</p> <p>If an Amazon Web Services Region doesn't have a default view configured, then users must explicitly specify a view with every <code>Search</code> operation performed in that Region.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.disassociate_default_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.disassociate_default_view.async_disassociate_default_view(
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

    async def get_account_level_service_configuration(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> "aws_sdk_resource_explorer_2.types.get_account_level_service_configuration_output.GetAccountLevelServiceConfigurationOutput":
        """<p>Retrieves the status of your account's Amazon Web Services service access, and validates the service linked role required to access the multi-account search feature. Only the management account can invoke this API call. </p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_account_level_service_configuration_output.GetAccountLevelServiceConfigurationOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_account_level_service_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_account_level_service_configuration.async_get_account_level_service_configuration(
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

    async def get_default_view(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> (
        "aws_sdk_resource_explorer_2.types.get_default_view_output.GetDefaultViewOutput"
    ):
        """<p>Retrieves the Amazon Resource Name (ARN) of the view that is the default for the Amazon Web Services Region in which you call this operation. You can then call <a>GetView</a> to retrieve the details of that view.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_default_view_output.GetDefaultViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_default_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_default_view.async_get_default_view(
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

    async def get_index(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> "aws_sdk_resource_explorer_2.types.get_index_output.GetIndexOutput":
        """<p>Retrieves details about the Amazon Web Services Resource Explorer index in the Amazon Web Services Region in which you invoked the operation.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_index_output.GetIndexOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_index

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_index.async_get_index(
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

    async def get_managed_view(
        self,
        managed_view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> (
        "aws_sdk_resource_explorer_2.types.get_managed_view_output.GetManagedViewOutput"
    ):
        r"""<p>Retrieves details of the specified <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html\">Amazon Web Services-managed view</a>. </p>

        Args:
            managed_view_arn: <p>The Amazon resource name (ARN) of the managed view.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.get_managed_view_input.GetManagedViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_managed_view_output.GetManagedViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_managed_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_managed_view.async_get_managed_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.get_managed_view_input.GetManagedViewInput = {}  # type: ignore[typeddict-item]
        input_["managed_view_arn"] = managed_view_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_explorer_setup(
        self,
        task_id: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.get_resource_explorer_setup_output.GetResourceExplorerSetupOutput":
        """<p>Retrieves the status and details of a Resource Explorer setup operation. This operation returns information about the progress of creating or deleting Resource Explorer configurations across Regions.</p>

        Args:
            task_id: <p>The unique identifier of the setup task to retrieve status information for. This ID is returned by <code>CreateResourceExplorerSetup</code> or <code>DeleteResourceExplorerSetup</code> operations.</p>
            max_results: <p>The maximum number of Region status results to return in a single response. Valid values are between <code>1</code> and <code>100</code>.</p>
            next_token: <p>The pagination token from a previous <code>GetResourceExplorerSetup</code> response. Use this token to retrieve the next set of results.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.get_resource_explorer_setup_input.GetResourceExplorerSetupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_resource_explorer_setup_output.GetResourceExplorerSetupOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_resource_explorer_setup

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_resource_explorer_setup.async_get_resource_explorer_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.get_resource_explorer_setup_input.GetResourceExplorerSetupInput = {}  # type: ignore[typeddict-item]
        input_["task_id"] = task_id
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

    async def iter_get_resource_explorer_setup(
        self,
        task_id: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.region_status.RegionStatus]":
        _token = next_token
        while True:
            _response = await self.get_resource_explorer_setup(
                task_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("regions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_service_index(
        self, *, config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None
    ) -> "aws_sdk_resource_explorer_2.types.get_service_index_output.GetServiceIndexOutput":
        """<p>Retrieves information about the Resource Explorer index in the current Amazon Web Services Region. This operation returns the ARN and type of the index if one exists.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_service_index_output.GetServiceIndexOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_service_index

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_service_index.async_get_service_index(
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

    async def get_service_view(
        self,
        service_view_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> (
        "aws_sdk_resource_explorer_2.types.get_service_view_output.GetServiceViewOutput"
    ):
        """<p>Retrieves details about a specific Resource Explorer service view. This operation returns the configuration and properties of the specified view.</p>

        Args:
            service_view_arn: <p>The Amazon Resource Name (ARN) of the service view to retrieve details for.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.get_service_view_input.GetServiceViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.get_service_view_output.GetServiceViewOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.get_service_view

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.get_service_view.async_get_service_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.get_service_view_input.GetServiceViewInput = {}  # type: ignore[typeddict-item]
        input_["service_view_arn"] = service_view_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_indexes_for_members(
        self,
        account_id_list: "aws_sdk_resource_explorer_2.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_indexes_for_members_output.ListIndexesForMembersOutput":
        """<p>Retrieves a list of a member's indexes in all Amazon Web Services Regions that are currently collecting resource information for Amazon Web Services Resource Explorer. Only the management account or a delegated administrator with service access enabled can invoke this API call. </p>

        Args:
            account_id_list: <p>The account IDs will limit the output to only indexes from these accounts.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_indexes_for_members_input.ListIndexesForMembersInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_indexes_for_members_output.ListIndexesForMembersOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_indexes_for_members

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_indexes_for_members.async_list_indexes_for_members(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_indexes_for_members_input.ListIndexesForMembersInput = {}  # type: ignore[typeddict-item]
        input_["account_id_list"] = account_id_list
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

    async def iter_list_indexes_for_members(
        self,
        account_id_list: "aws_sdk_resource_explorer_2.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.member_index.MemberIndex]":
        _token = next_token
        while True:
            _response = await self.list_indexes_for_members(
                account_id_list,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("indexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_managed_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        service_principal: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_managed_views_output.ListManagedViewsOutput":
        r"""<p>Lists the Amazon resource names (ARNs) of the <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html\">Amazon Web Services-managed views</a> available in the Amazon Web Services Region in which you call this operation. </p>

        Args:
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            service_principal: <p>Specifies a service principal name. If specified, then the operation only returns the managed views that are managed by the input service. </p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_managed_views_input.ListManagedViewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_managed_views_output.ListManagedViewsOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_managed_views

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_managed_views.async_list_managed_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_managed_views_input.ListManagedViewsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if service_principal is not None:
            input_["service_principal"] = service_principal

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_managed_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        service_principal: Optional[str] = None,
    ) -> "AsyncIterator[str]":
        _token = next_token
        while True:
            _response = await self.list_managed_views(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                service_principal=service_principal,
            )
            _page = _resolve_path(_response, ("managed_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        filters: Optional[
            "aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_resources_output.ListResourcesOutput":
        r"""<p>Returns a list of resources and their details that match the specified criteria. This query must use a view. If you don’t explicitly specify a view, then Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation. </p>

        Args:
            filters: <p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters\">filter prefixes</a> with optional <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators\">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            view_arn: <p>Specifies the Amazon resource name (ARN) of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a 401 Unauthorized exception.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p> <note> <p>The <code>ListResources</code> operation does not generate a <code>NextToken</code> if you set <code>MaxResults</code> to 1000. </p> </note>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_resources_input.ListResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_resources_output.ListResourcesOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_resources

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_resources.async_list_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_resources_input.ListResourcesInput = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if view_arn is not None:
            input_["view_arn"] = view_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        filters: Optional[
            "aws_sdk_resource_explorer_2.types.search_filter.SearchFilter"
        ] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.resource.Resource]":
        _token = next_token
        while True:
            _response = await self.list_resources(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                view_arn=view_arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_indexes(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        regions: Optional[
            "aws_sdk_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_service_indexes_output.ListServiceIndexesOutput":
        """<p>Lists all Resource Explorer indexes across the specified Amazon Web Services Regions. This operation returns information about indexes including their ARNs, types, and Regions.</p>

        Args:
            regions: <p>A list of Amazon Web Services Regions to include in the search for indexes. If not specified, indexes from all Regions are returned.</p>
            max_results: <p>The maximum number of index results to return in a single response. Valid values are between <code>1</code> and <code>100</code>.</p>
            next_token: <p>The pagination token from a previous <code>ListServiceIndexes</code> response. Use this token to retrieve the next set of results.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_service_indexes_input.ListServiceIndexesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_service_indexes_output.ListServiceIndexesOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_service_indexes

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_service_indexes.async_list_service_indexes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_service_indexes_input.ListServiceIndexesInput = {}  # type: ignore[typeddict-item]
        if regions is not None:
            input_["regions"] = regions
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

    async def iter_list_service_indexes(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        regions: Optional[
            "aws_sdk_resource_explorer_2.types.region_list.RegionList"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.index.Index]":
        _token = next_token
        while True:
            _response = await self.list_service_indexes(
                config_overrides=config_overrides,
                regions=regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("indexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_service_views_output.ListServiceViewsOutput":
        """<p>Lists all Resource Explorer service views available in the current Amazon Web Services account. This operation returns the ARNs of available service views.</p>

        Args:
            max_results: <p>The maximum number of service view results to return in a single response. Valid values are between <code>1</code> and <code>50</code>.</p>
            next_token: <p>The pagination token from a previous <code>ListServiceViews</code> response. Use this token to retrieve the next set of results.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_service_views_input.ListServiceViewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_service_views_output.ListServiceViewsOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_service_views

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_service_views.async_list_service_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_service_views_input.ListServiceViewsInput = {}  # type: ignore[typeddict-item]
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

    async def iter_list_service_views(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[str]":
        _token = next_token
        while True:
            _response = await self.list_service_views(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_views",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_streaming_access_for_services(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_streaming_access_for_services_output.ListStreamingAccessForServicesOutput":
        """<p>Returns a list of Amazon Web Services services that have been granted streaming access to your Resource Explorer data. Streaming access allows Amazon Web Services services to receive real-time updates about your resources as they are indexed by Resource Explorer.</p>

        Args:
            max_results: <p>The maximum number of streaming access entries to return in the response. If there are more results available, the response includes a NextToken value that you can use in a subsequent call to get the next set of results. The value must be between 1 and 50. If you don't specify a value, the default is 50.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_streaming_access_for_services_input.ListStreamingAccessForServicesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_streaming_access_for_services_output.ListStreamingAccessForServicesOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_streaming_access_for_services

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_streaming_access_for_services.async_list_streaming_access_for_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_streaming_access_for_services_input.ListStreamingAccessForServicesInput = {}  # type: ignore[typeddict-item]
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

    async def iter_list_streaming_access_for_services(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.streaming_access_details.StreamingAccessDetails]":
        _token = next_token
        while True:
            _response = await self.list_streaming_access_for_services(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("streaming_access_for_services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_supported_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_supported_resource_types_output.ListSupportedResourceTypesOutput":
        """<p>Retrieves a list of all resource types currently supported by Amazon Web Services Resource Explorer.</p>

        Args:
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_supported_resource_types_input.ListSupportedResourceTypesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_supported_resource_types_output.ListSupportedResourceTypesOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_supported_resource_types

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_supported_resource_types.async_list_supported_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_supported_resource_types_input.ListSupportedResourceTypesInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_supported_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.supported_resource_type.SupportedResourceType]":
        _token = next_token
        while True:
            _response = await self.list_supported_resource_types(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resource_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "aws_sdk_resource_explorer_2.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>Lists the tags that are attached to the specified resource.</p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view or index that you want to attach tags to.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search(
        self,
        query_string: "aws_sdk_resource_explorer_2.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_resource_explorer_2.types.search_output.SearchOutput":
        r"""<p>Searches for resources and displays details about all resources that match the specified criteria. You must specify a query string.</p> <p>All search queries must use a view. If you don't explicitly specify a view, then Amazon Web Services Resource Explorer uses the default view for the Amazon Web Services Region in which you call this operation. The results are the logical intersection of the results that match both the <code>QueryString</code> parameter supplied to this operation and the <code>SearchFilter</code> parameter attached to the view.</p> <p>For the complete syntax supported by the <code>QueryString</code> parameter, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html\">Search query syntax reference for Resource Explorer</a>.</p> <p>If your search results are empty, or are missing results that you think should be there, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/troubleshooting_search.html\">Troubleshooting Resource Explorer search</a>.</p>

        Args:
            query_string: <p>A string that includes keywords and filters that specify the resources that you want to include in the results.</p> <p>For the complete syntax supported by the <code>QueryString</code> parameter, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\">Search query syntax reference for Resource Explorer</a>.</p> <p>The search is completely case insensitive. You can specify an empty string to return all results up to the limit of 1,000 total results.</p> <note> <p>The operation can return only the first 1,000 results. If the resource you want is not included, then use a different value for <code>QueryString</code> to refine the results.</p> </note>
            max_results: <p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>
            view_arn: <p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon resource name (ARN)</a> of the view to use for the query. If you don't specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn't have a default view or if you don't have permission to use the default view, then the operation fails with a <code>401 Unauthorized</code> exception.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.search_input.SearchInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.search_output.SearchOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.search

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.search.async_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.search_input.SearchInput = {}  # type: ignore[typeddict-item]
        input_["query_string"] = query_string
        if max_results is not None:
            input_["max_results"] = max_results
        if view_arn is not None:
            input_["view_arn"] = view_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_search(
        self,
        query_string: "aws_sdk_resource_explorer_2.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        max_results: Optional[int] = None,
        view_arn: Optional[str] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_resource_explorer_2.types.resource.Resource]":
        _token = next_token
        while True:
            _response = await self.search(
                query_string,
                config_overrides=config_overrides,
                max_results=max_results,
                view_arn=view_arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def tag_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
        tags: Optional["aws_sdk_resource_explorer_2.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_resource_explorer_2.types.tag_resource_output.TagResourceOutput":
        """<p>Adds one or more tag key and value pairs to an Amazon Web Services Resource Explorer view or index.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the view or index that you want to attach tags to.</p>
            tags: <p>A list of tag key and value pairs that you want to attach to the specified view or index.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.conflict_exception.ConflictException: <p>If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this Amazon Web Services Region.</p> <p>If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current Amazon Web Services Region.</p> <p>If you attempted to update an index type to <code>AGGREGATOR</code>, then the request failed because you already have an <code>AGGREGATOR</code> index in a different Amazon Web Services Region.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "aws_sdk_resource_explorer_2.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncResourceExplorer2ClientConfig] = None,
    ) -> "aws_sdk_resource_explorer_2.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tag key and value pairs from an Amazon Web Services Resource Explorer view or index.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the view or index that you want to remove tags from.</p>
            tag_keys: <p>A list of the keys for the tags that you want to remove from the specified view or index.</p>

        Raises:
            aws_sdk_resource_explorer_2.errors.access_denied_exception.AccessDeniedException: <p>The credentials that you used to call this operation don't have the minimum required permissions.</p>
            aws_sdk_resource_explorer_2.errors.internal_server_exception.InternalServerException: <p>The request failed because of internal service error. Try your request again later.</p>
            aws_sdk_resource_explorer_2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.</p>
            aws_sdk_resource_explorer_2.errors.throttling_exception.ThrottlingException: <p>The request failed because you exceeded a rate limit for this operation. For more information, see <a href=\"https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html\">Quotas for Resource Explorer</a>.</p>
            aws_sdk_resource_explorer_2.errors.unauthorized_exception.UnauthorizedException: <p>The principal making the request isn't permitted to perform the operation.</p>
            aws_sdk_resource_explorer_2.errors.validation_exception.ValidationException: <p>You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.</p>
            aws_sdk_resource_explorer_2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_resource_explorer_2.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_resource_explorer_2.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_resource_explorer_2._operations.resource_explorer.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_resource_explorer_2._operations.resource_explorer.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_resource_explorer_2.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
