"""Generated from Smithy shape ``com.amazonaws.appintegrations#AmazonAppIntegrationService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_appintegrations._auth._signers
import aws_sdk_appintegrations._auth._sigv4
from aws_sdk_appintegrations._auth._identity import Credentials
from aws_sdk_appintegrations._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_appintegrations._auth._zapros_handler import AuthMiddleware
from aws_sdk_appintegrations._pagination import resolve_path as _resolve_path
from aws_sdk_appintegrations._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_association_summary
    import aws_sdk_appintegrations.types.application_config
    import aws_sdk_appintegrations.types.application_name
    import aws_sdk_appintegrations.types.application_namespace
    import aws_sdk_appintegrations.types.application_source_config
    import aws_sdk_appintegrations.types.application_summary
    import aws_sdk_appintegrations.types.application_type
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.arn_or_uuid
    import aws_sdk_appintegrations.types.boolean
    import aws_sdk_appintegrations.types.client_association_metadata
    import aws_sdk_appintegrations.types.client_id
    import aws_sdk_appintegrations.types.create_application_request
    import aws_sdk_appintegrations.types.create_application_response
    import aws_sdk_appintegrations.types.create_data_integration_association_request
    import aws_sdk_appintegrations.types.create_data_integration_association_response
    import aws_sdk_appintegrations.types.create_data_integration_request
    import aws_sdk_appintegrations.types.create_data_integration_response
    import aws_sdk_appintegrations.types.create_event_integration_request
    import aws_sdk_appintegrations.types.create_event_integration_response
    import aws_sdk_appintegrations.types.data_integration_association_summary
    import aws_sdk_appintegrations.types.data_integration_summary
    import aws_sdk_appintegrations.types.delete_application_request
    import aws_sdk_appintegrations.types.delete_application_response
    import aws_sdk_appintegrations.types.delete_data_integration_request
    import aws_sdk_appintegrations.types.delete_data_integration_response
    import aws_sdk_appintegrations.types.delete_event_integration_request
    import aws_sdk_appintegrations.types.delete_event_integration_response
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.destination_uri
    import aws_sdk_appintegrations.types.event_bridge_bus
    import aws_sdk_appintegrations.types.event_filter
    import aws_sdk_appintegrations.types.event_integration
    import aws_sdk_appintegrations.types.event_integration_association
    import aws_sdk_appintegrations.types.execution_configuration
    import aws_sdk_appintegrations.types.file_configuration
    import aws_sdk_appintegrations.types.get_application_request
    import aws_sdk_appintegrations.types.get_application_response
    import aws_sdk_appintegrations.types.get_data_integration_request
    import aws_sdk_appintegrations.types.get_data_integration_response
    import aws_sdk_appintegrations.types.get_event_integration_request
    import aws_sdk_appintegrations.types.get_event_integration_response
    import aws_sdk_appintegrations.types.idempotency_token
    import aws_sdk_appintegrations.types.identifier
    import aws_sdk_appintegrations.types.iframe_config
    import aws_sdk_appintegrations.types.initialization_timeout
    import aws_sdk_appintegrations.types.list_application_associations_request
    import aws_sdk_appintegrations.types.list_application_associations_response
    import aws_sdk_appintegrations.types.list_applications_request
    import aws_sdk_appintegrations.types.list_applications_response
    import aws_sdk_appintegrations.types.list_data_integration_associations_request
    import aws_sdk_appintegrations.types.list_data_integration_associations_response
    import aws_sdk_appintegrations.types.list_data_integrations_request
    import aws_sdk_appintegrations.types.list_data_integrations_response
    import aws_sdk_appintegrations.types.list_event_integration_associations_request
    import aws_sdk_appintegrations.types.list_event_integration_associations_response
    import aws_sdk_appintegrations.types.list_event_integrations_request
    import aws_sdk_appintegrations.types.list_event_integrations_response
    import aws_sdk_appintegrations.types.list_tags_for_resource_request
    import aws_sdk_appintegrations.types.list_tags_for_resource_response
    import aws_sdk_appintegrations.types.max_results
    import aws_sdk_appintegrations.types.name
    import aws_sdk_appintegrations.types.next_token
    import aws_sdk_appintegrations.types.non_blank_string
    import aws_sdk_appintegrations.types.object_configuration
    import aws_sdk_appintegrations.types.permission_list
    import aws_sdk_appintegrations.types.publication_list
    import aws_sdk_appintegrations.types.schedule_configuration
    import aws_sdk_appintegrations.types.source_uri
    import aws_sdk_appintegrations.types.subscription_list
    import aws_sdk_appintegrations.types.tag_key_list
    import aws_sdk_appintegrations.types.tag_map
    import aws_sdk_appintegrations.types.tag_resource_request
    import aws_sdk_appintegrations.types.tag_resource_response
    import aws_sdk_appintegrations.types.untag_resource_request
    import aws_sdk_appintegrations.types.untag_resource_response
    import aws_sdk_appintegrations.types.update_application_request
    import aws_sdk_appintegrations.types.update_application_response
    import aws_sdk_appintegrations.types.update_data_integration_association_request
    import aws_sdk_appintegrations.types.update_data_integration_association_response
    import aws_sdk_appintegrations.types.update_data_integration_request
    import aws_sdk_appintegrations.types.update_data_integration_response
    import aws_sdk_appintegrations.types.update_event_integration_request
    import aws_sdk_appintegrations.types.update_event_integration_response


class AsyncAppIntegrationsClientConfig(TypedDict, total=False):
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


class AsyncAppIntegrationsClient:
    """A client for the ``AppIntegrations`` service.

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
        self.config = AsyncAppIntegrationsClientConfig(
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
        self, config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAppIntegrationsClientConfig = config_overrides or {}
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

    async def create_application(
        self,
        name: "aws_sdk_appintegrations.types.application_name.ApplicationName",
        namespace: "aws_sdk_appintegrations.types.application_namespace.ApplicationNamespace",
        application_source_config: "aws_sdk_appintegrations.types.application_source_config.ApplicationSourceConfig",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_appintegrations.types.description.Description"
        ] = None,
        subscriptions: Optional[
            "aws_sdk_appintegrations.types.subscription_list.SubscriptionList"
        ] = None,
        publications: Optional[
            "aws_sdk_appintegrations.types.publication_list.PublicationList"
        ] = None,
        client_token: Optional[
            "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_appintegrations.types.tag_map.TagMap"] = None,
        permissions: Optional[
            "aws_sdk_appintegrations.types.permission_list.PermissionList"
        ] = None,
        is_service: Optional["aws_sdk_appintegrations.types.boolean.Boolean"] = None,
        initialization_timeout: Optional[
            "aws_sdk_appintegrations.types.initialization_timeout.InitializationTimeout"
        ] = None,
        application_config: Optional[
            "aws_sdk_appintegrations.types.application_config.ApplicationConfig"
        ] = None,
        iframe_config: Optional[
            "aws_sdk_appintegrations.types.iframe_config.IframeConfig"
        ] = None,
        application_type: Optional[
            "aws_sdk_appintegrations.types.application_type.ApplicationType"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.create_application_response.CreateApplicationResponse":
        """<p>Creates and persists an Application resource.</p>

        Args:
            name: <p>The name of the application.</p>
            namespace: <p>The namespace of the application.</p>
            description: <p>The description of the application.</p>
            application_source_config: <p>The configuration for where the application should be loaded from.</p>
            subscriptions: <p>The events that the application subscribes.</p>
            publications: <p>The events that the application publishes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
            permissions: <p>The configuration of events or requests that the application has access to.</p>
            is_service: <p>Indicates whether the application is a service.</p>
            initialization_timeout: <p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>
            application_config: <p>The configuration settings for the application.</p>
            iframe_config: <p>The iframe configuration for the application.</p>
            application_type: <p>The type of application.</p>

        Examples:
            To create an application
            The following creates an application named My Application with access url https://example.com.

            >>> await client.create_application(name='My Application', namespace='myapplication', description='My first application.', application_source_config={'ExternalUrlConfig': {'AccessUrl': 'https://example.com'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.create_application_response.CreateApplicationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.create_application

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["namespace"] = namespace
        if description is not None:
            input["description"] = description
        input["application_source_config"] = application_source_config
        if subscriptions is not None:
            input["subscriptions"] = subscriptions
        if publications is not None:
            input["publications"] = publications
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags
        if permissions is not None:
            input["permissions"] = permissions
        if is_service is not None:
            input["is_service"] = is_service
        if initialization_timeout is not None:
            input["initialization_timeout"] = initialization_timeout
        if application_config is not None:
            input["application_config"] = application_config
        if iframe_config is not None:
            input["iframe_config"] = iframe_config
        if application_type is not None:
            input["application_type"] = application_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_data_integration(
        self,
        name: "aws_sdk_appintegrations.types.name.Name",
        kms_key: "aws_sdk_appintegrations.types.non_blank_string.NonBlankString",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_appintegrations.types.description.Description"
        ] = None,
        source_uri: Optional[
            "aws_sdk_appintegrations.types.source_uri.SourceURI"
        ] = None,
        schedule_config: Optional[
            "aws_sdk_appintegrations.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        tags: Optional["aws_sdk_appintegrations.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        file_configuration: Optional[
            "aws_sdk_appintegrations.types.file_configuration.FileConfiguration"
        ] = None,
        object_configuration: Optional[
            "aws_sdk_appintegrations.types.object_configuration.ObjectConfiguration"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.create_data_integration_response.CreateDataIntegrationResponse":
        """<p>Creates and persists a DataIntegration resource.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <code>CreateDataIntegration</code> API.</p> </note>

        Args:
            name: <p>The name of the DataIntegration.</p>
            description: <p>A description of the DataIntegration.</p>
            kms_key: <p>The KMS key ARN for the DataIntegration.</p>
            source_uri: <p>The URI of the data source.</p>
            schedule_config: <p>The name of the data and how often it should be pulled from the source.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            file_configuration: <p>The configuration for what files should be pulled from the source.</p>
            object_configuration: <p>The configuration for what data should be pulled from the source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.create_data_integration_request.CreateDataIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.create_data_integration_response.CreateDataIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.create_data_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.create_data_integration.async_create_data_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.create_data_integration_request.CreateDataIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["kms_key"] = kms_key
        if source_uri is not None:
            input["source_uri"] = source_uri
        if schedule_config is not None:
            input["schedule_config"] = schedule_config
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token
        if file_configuration is not None:
            input["file_configuration"] = file_configuration
        if object_configuration is not None:
            input["object_configuration"] = object_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_data_integration_association(
        self,
        data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        client_id: Optional["aws_sdk_appintegrations.types.client_id.ClientId"] = None,
        object_configuration: Optional[
            "aws_sdk_appintegrations.types.object_configuration.ObjectConfiguration"
        ] = None,
        destination_uri: Optional[
            "aws_sdk_appintegrations.types.destination_uri.DestinationURI"
        ] = None,
        client_association_metadata: Optional[
            "aws_sdk_appintegrations.types.client_association_metadata.ClientAssociationMetadata"
        ] = None,
        client_token: Optional[
            "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        execution_configuration: Optional[
            "aws_sdk_appintegrations.types.execution_configuration.ExecutionConfiguration"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.create_data_integration_association_response.CreateDataIntegrationAssociationResponse":
        """<p>Creates and persists a DataIntegrationAssociation resource.</p>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
            client_id: <p>The identifier for the client that is associated with the DataIntegration association.</p>
            destination_uri: <p>The URI of the data destination.</p>
            client_association_metadata: <p>The mapping of metadata to be extracted from the data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            execution_configuration: <p>The configuration for how the files should be pulled from the source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.create_data_integration_association_request.CreateDataIntegrationAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.create_data_integration_association_response.CreateDataIntegrationAssociationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.create_data_integration_association

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.create_data_integration_association.async_create_data_integration_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.create_data_integration_association_request.CreateDataIntegrationAssociationRequest = {}  # type: ignore[typeddict-item]
        input["data_integration_identifier"] = data_integration_identifier
        if client_id is not None:
            input["client_id"] = client_id
        if object_configuration is not None:
            input["object_configuration"] = object_configuration
        if destination_uri is not None:
            input["destination_uri"] = destination_uri
        if client_association_metadata is not None:
            input["client_association_metadata"] = client_association_metadata
        if client_token is not None:
            input["client_token"] = client_token
        if execution_configuration is not None:
            input["execution_configuration"] = execution_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_event_integration(
        self,
        name: "aws_sdk_appintegrations.types.name.Name",
        event_filter: "aws_sdk_appintegrations.types.event_filter.EventFilter",
        event_bridge_bus: "aws_sdk_appintegrations.types.event_bridge_bus.EventBridgeBus",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_appintegrations.types.description.Description"
        ] = None,
        client_token: Optional[
            "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["aws_sdk_appintegrations.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_appintegrations.types.create_event_integration_response.CreateEventIntegrationResponse":
        """<p>Creates an EventIntegration, given a specified name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that pushes events to that bus. No objects are created in the your account, only metadata that is persisted on the EventIntegration control plane.</p>

        Args:
            name: <p>The name of the event integration.</p>
            description: <p>The description of the event integration.</p>
            event_filter: <p>The event filter.</p>
            event_bridge_bus: <p>The EventBridge bus.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.create_event_integration_request.CreateEventIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.create_event_integration_response.CreateEventIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.create_event_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.create_event_integration.async_create_event_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.create_event_integration_request.CreateEventIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        input["event_filter"] = event_filter
        input["event_bridge_bus"] = event_bridge_bus
        if client_token is not None:
            input["client_token"] = client_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_application(
        self,
        arn: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes the Application. Only Applications that don't have any Application Associations can be deleted.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Application.</p>

        Examples:
            To delete an application
            The following deletes an application.

            >>> await client.delete_application(arn='arn:aws:app-integrations:us-west-2:0123456789012:application/98542c53-e8ac-4570-9c85-c6552c8d9c5e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.delete_application

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_data_integration(
        self,
        data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.delete_data_integration_response.DeleteDataIntegrationResponse":
        """<p>Deletes the DataIntegration. Only DataIntegrations that don't have any DataIntegrationAssociations can be deleted. Deleting a DataIntegration also deletes the underlying Amazon AppFlow flow and service linked role. </p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href=\"https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\">CreateDataIntegration</a> API.</p> </note>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.delete_data_integration_request.DeleteDataIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.delete_data_integration_response.DeleteDataIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.delete_data_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.delete_data_integration.async_delete_data_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.delete_data_integration_request.DeleteDataIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["data_integration_identifier"] = data_integration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_event_integration(
        self,
        name: "aws_sdk_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.delete_event_integration_response.DeleteEventIntegrationResponse":
        """<p>Deletes the specified existing event integration. If the event integration is associated with clients, the request is rejected.</p>

        Args:
            name: <p>The name of the event integration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.delete_event_integration_request.DeleteEventIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.delete_event_integration_response.DeleteEventIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.delete_event_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.delete_event_integration.async_delete_event_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.delete_event_integration_request.DeleteEventIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_application(
        self,
        arn: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> (
        "aws_sdk_appintegrations.types.get_application_response.GetApplicationResponse"
    ):
        """<p>Get an Application resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Application.</p>

        Examples:
            To get an application
            The following retrives an application.

            >>> await client.get_application(arn='arn:aws:app-integrations:us-west-2:0123456789012:application/98542c53-e8ac-4570-9c85-c6552c8d9c5e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.get_application_response.GetApplicationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.get_application

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.get_application_request.GetApplicationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_data_integration(
        self,
        identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.get_data_integration_response.GetDataIntegrationResponse":
        """<p>Returns information about the DataIntegration.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href=\"https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\">CreateDataIntegration</a> API.</p> </note>

        Args:
            identifier: <p>A unique identifier.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.get_data_integration_request.GetDataIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.get_data_integration_response.GetDataIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.get_data_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.get_data_integration.async_get_data_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.get_data_integration_request.GetDataIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_event_integration(
        self,
        name: "aws_sdk_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.get_event_integration_response.GetEventIntegrationResponse":
        """<p>Returns information about the event integration.</p>

        Args:
            name: <p>The name of the event integration. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.get_event_integration_request.GetEventIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.get_event_integration_response.GetEventIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.get_event_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.get_event_integration.async_get_event_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.get_event_integration_request.GetEventIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_application_associations(
        self,
        application_id: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.list_application_associations_response.ListApplicationAssociationsResponse":
        """<p>Returns a paginated list of application associations for an application.</p>

        Args:
            application_id: <p>A unique identifier for the Application.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Examples:
            To list application associations of an application
            The following retrives application associations of an application

            >>> await client.list_application_associations(application_id='98542c53-e8ac-4570-9c85-c6552c8d9c5e')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_application_associations_request.ListApplicationAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_application_associations_response.ListApplicationAssociationsResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_application_associations

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_application_associations.async_list_application_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_application_associations_request.ListApplicationAssociationsRequest = {}  # type: ignore[typeddict-item]
        input["application_id"] = application_id
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_application_associations(
        self,
        application_id: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_appintegrations.types.application_association_summary.ApplicationAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_application_associations(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
        application_type: Optional[
            "aws_sdk_appintegrations.types.application_type.ApplicationType"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists applications in the account.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            application_type: <p>The type of application.</p>

        Examples:
            To list applications in the account
            The following lists application summary in the account.

            >>> await client.list_applications(max_results=1)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_applications

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results
        if application_type is not None:
            input["application_type"] = application_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
        application_type: Optional[
            "aws_sdk_appintegrations.types.application_type.ApplicationType"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_appintegrations.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                application_type=application_type,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_integration_associations(
        self,
        data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.list_data_integration_associations_response.ListDataIntegrationAssociationsResponse":
        """<p>Returns a paginated list of DataIntegration associations in the account.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href=\"https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\">CreateDataIntegration</a> API.</p> </note>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_data_integration_associations_request.ListDataIntegrationAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_data_integration_associations_response.ListDataIntegrationAssociationsResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_data_integration_associations

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_data_integration_associations.async_list_data_integration_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_data_integration_associations_request.ListDataIntegrationAssociationsRequest = {}  # type: ignore[typeddict-item]
        input["data_integration_identifier"] = data_integration_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_data_integration_associations(
        self,
        data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_appintegrations.types.data_integration_association_summary.DataIntegrationAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_integration_associations(
                data_integration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_integration_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_integrations(
        self,
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.list_data_integrations_response.ListDataIntegrationsResponse":
        """<p>Returns a paginated list of DataIntegrations in the account.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href=\"https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\">CreateDataIntegration</a> API.</p> </note>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_data_integrations_request.ListDataIntegrationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_data_integrations_response.ListDataIntegrationsResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_data_integrations

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_data_integrations.async_list_data_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_data_integrations_request.ListDataIntegrationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_data_integrations(
        self,
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_appintegrations.types.data_integration_summary.DataIntegrationSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_integrations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_integrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_event_integration_associations(
        self,
        event_integration_name: "aws_sdk_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.list_event_integration_associations_response.ListEventIntegrationAssociationsResponse":
        """<p>Returns a paginated list of event integration associations in the account. </p>

        Args:
            event_integration_name: <p>The name of the event integration. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_event_integration_associations_request.ListEventIntegrationAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_event_integration_associations_response.ListEventIntegrationAssociationsResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_event_integration_associations

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_event_integration_associations.async_list_event_integration_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_event_integration_associations_request.ListEventIntegrationAssociationsRequest = {}  # type: ignore[typeddict-item]
        input["event_integration_name"] = event_integration_name
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_event_integration_associations(
        self,
        event_integration_name: "aws_sdk_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_appintegrations.types.event_integration_association.EventIntegrationAssociation]":
        _token = next_token
        while True:
            _response = await self.list_event_integration_associations(
                event_integration_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_integration_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_event_integrations(
        self,
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.list_event_integrations_response.ListEventIntegrationsResponse":
        """<p>Returns a paginated list of event integrations in the account.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_event_integrations_request.ListEventIntegrationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_event_integrations_response.ListEventIntegrationsResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_event_integrations

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_event_integrations.async_list_event_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_event_integrations_request.ListEventIntegrationsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_event_integrations(
        self,
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_appintegrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_appintegrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_appintegrations.types.event_integration.EventIntegration]":
        _token = next_token
        while True:
            _response = await self.list_event_integrations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_integrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_appintegrations.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_appintegrations.types.arn.Arn",
        tags: "aws_sdk_appintegrations.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_appintegrations.types.arn.Arn",
        tag_keys: "aws_sdk_appintegrations.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_application(
        self,
        arn: "aws_sdk_appintegrations.types.arn_or_uuid.ArnOrUUID",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        name: Optional[
            "aws_sdk_appintegrations.types.application_name.ApplicationName"
        ] = None,
        description: Optional[
            "aws_sdk_appintegrations.types.description.Description"
        ] = None,
        application_source_config: Optional[
            "aws_sdk_appintegrations.types.application_source_config.ApplicationSourceConfig"
        ] = None,
        subscriptions: Optional[
            "aws_sdk_appintegrations.types.subscription_list.SubscriptionList"
        ] = None,
        publications: Optional[
            "aws_sdk_appintegrations.types.publication_list.PublicationList"
        ] = None,
        permissions: Optional[
            "aws_sdk_appintegrations.types.permission_list.PermissionList"
        ] = None,
        is_service: Optional["aws_sdk_appintegrations.types.boolean.Boolean"] = None,
        initialization_timeout: Optional[
            "aws_sdk_appintegrations.types.initialization_timeout.InitializationTimeout"
        ] = None,
        application_config: Optional[
            "aws_sdk_appintegrations.types.application_config.ApplicationConfig"
        ] = None,
        iframe_config: Optional[
            "aws_sdk_appintegrations.types.iframe_config.IframeConfig"
        ] = None,
        application_type: Optional[
            "aws_sdk_appintegrations.types.application_type.ApplicationType"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates and persists an Application resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Application.</p>
            name: <p>The name of the application.</p>
            description: <p>The description of the application.</p>
            application_source_config: <p>The configuration for where the application should be loaded from.</p>
            subscriptions: <p>The events that the application subscribes.</p>
            publications: <p>The events that the application publishes.</p>
            permissions: <p>The configuration of events or requests that the application has access to.</p>
            is_service: <p>Indicates whether the application is a service.</p>
            initialization_timeout: <p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>
            application_config: <p>The configuration settings for the application.</p>
            iframe_config: <p>The iframe configuration for the application.</p>
            application_type: <p>The type of application.</p>

        Examples:
            To update an application
            The following updates an existing application named with a new name.

            >>> await client.update_application(arn='arn:aws:app-integrations:us-west-2:0123456789012:application/98542c53-e8ac-4570-9c85-c6552c8d9c5e', name='My New Application Name')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.update_application_response.UpdateApplicationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.update_application

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input["arn"] = arn
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if application_source_config is not None:
            input["application_source_config"] = application_source_config
        if subscriptions is not None:
            input["subscriptions"] = subscriptions
        if publications is not None:
            input["publications"] = publications
        if permissions is not None:
            input["permissions"] = permissions
        if is_service is not None:
            input["is_service"] = is_service
        if initialization_timeout is not None:
            input["initialization_timeout"] = initialization_timeout
        if application_config is not None:
            input["application_config"] = application_config
        if iframe_config is not None:
            input["iframe_config"] = iframe_config
        if application_type is not None:
            input["application_type"] = application_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_data_integration(
        self,
        identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        name: Optional["aws_sdk_appintegrations.types.name.Name"] = None,
        description: Optional[
            "aws_sdk_appintegrations.types.description.Description"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.update_data_integration_response.UpdateDataIntegrationResponse":
        """<p>Updates the description of a DataIntegration.</p> <note> <p>You cannot create a DataIntegration association for a DataIntegration that has been previously associated. Use a different DataIntegration, or recreate the DataIntegration using the <a href=\"https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html\">CreateDataIntegration</a> API.</p> </note>

        Args:
            identifier: <p>A unique identifier for the DataIntegration.</p>
            name: <p>The name of the DataIntegration.</p>
            description: <p>A description of the DataIntegration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.update_data_integration_request.UpdateDataIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.update_data_integration_response.UpdateDataIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.update_data_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.update_data_integration.async_update_data_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.update_data_integration_request.UpdateDataIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["identifier"] = identifier
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_data_integration_association(
        self,
        data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        data_integration_association_identifier: "aws_sdk_appintegrations.types.identifier.Identifier",
        execution_configuration: "aws_sdk_appintegrations.types.execution_configuration.ExecutionConfiguration",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
    ) -> "aws_sdk_appintegrations.types.update_data_integration_association_response.UpdateDataIntegrationAssociationResponse":
        """<p>Updates and persists a DataIntegrationAssociation resource.</p> <note> <p> Updating a DataIntegrationAssociation with ExecutionConfiguration will rerun the on-demand job. </p> </note>

        Args:
            data_integration_identifier: <p>A unique identifier for the DataIntegration.</p>
            data_integration_association_identifier: <p>A unique identifier. of the DataIntegrationAssociation resource</p>
            execution_configuration: <p>The configuration for how the files should be pulled from the source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.update_data_integration_association_request.UpdateDataIntegrationAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.update_data_integration_association_response.UpdateDataIntegrationAssociationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.update_data_integration_association

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.update_data_integration_association.async_update_data_integration_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.update_data_integration_association_request.UpdateDataIntegrationAssociationRequest = {}  # type: ignore[typeddict-item]
        input["data_integration_identifier"] = data_integration_identifier
        input["data_integration_association_identifier"] = (
            data_integration_association_identifier
        )
        input["execution_configuration"] = execution_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_event_integration(
        self,
        name: "aws_sdk_appintegrations.types.name.Name",
        *,
        config_overrides: Optional[AsyncAppIntegrationsClientConfig] = None,
        description: Optional[
            "aws_sdk_appintegrations.types.description.Description"
        ] = None,
    ) -> "aws_sdk_appintegrations.types.update_event_integration_response.UpdateEventIntegrationResponse":
        """<p>Updates the description of an event integration.</p>

        Args:
            name: <p>The name of the event integration.</p>
            description: <p>The description of the event integration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_appintegrations.types.update_event_integration_request.UpdateEventIntegrationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_appintegrations.types.update_event_integration_response.UpdateEventIntegrationResponse"
        ]:
            import aws_sdk_appintegrations._operations.amazon_app_integration_service.update_event_integration

            (
                output,
                http_response,
            ) = await aws_sdk_appintegrations._operations.amazon_app_integration_service.update_event_integration.async_update_event_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_appintegrations.types.update_event_integration_request.UpdateEventIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description

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
