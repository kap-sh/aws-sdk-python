"""Generated from Smithy shape ``com.amazonaws.devopsguru#CapstoneControlPlaneService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_devops_guru._auth._signers
import aws_sdk_devops_guru._auth._sigv4
from aws_sdk_devops_guru._auth._identity import Credentials
from aws_sdk_devops_guru._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_devops_guru._auth._zapros_handler import AuthMiddleware
from aws_sdk_devops_guru._pagination import resolve_path as _resolve_path
from aws_sdk_devops_guru._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.account_id_list
    import aws_sdk_devops_guru.types.add_notification_channel_request
    import aws_sdk_devops_guru.types.add_notification_channel_response
    import aws_sdk_devops_guru.types.anomaly_id
    import aws_sdk_devops_guru.types.aws_account_id
    import aws_sdk_devops_guru.types.client_token
    import aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter
    import aws_sdk_devops_guru.types.delete_insight_request
    import aws_sdk_devops_guru.types.delete_insight_response
    import aws_sdk_devops_guru.types.describe_account_health_request
    import aws_sdk_devops_guru.types.describe_account_health_response
    import aws_sdk_devops_guru.types.describe_account_overview_request
    import aws_sdk_devops_guru.types.describe_account_overview_response
    import aws_sdk_devops_guru.types.describe_anomaly_request
    import aws_sdk_devops_guru.types.describe_anomaly_response
    import aws_sdk_devops_guru.types.describe_event_sources_config_request
    import aws_sdk_devops_guru.types.describe_event_sources_config_response
    import aws_sdk_devops_guru.types.describe_feedback_request
    import aws_sdk_devops_guru.types.describe_feedback_response
    import aws_sdk_devops_guru.types.describe_insight_request
    import aws_sdk_devops_guru.types.describe_insight_response
    import aws_sdk_devops_guru.types.describe_organization_health_request
    import aws_sdk_devops_guru.types.describe_organization_health_response
    import aws_sdk_devops_guru.types.describe_organization_overview_request
    import aws_sdk_devops_guru.types.describe_organization_overview_response
    import aws_sdk_devops_guru.types.describe_organization_resource_collection_health_request
    import aws_sdk_devops_guru.types.describe_organization_resource_collection_health_response
    import aws_sdk_devops_guru.types.describe_resource_collection_health_request
    import aws_sdk_devops_guru.types.describe_resource_collection_health_response
    import aws_sdk_devops_guru.types.describe_service_integration_request
    import aws_sdk_devops_guru.types.describe_service_integration_response
    import aws_sdk_devops_guru.types.event
    import aws_sdk_devops_guru.types.event_sources_config
    import aws_sdk_devops_guru.types.get_cost_estimation_request
    import aws_sdk_devops_guru.types.get_cost_estimation_response
    import aws_sdk_devops_guru.types.get_resource_collection_request
    import aws_sdk_devops_guru.types.get_resource_collection_response
    import aws_sdk_devops_guru.types.insight_feedback
    import aws_sdk_devops_guru.types.insight_id
    import aws_sdk_devops_guru.types.insight_type
    import aws_sdk_devops_guru.types.list_anomalies_for_insight_filters
    import aws_sdk_devops_guru.types.list_anomalies_for_insight_max_results
    import aws_sdk_devops_guru.types.list_anomalies_for_insight_request
    import aws_sdk_devops_guru.types.list_anomalies_for_insight_response
    import aws_sdk_devops_guru.types.list_anomalous_log_groups_max_results
    import aws_sdk_devops_guru.types.list_anomalous_log_groups_request
    import aws_sdk_devops_guru.types.list_anomalous_log_groups_response
    import aws_sdk_devops_guru.types.list_events_filters
    import aws_sdk_devops_guru.types.list_events_max_results
    import aws_sdk_devops_guru.types.list_events_request
    import aws_sdk_devops_guru.types.list_events_response
    import aws_sdk_devops_guru.types.list_insights_account_id_list
    import aws_sdk_devops_guru.types.list_insights_max_results
    import aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list
    import aws_sdk_devops_guru.types.list_insights_request
    import aws_sdk_devops_guru.types.list_insights_response
    import aws_sdk_devops_guru.types.list_insights_status_filter
    import aws_sdk_devops_guru.types.list_monitored_resources_filters
    import aws_sdk_devops_guru.types.list_monitored_resources_max_results
    import aws_sdk_devops_guru.types.list_monitored_resources_request
    import aws_sdk_devops_guru.types.list_monitored_resources_response
    import aws_sdk_devops_guru.types.list_notification_channels_request
    import aws_sdk_devops_guru.types.list_notification_channels_response
    import aws_sdk_devops_guru.types.list_organization_insights_request
    import aws_sdk_devops_guru.types.list_organization_insights_response
    import aws_sdk_devops_guru.types.list_recommendations_request
    import aws_sdk_devops_guru.types.list_recommendations_response
    import aws_sdk_devops_guru.types.locale
    import aws_sdk_devops_guru.types.notification_channel
    import aws_sdk_devops_guru.types.notification_channel_config
    import aws_sdk_devops_guru.types.notification_channel_id
    import aws_sdk_devops_guru.types.organization_resource_collection_max_results
    import aws_sdk_devops_guru.types.organization_resource_collection_type
    import aws_sdk_devops_guru.types.organizational_unit_id_list
    import aws_sdk_devops_guru.types.put_feedback_request
    import aws_sdk_devops_guru.types.put_feedback_response
    import aws_sdk_devops_guru.types.recommendation
    import aws_sdk_devops_guru.types.remove_notification_channel_request
    import aws_sdk_devops_guru.types.remove_notification_channel_response
    import aws_sdk_devops_guru.types.resource_collection_type
    import aws_sdk_devops_guru.types.search_insights_account_id_list
    import aws_sdk_devops_guru.types.search_insights_filters
    import aws_sdk_devops_guru.types.search_insights_max_results
    import aws_sdk_devops_guru.types.search_insights_request
    import aws_sdk_devops_guru.types.search_insights_response
    import aws_sdk_devops_guru.types.search_organization_insights_filters
    import aws_sdk_devops_guru.types.search_organization_insights_max_results
    import aws_sdk_devops_guru.types.search_organization_insights_request
    import aws_sdk_devops_guru.types.search_organization_insights_response
    import aws_sdk_devops_guru.types.start_cost_estimation_request
    import aws_sdk_devops_guru.types.start_cost_estimation_response
    import aws_sdk_devops_guru.types.start_time_range
    import aws_sdk_devops_guru.types.timestamp
    import aws_sdk_devops_guru.types.update_event_sources_config_request
    import aws_sdk_devops_guru.types.update_event_sources_config_response
    import aws_sdk_devops_guru.types.update_resource_collection_action
    import aws_sdk_devops_guru.types.update_resource_collection_filter
    import aws_sdk_devops_guru.types.update_resource_collection_request
    import aws_sdk_devops_guru.types.update_resource_collection_response
    import aws_sdk_devops_guru.types.update_service_integration_config
    import aws_sdk_devops_guru.types.update_service_integration_request
    import aws_sdk_devops_guru.types.update_service_integration_response
    import aws_sdk_devops_guru.types.uuid_next_token


class DevOpsGuruClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class DevOpsGuruClient:
    """A client for the ``DevOpsGuru`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self.config = DevOpsGuruClientConfig(
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
        self, config_overrides: Optional[DevOpsGuruClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DevOpsGuruClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def add_notification_channel(
        self,
        config: "aws_sdk_devops_guru.types.notification_channel_config.NotificationChannelConfig",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
    ) -> "aws_sdk_devops_guru.types.add_notification_channel_response.AddNotificationChannelResponse":
        """<p> Adds a notification channel to DevOps Guru. A notification channel is used to notify you about important DevOps Guru events, such as when an insight is generated. </p> <p>If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html\">Permissions for Amazon SNS topics</a>.</p> <p>If you use an Amazon SNS topic that is encrypted by an Amazon Web Services Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html\">Permissions for Amazon Web Services KMS–encrypted Amazon SNS topics</a>.</p>

        Args:
            config: <p> A <code>NotificationChannelConfig</code> object that specifies what type of notification channel to add. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS). </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.add_notification_channel_request.AddNotificationChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.add_notification_channel_response.AddNotificationChannelResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.add_notification_channel

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.add_notification_channel.add_notification_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.add_notification_channel_request.AddNotificationChannelRequest = {}  # type: ignore[typeddict-item]
        input["config"] = config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_insight(
        self,
        id: "aws_sdk_devops_guru.types.insight_id.InsightId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
    ) -> "aws_sdk_devops_guru.types.delete_insight_response.DeleteInsightResponse":
        """<p>Deletes the insight along with the associated anomalies, events and recommendations.</p>

        Args:
            id: <p>The ID of the insight.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.delete_insight_request.DeleteInsightRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.delete_insight_response.DeleteInsightResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.delete_insight

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.delete_insight.delete_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.delete_insight_request.DeleteInsightRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_account_health(
        self, *, config_overrides: Optional[DevOpsGuruClientConfig] = None
    ) -> "aws_sdk_devops_guru.types.describe_account_health_response.DescribeAccountHealthResponse":
        """<p> Returns the number of open reactive insights, the number of open proactive insights, and the number of metrics analyzed in your Amazon Web Services account. Use these numbers to gauge the health of operations in your Amazon Web Services account. </p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_account_health_request.DescribeAccountHealthRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_account_health_response.DescribeAccountHealthResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_account_health

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_account_health.describe_account_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_account_health_request.DescribeAccountHealthRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_account_overview(
        self,
        from_time: "aws_sdk_devops_guru.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        to_time: Optional["aws_sdk_devops_guru.types.timestamp.Timestamp"] = None,
    ) -> "aws_sdk_devops_guru.types.describe_account_overview_response.DescribeAccountOverviewResponse":
        """<p> For the time range passed in, returns the number of open reactive insight that were created, the number of open proactive insights that were created, and the Mean Time to Recover (MTTR) for all closed reactive insights. </p>

        Args:
            from_time: <p> The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day. </p>
            to_time: <p> The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_account_overview_request.DescribeAccountOverviewRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_account_overview_response.DescribeAccountOverviewResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_account_overview

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_account_overview.describe_account_overview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_account_overview_request.DescribeAccountOverviewRequest = {}  # type: ignore[typeddict-item]
        input["from_time"] = from_time
        if to_time is not None:
            input["to_time"] = to_time

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_anomaly(
        self,
        id: "aws_sdk_devops_guru.types.anomaly_id.AnomalyId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.describe_anomaly_response.DescribeAnomalyResponse":
        """<p> Returns details about an anomaly that you specify using its ID. </p>

        Args:
            id: <p> The ID of the anomaly. </p>
            account_id: <p>The ID of the member account.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_anomaly_request.DescribeAnomalyRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_anomaly_response.DescribeAnomalyResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_anomaly

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_anomaly.describe_anomaly(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_anomaly_request.DescribeAnomalyRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_event_sources_config(
        self, *, config_overrides: Optional[DevOpsGuruClientConfig] = None
    ) -> "aws_sdk_devops_guru.types.describe_event_sources_config_response.DescribeEventSourcesConfigResponse":
        """<p>Returns the integration status of services that are integrated with DevOps Guru as Consumer via EventBridge. The one service that can be integrated with DevOps Guru is Amazon CodeGuru Profiler, which can produce proactive recommendations which can be stored and viewed in DevOps Guru.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_event_sources_config_request.DescribeEventSourcesConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_event_sources_config_response.DescribeEventSourcesConfigResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_event_sources_config

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_event_sources_config.describe_event_sources_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_event_sources_config_request.DescribeEventSourcesConfigRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_feedback(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        insight_id: Optional["aws_sdk_devops_guru.types.insight_id.InsightId"] = None,
    ) -> (
        "aws_sdk_devops_guru.types.describe_feedback_response.DescribeFeedbackResponse"
    ):
        """<p> Returns the most recent feedback submitted in the current Amazon Web Services account and Region. </p>

        Args:
            insight_id: <p> The ID of the insight for which the feedback was provided. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_feedback_request.DescribeFeedbackRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_feedback_response.DescribeFeedbackResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_feedback

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_feedback.describe_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_feedback_request.DescribeFeedbackRequest = {}  # type: ignore[typeddict-item]
        if insight_id is not None:
            input["insight_id"] = insight_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_insight(
        self,
        id: "aws_sdk_devops_guru.types.insight_id.InsightId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.describe_insight_response.DescribeInsightResponse":
        """<p> Returns details about an insight that you specify using its ID. </p>

        Args:
            id: <p> The ID of the insight. </p>
            account_id: <p>The ID of the member account in the organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_insight_request.DescribeInsightRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_insight_response.DescribeInsightResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_insight

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_insight.describe_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_insight_request.DescribeInsightRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization_health(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_devops_guru.types.account_id_list.AccountIdList"
        ] = None,
        organizational_unit_ids: Optional[
            "aws_sdk_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.describe_organization_health_response.DescribeOrganizationHealthResponse":
        """<p>Returns active insights, predictive insights, and resource hours analyzed in last hour.</p>

        Args:
            account_ids: <p>The ID of the Amazon Web Services account.</p>
            organizational_unit_ids: <p>The ID of the organizational unit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_organization_health_request.DescribeOrganizationHealthRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_organization_health_response.DescribeOrganizationHealthResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_organization_health

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_organization_health.describe_organization_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_organization_health_request.DescribeOrganizationHealthRequest = {}  # type: ignore[typeddict-item]
        if account_ids is not None:
            input["account_ids"] = account_ids
        if organizational_unit_ids is not None:
            input["organizational_unit_ids"] = organizational_unit_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization_overview(
        self,
        from_time: "aws_sdk_devops_guru.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        to_time: Optional["aws_sdk_devops_guru.types.timestamp.Timestamp"] = None,
        account_ids: Optional[
            "aws_sdk_devops_guru.types.account_id_list.AccountIdList"
        ] = None,
        organizational_unit_ids: Optional[
            "aws_sdk_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.describe_organization_overview_response.DescribeOrganizationOverviewResponse":
        """<p>Returns an overview of your organization's history based on the specified time range. The overview includes the total reactive and proactive insights.</p>

        Args:
            from_time: <p> The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day. </p>
            to_time: <p> The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used. </p>
            account_ids: <p>The ID of the Amazon Web Services account.</p>
            organizational_unit_ids: <p>The ID of the organizational unit.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_organization_overview_request.DescribeOrganizationOverviewRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_organization_overview_response.DescribeOrganizationOverviewResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_organization_overview

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_organization_overview.describe_organization_overview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_organization_overview_request.DescribeOrganizationOverviewRequest = {}  # type: ignore[typeddict-item]
        input["from_time"] = from_time
        if to_time is not None:
            input["to_time"] = to_time
        if account_ids is not None:
            input["account_ids"] = account_ids
        if organizational_unit_ids is not None:
            input["organizational_unit_ids"] = organizational_unit_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_organization_resource_collection_health(
        self,
        organization_resource_collection_type: "aws_sdk_devops_guru.types.organization_resource_collection_type.OrganizationResourceCollectionType",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        account_ids: Optional[
            "aws_sdk_devops_guru.types.account_id_list.AccountIdList"
        ] = None,
        organizational_unit_ids: Optional[
            "aws_sdk_devops_guru.types.organizational_unit_id_list.OrganizationalUnitIdList"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.organization_resource_collection_max_results.OrganizationResourceCollectionMaxResults"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.describe_organization_resource_collection_health_response.DescribeOrganizationResourceCollectionHealthResponse":
        """<p>Provides an overview of your system's health. If additional member accounts are part of your organization, you can filter those accounts using the <code>AccountIds</code> field.</p>

        Args:
            organization_resource_collection_type: <p> An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>
            account_ids: <p>The ID of the Amazon Web Services account.</p>
            organizational_unit_ids: <p>The ID of the organizational unit.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_organization_resource_collection_health_request.DescribeOrganizationResourceCollectionHealthRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_organization_resource_collection_health_response.DescribeOrganizationResourceCollectionHealthResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_organization_resource_collection_health

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_organization_resource_collection_health.describe_organization_resource_collection_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_organization_resource_collection_health_request.DescribeOrganizationResourceCollectionHealthRequest = {}  # type: ignore[typeddict-item]
        input["organization_resource_collection_type"] = (
            organization_resource_collection_type
        )
        if account_ids is not None:
            input["account_ids"] = account_ids
        if organizational_unit_ids is not None:
            input["organizational_unit_ids"] = organizational_unit_ids
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_resource_collection_health(
        self,
        resource_collection_type: "aws_sdk_devops_guru.types.resource_collection_type.ResourceCollectionType",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.describe_resource_collection_health_response.DescribeResourceCollectionHealthResponse":
        """<p> Returns the number of open proactive insights, open reactive insights, and the Mean Time to Recover (MTTR) for all closed insights in resource collections in your account. You specify the type of Amazon Web Services resources collection. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>

        Args:
            resource_collection_type: <p> An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_resource_collection_health_request.DescribeResourceCollectionHealthRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_resource_collection_health_response.DescribeResourceCollectionHealthResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_resource_collection_health

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_resource_collection_health.describe_resource_collection_health(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_resource_collection_health_request.DescribeResourceCollectionHealthRequest = {}  # type: ignore[typeddict-item]
        input["resource_collection_type"] = resource_collection_type
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_service_integration(
        self, *, config_overrides: Optional[DevOpsGuruClientConfig] = None
    ) -> "aws_sdk_devops_guru.types.describe_service_integration_response.DescribeServiceIntegrationResponse":
        """<p> Returns the integration status of services that are integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight. </p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.describe_service_integration_request.DescribeServiceIntegrationRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.describe_service_integration_response.DescribeServiceIntegrationResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_service_integration

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.describe_service_integration.describe_service_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.describe_service_integration_request.DescribeServiceIntegrationRequest = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_cost_estimation(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.get_cost_estimation_response.GetCostEstimationResponse":
        """<p>Returns an estimate of the monthly cost for DevOps Guru to analyze your Amazon Web Services resources. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html\">Estimate your Amazon DevOps Guru costs</a> and <a href=\"http://aws.amazon.com/devops-guru/pricing/\">Amazon DevOps Guru pricing</a>.</p>

        Args:
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.get_cost_estimation_request.GetCostEstimationRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.get_cost_estimation_response.GetCostEstimationResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.get_cost_estimation

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.get_cost_estimation.get_cost_estimation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.get_cost_estimation_request.GetCostEstimationRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_collection(
        self,
        resource_collection_type: "aws_sdk_devops_guru.types.resource_collection_type.ResourceCollectionType",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.get_resource_collection_response.GetResourceCollectionResponse":
        """<p> Returns lists Amazon Web Services resources that are of the specified resource collection type. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>

        Args:
            resource_collection_type: <p> The type of Amazon Web Services resource collections to return. The one valid value is <code>CLOUD_FORMATION</code> for Amazon Web Services CloudFormation stacks. </p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.get_resource_collection_request.GetResourceCollectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.get_resource_collection_response.GetResourceCollectionResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.get_resource_collection

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.get_resource_collection.get_resource_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.get_resource_collection_request.GetResourceCollectionRequest = {}  # type: ignore[typeddict-item]
        input["resource_collection_type"] = resource_collection_type
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_anomalies_for_insight(
        self,
        insight_id: "aws_sdk_devops_guru.types.insight_id.InsightId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        start_time_range: Optional[
            "aws_sdk_devops_guru.types.start_time_range.StartTimeRange"
        ] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_anomalies_for_insight_max_results.ListAnomaliesForInsightMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
        filters: Optional[
            "aws_sdk_devops_guru.types.list_anomalies_for_insight_filters.ListAnomaliesForInsightFilters"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_anomalies_for_insight_response.ListAnomaliesForInsightResponse":
        """<p> Returns a list of the anomalies that belong to an insight that you specify using its ID. </p>

        Args:
            insight_id: <p> The ID of the insight. The returned anomalies belong to this insight. </p>
            start_time_range: <p> A time range used to specify when the requested anomalies started. All returned anomalies started during this time range. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            account_id: <p>The ID of the Amazon Web Services account. </p>
            filters: <p> Specifies one or more service names that are used to list anomalies. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_anomalies_for_insight_request.ListAnomaliesForInsightRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_anomalies_for_insight_response.ListAnomaliesForInsightResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_anomalies_for_insight

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_anomalies_for_insight.list_anomalies_for_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_anomalies_for_insight_request.ListAnomaliesForInsightRequest = {}  # type: ignore[typeddict-item]
        input["insight_id"] = insight_id
        if start_time_range is not None:
            input["start_time_range"] = start_time_range
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_anomalous_log_groups(
        self,
        insight_id: "aws_sdk_devops_guru.types.insight_id.InsightId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_anomalous_log_groups_max_results.ListAnomalousLogGroupsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_anomalous_log_groups_response.ListAnomalousLogGroupsResponse":
        """<p> Returns the list of log groups that contain log anomalies. </p>

        Args:
            insight_id: <p> The ID of the insight containing the log groups. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_anomalous_log_groups_request.ListAnomalousLogGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_anomalous_log_groups_response.ListAnomalousLogGroupsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_anomalous_log_groups

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_anomalous_log_groups.list_anomalous_log_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_anomalous_log_groups_request.ListAnomalousLogGroupsRequest = {}  # type: ignore[typeddict-item]
        input["insight_id"] = insight_id
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_events(
        self,
        filters: "aws_sdk_devops_guru.types.list_events_filters.ListEventsFilters",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_events_max_results.ListEventsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_events_response.ListEventsResponse":
        """<p> Returns a list of the events emitted by the resources that are evaluated by DevOps Guru. You can use filters to specify which events are returned. </p>

        Args:
            filters: <p> A <code>ListEventsFilters</code> object used to specify which events to return. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            account_id: <p>The ID of the Amazon Web Services account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_events_request.ListEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_events_response.ListEventsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_events

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_events.list_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_events_request.ListEventsRequest = {}  # type: ignore[typeddict-item]
        input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_events(
        self,
        filters: "aws_sdk_devops_guru.types.list_events_filters.ListEventsFilters",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_events_max_results.ListEventsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "Iterator[aws_sdk_devops_guru.types.event.Event]":
        _token = next_token
        while True:
            _response = self.list_events(
                filters,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_insights(
        self,
        status_filter: "aws_sdk_devops_guru.types.list_insights_status_filter.ListInsightsStatusFilter",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_insights_max_results.ListInsightsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_insights_response.ListInsightsResponse":
        """<p> Returns a list of insights in your Amazon Web Services account. You can specify which insights are returned by their start time and status (<code>ONGOING</code>, <code>CLOSED</code>, or <code>ANY</code>). </p>

        Args:
            status_filter: <p> A filter used to filter the returned insights by their status. You can specify one status filter. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_insights_request.ListInsightsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_insights_response.ListInsightsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_insights

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_insights.list_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_insights_request.ListInsightsRequest = {}  # type: ignore[typeddict-item]
        input["status_filter"] = status_filter
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_monitored_resources(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        filters: Optional[
            "aws_sdk_devops_guru.types.list_monitored_resources_filters.ListMonitoredResourcesFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_monitored_resources_max_results.ListMonitoredResourcesMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_monitored_resources_response.ListMonitoredResourcesResponse":
        """<p> Returns the list of all log groups that are being monitored and tagged by DevOps Guru. </p>

        Args:
            filters: <p> Filters to determine which monitored resources you want to retrieve. You can filter by resource type or resource permission status. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_monitored_resources_request.ListMonitoredResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_monitored_resources_response.ListMonitoredResourcesResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_monitored_resources

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_monitored_resources.list_monitored_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_monitored_resources_request.ListMonitoredResourcesRequest = {}  # type: ignore[typeddict-item]
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_notification_channels(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_notification_channels_response.ListNotificationChannelsResponse":
        """<p> Returns a list of notification channels configured for DevOps Guru. Each notification channel is used to notify you when DevOps Guru generates an insight that contains information about how to improve your operations. The one supported notification channel is Amazon Simple Notification Service (Amazon SNS). </p>

        Args:
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_notification_channels_request.ListNotificationChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_notification_channels_response.ListNotificationChannelsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_notification_channels

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_notification_channels.list_notification_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_notification_channels_request.ListNotificationChannelsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_notification_channels(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_devops_guru.types.notification_channel.NotificationChannel]":
        _token = next_token
        while True:
            _response = self.list_notification_channels(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_organization_insights(
        self,
        status_filter: "aws_sdk_devops_guru.types.list_insights_status_filter.ListInsightsStatusFilter",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.list_insights_max_results.ListInsightsMaxResults"
        ] = None,
        account_ids: Optional[
            "aws_sdk_devops_guru.types.list_insights_account_id_list.ListInsightsAccountIdList"
        ] = None,
        organizational_unit_ids: Optional[
            "aws_sdk_devops_guru.types.list_insights_organizational_unit_id_list.ListInsightsOrganizationalUnitIdList"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_organization_insights_response.ListOrganizationInsightsResponse":
        """<p>Returns a list of insights associated with the account or OU Id.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            account_ids: <p>The ID of the Amazon Web Services account. </p>
            organizational_unit_ids: <p>The ID of the organizational unit.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_organization_insights_request.ListOrganizationInsightsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_organization_insights_response.ListOrganizationInsightsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_organization_insights

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_organization_insights.list_organization_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_organization_insights_request.ListOrganizationInsightsRequest = {}  # type: ignore[typeddict-item]
        input["status_filter"] = status_filter
        if max_results is not None:
            input["max_results"] = max_results
        if account_ids is not None:
            input["account_ids"] = account_ids
        if organizational_unit_ids is not None:
            input["organizational_unit_ids"] = organizational_unit_ids
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_recommendations(
        self,
        insight_id: "aws_sdk_devops_guru.types.insight_id.InsightId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
        locale: Optional["aws_sdk_devops_guru.types.locale.Locale"] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.list_recommendations_response.ListRecommendationsResponse":
        """<p> Returns a list of a specified insight's recommendations. Each recommendation includes a list of related metrics and a list of related events. </p>

        Args:
            insight_id: <p> The ID of the requested insight. </p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            locale: <p>A locale that specifies the language to use for recommendations.</p>
            account_id: <p>The ID of the Amazon Web Services account. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.list_recommendations

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.list_recommendations.list_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.list_recommendations_request.ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
        input["insight_id"] = insight_id
        if next_token is not None:
            input["next_token"] = next_token
        if locale is not None:
            input["locale"] = locale
        if account_id is not None:
            input["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_recommendations(
        self,
        insight_id: "aws_sdk_devops_guru.types.insight_id.InsightId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
        locale: Optional["aws_sdk_devops_guru.types.locale.Locale"] = None,
        account_id: Optional[
            "aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "Iterator[aws_sdk_devops_guru.types.recommendation.Recommendation]":
        _token = next_token
        while True:
            _response = self.list_recommendations(
                insight_id,
                config_overrides=config_overrides,
                next_token=_token,
                locale=locale,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_feedback(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        insight_feedback: Optional[
            "aws_sdk_devops_guru.types.insight_feedback.InsightFeedback"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.put_feedback_response.PutFeedbackResponse":
        """<p> Collects customer feedback about the specified insight. </p>

        Args:
            insight_feedback: <p> The feedback from customers is about the recommendations in this insight. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.put_feedback_request.PutFeedbackRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.put_feedback_response.PutFeedbackResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.put_feedback

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.put_feedback.put_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.put_feedback_request.PutFeedbackRequest = {}  # type: ignore[typeddict-item]
        if insight_feedback is not None:
            input["insight_feedback"] = insight_feedback

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_notification_channel(
        self,
        id: "aws_sdk_devops_guru.types.notification_channel_id.NotificationChannelId",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
    ) -> "aws_sdk_devops_guru.types.remove_notification_channel_response.RemoveNotificationChannelResponse":
        """<p> Removes a notification channel from DevOps Guru. A notification channel is used to notify you when DevOps Guru generates an insight that contains information about how to improve your operations. </p>

        Args:
            id: <p> The ID of the notification channel to be removed. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.remove_notification_channel_request.RemoveNotificationChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.remove_notification_channel_response.RemoveNotificationChannelResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.remove_notification_channel

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.remove_notification_channel.remove_notification_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.remove_notification_channel_request.RemoveNotificationChannelRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_insights(
        self,
        start_time_range: "aws_sdk_devops_guru.types.start_time_range.StartTimeRange",
        type: "aws_sdk_devops_guru.types.insight_type.InsightType",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        filters: Optional[
            "aws_sdk_devops_guru.types.search_insights_filters.SearchInsightsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.search_insights_max_results.SearchInsightsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.search_insights_response.SearchInsightsResponse":
        """<p> Returns a list of insights in your Amazon Web Services account. You can specify which insights are returned by their start time, one or more statuses (<code>ONGOING</code> or <code>CLOSED</code>), one or more severities (<code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>), and type (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p> <p> Use the <code>Filters</code> parameter to specify status and severity search parameters. Use the <code>Type</code> parameter to specify <code>REACTIVE</code> or <code>PROACTIVE</code> in your search. </p>

        Args:
            start_time_range: <p> The start of the time range passed in. Returned insights occurred after this time. </p>
            filters: <p> A <code>SearchInsightsFilters</code> object that is used to set the severity and status filters on your insight search. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            type: <p> The type of insights you are searching for (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.search_insights_request.SearchInsightsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.search_insights_response.SearchInsightsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.search_insights

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.search_insights.search_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.search_insights_request.SearchInsightsRequest = {}  # type: ignore[typeddict-item]
        input["start_time_range"] = start_time_range
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_organization_insights(
        self,
        account_ids: "aws_sdk_devops_guru.types.search_insights_account_id_list.SearchInsightsAccountIdList",
        start_time_range: "aws_sdk_devops_guru.types.start_time_range.StartTimeRange",
        type: "aws_sdk_devops_guru.types.insight_type.InsightType",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        filters: Optional[
            "aws_sdk_devops_guru.types.search_organization_insights_filters.SearchOrganizationInsightsFilters"
        ] = None,
        max_results: Optional[
            "aws_sdk_devops_guru.types.search_organization_insights_max_results.SearchOrganizationInsightsMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.search_organization_insights_response.SearchOrganizationInsightsResponse":
        """<p> Returns a list of insights in your organization. You can specify which insights are returned by their start time, one or more statuses (<code>ONGOING</code>, <code>CLOSED</code>, and <code>CLOSED</code>), one or more severities (<code>LOW</code>, <code>MEDIUM</code>, and <code>HIGH</code>), and type (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p> <p> Use the <code>Filters</code> parameter to specify status and severity search parameters. Use the <code>Type</code> parameter to specify <code>REACTIVE</code> or <code>PROACTIVE</code> in your search. </p>

        Args:
            account_ids: <p>The ID of the Amazon Web Services account. </p>
            filters: <p> A <code>SearchOrganizationInsightsFilters</code> object that is used to set the severity and status filters on your insight search. </p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>
            type: <p> The type of insights you are searching for (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.search_organization_insights_request.SearchOrganizationInsightsRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.search_organization_insights_response.SearchOrganizationInsightsResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.search_organization_insights

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.search_organization_insights.search_organization_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.search_organization_insights_request.SearchOrganizationInsightsRequest = {}  # type: ignore[typeddict-item]
        input["account_ids"] = account_ids
        input["start_time_range"] = start_time_range
        if filters is not None:
            input["filters"] = filters
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_cost_estimation(
        self,
        resource_collection: "aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter.CostEstimationResourceCollectionFilter",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        client_token: Optional[
            "aws_sdk_devops_guru.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.start_cost_estimation_response.StartCostEstimationResponse":
        """<p>Starts the creation of an estimate of the monthly cost to analyze your Amazon Web Services resources.</p>

        Args:
            resource_collection: <p>The collection of Amazon Web Services resources used to create a monthly DevOps Guru cost estimate.</p>
            client_token: <p>The idempotency token used to identify each cost estimate request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.start_cost_estimation_request.StartCostEstimationRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.start_cost_estimation_response.StartCostEstimationResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.start_cost_estimation

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.start_cost_estimation.start_cost_estimation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.start_cost_estimation_request.StartCostEstimationRequest = {}  # type: ignore[typeddict-item]
        input["resource_collection"] = resource_collection
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_event_sources_config(
        self,
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
        event_sources: Optional[
            "aws_sdk_devops_guru.types.event_sources_config.EventSourcesConfig"
        ] = None,
    ) -> "aws_sdk_devops_guru.types.update_event_sources_config_response.UpdateEventSourcesConfigResponse":
        """<p>Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon CodeGuru Profiler, which can produce proactive recommendations which can be stored and viewed in DevOps Guru.</p>

        Args:
            event_sources: <p>Configuration information about the integration of DevOps Guru as the Consumer via EventBridge with another AWS Service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.update_event_sources_config_request.UpdateEventSourcesConfigRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.update_event_sources_config_response.UpdateEventSourcesConfigResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.update_event_sources_config

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.update_event_sources_config.update_event_sources_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.update_event_sources_config_request.UpdateEventSourcesConfigRequest = {}  # type: ignore[typeddict-item]
        if event_sources is not None:
            input["event_sources"] = event_sources

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_resource_collection(
        self,
        action: "aws_sdk_devops_guru.types.update_resource_collection_action.UpdateResourceCollectionAction",
        resource_collection: "aws_sdk_devops_guru.types.update_resource_collection_filter.UpdateResourceCollectionFilter",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
    ) -> "aws_sdk_devops_guru.types.update_resource_collection_response.UpdateResourceCollectionResponse":
        """<p> Updates the collection of resources that DevOps Guru analyzes. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. This method also creates the IAM role required for you to use DevOps Guru. </p>

        Args:
            action: <p> Specifies if the resource collection in the request is added or deleted to the resource collection. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.update_resource_collection_request.UpdateResourceCollectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.update_resource_collection_response.UpdateResourceCollectionResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.update_resource_collection

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.update_resource_collection.update_resource_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.update_resource_collection_request.UpdateResourceCollectionRequest = {}  # type: ignore[typeddict-item]
        input["action"] = action
        input["resource_collection"] = resource_collection

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_service_integration(
        self,
        service_integration: "aws_sdk_devops_guru.types.update_service_integration_config.UpdateServiceIntegrationConfig",
        *,
        config_overrides: Optional[DevOpsGuruClientConfig] = None,
    ) -> "aws_sdk_devops_guru.types.update_service_integration_response.UpdateServiceIntegrationResponse":
        """<p> Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight. </p>

        Args:
            service_integration: <p> An <code>IntegratedServiceConfig</code> object used to specify the integrated service you want to update, and whether you want to update it to enabled or disabled. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_devops_guru.types.update_service_integration_request.UpdateServiceIntegrationRequest]",
        ) -> OperationResponse[
            "aws_sdk_devops_guru.types.update_service_integration_response.UpdateServiceIntegrationResponse"
        ]:
            import aws_sdk_devops_guru._operations.capstone_control_plane_service.update_service_integration

            output, http_response = (
                aws_sdk_devops_guru._operations.capstone_control_plane_service.update_service_integration.update_service_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_devops_guru.types.update_service_integration_request.UpdateServiceIntegrationRequest = {}  # type: ignore[typeddict-item]
        input["service_integration"] = service_integration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
