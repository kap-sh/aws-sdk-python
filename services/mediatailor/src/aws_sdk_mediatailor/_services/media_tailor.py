"""Generated from Smithy shape ``com.amazonaws.mediatailor#MediaTailor``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import aws_sdk_mediatailor._auth._signers
import aws_sdk_mediatailor._auth._sigv4
from aws_sdk_mediatailor._auth._identity import Credentials
from aws_sdk_mediatailor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_mediatailor._auth._zapros_handler import AuthMiddleware
from aws_sdk_mediatailor._pagination import resolve_path as _resolve_path
from aws_sdk_mediatailor._resources.media_tailor.channel_resource import ChannelResource
from aws_sdk_mediatailor._resources.media_tailor.function_resource import (
    FunctionResource,
)
from aws_sdk_mediatailor._resources.media_tailor.live_source_resource import (
    LiveSourceResource,
)
from aws_sdk_mediatailor._resources.media_tailor.playback_configuration_resource import (
    PlaybackConfigurationResource,
)
from aws_sdk_mediatailor._resources.media_tailor.prefetch_schedule_resource import (
    PrefetchScheduleResource,
)
from aws_sdk_mediatailor._resources.media_tailor.source_location_resource import (
    SourceLocationResource,
)
from aws_sdk_mediatailor._resources.media_tailor.vod_source_resource import (
    VodSourceResource,
)
from aws_sdk_mediatailor._services._aws_config import aws_config
from aws_sdk_mediatailor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer
    import aws_sdk_mediatailor.types.__list_of__string
    import aws_sdk_mediatailor.types.__list_of_logging_strategies
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.ads_interaction_log
    import aws_sdk_mediatailor.types.alert
    import aws_sdk_mediatailor.types.configure_logs_for_playback_configuration_request
    import aws_sdk_mediatailor.types.configure_logs_for_playback_configuration_response
    import aws_sdk_mediatailor.types.list_alerts_request
    import aws_sdk_mediatailor.types.list_alerts_response
    import aws_sdk_mediatailor.types.list_tags_for_resource_request
    import aws_sdk_mediatailor.types.list_tags_for_resource_response
    import aws_sdk_mediatailor.types.manifest_service_interaction_log
    import aws_sdk_mediatailor.types.max_results
    import aws_sdk_mediatailor.types.tag_resource_request
    import aws_sdk_mediatailor.types.untag_resource_request


class MediaTailorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MediaTailorClient:
    """A client for the ``MediaTailor`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = MediaTailorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.channel_resource = ChannelResource(self)
        self.function_resource = FunctionResource(self)
        self.live_source_resource = LiveSourceResource(self)
        self.playback_configuration_resource = PlaybackConfigurationResource(self)
        self.prefetch_schedule_resource = PrefetchScheduleResource(self)
        self.source_location_resource = SourceLocationResource(self)
        self.vod_source_resource = VodSourceResource(self)

    def operation_options(
        self, config_overrides: Optional[MediaTailorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaTailorClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def configure_logs_for_playback_configuration(
        self,
        percent_enabled: "aws_sdk_mediatailor.types.__integer.__integer",
        playback_configuration_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        enabled_logging_strategies: Optional[
            "aws_sdk_mediatailor.types.__list_of_logging_strategies.__listOfLoggingStrategies"
        ] = None,
        ads_interaction_log: Optional[
            "aws_sdk_mediatailor.types.ads_interaction_log.AdsInteractionLog"
        ] = None,
        manifest_service_interaction_log: Optional[
            "aws_sdk_mediatailor.types.manifest_service_interaction_log.ManifestServiceInteractionLog"
        ] = None,
    ) -> "aws_sdk_mediatailor.types.configure_logs_for_playback_configuration_response.ConfigureLogsForPlaybackConfigurationResponse":
        r"""<p>Defines where AWS Elemental MediaTailor sends logs for the playback configuration.</p>

        Args:
            percent_enabled: <p>The percentage of session logs that MediaTailor sends to your CloudWatch Logs account. For example, if your playback configuration has 1000 sessions and percentEnabled is set to <code>60</code>, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html\">debug log mode</a>.</p> <p>Valid values: <code>0</code> - <code>100</code> </p>
            playback_configuration_name: <p>The name of the playback configuration.</p>
            enabled_logging_strategies: <p>The method used for collecting logs from AWS Elemental MediaTailor. To configure MediaTailor to send logs directly to Amazon CloudWatch Logs, choose <code>LEGACY_CLOUDWATCH</code>. To configure MediaTailor to send logs to CloudWatch, which then vends the logs to your destination of choice, choose <code>VENDED_LOGS</code>. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.</p> <p>To use vended logs, you must configure the delivery destination in Amazon CloudWatch, as described in <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-vended-logs-permissions-V2\">Enable logging from AWS services, Logging that requires additional permissions [V2]</a>.</p>
            ads_interaction_log: <p>The event types that MediaTailor emits in logs for interactions with the ADS.</p>
            manifest_service_interaction_log: <p>The event types that MediaTailor emits in logs for interactions with the origin server.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.configure_logs_for_playback_configuration_request.ConfigureLogsForPlaybackConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.configure_logs_for_playback_configuration_response.ConfigureLogsForPlaybackConfigurationResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.configure_logs_for_playback_configuration

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.configure_logs_for_playback_configuration.configure_logs_for_playback_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.configure_logs_for_playback_configuration_request.ConfigureLogsForPlaybackConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["percent_enabled"] = percent_enabled
        input_["playback_configuration_name"] = playback_configuration_name
        if enabled_logging_strategies is not None:
            input_["enabled_logging_strategies"] = enabled_logging_strategies
        if ads_interaction_log is not None:
            input_["ads_interaction_log"] = ads_interaction_log
        if manifest_service_interaction_log is not None:
            input_["manifest_service_interaction_log"] = (
                manifest_service_interaction_log
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_alerts(
        self,
        resource_arn: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediatailor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
    ) -> "aws_sdk_mediatailor.types.list_alerts_response.ListAlertsResponse":
        """<p>Lists the alerts that are associated with a MediaTailor channel assembly resource.</p>

        Args:
            max_results: <p>The maximum number of alerts that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> alerts, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListAlerts</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.list_alerts_request.ListAlertsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.list_alerts_response.ListAlertsResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_alerts

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.list_alerts.list_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.list_alerts_request.ListAlertsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_alerts(
        self,
        resource_arn: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediatailor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[aws_sdk_mediatailor.types.alert.Alert]":
        _token = next_token
        while True:
            _response = self.list_alerts(
                resource_arn,
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>A list of tags that are associated with this resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with this resource.</p>

        Raises:
            aws_sdk_mediatailor.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data.</p>
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_tags_for_resource

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_mediatailor.types.__string.__string",
        tags: "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> None:
        r"""<p>The resource to tag. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource.</p>
            tags: <p>The tags to assign to the resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            aws_sdk_mediatailor.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data.</p>
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mediatailor._operations.media_tailor.tag_resource

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_mediatailor.types.__string.__string",
        tag_keys: "aws_sdk_mediatailor.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> None:
        """<p>The resource to untag.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to untag.</p>
            tag_keys: <p>The tag keys associated with the resource.</p>

        Raises:
            aws_sdk_mediatailor.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data.</p>
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_mediatailor._operations.media_tailor.untag_resource

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
