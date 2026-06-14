"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#AWSEvents``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_cloudwatch_events._auth._signers
import aws_sdk_cloudwatch_events._auth._sigv4
from aws_sdk_cloudwatch_events._auth._identity import Credentials
from aws_sdk_cloudwatch_events._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudwatch_events._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudwatch_events._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.account_id
    import aws_sdk_cloudwatch_events.types.action
    import aws_sdk_cloudwatch_events.types.activate_event_source_request
    import aws_sdk_cloudwatch_events.types.api_destination_description
    import aws_sdk_cloudwatch_events.types.api_destination_http_method
    import aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second
    import aws_sdk_cloudwatch_events.types.api_destination_name
    import aws_sdk_cloudwatch_events.types.archive_description
    import aws_sdk_cloudwatch_events.types.archive_name
    import aws_sdk_cloudwatch_events.types.archive_state
    import aws_sdk_cloudwatch_events.types.arn
    import aws_sdk_cloudwatch_events.types.boolean
    import aws_sdk_cloudwatch_events.types.cancel_replay_request
    import aws_sdk_cloudwatch_events.types.cancel_replay_response
    import aws_sdk_cloudwatch_events.types.condition
    import aws_sdk_cloudwatch_events.types.connection_arn
    import aws_sdk_cloudwatch_events.types.connection_authorization_type
    import aws_sdk_cloudwatch_events.types.connection_description
    import aws_sdk_cloudwatch_events.types.connection_name
    import aws_sdk_cloudwatch_events.types.connection_state
    import aws_sdk_cloudwatch_events.types.create_api_destination_request
    import aws_sdk_cloudwatch_events.types.create_api_destination_response
    import aws_sdk_cloudwatch_events.types.create_archive_request
    import aws_sdk_cloudwatch_events.types.create_archive_response
    import aws_sdk_cloudwatch_events.types.create_connection_auth_request_parameters
    import aws_sdk_cloudwatch_events.types.create_connection_request
    import aws_sdk_cloudwatch_events.types.create_connection_response
    import aws_sdk_cloudwatch_events.types.create_event_bus_request
    import aws_sdk_cloudwatch_events.types.create_event_bus_response
    import aws_sdk_cloudwatch_events.types.create_partner_event_source_request
    import aws_sdk_cloudwatch_events.types.create_partner_event_source_response
    import aws_sdk_cloudwatch_events.types.deactivate_event_source_request
    import aws_sdk_cloudwatch_events.types.deauthorize_connection_request
    import aws_sdk_cloudwatch_events.types.deauthorize_connection_response
    import aws_sdk_cloudwatch_events.types.delete_api_destination_request
    import aws_sdk_cloudwatch_events.types.delete_api_destination_response
    import aws_sdk_cloudwatch_events.types.delete_archive_request
    import aws_sdk_cloudwatch_events.types.delete_archive_response
    import aws_sdk_cloudwatch_events.types.delete_connection_request
    import aws_sdk_cloudwatch_events.types.delete_connection_response
    import aws_sdk_cloudwatch_events.types.delete_event_bus_request
    import aws_sdk_cloudwatch_events.types.delete_partner_event_source_request
    import aws_sdk_cloudwatch_events.types.delete_rule_request
    import aws_sdk_cloudwatch_events.types.describe_api_destination_request
    import aws_sdk_cloudwatch_events.types.describe_api_destination_response
    import aws_sdk_cloudwatch_events.types.describe_archive_request
    import aws_sdk_cloudwatch_events.types.describe_archive_response
    import aws_sdk_cloudwatch_events.types.describe_connection_request
    import aws_sdk_cloudwatch_events.types.describe_connection_response
    import aws_sdk_cloudwatch_events.types.describe_event_bus_request
    import aws_sdk_cloudwatch_events.types.describe_event_bus_response
    import aws_sdk_cloudwatch_events.types.describe_event_source_request
    import aws_sdk_cloudwatch_events.types.describe_event_source_response
    import aws_sdk_cloudwatch_events.types.describe_partner_event_source_request
    import aws_sdk_cloudwatch_events.types.describe_partner_event_source_response
    import aws_sdk_cloudwatch_events.types.describe_replay_request
    import aws_sdk_cloudwatch_events.types.describe_replay_response
    import aws_sdk_cloudwatch_events.types.describe_rule_request
    import aws_sdk_cloudwatch_events.types.describe_rule_response
    import aws_sdk_cloudwatch_events.types.disable_rule_request
    import aws_sdk_cloudwatch_events.types.enable_rule_request
    import aws_sdk_cloudwatch_events.types.event_bus_name
    import aws_sdk_cloudwatch_events.types.event_bus_name_or_arn
    import aws_sdk_cloudwatch_events.types.event_pattern
    import aws_sdk_cloudwatch_events.types.event_source_name
    import aws_sdk_cloudwatch_events.types.event_source_name_prefix
    import aws_sdk_cloudwatch_events.types.https_endpoint
    import aws_sdk_cloudwatch_events.types.limit_max100
    import aws_sdk_cloudwatch_events.types.list_api_destinations_request
    import aws_sdk_cloudwatch_events.types.list_api_destinations_response
    import aws_sdk_cloudwatch_events.types.list_archives_request
    import aws_sdk_cloudwatch_events.types.list_archives_response
    import aws_sdk_cloudwatch_events.types.list_connections_request
    import aws_sdk_cloudwatch_events.types.list_connections_response
    import aws_sdk_cloudwatch_events.types.list_event_buses_request
    import aws_sdk_cloudwatch_events.types.list_event_buses_response
    import aws_sdk_cloudwatch_events.types.list_event_sources_request
    import aws_sdk_cloudwatch_events.types.list_event_sources_response
    import aws_sdk_cloudwatch_events.types.list_partner_event_source_accounts_request
    import aws_sdk_cloudwatch_events.types.list_partner_event_source_accounts_response
    import aws_sdk_cloudwatch_events.types.list_partner_event_sources_request
    import aws_sdk_cloudwatch_events.types.list_partner_event_sources_response
    import aws_sdk_cloudwatch_events.types.list_replays_request
    import aws_sdk_cloudwatch_events.types.list_replays_response
    import aws_sdk_cloudwatch_events.types.list_rule_names_by_target_request
    import aws_sdk_cloudwatch_events.types.list_rule_names_by_target_response
    import aws_sdk_cloudwatch_events.types.list_rules_request
    import aws_sdk_cloudwatch_events.types.list_rules_response
    import aws_sdk_cloudwatch_events.types.list_tags_for_resource_request
    import aws_sdk_cloudwatch_events.types.list_tags_for_resource_response
    import aws_sdk_cloudwatch_events.types.list_targets_by_rule_request
    import aws_sdk_cloudwatch_events.types.list_targets_by_rule_response
    import aws_sdk_cloudwatch_events.types.next_token
    import aws_sdk_cloudwatch_events.types.non_partner_event_bus_name
    import aws_sdk_cloudwatch_events.types.partner_event_source_name_prefix
    import aws_sdk_cloudwatch_events.types.principal
    import aws_sdk_cloudwatch_events.types.put_events_request
    import aws_sdk_cloudwatch_events.types.put_events_request_entry_list
    import aws_sdk_cloudwatch_events.types.put_events_response
    import aws_sdk_cloudwatch_events.types.put_partner_events_request
    import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list
    import aws_sdk_cloudwatch_events.types.put_partner_events_response
    import aws_sdk_cloudwatch_events.types.put_permission_request
    import aws_sdk_cloudwatch_events.types.put_rule_request
    import aws_sdk_cloudwatch_events.types.put_rule_response
    import aws_sdk_cloudwatch_events.types.put_targets_request
    import aws_sdk_cloudwatch_events.types.put_targets_response
    import aws_sdk_cloudwatch_events.types.remove_permission_request
    import aws_sdk_cloudwatch_events.types.remove_targets_request
    import aws_sdk_cloudwatch_events.types.remove_targets_response
    import aws_sdk_cloudwatch_events.types.replay_description
    import aws_sdk_cloudwatch_events.types.replay_destination
    import aws_sdk_cloudwatch_events.types.replay_name
    import aws_sdk_cloudwatch_events.types.replay_state
    import aws_sdk_cloudwatch_events.types.retention_days
    import aws_sdk_cloudwatch_events.types.role_arn
    import aws_sdk_cloudwatch_events.types.rule_description
    import aws_sdk_cloudwatch_events.types.rule_name
    import aws_sdk_cloudwatch_events.types.rule_state
    import aws_sdk_cloudwatch_events.types.schedule_expression
    import aws_sdk_cloudwatch_events.types.start_replay_request
    import aws_sdk_cloudwatch_events.types.start_replay_response
    import aws_sdk_cloudwatch_events.types.statement_id
    import aws_sdk_cloudwatch_events.types.string
    import aws_sdk_cloudwatch_events.types.tag_key_list
    import aws_sdk_cloudwatch_events.types.tag_list
    import aws_sdk_cloudwatch_events.types.tag_resource_request
    import aws_sdk_cloudwatch_events.types.tag_resource_response
    import aws_sdk_cloudwatch_events.types.target_arn
    import aws_sdk_cloudwatch_events.types.target_id_list
    import aws_sdk_cloudwatch_events.types.target_list
    import aws_sdk_cloudwatch_events.types.test_event_pattern_request
    import aws_sdk_cloudwatch_events.types.test_event_pattern_response
    import aws_sdk_cloudwatch_events.types.timestamp
    import aws_sdk_cloudwatch_events.types.untag_resource_request
    import aws_sdk_cloudwatch_events.types.untag_resource_response
    import aws_sdk_cloudwatch_events.types.update_api_destination_request
    import aws_sdk_cloudwatch_events.types.update_api_destination_response
    import aws_sdk_cloudwatch_events.types.update_archive_request
    import aws_sdk_cloudwatch_events.types.update_archive_response
    import aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters
    import aws_sdk_cloudwatch_events.types.update_connection_request
    import aws_sdk_cloudwatch_events.types.update_connection_response


class AsyncCloudWatchEventsClientConfig(TypedDict, total=False):
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


class AsyncCloudWatchEventsClient:
    """A client for the ``CloudWatchEvents`` service.

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
        self.config = AsyncCloudWatchEventsClientConfig(
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
        self, config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudWatchEventsClientConfig = config_overrides or {}
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

    async def activate_event_source(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> None:
        """<p>Activates a partner event source that has been deactivated. Once activated, your matching event bus will start receiving events from the event source.</p>

        Args:
            name: <p>The name of the partner event source to activate.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.activate_event_source_request.ActivateEventSourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.activate_event_source

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.activate_event_source.async_activate_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.activate_event_source_request.ActivateEventSourceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_replay(
        self,
        replay_name: "aws_sdk_cloudwatch_events.types.replay_name.ReplayName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.cancel_replay_response.CancelReplayResponse":
        """<p>Cancels the specified replay.</p>

        Args:
            replay_name: <p>The name of the replay to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.cancel_replay_request.CancelReplayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.cancel_replay_response.CancelReplayResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.cancel_replay

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.cancel_replay.async_cancel_replay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.cancel_replay_request.CancelReplayRequest = {}  # type: ignore[typeddict-item]
        input_["replay_name"] = replay_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_api_destination(
        self,
        name: "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName",
        connection_arn: "aws_sdk_cloudwatch_events.types.connection_arn.ConnectionArn",
        invocation_endpoint: "aws_sdk_cloudwatch_events.types.https_endpoint.HttpsEndpoint",
        http_method: "aws_sdk_cloudwatch_events.types.api_destination_http_method.ApiDestinationHttpMethod",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.api_destination_description.ApiDestinationDescription"
        ] = None,
        invocation_rate_limit_per_second: Optional[
            "aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.create_api_destination_response.CreateApiDestinationResponse":
        """<p>Creates an API destination, which is an HTTP invocation endpoint configured as a target for events.</p>

        Args:
            name: <p>The name for the API destination to create.</p>
            description: <p>A description for the API destination to create.</p>
            connection_arn: <p>The ARN of the connection to use for the API destination. The destination endpoint must support the authorization type specified for the connection.</p>
            invocation_endpoint: <p>The URL to the HTTP invocation endpoint for the API destination.</p>
            http_method: <p>The method to use for the request to the HTTP invocation endpoint.</p>
            invocation_rate_limit_per_second: <p>The maximum number of requests per second to send to the HTTP invocation endpoint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.create_api_destination_request.CreateApiDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.create_api_destination_response.CreateApiDestinationResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.create_api_destination

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.create_api_destination.async_create_api_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.create_api_destination_request.CreateApiDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["connection_arn"] = connection_arn
        input_["invocation_endpoint"] = invocation_endpoint
        input_["http_method"] = http_method
        if invocation_rate_limit_per_second is not None:
            input_["invocation_rate_limit_per_second"] = (
                invocation_rate_limit_per_second
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_archive(
        self,
        archive_name: "aws_sdk_cloudwatch_events.types.archive_name.ArchiveName",
        event_source_arn: "aws_sdk_cloudwatch_events.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.archive_description.ArchiveDescription"
        ] = None,
        event_pattern: Optional[
            "aws_sdk_cloudwatch_events.types.event_pattern.EventPattern"
        ] = None,
        retention_days: Optional[
            "aws_sdk_cloudwatch_events.types.retention_days.RetentionDays"
        ] = None,
    ) -> (
        "aws_sdk_cloudwatch_events.types.create_archive_response.CreateArchiveResponse"
    ):
        """<p>Creates an archive of events with the specified settings. When you create an archive, incoming events might not immediately start being sent to the archive. Allow a short period of time for changes to take effect. If you do not specify a pattern to filter events sent to the archive, all events are sent to the archive except replayed events. Replayed events are not sent to an archive.</p>

        Args:
            archive_name: <p>The name for the archive to create.</p>
            event_source_arn: <p>The ARN of the event bus that sends events to the archive.</p>
            description: <p>A description for the archive.</p>
            event_pattern: <p>An event pattern to use to filter events sent to the archive.</p>
            retention_days: <p>The number of days to retain events for. Default value is 0. If set to 0, events are retained indefinitely</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.create_archive_request.CreateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.create_archive_response.CreateArchiveResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.create_archive

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.create_archive.async_create_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.create_archive_request.CreateArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_name"] = archive_name
        input_["event_source_arn"] = event_source_arn
        if description is not None:
            input_["description"] = description
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if retention_days is not None:
            input_["retention_days"] = retention_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_connection(
        self,
        name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName",
        authorization_type: "aws_sdk_cloudwatch_events.types.connection_authorization_type.ConnectionAuthorizationType",
        auth_parameters: "aws_sdk_cloudwatch_events.types.create_connection_auth_request_parameters.CreateConnectionAuthRequestParameters",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.connection_description.ConnectionDescription"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.create_connection_response.CreateConnectionResponse":
        """<p>Creates a connection. A connection defines the authorization type and credentials to use for authorization with an API destination HTTP endpoint.</p>

        Args:
            name: <p>The name for the connection to create.</p>
            description: <p>A description for the connection to create.</p>
            authorization_type: <p>The type of authorization to use for the connection.</p>
            auth_parameters: <p>A <code>CreateConnectionAuthRequestParameters</code> object that contains the authorization parameters to use to authorize with the endpoint. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.create_connection_request.CreateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.create_connection_response.CreateConnectionResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.create_connection

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.create_connection_request.CreateConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["authorization_type"] = authorization_type
        input_["auth_parameters"] = auth_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_event_bus(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_bus_name.EventBusName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_source_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName"
        ] = None,
        tags: Optional["aws_sdk_cloudwatch_events.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_cloudwatch_events.types.create_event_bus_response.CreateEventBusResponse":
        """<p>Creates a new event bus within your account. This can be a custom event bus which you can use to receive events from your custom applications and services, or it can be a partner event bus which can be matched to a partner event source.</p>

        Args:
            name: <p>The name of the new event bus. </p> <p>Event bus names cannot contain the / character. You can't use the name <code>default</code> for a custom event bus, as this name is already used for your account's default event bus.</p> <p>If this is a partner event bus, the name must exactly match the name of the partner event source that this event bus is matched to.</p>
            event_source_name: <p>If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.</p>
            tags: <p>Tags to associate with the event bus.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.create_event_bus_request.CreateEventBusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.create_event_bus_response.CreateEventBusResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.create_event_bus

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.create_event_bus.async_create_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.create_event_bus_request.CreateEventBusRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if event_source_name is not None:
            input_["event_source_name"] = event_source_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_partner_event_source(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        account: "aws_sdk_cloudwatch_events.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.create_partner_event_source_response.CreatePartnerEventSourceResponse":
        """<p>Called by an SaaS partner to create a partner event source. This operation is not used by Amazon Web Services customers.</p> <p>Each partner event source can be used by one Amazon Web Services account to create a matching partner event bus in that Amazon Web Services account. A SaaS partner must create one partner event source for each Amazon Web Services account that wants to receive those event types. </p> <p>A partner event source creates events based on resources within the SaaS partner's service or application.</p> <p>An Amazon Web Services account that creates a partner event bus that matches the partner event source can use that event bus to receive events from the partner, and then process them using Amazon Web Services Events rules and targets.</p> <p>Partner event source names follow this format:</p> <p> <code> <i>partner_name</i>/<i>event_namespace</i>/<i>event_name</i> </code> </p> <p> <i>partner_name</i> is determined during partner registration and identifies the partner to Amazon Web Services customers. <i>event_namespace</i> is determined by the partner and is a way for the partner to categorize their events. <i>event_name</i> is determined by the partner, and should uniquely identify an event-generating resource within the partner system. The combination of <i>event_namespace</i> and <i>event_name</i> should help Amazon Web Services customers decide whether to create an event bus to receive these events.</p>

        Args:
            name: <p>The name of the partner event source. This name must be unique and must be in the format <code> <i>partner_name</i>/<i>event_namespace</i>/<i>event_name</i> </code>. The Amazon Web Services account that wants to use this partner event source must create a partner event bus with a name that matches the name of the partner event source.</p>
            account: <p>The Amazon Web Services account ID that is permitted to create a matching partner event bus for this partner event source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.create_partner_event_source_request.CreatePartnerEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.create_partner_event_source_response.CreatePartnerEventSourceResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.create_partner_event_source

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.create_partner_event_source.async_create_partner_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.create_partner_event_source_request.CreatePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["account"] = account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deactivate_event_source(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> None:
        """<p>You can use this operation to temporarily stop receiving events from the specified partner event source. The matching event bus is not deleted. </p> <p>When you deactivate a partner event source, the source goes into PENDING state. If it remains in PENDING state for more than two weeks, it is deleted.</p> <p>To activate a deactivated partner event source, use <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ActivateEventSource.html\">ActivateEventSource</a>.</p>

        Args:
            name: <p>The name of the partner event source to deactivate.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.deactivate_event_source_request.DeactivateEventSourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.deactivate_event_source

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.deactivate_event_source.async_deactivate_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.deactivate_event_source_request.DeactivateEventSourceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deauthorize_connection(
        self,
        name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.deauthorize_connection_response.DeauthorizeConnectionResponse":
        """<p>Removes all authorization parameters from the connection. This lets you remove the secret from the connection so you can reuse it without having to create a new connection.</p>

        Args:
            name: <p>The name of the connection to remove authorization from.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.deauthorize_connection_request.DeauthorizeConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.deauthorize_connection_response.DeauthorizeConnectionResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.deauthorize_connection

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.deauthorize_connection.async_deauthorize_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.deauthorize_connection_request.DeauthorizeConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_api_destination(
        self,
        name: "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.delete_api_destination_response.DeleteApiDestinationResponse":
        """<p>Deletes the specified API destination.</p>

        Args:
            name: <p>The name of the destination to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.delete_api_destination_request.DeleteApiDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.delete_api_destination_response.DeleteApiDestinationResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.delete_api_destination

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.delete_api_destination.async_delete_api_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.delete_api_destination_request.DeleteApiDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_archive(
        self,
        archive_name: "aws_sdk_cloudwatch_events.types.archive_name.ArchiveName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> (
        "aws_sdk_cloudwatch_events.types.delete_archive_response.DeleteArchiveResponse"
    ):
        """<p>Deletes the specified archive.</p>

        Args:
            archive_name: <p>The name of the archive to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.delete_archive_request.DeleteArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.delete_archive_response.DeleteArchiveResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.delete_archive

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.delete_archive.async_delete_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.delete_archive_request.DeleteArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_name"] = archive_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_connection(
        self,
        name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Deletes a connection.</p>

        Args:
            name: <p>The name of the connection to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.delete_connection

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.delete_connection_request.DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_event_bus(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_bus_name.EventBusName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified custom event bus or partner event bus. All rules associated with this event bus need to be deleted. You can't delete your account's default event bus.</p>

        Args:
            name: <p>The name of the event bus to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.delete_event_bus_request.DeleteEventBusRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.delete_event_bus

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.delete_event_bus.async_delete_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.delete_event_bus_request.DeleteEventBusRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_partner_event_source(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        account: "aws_sdk_cloudwatch_events.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> None:
        """<p>This operation is used by SaaS partners to delete a partner event source. This operation is not used by Amazon Web Services customers.</p> <p>When you delete an event source, the status of the corresponding partner event bus in the Amazon Web Services customer account becomes DELETED.</p> <p></p>

        Args:
            name: <p>The name of the event source to delete.</p>
            account: <p>The Amazon Web Services account ID of the Amazon Web Services customer that the event source was created for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.delete_partner_event_source_request.DeletePartnerEventSourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.delete_partner_event_source

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.delete_partner_event_source.async_delete_partner_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.delete_partner_event_source_request.DeletePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["account"] = account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_rule(
        self,
        name: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
        force: Optional["aws_sdk_cloudwatch_events.types.boolean.Boolean"] = None,
    ) -> None:
        """<p>Deletes the specified rule.</p> <p>Before you can delete the rule, you must remove all targets, using <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemoveTargets.html\">RemoveTargets</a>.</p> <p>When you delete a rule, incoming events might continue to match to the deleted rule. Allow a short period of time for changes to take effect.</p> <p>If you call delete rule multiple times for the same rule, all calls will succeed. When you call delete rule for a non-existent custom eventbus, <code>ResourceNotFoundException</code> is returned.</p> <p>Managed rules are rules created and managed by another Amazon Web Services service on your behalf. These rules are created by those other Amazon Web Services services to support functionality in those services. You can delete these rules using the <code>Force</code> option, but you should do so only if you are sure the other service is not still using that rule.</p>

        Args:
            name: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
            force: <p>If this is a managed rule, created by an Amazon Web Services service on your behalf, you must specify <code>Force</code> as <code>True</code> to delete the rule. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using <code>DescribeRule</code> or <code>ListRules</code> and checking the <code>ManagedBy</code> field of the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.delete_rule_request.DeleteRuleRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.delete_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.delete_rule_request.DeleteRuleRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_api_destination(
        self,
        name: "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_api_destination_response.DescribeApiDestinationResponse":
        """<p>Retrieves details about an API destination.</p>

        Args:
            name: <p>The name of the API destination to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_api_destination_request.DescribeApiDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_api_destination_response.DescribeApiDestinationResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_api_destination

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_api_destination.async_describe_api_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_api_destination_request.DescribeApiDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_archive(
        self,
        archive_name: "aws_sdk_cloudwatch_events.types.archive_name.ArchiveName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_archive_response.DescribeArchiveResponse":
        """<p>Retrieves details about an archive.</p>

        Args:
            archive_name: <p>The name of the archive to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_archive_request.DescribeArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_archive_response.DescribeArchiveResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_archive

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_archive.async_describe_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_archive_request.DescribeArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_name"] = archive_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_connection(
        self,
        name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_connection_response.DescribeConnectionResponse":
        """<p>Retrieves details about a connection.</p>

        Args:
            name: <p>The name of the connection to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_connection_request.DescribeConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_connection_response.DescribeConnectionResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_connection

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_connection.async_describe_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_connection_request.DescribeConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_event_bus(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_event_bus_response.DescribeEventBusResponse":
        """<p>Displays details about an event bus in your account. This can include the external Amazon Web Services accounts that are permitted to write events to your default event bus, and the associated policy. For custom event buses and partner event buses, it displays the name, ARN, policy, state, and creation time.</p> <p> To enable your account to receive events from other accounts on its default event bus, use <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html\">PutPermission</a>.</p> <p>For more information about partner event buses, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html\">CreateEventBus</a>.</p>

        Args:
            name: <p>The name or ARN of the event bus to show details for. If you omit this, the default event bus is displayed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_event_bus_request.DescribeEventBusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_event_bus_response.DescribeEventBusResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_event_bus

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_event_bus.async_describe_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_event_bus_request.DescribeEventBusRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_event_source(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_event_source_response.DescribeEventSourceResponse":
        """<p>This operation lists details about a partner event source that is shared with your account.</p>

        Args:
            name: <p>The name of the partner event source to display the details of.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_event_source_request.DescribeEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_event_source_response.DescribeEventSourceResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_event_source

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_event_source.async_describe_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_event_source_request.DescribeEventSourceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_partner_event_source(
        self,
        name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_partner_event_source_response.DescribePartnerEventSourceResponse":
        """<p>An SaaS partner can use this operation to list details about a partner event source that they have created. Amazon Web Services customers do not use this operation. Instead, Amazon Web Services customers can use <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventSource.html\">DescribeEventSource</a> to see details about a partner event source that is shared with them.</p>

        Args:
            name: <p>The name of the event source to display.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_partner_event_source_request.DescribePartnerEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_partner_event_source_response.DescribePartnerEventSourceResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_partner_event_source

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_partner_event_source.async_describe_partner_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_partner_event_source_request.DescribePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_replay(
        self,
        replay_name: "aws_sdk_cloudwatch_events.types.replay_name.ReplayName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_replay_response.DescribeReplayResponse":
        """<p>Retrieves details about a replay. Use <code>DescribeReplay</code> to determine the progress of a running replay. A replay processes events to replay based on the time in the event, and replays them using 1 minute intervals. If you use <code>StartReplay</code> and specify an <code>EventStartTime</code> and an <code>EventEndTime</code> that covers a 20 minute time range, the events are replayed from the first minute of that 20 minute range first. Then the events from the second minute are replayed. You can use <code>DescribeReplay</code> to determine the progress of a replay. The value returned for <code>EventLastReplayedTime</code> indicates the time within the specified time range associated with the last event replayed.</p>

        Args:
            replay_name: <p>The name of the replay to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_replay_request.DescribeReplayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_replay_response.DescribeReplayResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_replay

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_replay.async_describe_replay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_replay_request.DescribeReplayRequest = {}  # type: ignore[typeddict-item]
        input_["replay_name"] = replay_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_rule(
        self,
        name: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.describe_rule_response.DescribeRuleResponse":
        """<p>Describes the specified rule.</p> <p>DescribeRule does not list the targets of a rule. To see the targets associated with a rule, use <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html\">ListTargetsByRule</a>.</p>

        Args:
            name: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.describe_rule_request.DescribeRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.describe_rule_response.DescribeRuleResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.describe_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.describe_rule.async_describe_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.describe_rule_request.DescribeRuleRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_rule(
        self,
        name: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
    ) -> None:
        """<p>Disables the specified rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression.</p> <p>When you disable a rule, incoming events might continue to match to the disabled rule. Allow a short period of time for changes to take effect.</p>

        Args:
            name: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.disable_rule_request.DisableRuleRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.disable_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.disable_rule.async_disable_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.disable_rule_request.DisableRuleRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_rule(
        self,
        name: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
    ) -> None:
        """<p>Enables the specified rule. If the rule does not exist, the operation fails.</p> <p>When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Allow a short period of time for changes to take effect.</p>

        Args:
            name: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.enable_rule_request.EnableRuleRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.enable_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.enable_rule.async_enable_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.enable_rule_request.EnableRuleRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_api_destinations(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName"
        ] = None,
        connection_arn: Optional[
            "aws_sdk_cloudwatch_events.types.connection_arn.ConnectionArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_api_destinations_response.ListApiDestinationsResponse":
        """<p>Retrieves a list of API destination in the account in the current Region.</p>

        Args:
            name_prefix: <p>A name prefix to filter results returned. Only API destinations with a name that starts with the prefix are returned.</p>
            connection_arn: <p>The ARN of the connection specified for the API destination.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of API destinations to include in the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_api_destinations_request.ListApiDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_api_destinations_response.ListApiDestinationsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_api_destinations

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_api_destinations.async_list_api_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_api_destinations_request.ListApiDestinationsRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if connection_arn is not None:
            input_["connection_arn"] = connection_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_archives(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.archive_name.ArchiveName"
        ] = None,
        event_source_arn: Optional["aws_sdk_cloudwatch_events.types.arn.Arn"] = None,
        state: Optional[
            "aws_sdk_cloudwatch_events.types.archive_state.ArchiveState"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_archives_response.ListArchivesResponse":
        """<p>Lists your archives. You can either list all the archives or you can provide a prefix to match to the archive names. Filter parameters are exclusive.</p>

        Args:
            name_prefix: <p>A name prefix to filter the archives returned. Only archives with name that match the prefix are returned.</p>
            event_source_arn: <p>The ARN of the event source associated with the archive.</p>
            state: <p>The state of the archive.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_archives_request.ListArchivesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_archives_response.ListArchivesResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_archives

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_archives.async_list_archives(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_archives_request.ListArchivesRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if state is not None:
            input_["state"] = state
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_connections(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName"
        ] = None,
        connection_state: Optional[
            "aws_sdk_cloudwatch_events.types.connection_state.ConnectionState"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_connections_response.ListConnectionsResponse":
        """<p>Retrieves a list of connections from the account.</p>

        Args:
            name_prefix: <p>A name prefix to filter results returned. Only connections with a name that starts with the prefix are returned.</p>
            connection_state: <p>The state of the connection.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of connections to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_connections_request.ListConnectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_connections_response.ListConnectionsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_connections

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_connections_request.ListConnectionsRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if connection_state is not None:
            input_["connection_state"] = connection_state
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_event_buses(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name.EventBusName"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_event_buses_response.ListEventBusesResponse":
        """<p>Lists all the event buses in your account, including the default event bus, custom event buses, and partner event buses.</p>

        Args:
            name_prefix: <p>Specifying this limits the results to only those event buses with names that start with the specified prefix.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_event_buses_request.ListEventBusesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_event_buses_response.ListEventBusesResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_event_buses

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_event_buses.async_list_event_buses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_event_buses_request.ListEventBusesRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_event_sources(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.event_source_name_prefix.EventSourceNamePrefix"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_event_sources_response.ListEventSourcesResponse":
        """<p>You can use this to see all the partner event sources that have been shared with your Amazon Web Services account. For more information about partner event sources, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html\">CreateEventBus</a>.</p>

        Args:
            name_prefix: <p>Specifying this limits the results to only those partner event sources with names that start with the specified prefix.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_event_sources_request.ListEventSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_event_sources_response.ListEventSourcesResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_event_sources

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_event_sources.async_list_event_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_event_sources_request.ListEventSourcesRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_partner_event_source_accounts(
        self,
        event_source_name: "aws_sdk_cloudwatch_events.types.event_source_name.EventSourceName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_partner_event_source_accounts_response.ListPartnerEventSourceAccountsResponse":
        """<p>An SaaS partner can use this operation to display the Amazon Web Services account ID that a particular partner event source name is associated with. This operation is not used by Amazon Web Services customers.</p>

        Args:
            event_source_name: <p>The name of the partner event source to display account information about.</p>
            next_token: <p>The token returned by a previous call to this operation. Specifying this retrieves the next set of results.</p>
            limit: <p>Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_partner_event_source_accounts_request.ListPartnerEventSourceAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_partner_event_source_accounts_response.ListPartnerEventSourceAccountsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_partner_event_source_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_partner_event_source_accounts.async_list_partner_event_source_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_partner_event_source_accounts_request.ListPartnerEventSourceAccountsRequest = {}  # type: ignore[typeddict-item]
        input_["event_source_name"] = event_source_name
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_partner_event_sources(
        self,
        name_prefix: "aws_sdk_cloudwatch_events.types.partner_event_source_name_prefix.PartnerEventSourceNamePrefix",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_partner_event_sources_response.ListPartnerEventSourcesResponse":
        """<p>An SaaS partner can use this operation to list all the partner event source names that they have created. This operation is not used by Amazon Web Services customers.</p>

        Args:
            name_prefix: <p>If you specify this, the results are limited to only those partner event sources that start with the string you specify.</p>
            next_token: <p>The token returned by a previous call to this operation. Specifying this retrieves the next set of results.</p>
            limit: <p>pecifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_partner_event_sources_request.ListPartnerEventSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_partner_event_sources_response.ListPartnerEventSourcesResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_partner_event_sources

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_partner_event_sources.async_list_partner_event_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_partner_event_sources_request.ListPartnerEventSourcesRequest = {}  # type: ignore[typeddict-item]
        input_["name_prefix"] = name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_replays(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.replay_name.ReplayName"
        ] = None,
        state: Optional[
            "aws_sdk_cloudwatch_events.types.replay_state.ReplayState"
        ] = None,
        event_source_arn: Optional["aws_sdk_cloudwatch_events.types.arn.Arn"] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_replays_response.ListReplaysResponse":
        """<p>Lists your replays. You can either list all the replays or you can provide a prefix to match to the replay names. Filter parameters are exclusive.</p>

        Args:
            name_prefix: <p>A name prefix to filter the replays returned. Only replays with name that match the prefix are returned.</p>
            state: <p>The state of the replay.</p>
            event_source_arn: <p>The ARN of the archive from which the events are replayed.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of replays to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_replays_request.ListReplaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_replays_response.ListReplaysResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_replays

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_replays.async_list_replays(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_replays_request.ListReplaysRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if state is not None:
            input_["state"] = state
        if event_source_arn is not None:
            input_["event_source_arn"] = event_source_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_rule_names_by_target(
        self,
        target_arn: "aws_sdk_cloudwatch_events.types.target_arn.TargetArn",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_rule_names_by_target_response.ListRuleNamesByTargetResponse":
        """<p>Lists the rules for the specified target. You can see which of the rules in Amazon EventBridge can invoke a specific target in your account.</p>

        Args:
            target_arn: <p>The Amazon Resource Name (ARN) of the target resource.</p>
            event_bus_name: <p>The name or ARN of the event bus to list rules for. If you omit this, the default event bus is used.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_rule_names_by_target_request.ListRuleNamesByTargetRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_rule_names_by_target_response.ListRuleNamesByTargetResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_rule_names_by_target

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_rule_names_by_target.async_list_rule_names_by_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_rule_names_by_target_request.ListRuleNamesByTargetRequest = {}  # type: ignore[typeddict-item]
        input_["target_arn"] = target_arn
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_rules(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudwatch_events.types.rule_name.RuleName"
        ] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_rules_response.ListRulesResponse":
        """<p>Lists your Amazon EventBridge rules. You can either list all the rules or you can provide a prefix to match to the rule names.</p> <p>ListRules does not list the targets of a rule. To see the targets associated with a rule, use <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTargetsByRule.html\">ListTargetsByRule</a>.</p>

        Args:
            name_prefix: <p>The prefix matching the rule name.</p>
            event_bus_name: <p>The name or ARN of the event bus to list the rules for. If you omit this, the default event bus is used.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_rules_request.ListRulesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_rules_response.ListRulesResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_rules

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_rules_request.ListRulesRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_cloudwatch_events.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with an EventBridge resource. In EventBridge, rules and event buses can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the EventBridge resource for which you want to view tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_targets_by_rule(
        self,
        rule: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudwatch_events.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "aws_sdk_cloudwatch_events.types.limit_max100.LimitMax100"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.list_targets_by_rule_response.ListTargetsByRuleResponse":
        """<p>Lists the targets assigned to the specified rule.</p>

        Args:
            rule: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            limit: <p>The maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.list_targets_by_rule_request.ListTargetsByRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.list_targets_by_rule_response.ListTargetsByRuleResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.list_targets_by_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.list_targets_by_rule.async_list_targets_by_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.list_targets_by_rule_request.ListTargetsByRuleRequest = {}  # type: ignore[typeddict-item]
        input_["rule"] = rule
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_events(
        self,
        entries: "aws_sdk_cloudwatch_events.types.put_events_request_entry_list.PutEventsRequestEntryList",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.put_events_response.PutEventsResponse":
        """<p>Sends custom events to Amazon EventBridge so that they can be matched to rules.</p>

        Args:
            entries: <p>The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.put_events_request.PutEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.put_events_response.PutEventsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.put_events

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.put_events.async_put_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.put_events_request.PutEventsRequest = {}  # type: ignore[typeddict-item]
        input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_partner_events(
        self,
        entries: "aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list.PutPartnerEventsRequestEntryList",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.put_partner_events_response.PutPartnerEventsResponse":
        """<p>This is used by SaaS partners to write events to a customer's partner event bus. Amazon Web Services customers do not use this operation.</p>

        Args:
            entries: <p>The list of events to write to the event bus.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.put_partner_events_request.PutPartnerEventsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.put_partner_events_response.PutPartnerEventsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.put_partner_events

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.put_partner_events.async_put_partner_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.put_partner_events_request.PutPartnerEventsRequest = {}  # type: ignore[typeddict-item]
        input_["entries"] = entries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_permission(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.non_partner_event_bus_name.NonPartnerEventBusName"
        ] = None,
        action: Optional["aws_sdk_cloudwatch_events.types.action.Action"] = None,
        principal: Optional[
            "aws_sdk_cloudwatch_events.types.principal.Principal"
        ] = None,
        statement_id: Optional[
            "aws_sdk_cloudwatch_events.types.statement_id.StatementId"
        ] = None,
        condition: Optional[
            "aws_sdk_cloudwatch_events.types.condition.Condition"
        ] = None,
        policy: Optional["aws_sdk_cloudwatch_events.types.string.String"] = None,
    ) -> None:
        """<p>Running <code>PutPermission</code> permits the specified Amazon Web Services account or Amazon Web Services organization to put events to the specified <i>event bus</i>. Amazon EventBridge (CloudWatch Events) rules in your account are triggered by these events arriving to an event bus in your account. </p> <p>For another account to send events to your account, that external account must have an EventBridge rule with your account's event bus as a target.</p> <p>To enable multiple Amazon Web Services accounts to put events to your event bus, run <code>PutPermission</code> once for each of these accounts. Or, if all the accounts are members of the same Amazon Web Services organization, you can run <code>PutPermission</code> once specifying <code>Principal</code> as \"*\" and specifying the Amazon Web Services organization ID in <code>Condition</code>, to grant permissions to all accounts in that organization.</p> <p>If you grant permissions using an organization, then accounts in that organization must specify a <code>RoleArn</code> with proper permissions when they use <code>PutTarget</code> to add your account's event bus as a target. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html\">Sending and Receiving Events Between Amazon Web Services Accounts</a> in the <i>Amazon EventBridge User Guide</i>.</p> <p>The permission policy on the event bus cannot exceed 10 KB in size.</p>

        Args:
            event_bus_name: <p>The name of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
            action: <p>The action that you are enabling the other account to perform.</p>
            principal: <p>The 12-digit Amazon Web Services account ID that you are permitting to put events to your default event bus. Specify \"*\" to permit any account to put events to your default event bus.</p> <p>If you specify \"*\" without specifying <code>Condition</code>, avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an <code>account</code> field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.</p>
            statement_id: <p>An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this <code>StatementId</code> when you run <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RemovePermission.html\">RemovePermission</a>.</p>
            condition: <p>This parameter enables you to limit the permission to accounts that fulfill a certain condition, such as being a member of a certain Amazon Web Services organization. For more information about Amazon Web Services Organizations, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html\">What Is Amazon Web Services Organizations</a> in the <i>Amazon Web Services Organizations User Guide</i>.</p> <p>If you specify <code>Condition</code> with an Amazon Web Services organization ID, and specify \"*\" as the value for <code>Principal</code>, you grant permission to all the accounts in the named organization.</p> <p>The <code>Condition</code> is a JSON string which must contain <code>Type</code>, <code>Key</code>, and <code>Value</code> fields.</p>
            policy: <p>A JSON string that describes the permission policy statement. You can include a <code>Policy</code> parameter in the request instead of using the <code>StatementId</code>, <code>Action</code>, <code>Principal</code>, or <code>Condition</code> parameters.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.put_permission_request.PutPermissionRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.put_permission

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.put_permission.async_put_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.put_permission_request.PutPermissionRequest = {}  # type: ignore[typeddict-item]
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        if action is not None:
            input_["action"] = action
        if principal is not None:
            input_["principal"] = principal
        if statement_id is not None:
            input_["statement_id"] = statement_id
        if condition is not None:
            input_["condition"] = condition
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_rule(
        self,
        name: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        schedule_expression: Optional[
            "aws_sdk_cloudwatch_events.types.schedule_expression.ScheduleExpression"
        ] = None,
        event_pattern: Optional[
            "aws_sdk_cloudwatch_events.types.event_pattern.EventPattern"
        ] = None,
        state: Optional["aws_sdk_cloudwatch_events.types.rule_state.RuleState"] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.rule_description.RuleDescription"
        ] = None,
        role_arn: Optional["aws_sdk_cloudwatch_events.types.role_arn.RoleArn"] = None,
        tags: Optional["aws_sdk_cloudwatch_events.types.tag_list.TagList"] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.put_rule_response.PutRuleResponse":
        """<p>Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html\">DisableRule</a>.</p> <p>A single rule watches for events from a single event bus. Events generated by Amazon Web Services services go to your account's default event bus. Events generated by SaaS partner services or applications go to the matching partner event bus. If you have custom applications or services, you can specify whether their events go to your default event bus or a custom event bus that you have created. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEventBus.html\">CreateEventBus</a>.</p> <p>If you are updating an existing rule, the rule is replaced with what you specify in this <code>PutRule</code> command. If you omit arguments in <code>PutRule</code>, the old values for those arguments are not kept. Instead, they are replaced with null values.</p> <p>When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Allow a short period of time for changes to take effect.</p> <p>A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule.</p> <p>When you initially create a rule, you can optionally assign one or more tags to the rule. Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only rules with certain tag values. To use the <code>PutRule</code> operation and assign tags, you must have both the <code>events:PutRule</code> and <code>events:TagResource</code> permissions.</p> <p>If you are updating an existing rule, any tags you specify in the <code>PutRule</code> operation are ignored. To update the tags of an existing rule, use <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TagResource.html\">TagResource</a> and <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UntagResource.html\">UntagResource</a>.</p> <p>Most services in Amazon Web Services treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.</p> <p>In EventBridge, it is possible to create rules that lead to infinite loops, where a rule is fired repeatedly. For example, a rule might detect that ACLs have changed on an S3 bucket, and trigger software to change them to the desired state. If the rule is not written carefully, the subsequent change to the ACLs fires the rule again, creating an infinite loop.</p> <p>To prevent this, write the rules so that the triggered actions do not re-fire the same rule. For example, your rule could fire only if ACLs are found to be in a bad state, instead of after any change. </p> <p>An infinite loop can quickly cause higher than expected charges. We recommend that you use budgeting, which alerts you when charges exceed your specified limit. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html\">Managing Your Costs with Budgets</a>.</p>

        Args:
            name: <p>The name of the rule that you are creating or updating.</p>
            schedule_expression: <p>The scheduling expression. For example, \"cron(0 20 * * ? *)\" or \"rate(5 minutes)\".</p>
            event_pattern: <p>The event pattern. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html\">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            state: <p>Indicates whether the rule is enabled or disabled.</p>
            description: <p>A description of the rule.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role associated with the rule.</p> <p>If you're setting an event bus in another account as the target and that account granted permission to your account through an organization instead of directly by the account ID, you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure, instead of here in this parameter.</p>
            tags: <p>The list of key-value pairs to associate with the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus to associate with this rule. If you omit this, the default event bus is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.put_rule_request.PutRuleRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.put_rule_response.PutRuleResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.put_rule

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.put_rule.async_put_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.put_rule_request.PutRuleRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if schedule_expression is not None:
            input_["schedule_expression"] = schedule_expression
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if state is not None:
            input_["state"] = state
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_targets(
        self,
        rule: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        targets: "aws_sdk_cloudwatch_events.types.target_list.TargetList",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.put_targets_response.PutTargetsResponse":
        """<p>Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.</p> <p>Targets are the resources that are invoked when a rule is triggered.</p> <p>You can configure the following as targets for Events:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html\">API destination</a> </p> </li> <li> <p>Amazon API Gateway REST API endpoints</p> </li> <li> <p>API Gateway</p> </li> <li> <p>Batch job queue</p> </li> <li> <p>CloudWatch Logs group</p> </li> <li> <p>CodeBuild project</p> </li> <li> <p>CodePipeline</p> </li> <li> <p>Amazon EC2 <code>CreateSnapshot</code> API call</p> </li> <li> <p>Amazon EC2 <code>RebootInstances</code> API call</p> </li> <li> <p>Amazon EC2 <code>StopInstances</code> API call</p> </li> <li> <p>Amazon EC2 <code>TerminateInstances</code> API call</p> </li> <li> <p>Amazon ECS tasks</p> </li> <li> <p>Event bus in a different Amazon Web Services account or Region.</p> <p>You can use an event bus in the US East (N. Virginia) us-east-1, US West (Oregon) us-west-2, or Europe (Ireland) eu-west-1 Regions as a target for a rule.</p> </li> <li> <p>Firehose delivery stream (Firehose)</p> </li> <li> <p>Inspector assessment template (Amazon Inspector)</p> </li> <li> <p>Kinesis stream (Kinesis Data Stream)</p> </li> <li> <p>Lambda function</p> </li> <li> <p>Redshift clusters (Data API statement execution)</p> </li> <li> <p>Amazon SNS topic</p> </li> <li> <p>Amazon SQS queues (includes FIFO queues</p> </li> <li> <p>SSM Automation</p> </li> <li> <p>SSM OpsItem</p> </li> <li> <p>SSM Run Command</p> </li> <li> <p>Step Functions state machines</p> </li> </ul> <p>Creating rules with built-in targets is supported only in the Amazon Web Services Management Console. The built-in targets are <code>EC2 CreateSnapshot API call</code>, <code>EC2 RebootInstances API call</code>, <code>EC2 StopInstances API call</code>, and <code>EC2 TerminateInstances API call</code>. </p> <p>For some target types, <code>PutTargets</code> provides target-specific parameters. If the target is a Kinesis data stream, you can optionally specify which shard the event goes to by using the <code>KinesisParameters</code> argument. To invoke a command on multiple EC2 instances with one rule, you can use the <code>RunCommandParameters</code> field.</p> <p>To be able to make API calls against the resources that you own, Amazon EventBridge needs the appropriate permissions. For Lambda and Amazon SNS resources, EventBridge relies on resource-based policies. For EC2 instances, Kinesis Data Streams, Step Functions state machines and API Gateway REST APIs, EventBridge relies on IAM roles that you specify in the <code>RoleARN</code> argument in <code>PutTargets</code>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/auth-and-access-control-eventbridge.html\">Authentication and Access Control</a> in the <i>Amazon EventBridge User Guide</i>.</p> <p>If another Amazon Web Services account is in the same region and has granted you permission (using <code>PutPermission</code>), you can send events to that account. Set that account's event bus as a target of the rules in your account. To send the matched events to the other account, specify that account's event bus as the <code>Arn</code> value when you run <code>PutTargets</code>. If your account sends events to another account, your account is charged for each sent event. Each event sent to another account is charged as a custom event. The account receiving the event is not charged. For more information, see <a href=\"http://aws.amazon.com/eventbridge/pricing/\">Amazon EventBridge Pricing</a>.</p> <note> <p> <code>Input</code>, <code>InputPath</code>, and <code>InputTransformer</code> are not available with <code>PutTarget</code> if the target is an event bus of a different Amazon Web Services account.</p> </note> <p>If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html\">Sending and Receiving Events Between Amazon Web Services Accounts</a> in the <i>Amazon EventBridge User Guide</i>.</p> <p>For more information about enabling cross-account events, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutPermission.html\">PutPermission</a>.</p> <p> <b>Input</b>, <b>InputPath</b>, and <b>InputTransformer</b> are mutually exclusive and optional parameters of a target. When a rule is triggered due to a matched event:</p> <ul> <li> <p>If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).</p> </li> <li> <p>If <b>Input</b> is specified in the form of valid JSON, then the matched event is overridden with this constant.</p> </li> <li> <p>If <b>InputPath</b> is specified in the form of JSONPath (for example, <code>$.detail</code>), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).</p> </li> <li> <p>If <b>InputTransformer</b> is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.</p> </li> </ul> <p>When you specify <code>InputPath</code> or <code>InputTransformer</code>, you must use JSON dot notation, not bracket notation.</p> <p>When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect.</p> <p>This action can partially fail if too many requests are made at the same time. If that happens, <code>FailedEntryCount</code> is non-zero in the response and each entry in <code>FailedEntries</code> provides the ID of the failed target and the error code.</p>

        Args:
            rule: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
            targets: <p>The targets to update or add to the rule.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.put_targets_request.PutTargetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.put_targets_response.PutTargetsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.put_targets

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.put_targets.async_put_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.put_targets_request.PutTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["rule"] = rule
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        input_["targets"] = targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_permission(
        self,
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        statement_id: Optional[
            "aws_sdk_cloudwatch_events.types.statement_id.StatementId"
        ] = None,
        remove_all_permissions: Optional[
            "aws_sdk_cloudwatch_events.types.boolean.Boolean"
        ] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.non_partner_event_bus_name.NonPartnerEventBusName"
        ] = None,
    ) -> None:
        """<p>Revokes the permission of another Amazon Web Services account to be able to put events to the specified event bus. Specify the account to revoke by the <code>StatementId</code> value that you associated with the account when you granted it permission with <code>PutPermission</code>. You can find the <code>StatementId</code> by using <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEventBus.html\">DescribeEventBus</a>.</p>

        Args:
            statement_id: <p>The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.</p>
            remove_all_permissions: <p>Specifies whether to remove all permissions.</p>
            event_bus_name: <p>The name of the event bus to revoke permissions for. If you omit this, the default event bus is used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.remove_permission_request.RemovePermissionRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_cloudwatch_events._operations.aws_events.remove_permission

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.remove_permission.async_remove_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.remove_permission_request.RemovePermissionRequest = {}  # type: ignore[typeddict-item]
        if statement_id is not None:
            input_["statement_id"] = statement_id
        if remove_all_permissions is not None:
            input_["remove_all_permissions"] = remove_all_permissions
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def remove_targets(
        self,
        rule: "aws_sdk_cloudwatch_events.types.rule_name.RuleName",
        ids: "aws_sdk_cloudwatch_events.types.target_id_list.TargetIdList",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        event_bus_name: Optional[
            "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
        ] = None,
        force: Optional["aws_sdk_cloudwatch_events.types.boolean.Boolean"] = None,
    ) -> (
        "aws_sdk_cloudwatch_events.types.remove_targets_response.RemoveTargetsResponse"
    ):
        """<p>Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.</p> <p>When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Allow a short period of time for changes to take effect.</p> <p>This action can partially fail if too many requests are made at the same time. If that happens, <code>FailedEntryCount</code> is non-zero in the response and each entry in <code>FailedEntries</code> provides the ID of the failed target and the error code.</p>

        Args:
            rule: <p>The name of the rule.</p>
            event_bus_name: <p>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</p>
            ids: <p>The IDs of the targets to remove from the rule.</p>
            force: <p>If this is a managed rule, created by an Amazon Web Services service on your behalf, you must specify <code>Force</code> as <code>True</code> to remove targets. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using <code>DescribeRule</code> or <code>ListRules</code> and checking the <code>ManagedBy</code> field of the response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.remove_targets_request.RemoveTargetsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.remove_targets_response.RemoveTargetsResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.remove_targets

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.remove_targets.async_remove_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.remove_targets_request.RemoveTargetsRequest = {}  # type: ignore[typeddict-item]
        input_["rule"] = rule
        if event_bus_name is not None:
            input_["event_bus_name"] = event_bus_name
        input_["ids"] = ids
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def start_replay(
        self,
        replay_name: "aws_sdk_cloudwatch_events.types.replay_name.ReplayName",
        event_source_arn: "aws_sdk_cloudwatch_events.types.arn.Arn",
        event_start_time: "aws_sdk_cloudwatch_events.types.timestamp.Timestamp",
        event_end_time: "aws_sdk_cloudwatch_events.types.timestamp.Timestamp",
        destination: "aws_sdk_cloudwatch_events.types.replay_destination.ReplayDestination",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.replay_description.ReplayDescription"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.start_replay_response.StartReplayResponse":
        """<p>Starts the specified replay. Events are not necessarily replayed in the exact same order that they were added to the archive. A replay processes events to replay based on the time in the event, and replays them using 1 minute intervals. If you specify an <code>EventStartTime</code> and an <code>EventEndTime</code> that covers a 20 minute time range, the events are replayed from the first minute of that 20 minute range first. Then the events from the second minute are replayed. You can use <code>DescribeReplay</code> to determine the progress of a replay. The value returned for <code>EventLastReplayedTime</code> indicates the time within the specified time range associated with the last event replayed.</p>

        Args:
            replay_name: <p>The name of the replay to start.</p>
            description: <p>A description for the replay to start.</p>
            event_source_arn: <p>The ARN of the archive to replay events from.</p>
            event_start_time: <p>A time stamp for the time to start replaying events. Only events that occurred between the <code>EventStartTime</code> and <code>EventEndTime</code> are replayed.</p>
            event_end_time: <p>A time stamp for the time to stop replaying events. Only events that occurred between the <code>EventStartTime</code> and <code>EventEndTime</code> are replayed.</p>
            destination: <p>A <code>ReplayDestination</code> object that includes details about the destination for the replay.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.start_replay_request.StartReplayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.start_replay_response.StartReplayResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.start_replay

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.start_replay.async_start_replay(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.start_replay_request.StartReplayRequest = {}  # type: ignore[typeddict-item]
        input_["replay_name"] = replay_name
        if description is not None:
            input_["description"] = description
        input_["event_source_arn"] = event_source_arn
        input_["event_start_time"] = event_start_time
        input_["event_end_time"] = event_end_time
        input_["destination"] = destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_cloudwatch_events.types.arn.Arn",
        tags: "aws_sdk_cloudwatch_events.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified EventBridge resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In EventBridge, rules and event buses can be tagged.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The ARN of the EventBridge resource that you're adding tags to.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_event_pattern(
        self,
        event_pattern: "aws_sdk_cloudwatch_events.types.event_pattern.EventPattern",
        event: "aws_sdk_cloudwatch_events.types.string.String",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> "aws_sdk_cloudwatch_events.types.test_event_pattern_response.TestEventPatternResponse":
        """<p>Tests whether the specified event pattern matches the provided event.</p> <p>Most services in Amazon Web Services treat : or / as the same character in Amazon Resource Names (ARNs). However, EventBridge uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.</p>

        Args:
            event_pattern: <p>The event pattern. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html\">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            event: <p>The event, in JSON format, to test against the event pattern. The JSON must follow the format specified in <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html\">Amazon Web Services Events</a>, and the following fields are mandatory:</p> <ul> <li> <p> <code>id</code> </p> </li> <li> <p> <code>account</code> </p> </li> <li> <p> <code>source</code> </p> </li> <li> <p> <code>time</code> </p> </li> <li> <p> <code>region</code> </p> </li> <li> <p> <code>resources</code> </p> </li> <li> <p> <code>detail-type</code> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.test_event_pattern_request.TestEventPatternRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.test_event_pattern_response.TestEventPatternResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.test_event_pattern

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.test_event_pattern.async_test_event_pattern(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.test_event_pattern_request.TestEventPatternRequest = {}  # type: ignore[typeddict-item]
        input_["event_pattern"] = event_pattern
        input_["event"] = event

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_cloudwatch_events.types.arn.Arn",
        tag_keys: "aws_sdk_cloudwatch_events.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
    ) -> (
        "aws_sdk_cloudwatch_events.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Removes one or more tags from the specified EventBridge resource. In Amazon EventBridge (CloudWatch Events), rules and event buses can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the EventBridge resource from which you are removing tags.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_api_destination(
        self,
        name: "aws_sdk_cloudwatch_events.types.api_destination_name.ApiDestinationName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.api_destination_description.ApiDestinationDescription"
        ] = None,
        connection_arn: Optional[
            "aws_sdk_cloudwatch_events.types.connection_arn.ConnectionArn"
        ] = None,
        invocation_endpoint: Optional[
            "aws_sdk_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
        ] = None,
        http_method: Optional[
            "aws_sdk_cloudwatch_events.types.api_destination_http_method.ApiDestinationHttpMethod"
        ] = None,
        invocation_rate_limit_per_second: Optional[
            "aws_sdk_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.update_api_destination_response.UpdateApiDestinationResponse":
        """<p>Updates an API destination.</p>

        Args:
            name: <p>The name of the API destination to update.</p>
            description: <p>The name of the API destination to update.</p>
            connection_arn: <p>The ARN of the connection to use for the API destination.</p>
            invocation_endpoint: <p>The URL to the endpoint to use for the API destination.</p>
            http_method: <p>The method to use for the API destination.</p>
            invocation_rate_limit_per_second: <p>The maximum number of invocations per second to send to the API destination.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.update_api_destination_request.UpdateApiDestinationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.update_api_destination_response.UpdateApiDestinationResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.update_api_destination

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.update_api_destination.async_update_api_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.update_api_destination_request.UpdateApiDestinationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if connection_arn is not None:
            input_["connection_arn"] = connection_arn
        if invocation_endpoint is not None:
            input_["invocation_endpoint"] = invocation_endpoint
        if http_method is not None:
            input_["http_method"] = http_method
        if invocation_rate_limit_per_second is not None:
            input_["invocation_rate_limit_per_second"] = (
                invocation_rate_limit_per_second
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_archive(
        self,
        archive_name: "aws_sdk_cloudwatch_events.types.archive_name.ArchiveName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.archive_description.ArchiveDescription"
        ] = None,
        event_pattern: Optional[
            "aws_sdk_cloudwatch_events.types.event_pattern.EventPattern"
        ] = None,
        retention_days: Optional[
            "aws_sdk_cloudwatch_events.types.retention_days.RetentionDays"
        ] = None,
    ) -> (
        "aws_sdk_cloudwatch_events.types.update_archive_response.UpdateArchiveResponse"
    ):
        """<p>Updates the specified archive.</p>

        Args:
            archive_name: <p>The name of the archive to update.</p>
            description: <p>The description for the archive.</p>
            event_pattern: <p>The event pattern to use to filter events sent to the archive.</p>
            retention_days: <p>The number of days to retain events in the archive.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.update_archive_request.UpdateArchiveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.update_archive_response.UpdateArchiveResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.update_archive

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.update_archive.async_update_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.update_archive_request.UpdateArchiveRequest = {}  # type: ignore[typeddict-item]
        input_["archive_name"] = archive_name
        if description is not None:
            input_["description"] = description
        if event_pattern is not None:
            input_["event_pattern"] = event_pattern
        if retention_days is not None:
            input_["retention_days"] = retention_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_connection(
        self,
        name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncCloudWatchEventsClientConfig] = None,
        description: Optional[
            "aws_sdk_cloudwatch_events.types.connection_description.ConnectionDescription"
        ] = None,
        authorization_type: Optional[
            "aws_sdk_cloudwatch_events.types.connection_authorization_type.ConnectionAuthorizationType"
        ] = None,
        auth_parameters: Optional[
            "aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters.UpdateConnectionAuthRequestParameters"
        ] = None,
    ) -> "aws_sdk_cloudwatch_events.types.update_connection_response.UpdateConnectionResponse":
        """<p>Updates settings for a connection.</p>

        Args:
            name: <p>The name of the connection to update.</p>
            description: <p>A description for the connection.</p>
            authorization_type: <p>The type of authorization to use for the connection.</p>
            auth_parameters: <p>The authorization parameters to use for the connection.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_cloudwatch_events.types.update_connection_request.UpdateConnectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_cloudwatch_events.types.update_connection_response.UpdateConnectionResponse"
        ]:
            import aws_sdk_cloudwatch_events._operations.aws_events.update_connection

            (
                output,
                http_response,
            ) = await aws_sdk_cloudwatch_events._operations.aws_events.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudwatch_events.types.update_connection_request.UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if authorization_type is not None:
            input_["authorization_type"] = authorization_type
        if auth_parameters is not None:
            input_["auth_parameters"] = auth_parameters

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
