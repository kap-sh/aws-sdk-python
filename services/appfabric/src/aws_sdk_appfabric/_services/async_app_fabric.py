"""Generated from Smithy shape ``com.amazonaws.appfabric#FabricFrontEndService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_appfabric._auth._signers
import aws_sdk_appfabric._auth._sigv4
from aws_sdk_appfabric._auth._identity import Credentials
from aws_sdk_appfabric._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_appfabric._auth._zapros_handler import AuthMiddleware
from aws_sdk_appfabric._pagination import resolve_path as _resolve_path
from aws_sdk_appfabric._services._aws_config import aaws_config
from aws_sdk_appfabric._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.app_authorization_summary
    import aws_sdk_appfabric.types.app_bundle_summary
    import aws_sdk_appfabric.types.arn
    import aws_sdk_appfabric.types.auth_request
    import aws_sdk_appfabric.types.auth_type
    import aws_sdk_appfabric.types.batch_get_user_access_tasks_request
    import aws_sdk_appfabric.types.batch_get_user_access_tasks_response
    import aws_sdk_appfabric.types.connect_app_authorization_request
    import aws_sdk_appfabric.types.connect_app_authorization_response
    import aws_sdk_appfabric.types.create_app_authorization_request
    import aws_sdk_appfabric.types.create_app_authorization_response
    import aws_sdk_appfabric.types.create_app_bundle_request
    import aws_sdk_appfabric.types.create_app_bundle_response
    import aws_sdk_appfabric.types.create_ingestion_destination_request
    import aws_sdk_appfabric.types.create_ingestion_destination_response
    import aws_sdk_appfabric.types.create_ingestion_request
    import aws_sdk_appfabric.types.create_ingestion_response
    import aws_sdk_appfabric.types.credential
    import aws_sdk_appfabric.types.delete_app_authorization_request
    import aws_sdk_appfabric.types.delete_app_authorization_response
    import aws_sdk_appfabric.types.delete_app_bundle_request
    import aws_sdk_appfabric.types.delete_app_bundle_response
    import aws_sdk_appfabric.types.delete_ingestion_destination_request
    import aws_sdk_appfabric.types.delete_ingestion_destination_response
    import aws_sdk_appfabric.types.delete_ingestion_request
    import aws_sdk_appfabric.types.delete_ingestion_response
    import aws_sdk_appfabric.types.destination_configuration
    import aws_sdk_appfabric.types.email
    import aws_sdk_appfabric.types.get_app_authorization_request
    import aws_sdk_appfabric.types.get_app_authorization_response
    import aws_sdk_appfabric.types.get_app_bundle_request
    import aws_sdk_appfabric.types.get_app_bundle_response
    import aws_sdk_appfabric.types.get_ingestion_destination_request
    import aws_sdk_appfabric.types.get_ingestion_destination_response
    import aws_sdk_appfabric.types.get_ingestion_request
    import aws_sdk_appfabric.types.get_ingestion_response
    import aws_sdk_appfabric.types.identifier
    import aws_sdk_appfabric.types.ingestion_destination_summary
    import aws_sdk_appfabric.types.ingestion_summary
    import aws_sdk_appfabric.types.ingestion_type
    import aws_sdk_appfabric.types.list_app_authorizations_request
    import aws_sdk_appfabric.types.list_app_authorizations_response
    import aws_sdk_appfabric.types.list_app_bundles_request
    import aws_sdk_appfabric.types.list_app_bundles_response
    import aws_sdk_appfabric.types.list_ingestion_destinations_request
    import aws_sdk_appfabric.types.list_ingestion_destinations_response
    import aws_sdk_appfabric.types.list_ingestions_request
    import aws_sdk_appfabric.types.list_ingestions_response
    import aws_sdk_appfabric.types.list_tags_for_resource_request
    import aws_sdk_appfabric.types.list_tags_for_resource_response
    import aws_sdk_appfabric.types.max_results
    import aws_sdk_appfabric.types.processing_configuration
    import aws_sdk_appfabric.types.start_ingestion_request
    import aws_sdk_appfabric.types.start_ingestion_response
    import aws_sdk_appfabric.types.start_user_access_tasks_request
    import aws_sdk_appfabric.types.start_user_access_tasks_response
    import aws_sdk_appfabric.types.stop_ingestion_request
    import aws_sdk_appfabric.types.stop_ingestion_response
    import aws_sdk_appfabric.types.string255
    import aws_sdk_appfabric.types.string2048
    import aws_sdk_appfabric.types.tag_key_list
    import aws_sdk_appfabric.types.tag_list
    import aws_sdk_appfabric.types.tag_resource_request
    import aws_sdk_appfabric.types.tag_resource_response
    import aws_sdk_appfabric.types.task_id_list
    import aws_sdk_appfabric.types.tenant
    import aws_sdk_appfabric.types.tenant_identifier
    import aws_sdk_appfabric.types.untag_resource_request
    import aws_sdk_appfabric.types.untag_resource_response
    import aws_sdk_appfabric.types.update_app_authorization_request
    import aws_sdk_appfabric.types.update_app_authorization_response
    import aws_sdk_appfabric.types.update_ingestion_destination_request
    import aws_sdk_appfabric.types.update_ingestion_destination_response
    import aws_sdk_appfabric.types.uuid


class AsyncAppFabricClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncAppFabricClient:
    """A client for the ``AppFabric`` service.

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
        self._config = AsyncAppFabricClientConfig(
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
        self, config_overrides: Optional[AsyncAppFabricClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAppFabricClientConfig = config_overrides or {}
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

    async def batch_get_user_access_tasks(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        task_id_list: "aws_sdk_appfabric.types.task_id_list.TaskIdList",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.batch_get_user_access_tasks_response.BatchGetUserAccessTasksResponse":
        """<p>Gets user access details in a batch request.</p> <p>This action polls data from the tasks that are kicked off by the <code>StartUserAccessTasks</code> action.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            task_id_list: <p>The tasks IDs to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.batch_get_user_access_tasks_request.BatchGetUserAccessTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.batch_get_user_access_tasks_response.BatchGetUserAccessTasksResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.batch_get_user_access_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.batch_get_user_access_tasks.async_batch_get_user_access_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.batch_get_user_access_tasks_request.BatchGetUserAccessTasksRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["task_id_list"] = task_id_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def connect_app_authorization(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        auth_request: Optional[
            "aws_sdk_appfabric.types.auth_request.AuthRequest"
        ] = None,
    ) -> "aws_sdk_appfabric.types.connect_app_authorization_response.ConnectAppAuthorizationResponse":
        """<p>Establishes a connection between Amazon Web Services AppFabric and an application, which allows AppFabric to call the APIs of the application.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle that contains the app authorization to use for the request.</p>
            app_authorization_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>
            auth_request: <p>Contains OAuth2 authorization information.</p> <p>This is required if the app authorization for the request is configured with an OAuth2 (<code>oauth2</code>) authorization type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.connect_app_authorization_request.ConnectAppAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.connect_app_authorization_response.ConnectAppAuthorizationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.connect_app_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.connect_app_authorization.async_connect_app_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.connect_app_authorization_request.ConnectAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["app_authorization_identifier"] = app_authorization_identifier
        if auth_request is not None:
            input_["auth_request"] = auth_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_app_authorization(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app: "aws_sdk_appfabric.types.string255.String255",
        credential: "aws_sdk_appfabric.types.credential.Credential",
        tenant: "aws_sdk_appfabric.types.tenant.Tenant",
        auth_type: "aws_sdk_appfabric.types.auth_type.AuthType",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        client_token: Optional["aws_sdk_appfabric.types.uuid.UUID"] = None,
        tags: Optional["aws_sdk_appfabric.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_appfabric.types.create_app_authorization_response.CreateAppAuthorizationResponse":
        r"""<p>Creates an app authorization within an app bundle, which allows AppFabric to connect to an application.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            app: <p>The name of the application.</p> <p>Valid values are:</p> <ul> <li> <p> <code>SLACK</code> </p> </li> <li> <p> <code>ASANA</code> </p> </li> <li> <p> <code>JIRA</code> </p> </li> <li> <p> <code>M365</code> </p> </li> <li> <p> <code>M365AUDITLOGS</code> </p> </li> <li> <p> <code>ZOOM</code> </p> </li> <li> <p> <code>ZENDESK</code> </p> </li> <li> <p> <code>OKTA</code> </p> </li> <li> <p> <code>GOOGLE</code> </p> </li> <li> <p> <code>DROPBOX</code> </p> </li> <li> <p> <code>SMARTSHEET</code> </p> </li> <li> <p> <code>CISCO</code> </p> </li> </ul>
            credential: <p>Contains credentials for the application, such as an API key or OAuth2 client ID and secret.</p> <p>Specify credentials that match the authorization type for your request. For example, if the authorization type for your request is OAuth2 (<code>oauth2</code>), then you should provide only the OAuth2 credentials.</p>
            tenant: <p>Contains information about an application tenant, such as the application display name and identifier.</p>
            auth_type: <p>The authorization type for the app authorization.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.create_app_authorization_request.CreateAppAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.create_app_authorization_response.CreateAppAuthorizationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.create_app_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.create_app_authorization.async_create_app_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.create_app_authorization_request.CreateAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["app"] = app
        input_["credential"] = credential
        input_["tenant"] = tenant
        input_["auth_type"] = auth_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_app_bundle(
        self,
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        client_token: Optional["aws_sdk_appfabric.types.uuid.UUID"] = None,
        customer_managed_key_identifier: Optional[
            "aws_sdk_appfabric.types.identifier.Identifier"
        ] = None,
        tags: Optional["aws_sdk_appfabric.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_appfabric.types.create_app_bundle_response.CreateAppBundleResponse":
        r"""<p>Creates an app bundle to collect data from an application using AppFabric.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            customer_managed_key_identifier: <p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key to use to encrypt the application data. If this is not specified, an Amazon Web Services owned key is used for encryption.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.create_app_bundle_request.CreateAppBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.create_app_bundle_response.CreateAppBundleResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.create_app_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.create_app_bundle.async_create_app_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.create_app_bundle_request.CreateAppBundleRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        if customer_managed_key_identifier is not None:
            input_["customer_managed_key_identifier"] = customer_managed_key_identifier
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_ingestion(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app: "aws_sdk_appfabric.types.string255.String255",
        tenant_id: "aws_sdk_appfabric.types.tenant_identifier.TenantIdentifier",
        ingestion_type: "aws_sdk_appfabric.types.ingestion_type.IngestionType",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        client_token: Optional["aws_sdk_appfabric.types.uuid.UUID"] = None,
        tags: Optional["aws_sdk_appfabric.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_appfabric.types.create_ingestion_response.CreateIngestionResponse":
        r"""<p>Creates a data ingestion for an application.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            app: <p>The name of the application.</p> <p>Valid values are:</p> <ul> <li> <p> <code>SLACK</code> </p> </li> <li> <p> <code>ASANA</code> </p> </li> <li> <p> <code>JIRA</code> </p> </li> <li> <p> <code>M365</code> </p> </li> <li> <p> <code>M365AUDITLOGS</code> </p> </li> <li> <p> <code>ZOOM</code> </p> </li> <li> <p> <code>ZENDESK</code> </p> </li> <li> <p> <code>OKTA</code> </p> </li> <li> <p> <code>GOOGLE</code> </p> </li> <li> <p> <code>DROPBOX</code> </p> </li> <li> <p> <code>SMARTSHEET</code> </p> </li> <li> <p> <code>CISCO</code> </p> </li> </ul>
            tenant_id: <p>The ID of the application tenant.</p>
            ingestion_type: <p>The ingestion type.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.create_ingestion_request.CreateIngestionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.create_ingestion_response.CreateIngestionResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.create_ingestion

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.create_ingestion.async_create_ingestion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.create_ingestion_request.CreateIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["app"] = app
        input_["tenant_id"] = tenant_id
        input_["ingestion_type"] = ingestion_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_ingestion_destination(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        processing_configuration: "aws_sdk_appfabric.types.processing_configuration.ProcessingConfiguration",
        destination_configuration: "aws_sdk_appfabric.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        client_token: Optional["aws_sdk_appfabric.types.uuid.UUID"] = None,
        tags: Optional["aws_sdk_appfabric.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_appfabric.types.create_ingestion_destination_response.CreateIngestionDestinationResponse":
        r"""<p>Creates an ingestion destination, which specifies how an application's ingested data is processed by Amazon Web Services AppFabric and where it's delivered.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            processing_configuration: <p>Contains information about how ingested data is processed.</p>
            destination_configuration: <p>Contains information about the destination of ingested data.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.create_ingestion_destination_request.CreateIngestionDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.create_ingestion_destination_response.CreateIngestionDestinationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.create_ingestion_destination

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.create_ingestion_destination.async_create_ingestion_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.create_ingestion_destination_request.CreateIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier
        input_["processing_configuration"] = processing_configuration
        input_["destination_configuration"] = destination_configuration
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app_authorization(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.delete_app_authorization_response.DeleteAppAuthorizationResponse":
        """<p>Deletes an app authorization. You must delete the associated ingestion before you can delete an app authorization.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            app_authorization_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.delete_app_authorization_request.DeleteAppAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.delete_app_authorization_response.DeleteAppAuthorizationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.delete_app_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.delete_app_authorization.async_delete_app_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.delete_app_authorization_request.DeleteAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["app_authorization_identifier"] = app_authorization_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app_bundle(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.delete_app_bundle_response.DeleteAppBundleResponse":
        """<p>Deletes an app bundle. You must delete all associated app authorizations before you can delete an app bundle.</p>

        Args:
            app_bundle_identifier: <p>The ID or Amazon Resource Name (ARN) of the app bundle that needs to be deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.delete_app_bundle_request.DeleteAppBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.delete_app_bundle_response.DeleteAppBundleResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.delete_app_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.delete_app_bundle.async_delete_app_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.delete_app_bundle_request.DeleteAppBundleRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_ingestion(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.delete_ingestion_response.DeleteIngestionResponse":
        """<p>Deletes an ingestion. You must stop (disable) the ingestion and you must delete all associated ingestion destinations before you can delete an app ingestion.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.delete_ingestion_request.DeleteIngestionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.delete_ingestion_response.DeleteIngestionResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.delete_ingestion

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.delete_ingestion.async_delete_ingestion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.delete_ingestion_request.DeleteIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_ingestion_destination(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_destination_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.delete_ingestion_destination_response.DeleteIngestionDestinationResponse":
        """<p>Deletes an ingestion destination.</p> <p>This deletes the association between an ingestion and it's destination. It doesn't delete previously ingested data or the storage destination, such as the Amazon S3 bucket where the data is delivered. If the ingestion destination is deleted while the associated ingestion is enabled, the ingestion will fail and is eventually disabled.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            ingestion_destination_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.delete_ingestion_destination_request.DeleteIngestionDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.delete_ingestion_destination_response.DeleteIngestionDestinationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.delete_ingestion_destination

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.delete_ingestion_destination.async_delete_ingestion_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.delete_ingestion_destination_request.DeleteIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier
        input_["ingestion_destination_identifier"] = ingestion_destination_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_app_authorization(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.get_app_authorization_response.GetAppAuthorizationResponse":
        """<p>Returns information about an app authorization.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            app_authorization_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.get_app_authorization_request.GetAppAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.get_app_authorization_response.GetAppAuthorizationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.get_app_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.get_app_authorization.async_get_app_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.get_app_authorization_request.GetAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["app_authorization_identifier"] = app_authorization_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_app_bundle(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.get_app_bundle_response.GetAppBundleResponse":
        """<p>Returns information about an app bundle.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.get_app_bundle_request.GetAppBundleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.get_app_bundle_response.GetAppBundleResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.get_app_bundle

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.get_app_bundle.async_get_app_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.get_app_bundle_request.GetAppBundleRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ingestion(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.get_ingestion_response.GetIngestionResponse":
        """<p>Returns information about an ingestion.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.get_ingestion_request.GetIngestionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.get_ingestion_response.GetIngestionResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.get_ingestion

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.get_ingestion.async_get_ingestion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.get_ingestion_request.GetIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_ingestion_destination(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_destination_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.get_ingestion_destination_response.GetIngestionDestinationResponse":
        """<p>Returns information about an ingestion destination.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            ingestion_destination_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.get_ingestion_destination_request.GetIngestionDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.get_ingestion_destination_response.GetIngestionDestinationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.get_ingestion_destination

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.get_ingestion_destination.async_get_ingestion_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.get_ingestion_destination_request.GetIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier
        input_["ingestion_destination_identifier"] = ingestion_destination_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_app_authorizations(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_appfabric.types.string2048.String2048"] = None,
    ) -> "aws_sdk_appfabric.types.list_app_authorizations_response.ListAppAuthorizationsResponse":
        """<p>Returns a list of all app authorizations configured for an app bundle.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.list_app_authorizations_request.ListAppAuthorizationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.list_app_authorizations_response.ListAppAuthorizationsResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.list_app_authorizations

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.list_app_authorizations.async_list_app_authorizations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.list_app_authorizations_request.ListAppAuthorizationsRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
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

    async def iter_list_app_authorizations(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_appfabric.types.string2048.String2048"] = None,
    ) -> "AsyncIterator[aws_sdk_appfabric.types.app_authorization_summary.AppAuthorizationSummary]":
        _token = next_token
        while True:
            _response = await self.list_app_authorizations(
                app_bundle_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("app_authorization_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_app_bundles(
        self,
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_appfabric.types.string2048.String2048"] = None,
    ) -> "aws_sdk_appfabric.types.list_app_bundles_response.ListAppBundlesResponse":
        """<p>Returns a list of app bundles.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.list_app_bundles_request.ListAppBundlesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.list_app_bundles_response.ListAppBundlesResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.list_app_bundles

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.list_app_bundles.async_list_app_bundles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.list_app_bundles_request.ListAppBundlesRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_app_bundles(
        self,
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_appfabric.types.string2048.String2048"] = None,
    ) -> "AsyncIterator[aws_sdk_appfabric.types.app_bundle_summary.AppBundleSummary]":
        _token = next_token
        while True:
            _response = await self.list_app_bundles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("app_bundle_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ingestion_destinations(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_appfabric.types.list_ingestion_destinations_response.ListIngestionDestinationsResponse":
        """<p>Returns a list of all ingestion destinations configured for an ingestion.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.list_ingestion_destinations_request.ListIngestionDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.list_ingestion_destinations_response.ListIngestionDestinationsResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.list_ingestion_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.list_ingestion_destinations.async_list_ingestion_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.list_ingestion_destinations_request.ListIngestionDestinationsRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier
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

    async def iter_list_ingestion_destinations(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_appfabric.types.ingestion_destination_summary.IngestionDestinationSummary]":
        _token = next_token
        while True:
            _response = await self.list_ingestion_destinations(
                app_bundle_identifier,
                ingestion_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ingestion_destinations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ingestions(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_appfabric.types.list_ingestions_response.ListIngestionsResponse":
        """<p>Returns a list of all ingestions configured for an app bundle.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.list_ingestions_request.ListIngestionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.list_ingestions_response.ListIngestionsResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.list_ingestions

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.list_ingestions.async_list_ingestions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.list_ingestions_request.ListIngestionsRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
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

    async def iter_list_ingestions(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        max_results: Optional["aws_sdk_appfabric.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[aws_sdk_appfabric.types.ingestion_summary.IngestionSummary]":
        _token = next_token
        while True:
            _response = await self.list_ingestions(
                app_bundle_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ingestions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_appfabric.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_ingestion(
        self,
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.start_ingestion_response.StartIngestionResponse":
        """<p>Starts (enables) an ingestion, which collects data from an application.</p>

        Args:
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.start_ingestion_request.StartIngestionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.start_ingestion_response.StartIngestionResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.start_ingestion

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.start_ingestion.async_start_ingestion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.start_ingestion_request.StartIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["ingestion_identifier"] = ingestion_identifier
        input_["app_bundle_identifier"] = app_bundle_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_user_access_tasks(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        email: "aws_sdk_appfabric.types.email.Email",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.start_user_access_tasks_response.StartUserAccessTasksResponse":
        """<p>Starts the tasks to search user access status for a specific email address.</p> <p>The tasks are stopped when the user access status data is found. The tasks are terminated when the API calls to the application time out.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            email: <p>The email address of the target user.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.start_user_access_tasks_request.StartUserAccessTasksRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.start_user_access_tasks_response.StartUserAccessTasksResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.start_user_access_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.start_user_access_tasks.async_start_user_access_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.start_user_access_tasks_request.StartUserAccessTasksRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["email"] = email

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def stop_ingestion(
        self,
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.stop_ingestion_response.StopIngestionResponse":
        """<p>Stops (disables) an ingestion.</p>

        Args:
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.stop_ingestion_request.StopIngestionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.stop_ingestion_response.StopIngestionResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.stop_ingestion

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.stop_ingestion.async_stop_ingestion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.stop_ingestion_request.StopIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["ingestion_identifier"] = ingestion_identifier
        input_["app_bundle_identifier"] = app_bundle_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_appfabric.types.arn.Arn",
        tags: "aws_sdk_appfabric.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_appfabric.types.arn.Arn",
        tag_keys: "aws_sdk_appfabric.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_app_authorization(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
        credential: Optional["aws_sdk_appfabric.types.credential.Credential"] = None,
        tenant: Optional["aws_sdk_appfabric.types.tenant.Tenant"] = None,
    ) -> "aws_sdk_appfabric.types.update_app_authorization_response.UpdateAppAuthorizationResponse":
        """<p>Updates an app authorization within an app bundle, which allows AppFabric to connect to an application.</p> <p>If the app authorization was in a <code>connected</code> state, updating the app authorization will set it back to a <code>PendingConnect</code> state.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            app_authorization_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>
            credential: <p>Contains credentials for the application, such as an API key or OAuth2 client ID and secret.</p> <p>Specify credentials that match the authorization type of the app authorization to update. For example, if the authorization type of the app authorization is OAuth2 (<code>oauth2</code>), then you should provide only the OAuth2 credentials.</p>
            tenant: <p>Contains information about an application tenant, such as the application display name and identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.update_app_authorization_request.UpdateAppAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.update_app_authorization_response.UpdateAppAuthorizationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.update_app_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.update_app_authorization.async_update_app_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.update_app_authorization_request.UpdateAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["app_authorization_identifier"] = app_authorization_identifier
        if credential is not None:
            input_["credential"] = credential
        if tenant is not None:
            input_["tenant"] = tenant

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_ingestion_destination(
        self,
        app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        ingestion_destination_identifier: "aws_sdk_appfabric.types.identifier.Identifier",
        destination_configuration: "aws_sdk_appfabric.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[AsyncAppFabricClientConfig] = None,
    ) -> "aws_sdk_appfabric.types.update_ingestion_destination_response.UpdateIngestionDestinationResponse":
        """<p>Updates an ingestion destination, which specifies how an application's ingested data is processed by Amazon Web Services AppFabric and where it's delivered.</p>

        Args:
            app_bundle_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>
            ingestion_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion to use for the request.</p>
            ingestion_destination_identifier: <p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the ingestion destination to use for the request.</p>
            destination_configuration: <p>Contains information about the destination of ingested data.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appfabric.types.update_ingestion_destination_request.UpdateIngestionDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appfabric.types.update_ingestion_destination_response.UpdateIngestionDestinationResponse"
        ]:
            import aws_sdk_appfabric._operations.fabric_front_end_service.update_ingestion_destination

            (
                output,
                http_response,
            ) = await aws_sdk_appfabric._operations.fabric_front_end_service.update_ingestion_destination.async_update_ingestion_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_appfabric.types.update_ingestion_destination_request.UpdateIngestionDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["app_bundle_identifier"] = app_bundle_identifier
        input_["ingestion_identifier"] = ingestion_identifier
        input_["ingestion_destination_identifier"] = ingestion_destination_identifier
        input_["destination_configuration"] = destination_configuration

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
