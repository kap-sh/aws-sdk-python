"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#AWSBCMDashboardsService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_bcm_dashboards._auth._signers
import aws_sdk_bcm_dashboards._auth._sigv4
from aws_sdk_bcm_dashboards._auth._identity import Credentials
from aws_sdk_bcm_dashboards._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bcm_dashboards._auth._zapros_handler import AuthMiddleware
from aws_sdk_bcm_dashboards._pagination import resolve_path as _resolve_path
from aws_sdk_bcm_dashboards._services._aws_config import aws_config
from aws_sdk_bcm_dashboards._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.client_token
    import aws_sdk_bcm_dashboards.types.create_dashboard_request
    import aws_sdk_bcm_dashboards.types.create_dashboard_response
    import aws_sdk_bcm_dashboards.types.create_scheduled_report_request
    import aws_sdk_bcm_dashboards.types.create_scheduled_report_response
    import aws_sdk_bcm_dashboards.types.dashboard_arn
    import aws_sdk_bcm_dashboards.types.dashboard_name
    import aws_sdk_bcm_dashboards.types.dashboard_reference
    import aws_sdk_bcm_dashboards.types.date_time_range
    import aws_sdk_bcm_dashboards.types.delete_dashboard_request
    import aws_sdk_bcm_dashboards.types.delete_dashboard_response
    import aws_sdk_bcm_dashboards.types.delete_scheduled_report_request
    import aws_sdk_bcm_dashboards.types.delete_scheduled_report_response
    import aws_sdk_bcm_dashboards.types.description
    import aws_sdk_bcm_dashboards.types.execute_scheduled_report_request
    import aws_sdk_bcm_dashboards.types.execute_scheduled_report_response
    import aws_sdk_bcm_dashboards.types.get_dashboard_request
    import aws_sdk_bcm_dashboards.types.get_dashboard_response
    import aws_sdk_bcm_dashboards.types.get_resource_policy_request
    import aws_sdk_bcm_dashboards.types.get_resource_policy_response
    import aws_sdk_bcm_dashboards.types.get_scheduled_report_request
    import aws_sdk_bcm_dashboards.types.get_scheduled_report_response
    import aws_sdk_bcm_dashboards.types.list_dashboards_request
    import aws_sdk_bcm_dashboards.types.list_dashboards_response
    import aws_sdk_bcm_dashboards.types.list_scheduled_reports_request
    import aws_sdk_bcm_dashboards.types.list_scheduled_reports_response
    import aws_sdk_bcm_dashboards.types.list_tags_for_resource_request
    import aws_sdk_bcm_dashboards.types.list_tags_for_resource_response
    import aws_sdk_bcm_dashboards.types.max_results
    import aws_sdk_bcm_dashboards.types.next_page_token
    import aws_sdk_bcm_dashboards.types.resource_arn
    import aws_sdk_bcm_dashboards.types.resource_tag_key_list
    import aws_sdk_bcm_dashboards.types.resource_tag_list
    import aws_sdk_bcm_dashboards.types.schedule_config
    import aws_sdk_bcm_dashboards.types.scheduled_report_arn
    import aws_sdk_bcm_dashboards.types.scheduled_report_input
    import aws_sdk_bcm_dashboards.types.scheduled_report_name
    import aws_sdk_bcm_dashboards.types.scheduled_report_summary
    import aws_sdk_bcm_dashboards.types.service_role_arn
    import aws_sdk_bcm_dashboards.types.tag_resource_request
    import aws_sdk_bcm_dashboards.types.tag_resource_response
    import aws_sdk_bcm_dashboards.types.untag_resource_request
    import aws_sdk_bcm_dashboards.types.untag_resource_response
    import aws_sdk_bcm_dashboards.types.update_dashboard_request
    import aws_sdk_bcm_dashboards.types.update_dashboard_response
    import aws_sdk_bcm_dashboards.types.update_scheduled_report_request
    import aws_sdk_bcm_dashboards.types.update_scheduled_report_response
    import aws_sdk_bcm_dashboards.types.widget_id_list
    import aws_sdk_bcm_dashboards.types.widget_list


class BCMDashboardsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: CredentialsProvider | None


class BCMDashboardsClient:
    """A client for the ``BCMDashboards`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = BCMDashboardsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[BCMDashboardsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BCMDashboardsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_dashboard(
        self,
        name: "aws_sdk_bcm_dashboards.types.dashboard_name.DashboardName",
        widgets: "aws_sdk_bcm_dashboards.types.widget_list.WidgetList",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        description: Optional[
            "aws_sdk_bcm_dashboards.types.description.Description"
        ] = None,
        resource_tags: Optional[
            "aws_sdk_bcm_dashboards.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> (
        "aws_sdk_bcm_dashboards.types.create_dashboard_response.CreateDashboardResponse"
    ):
        """<p>Creates a new dashboard that can contain multiple widgets displaying cost and usage data. You can add custom widgets or use predefined widgets, arranging them in your preferred layout.</p>

        Args:
            name: <p>The name of the dashboard. The name must be unique within your account.</p>
            description: <p>A description of the dashboard's purpose or contents.</p>
            widgets: <p>An array of widget configurations that define the visualizations to be displayed in the dashboard. Each dashboard can contain up to 20 widgets.</p>
            resource_tags: <p>The tags to apply to the dashboard resource for organization and management.</p>

        Examples:
            Creating a dashboard

            >>> client.create_dashboard(name='cost-dashboards', description='Dashboard for tracking costs', widgets=[{'title': 'Monthly Cost Trend', 'width': 4, 'height': 7, 'horizontalOffset': 0, 'configs': [{'displayConfig': {'graph': {'costTrend': {'visualType': 'LINE'}}}, 'queryParameters': {'costAndUsage': {'granularity': 'MONTHLY', 'groupBy': [{'key': 'SERVICE', 'type': 'DIMENSION'}], 'metrics': ['UnblendedCost'], 'timeRange': {'endTime': {'type': 'RELATIVE', 'value': 'now'}, 'startTime': {'type': 'RELATIVE', 'value': '-9M'}}}}}]}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.create_dashboard_request.CreateDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.create_dashboard_response.CreateDashboardResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.create_dashboard

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.create_dashboard.create_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.create_dashboard_request.CreateDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        input_["widgets"] = widgets
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_scheduled_report(
        self,
        scheduled_report: "aws_sdk_bcm_dashboards.types.scheduled_report_input.ScheduledReportInput",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        resource_tags: Optional[
            "aws_sdk_bcm_dashboards.types.resource_tag_list.ResourceTagList"
        ] = None,
        client_token: Optional[
            "aws_sdk_bcm_dashboards.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse":
        """<p>Creates a new scheduled report for a dashboard. A scheduled report automatically generates and delivers dashboard snapshots on a recurring schedule. Reports are delivered within 15 minutes of the scheduled delivery time.</p>

        Args:
            scheduled_report: <p>The configuration for the scheduled report, including the dashboard to report on, the schedule, and the execution role that the service will use to generate the dashboard snapshot.</p>
            resource_tags: <p>The tags to apply to the scheduled report resource for organization and management.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.create_scheduled_report_request.CreateScheduledReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.create_scheduled_report_response.CreateScheduledReportResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.create_scheduled_report

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.create_scheduled_report.create_scheduled_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.create_scheduled_report_request.CreateScheduledReportRequest = {}  # type: ignore[typeddict-item]
        input_["scheduled_report"] = scheduled_report
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_dashboard(
        self,
        arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> (
        "aws_sdk_bcm_dashboards.types.delete_dashboard_response.DeleteDashboardResponse"
    ):
        """<p>Deletes a specified dashboard. This action cannot be undone.</p>

        Args:
            arn: <p>The ARN of the dashboard to be deleted.</p>

        Examples:
            Deleting a dashboard

            >>> client.delete_dashboard(arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.delete_dashboard_request.DeleteDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.delete_dashboard_response.DeleteDashboardResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.delete_dashboard

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.delete_dashboard.delete_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.delete_dashboard_request.DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_scheduled_report(
        self,
        arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.delete_scheduled_report_response.DeleteScheduledReportResponse":
        """<p>Deletes a specified scheduled report. This is an irreversible operation.</p>

        Args:
            arn: <p>The ARN of the scheduled report to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.delete_scheduled_report_request.DeleteScheduledReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.delete_scheduled_report_response.DeleteScheduledReportResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.delete_scheduled_report

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.delete_scheduled_report.delete_scheduled_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.delete_scheduled_report_request.DeleteScheduledReportRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def execute_scheduled_report(
        self,
        arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bcm_dashboards.types.client_token.ClientToken"
        ] = None,
        dry_run: Optional[bool] = None,
    ) -> "aws_sdk_bcm_dashboards.types.execute_scheduled_report_response.ExecuteScheduledReportResponse":
        """<p>Triggers an immediate execution of a scheduled report, outside of its regular schedule. The scheduled report must be in <code>ENABLED</code> state. Calling this operation on a <code>DISABLED</code> scheduled report returns a <code>ValidationException</code>.</p> <note> <p>If a <code>clientToken</code> is provided, the service uses it for idempotency. Requests with the same client token will not trigger a new execution within the same minute.</p> </note>

        Args:
            arn: <p>The ARN of the scheduled report to execute.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            dry_run: <p>When set to <code>true</code>, validates the scheduled report configuration without triggering an actual execution.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.execute_scheduled_report_request.ExecuteScheduledReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.execute_scheduled_report_response.ExecuteScheduledReportResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.execute_scheduled_report

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.execute_scheduled_report.execute_scheduled_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.execute_scheduled_report_request.ExecuteScheduledReportRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if client_token is not None:
            input_["client_token"] = client_token
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_dashboard(
        self,
        arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.get_dashboard_response.GetDashboardResponse":
        """<p>Retrieves the configuration and metadata of a specified dashboard, including its widgets and layout settings.</p>

        Args:
            arn: <p>The ARN of the dashboard to retrieve. This is required to uniquely identify the dashboard.</p>

        Examples:
            Getting information about a dashboard

            >>> client.get_dashboard(arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.get_dashboard_request.GetDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.get_dashboard_response.GetDashboardResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.get_dashboard

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.get_dashboard.get_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.get_dashboard_request.GetDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy attached to a dashboard, showing sharing configurations and permissions.</p>

        Args:
            resource_arn: <p>The ARN of the dashboard whose resource-based policy you want to retrieve.</p>

        Examples:
            Getting resource policy for a resource

            >>> client.get_resource_policy(resource_arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.get_resource_policy

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_scheduled_report(
        self,
        arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.get_scheduled_report_response.GetScheduledReportResponse":
        """<p>Retrieves the configuration and metadata of a specified scheduled report.</p>

        Args:
            arn: <p>The ARN of the scheduled report to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.get_scheduled_report_request.GetScheduledReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.get_scheduled_report_response.GetScheduledReportResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.get_scheduled_report

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.get_scheduled_report.get_scheduled_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.get_scheduled_report_request.GetScheduledReportRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_dashboards(
        self,
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bcm_dashboards.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "aws_sdk_bcm_dashboards.types.list_dashboards_response.ListDashboardsResponse":
        """<p>Returns a list of all dashboards in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>

        Examples:
            Listing dashboards for a user

            >>> client.list_dashboards()
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.list_dashboards_request.ListDashboardsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.list_dashboards_response.ListDashboardsResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.list_dashboards

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.list_dashboards.list_dashboards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.list_dashboards_request.ListDashboardsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_dashboards(
        self,
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bcm_dashboards.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
        ] = None,
    ) -> (
        "Iterator[aws_sdk_bcm_dashboards.types.dashboard_reference.DashboardReference]"
    ):
        _token = next_token
        while True:
            _response = self.list_dashboards(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dashboards",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scheduled_reports(
        self,
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_bcm_dashboards.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bcm_dashboards.types.list_scheduled_reports_response.ListScheduledReportsResponse":
        """<p>Returns a list of scheduled reports in your account.</p>

        Args:
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range is 1 to 100. The default value is 50.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.list_scheduled_reports_request.ListScheduledReportsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.list_scheduled_reports_response.ListScheduledReportsResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.list_scheduled_reports

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.list_scheduled_reports.list_scheduled_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.list_scheduled_reports_request.ListScheduledReportsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_scheduled_reports(
        self,
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bcm_dashboards.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_bcm_dashboards.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[aws_sdk_bcm_dashboards.types.scheduled_report_summary.ScheduledReportSummary]":
        _token = next_token
        while True:
            _response = self.list_scheduled_reports(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("scheduled_reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bcm_dashboards.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of all tags associated with a specified dashboard resource.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>

        Examples:
            Listing tags for a resource

            >>> client.list_tags_for_resource(resource_arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_bcm_dashboards.types.resource_arn.ResourceArn",
        resource_tags: "aws_sdk_bcm_dashboards.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a specified dashboard resource.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tags: <p>The tags to add to the dashboard resource.</p>

        Examples:
            Adding tag(s) to a resource

            >>> client.tag_resource(resource_arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh', resource_tags=[{'key': 'keyOne', 'value': 'valueOne'}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.tag_resource

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_bcm_dashboards.types.resource_arn.ResourceArn",
        resource_tag_keys: "aws_sdk_bcm_dashboards.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
    ) -> "aws_sdk_bcm_dashboards.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes specified tags from a dashboard resource.</p>

        Args:
            resource_arn: <p>The unique identifier for the resource.</p>
            resource_tag_keys: <p>The keys of the tags to remove from the dashboard resource.</p>

        Examples:
            Removing tag(s) from a resource

            >>> client.untag_resource(resource_arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh', resource_tag_keys=['keyOne'])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.untag_resource

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_tag_keys"] = resource_tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_dashboard(
        self,
        arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn",
        name: "aws_sdk_bcm_dashboards.types.dashboard_name.DashboardName",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        description: Optional[
            "aws_sdk_bcm_dashboards.types.description.Description"
        ] = None,
        widgets: Optional["aws_sdk_bcm_dashboards.types.widget_list.WidgetList"] = None,
    ) -> (
        "aws_sdk_bcm_dashboards.types.update_dashboard_response.UpdateDashboardResponse"
    ):
        """<p>Updates an existing dashboard's properties, including its name, description, and widget configurations.</p>

        Args:
            arn: <p>The ARN of the dashboard to update.</p>
            name: <p>The new name for the dashboard.</p>
            description: <p>The new description for the dashboard.</p>
            widgets: <p>The updated array of widget configurations for the dashboard. Replaces all existing widgets.</p>

        Examples:
            Updating a dashboard

            >>> client.update_dashboard(arn='arn:aws:bcm-dashboards::123456789012:dashboard/abcd1234-ab12-12ab-1ab2-abcd1234efgh', name='cost-dashboards-updated', description='Dashboard for tracking costs version 2', widgets=[{'title': 'Monthly Cost Trend', 'width': 4, 'height': 7, 'horizontalOffset': 2, 'configs': [{'displayConfig': {'graph': {'costTrend': {'visualType': 'LINE'}}}, 'queryParameters': {'costAndUsage': {'granularity': 'MONTHLY', 'groupBy': [{'key': 'SERVICE', 'type': 'DIMENSION'}], 'metrics': ['UnblendedCost'], 'timeRange': {'endTime': {'type': 'RELATIVE', 'value': 'now'}, 'startTime': {'type': 'RELATIVE', 'value': '-3M'}}}}}]}])
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.update_dashboard_request.UpdateDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.update_dashboard_response.UpdateDashboardResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.update_dashboard

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.update_dashboard.update_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.update_dashboard_request.UpdateDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if widgets is not None:
            input_["widgets"] = widgets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_scheduled_report(
        self,
        arn: "aws_sdk_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn",
        *,
        config_overrides: Optional[BCMDashboardsClientConfig] = None,
        name: Optional[
            "aws_sdk_bcm_dashboards.types.scheduled_report_name.ScheduledReportName"
        ] = None,
        description: Optional[
            "aws_sdk_bcm_dashboards.types.description.Description"
        ] = None,
        dashboard_arn: Optional[
            "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn"
        ] = None,
        scheduled_report_execution_role_arn: Optional[
            "aws_sdk_bcm_dashboards.types.service_role_arn.ServiceRoleArn"
        ] = None,
        schedule_config: Optional[
            "aws_sdk_bcm_dashboards.types.schedule_config.ScheduleConfig"
        ] = None,
        widget_ids: Optional[
            "aws_sdk_bcm_dashboards.types.widget_id_list.WidgetIdList"
        ] = None,
        widget_date_range_override: Optional[
            "aws_sdk_bcm_dashboards.types.date_time_range.DateTimeRange"
        ] = None,
        clear_widget_ids: Optional[bool] = None,
        clear_widget_date_range_override: Optional[bool] = None,
    ) -> "aws_sdk_bcm_dashboards.types.update_scheduled_report_response.UpdateScheduledReportResponse":
        """<p>Updates an existing scheduled report's properties, including its name, description, schedule configuration, and widget settings. Only the parameters included in the request are updated; all other properties remain unchanged.</p>

        Args:
            arn: <p>The ARN of the scheduled report to update.</p>
            name: <p>The new name for the scheduled report.</p>
            description: <p>The new description for the scheduled report.</p>
            dashboard_arn: <p>The ARN of the dashboard to associate with the scheduled report.</p>
            scheduled_report_execution_role_arn: <p>The ARN of the IAM role that the scheduled report uses to execute. Amazon Web Services Billing and Cost Management Dashboards will assume this IAM role while executing the scheduled report.</p>
            schedule_config: <p>The updated schedule configuration for the report.</p>
            widget_ids: <p>The list of widget identifiers to include in the scheduled report. If not specified, all widgets in the dashboard are included.</p>
            widget_date_range_override: <p>The date range override to apply to widgets in the scheduled report.</p>
            clear_widget_ids: Set to true to clear existing widgetIds.
            clear_widget_date_range_override: Set to true to clear existing widgetDateRangeOverride.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bcm_dashboards.types.update_scheduled_report_request.UpdateScheduledReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_bcm_dashboards.types.update_scheduled_report_response.UpdateScheduledReportResponse"
        ]:
            import aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.update_scheduled_report

            output, http_response = (
                aws_sdk_bcm_dashboards._operations.awsbcm_dashboards_service.update_scheduled_report.update_scheduled_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bcm_dashboards.types.update_scheduled_report_request.UpdateScheduledReportRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if dashboard_arn is not None:
            input_["dashboard_arn"] = dashboard_arn
        if scheduled_report_execution_role_arn is not None:
            input_["scheduled_report_execution_role_arn"] = (
                scheduled_report_execution_role_arn
            )
        if schedule_config is not None:
            input_["schedule_config"] = schedule_config
        if widget_ids is not None:
            input_["widget_ids"] = widget_ids
        if widget_date_range_override is not None:
            input_["widget_date_range_override"] = widget_date_range_override
        if clear_widget_ids is not None:
            input_["clear_widget_ids"] = clear_widget_ids
        if clear_widget_date_range_override is not None:
            input_["clear_widget_date_range_override"] = (
                clear_widget_date_range_override
            )

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
