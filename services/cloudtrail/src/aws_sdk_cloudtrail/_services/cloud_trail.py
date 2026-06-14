"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CloudTrail_20131101``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_cloudtrail._auth._signers
import aws_sdk_cloudtrail._auth._sigv4
from aws_sdk_cloudtrail._auth._identity import Credentials
from aws_sdk_cloudtrail._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_cloudtrail._auth._zapros_handler import AuthMiddleware
from aws_sdk_cloudtrail._pagination import resolve_path as _resolve_path
from aws_sdk_cloudtrail._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.account_id
    import aws_sdk_cloudtrail.types.add_tags_request
    import aws_sdk_cloudtrail.types.add_tags_response
    import aws_sdk_cloudtrail.types.advanced_event_selectors
    import aws_sdk_cloudtrail.types.aggregation_configurations
    import aws_sdk_cloudtrail.types.billing_mode
    import aws_sdk_cloudtrail.types.boolean
    import aws_sdk_cloudtrail.types.cancel_query_request
    import aws_sdk_cloudtrail.types.cancel_query_response
    import aws_sdk_cloudtrail.types.channel_arn
    import aws_sdk_cloudtrail.types.channel_name
    import aws_sdk_cloudtrail.types.context_key_selectors
    import aws_sdk_cloudtrail.types.create_channel_request
    import aws_sdk_cloudtrail.types.create_channel_response
    import aws_sdk_cloudtrail.types.create_dashboard_request
    import aws_sdk_cloudtrail.types.create_dashboard_response
    import aws_sdk_cloudtrail.types.create_event_data_store_request
    import aws_sdk_cloudtrail.types.create_event_data_store_response
    import aws_sdk_cloudtrail.types.create_trail_request
    import aws_sdk_cloudtrail.types.create_trail_response
    import aws_sdk_cloudtrail.types.dashboard_arn
    import aws_sdk_cloudtrail.types.dashboard_name
    import aws_sdk_cloudtrail.types.dashboard_type
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.delete_channel_request
    import aws_sdk_cloudtrail.types.delete_channel_response
    import aws_sdk_cloudtrail.types.delete_dashboard_request
    import aws_sdk_cloudtrail.types.delete_dashboard_response
    import aws_sdk_cloudtrail.types.delete_event_data_store_request
    import aws_sdk_cloudtrail.types.delete_event_data_store_response
    import aws_sdk_cloudtrail.types.delete_resource_policy_request
    import aws_sdk_cloudtrail.types.delete_resource_policy_response
    import aws_sdk_cloudtrail.types.delete_trail_request
    import aws_sdk_cloudtrail.types.delete_trail_response
    import aws_sdk_cloudtrail.types.delivery_s3_uri
    import aws_sdk_cloudtrail.types.deregister_organization_delegated_admin_request
    import aws_sdk_cloudtrail.types.deregister_organization_delegated_admin_response
    import aws_sdk_cloudtrail.types.describe_query_request
    import aws_sdk_cloudtrail.types.describe_query_response
    import aws_sdk_cloudtrail.types.describe_trails_request
    import aws_sdk_cloudtrail.types.describe_trails_response
    import aws_sdk_cloudtrail.types.destinations
    import aws_sdk_cloudtrail.types.disable_federation_request
    import aws_sdk_cloudtrail.types.disable_federation_response
    import aws_sdk_cloudtrail.types.enable_federation_request
    import aws_sdk_cloudtrail.types.enable_federation_response
    import aws_sdk_cloudtrail.types.error_code
    import aws_sdk_cloudtrail.types.event
    import aws_sdk_cloudtrail.types.event_category
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.event_data_store_kms_key_id
    import aws_sdk_cloudtrail.types.event_data_store_list
    import aws_sdk_cloudtrail.types.event_data_store_name
    import aws_sdk_cloudtrail.types.event_name
    import aws_sdk_cloudtrail.types.event_selectors
    import aws_sdk_cloudtrail.types.event_source
    import aws_sdk_cloudtrail.types.federation_role_arn
    import aws_sdk_cloudtrail.types.generate_query_request
    import aws_sdk_cloudtrail.types.generate_query_response
    import aws_sdk_cloudtrail.types.get_channel_request
    import aws_sdk_cloudtrail.types.get_channel_response
    import aws_sdk_cloudtrail.types.get_dashboard_request
    import aws_sdk_cloudtrail.types.get_dashboard_response
    import aws_sdk_cloudtrail.types.get_event_configuration_request
    import aws_sdk_cloudtrail.types.get_event_configuration_response
    import aws_sdk_cloudtrail.types.get_event_data_store_request
    import aws_sdk_cloudtrail.types.get_event_data_store_response
    import aws_sdk_cloudtrail.types.get_event_selectors_request
    import aws_sdk_cloudtrail.types.get_event_selectors_response
    import aws_sdk_cloudtrail.types.get_import_request
    import aws_sdk_cloudtrail.types.get_import_response
    import aws_sdk_cloudtrail.types.get_insight_selectors_request
    import aws_sdk_cloudtrail.types.get_insight_selectors_response
    import aws_sdk_cloudtrail.types.get_query_results_request
    import aws_sdk_cloudtrail.types.get_query_results_response
    import aws_sdk_cloudtrail.types.get_resource_policy_request
    import aws_sdk_cloudtrail.types.get_resource_policy_response
    import aws_sdk_cloudtrail.types.get_trail_request
    import aws_sdk_cloudtrail.types.get_trail_response
    import aws_sdk_cloudtrail.types.get_trail_status_request
    import aws_sdk_cloudtrail.types.get_trail_status_response
    import aws_sdk_cloudtrail.types.import_destinations
    import aws_sdk_cloudtrail.types.import_failure_list_item
    import aws_sdk_cloudtrail.types.import_source
    import aws_sdk_cloudtrail.types.import_status
    import aws_sdk_cloudtrail.types.imports_list_item
    import aws_sdk_cloudtrail.types.insight_selectors
    import aws_sdk_cloudtrail.types.insight_type
    import aws_sdk_cloudtrail.types.insights_metric_data_type
    import aws_sdk_cloudtrail.types.insights_metric_max_results
    import aws_sdk_cloudtrail.types.insights_metric_next_token
    import aws_sdk_cloudtrail.types.insights_metric_period
    import aws_sdk_cloudtrail.types.list_channels_max_results_count
    import aws_sdk_cloudtrail.types.list_channels_request
    import aws_sdk_cloudtrail.types.list_channels_response
    import aws_sdk_cloudtrail.types.list_dashboards_max_results_count
    import aws_sdk_cloudtrail.types.list_dashboards_request
    import aws_sdk_cloudtrail.types.list_dashboards_response
    import aws_sdk_cloudtrail.types.list_event_data_stores_max_results_count
    import aws_sdk_cloudtrail.types.list_event_data_stores_request
    import aws_sdk_cloudtrail.types.list_event_data_stores_response
    import aws_sdk_cloudtrail.types.list_import_failures_max_results_count
    import aws_sdk_cloudtrail.types.list_import_failures_request
    import aws_sdk_cloudtrail.types.list_import_failures_response
    import aws_sdk_cloudtrail.types.list_imports_max_results_count
    import aws_sdk_cloudtrail.types.list_imports_request
    import aws_sdk_cloudtrail.types.list_imports_response
    import aws_sdk_cloudtrail.types.list_insights_data_dimensions
    import aws_sdk_cloudtrail.types.list_insights_data_max_results_count
    import aws_sdk_cloudtrail.types.list_insights_data_request
    import aws_sdk_cloudtrail.types.list_insights_data_response
    import aws_sdk_cloudtrail.types.list_insights_data_type
    import aws_sdk_cloudtrail.types.list_insights_metric_data_request
    import aws_sdk_cloudtrail.types.list_insights_metric_data_response
    import aws_sdk_cloudtrail.types.list_public_keys_request
    import aws_sdk_cloudtrail.types.list_public_keys_response
    import aws_sdk_cloudtrail.types.list_queries_max_results_count
    import aws_sdk_cloudtrail.types.list_queries_request
    import aws_sdk_cloudtrail.types.list_queries_response
    import aws_sdk_cloudtrail.types.list_tags_request
    import aws_sdk_cloudtrail.types.list_tags_response
    import aws_sdk_cloudtrail.types.list_trails_request
    import aws_sdk_cloudtrail.types.list_trails_response
    import aws_sdk_cloudtrail.types.lookup_attributes_list
    import aws_sdk_cloudtrail.types.lookup_events_request
    import aws_sdk_cloudtrail.types.lookup_events_response
    import aws_sdk_cloudtrail.types.max_event_size
    import aws_sdk_cloudtrail.types.max_query_results
    import aws_sdk_cloudtrail.types.max_results
    import aws_sdk_cloudtrail.types.next_token
    import aws_sdk_cloudtrail.types.pagination_token
    import aws_sdk_cloudtrail.types.prompt
    import aws_sdk_cloudtrail.types.public_key
    import aws_sdk_cloudtrail.types.put_event_configuration_request
    import aws_sdk_cloudtrail.types.put_event_configuration_response
    import aws_sdk_cloudtrail.types.put_event_selectors_request
    import aws_sdk_cloudtrail.types.put_event_selectors_response
    import aws_sdk_cloudtrail.types.put_insight_selectors_request
    import aws_sdk_cloudtrail.types.put_insight_selectors_response
    import aws_sdk_cloudtrail.types.put_resource_policy_request
    import aws_sdk_cloudtrail.types.put_resource_policy_response
    import aws_sdk_cloudtrail.types.query_alias
    import aws_sdk_cloudtrail.types.query_parameter_values
    import aws_sdk_cloudtrail.types.query_parameters
    import aws_sdk_cloudtrail.types.query_statement
    import aws_sdk_cloudtrail.types.query_status
    import aws_sdk_cloudtrail.types.refresh_id
    import aws_sdk_cloudtrail.types.refresh_schedule
    import aws_sdk_cloudtrail.types.register_organization_delegated_admin_request
    import aws_sdk_cloudtrail.types.register_organization_delegated_admin_response
    import aws_sdk_cloudtrail.types.remove_tags_request
    import aws_sdk_cloudtrail.types.remove_tags_response
    import aws_sdk_cloudtrail.types.request_widget_list
    import aws_sdk_cloudtrail.types.resource_arn
    import aws_sdk_cloudtrail.types.resource_id_list
    import aws_sdk_cloudtrail.types.resource_policy
    import aws_sdk_cloudtrail.types.resource_tag
    import aws_sdk_cloudtrail.types.restore_event_data_store_request
    import aws_sdk_cloudtrail.types.restore_event_data_store_response
    import aws_sdk_cloudtrail.types.retention_period
    import aws_sdk_cloudtrail.types.search_sample_queries_max_results
    import aws_sdk_cloudtrail.types.search_sample_queries_request
    import aws_sdk_cloudtrail.types.search_sample_queries_response
    import aws_sdk_cloudtrail.types.search_sample_queries_search_phrase
    import aws_sdk_cloudtrail.types.source
    import aws_sdk_cloudtrail.types.start_dashboard_refresh_request
    import aws_sdk_cloudtrail.types.start_dashboard_refresh_response
    import aws_sdk_cloudtrail.types.start_event_data_store_ingestion_request
    import aws_sdk_cloudtrail.types.start_event_data_store_ingestion_response
    import aws_sdk_cloudtrail.types.start_import_request
    import aws_sdk_cloudtrail.types.start_import_response
    import aws_sdk_cloudtrail.types.start_logging_request
    import aws_sdk_cloudtrail.types.start_logging_response
    import aws_sdk_cloudtrail.types.start_query_request
    import aws_sdk_cloudtrail.types.start_query_response
    import aws_sdk_cloudtrail.types.stop_event_data_store_ingestion_request
    import aws_sdk_cloudtrail.types.stop_event_data_store_ingestion_response
    import aws_sdk_cloudtrail.types.stop_import_request
    import aws_sdk_cloudtrail.types.stop_import_response
    import aws_sdk_cloudtrail.types.stop_logging_request
    import aws_sdk_cloudtrail.types.stop_logging_response
    import aws_sdk_cloudtrail.types.string
    import aws_sdk_cloudtrail.types.tags_list
    import aws_sdk_cloudtrail.types.termination_protection_enabled
    import aws_sdk_cloudtrail.types.trail_info
    import aws_sdk_cloudtrail.types.trail_name_list
    import aws_sdk_cloudtrail.types.update_channel_request
    import aws_sdk_cloudtrail.types.update_channel_response
    import aws_sdk_cloudtrail.types.update_dashboard_request
    import aws_sdk_cloudtrail.types.update_dashboard_response
    import aws_sdk_cloudtrail.types.update_event_data_store_request
    import aws_sdk_cloudtrail.types.update_event_data_store_response
    import aws_sdk_cloudtrail.types.update_trail_request
    import aws_sdk_cloudtrail.types.update_trail_response
    import aws_sdk_cloudtrail.types.uuid


class CloudTrailClientConfig(TypedDict, total=False):
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


class CloudTrailClient:
    """A client for the ``CloudTrail`` service.

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
        self._config = CloudTrailClientConfig(
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
        self, config_overrides: Optional[CloudTrailClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudTrailClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    def add_tags(
        self,
        resource_id: "aws_sdk_cloudtrail.types.string.String",
        tags_list: "aws_sdk_cloudtrail.types.tags_list.TagsList",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.add_tags_response.AddTagsResponse":
        """<p>Adds one or more tags to a trail, event data store, dashboard, or channel, up to a limit of 50. Overwrites an existing tag's value when a new value is specified for an existing tag key. Tag key names must be unique; you cannot have two keys with the same name but different values. If you specify a key without a value, the tag will be created with the specified key and a value of null. You can tag a trail or event data store that applies to all Amazon Web Services Regions only from the Region in which the trail or event data store was created (also known as its home Region).</p>

        Args:
            resource_id: <p>Specifies the ARN of the trail, event data store, dashboard, or channel to which one or more tags will be added.</p> <p>The format of a trail ARN is: <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>The format of an event data store ARN is: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>The format of a dashboard ARN is: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>The format of a channel ARN is: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>
            tags_list: <p>Contains a list of tags, up to a limit of 50</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.add_tags_request.AddTagsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.add_tags_response.AddTagsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.add_tags

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.add_tags.add_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.add_tags_request.AddTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        input_["tags_list"] = tags_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_query(
        self,
        query_id: "aws_sdk_cloudtrail.types.uuid.UUID",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        event_data_store: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
        event_data_store_owner_account_id: Optional[
            "aws_sdk_cloudtrail.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.cancel_query_response.CancelQueryResponse":
        """<p>Cancels a query if the query is not in a terminated state, such as <code>CANCELLED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>FINISHED</code>. You must specify an ARN value for <code>EventDataStore</code>. The ID of the query that you want to cancel is also required. When you run <code>CancelQuery</code>, the query status might show as <code>CANCELLED</code> even if the operation is not yet finished.</p>

        Args:
            event_data_store: <p>The ARN (or the ID suffix of the ARN) of an event data store on which the specified query is running.</p>
            query_id: <p>The ID of the query that you want to cancel. The <code>QueryId</code> comes from the response of a <code>StartQuery</code> operation.</p>
            event_data_store_owner_account_id: <p> The account ID of the event data store owner. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.cancel_query_request.CancelQueryRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.cancel_query_response.CancelQueryResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.cancel_query

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.cancel_query.cancel_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.cancel_query_request.CancelQueryRequest = {}  # type: ignore[typeddict-item]
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store
        input_["query_id"] = query_id
        if event_data_store_owner_account_id is not None:
            input_["event_data_store_owner_account_id"] = (
                event_data_store_owner_account_id
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel(
        self,
        name: "aws_sdk_cloudtrail.types.channel_name.ChannelName",
        source: "aws_sdk_cloudtrail.types.source.Source",
        destinations: "aws_sdk_cloudtrail.types.destinations.Destinations",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        tags: Optional["aws_sdk_cloudtrail.types.tags_list.TagsList"] = None,
    ) -> "aws_sdk_cloudtrail.types.create_channel_response.CreateChannelResponse":
        r"""<p>Creates a channel for CloudTrail to ingest events from a partner or external source. After you create a channel, a CloudTrail Lake event data store can log events from the partner or source that you specify.</p>

        Args:
            name: <p>The name of the channel.</p>
            source: <p>The name of the partner or external event source. You cannot change this name after you create the channel. A maximum of one channel is allowed per source.</p> <p> A source can be either <code>Custom</code> for all valid non-Amazon Web Services events, or the name of a partner event source. For information about the source names for available partners, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information\">Additional information about integration partners</a> in the CloudTrail User Guide. </p>
            destinations: <p>One or more event data stores to which events arriving through a channel will be logged.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.create_channel_response.CreateChannelResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_channel

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.create_channel_request.CreateChannelRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["source"] = source
        input_["destinations"] = destinations
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_dashboard(
        self,
        name: "aws_sdk_cloudtrail.types.dashboard_name.DashboardName",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        refresh_schedule: Optional[
            "aws_sdk_cloudtrail.types.refresh_schedule.RefreshSchedule"
        ] = None,
        tags_list: Optional["aws_sdk_cloudtrail.types.tags_list.TagsList"] = None,
        termination_protection_enabled: Optional[
            "aws_sdk_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
        ] = None,
        widgets: Optional[
            "aws_sdk_cloudtrail.types.request_widget_list.RequestWidgetList"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.create_dashboard_response.CreateDashboardResponse":
        r"""<p> Creates a custom dashboard or the Highlights dashboard. </p> <ul> <li> <p> <b>Custom dashboards</b> - Custom dashboards allow you to query events in any event data store type. You can add up to 10 widgets to a custom dashboard. You can manually refresh a custom dashboard, or you can set a refresh schedule.</p> </li> <li> <p> <b>Highlights dashboard</b> - You can create the Highlights dashboard to see a summary of key user activities and API usage across all your event data stores. CloudTrail Lake manages the Highlights dashboard and refreshes the dashboard every 6 hours. To create the Highlights dashboard, you must set and enable a refresh schedule.</p> </li> </ul> <p> CloudTrail runs queries to populate the dashboard's widgets during a manual or scheduled refresh. CloudTrail must be granted permissions to run the <code>StartQuery</code> operation on your behalf. To provide permissions, run the <code>PutResourcePolicy</code> operation to attach a resource-based policy to each event data store. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard\">Example: Allow CloudTrail to run queries to populate a dashboard</a> in the <i>CloudTrail User Guide</i>. </p> <p> To set a refresh schedule, CloudTrail must be granted permissions to run the <code>StartDashboardRefresh</code> operation to refresh the dashboard on your behalf. To provide permissions, run the <code>PutResourcePolicy</code> operation to attach a resource-based policy to the dashboard. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards\"> Resource-based policy example for a dashboard</a> in the <i>CloudTrail User Guide</i>. </p> <p>For more information about dashboards, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard.html\">CloudTrail Lake dashboards</a> in the <i>CloudTrail User Guide</i>.</p>

        Args:
            name: <p> The name of the dashboard. The name must be unique to your account. </p> <p>To create the Highlights dashboard, the name must be <code>AWSCloudTrail-Highlights</code>.</p>
            refresh_schedule: <p> The refresh schedule configuration for the dashboard. </p> <p>To create the Highlights dashboard, you must set a refresh schedule and set the <code>Status</code> to <code>ENABLED</code>. The <code>Unit</code> for the refresh schedule must be <code>HOURS</code> and the <code>Value</code> must be <code>6</code>.</p>
            termination_protection_enabled: <p> Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled. </p>
            widgets: <p> An array of widgets for a custom dashboard. A custom dashboard can have a maximum of ten widgets. </p> <p>You do not need to specify widgets for the Highlights dashboard.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.create_dashboard_request.CreateDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.create_dashboard_response.CreateDashboardResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_dashboard

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_dashboard.create_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.create_dashboard_request.CreateDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if refresh_schedule is not None:
            input_["refresh_schedule"] = refresh_schedule
        if tags_list is not None:
            input_["tags_list"] = tags_list
        if termination_protection_enabled is not None:
            input_["termination_protection_enabled"] = termination_protection_enabled
        if widgets is not None:
            input_["widgets"] = widgets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_event_data_store(
        self,
        name: "aws_sdk_cloudtrail.types.event_data_store_name.EventDataStoreName",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        advanced_event_selectors: Optional[
            "aws_sdk_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
        ] = None,
        multi_region_enabled: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        organization_enabled: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        retention_period: Optional[
            "aws_sdk_cloudtrail.types.retention_period.RetentionPeriod"
        ] = None,
        termination_protection_enabled: Optional[
            "aws_sdk_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
        ] = None,
        tags_list: Optional["aws_sdk_cloudtrail.types.tags_list.TagsList"] = None,
        kms_key_id: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_kms_key_id.EventDataStoreKmsKeyId"
        ] = None,
        start_ingestion: Optional["aws_sdk_cloudtrail.types.boolean.Boolean"] = None,
        billing_mode: Optional[
            "aws_sdk_cloudtrail.types.billing_mode.BillingMode"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.create_event_data_store_response.CreateEventDataStoreResponse":
        r"""<p>Creates a new event data store.</p>

        Args:
            name: <p>The name of the event data store.</p>
            advanced_event_selectors: <p>The advanced event selectors to use to select the events for the data store. You can configure up to five advanced event selectors for each event data store.</p> <p> For more information about how to use advanced event selectors to log CloudTrail events, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced\">Log events by using advanced event selectors</a> in the CloudTrail User Guide.</p> <p>For more information about how to use advanced event selectors to include Config configuration items in your event data store, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-eds-cli.html#lake-cli-create-eds-config\">Create an event data store for Config configuration items</a> in the CloudTrail User Guide.</p> <p>For more information about how to use advanced event selectors to include events outside of Amazon Web Services events in your event data store, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-integrations-cli.html#lake-cli-create-integration\">Create an integration to log events from outside Amazon Web Services</a> in the CloudTrail User Guide.</p>
            multi_region_enabled: <p>Specifies whether the event data store includes events from all Regions, or only from the Region in which the event data store is created.</p>
            organization_enabled: <p>Specifies whether an event data store collects events logged for an organization in Organizations.</p>
            retention_period: <p>The retention period of the event data store, in days. If <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code>, you can set a retention period of up to 3653 days, the equivalent of 10 years. If <code>BillingMode</code> is set to <code>FIXED_RETENTION_PRICING</code>, you can set a retention period of up to 2557 days, the equivalent of seven years.</p> <p>CloudTrail Lake determines whether to retain an event by checking if the <code>eventTime</code> of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the <code>eventTime</code> is older than 90 days.</p> <note> <p>If you plan to copy trail events to this event data store, we recommend that you consider both the age of the events that you want to copy as well as how long you want to keep the copied events in your event data store. For example, if you copy trail events that are 5 years old and specify a retention period of 7 years, the event data store will retain those events for two years.</p> </note>
            termination_protection_enabled: <p>Specifies whether termination protection is enabled for the event data store. If termination protection is enabled, you cannot delete the event data store until termination protection is disabled.</p>
            kms_key_id: <p>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by <code>alias/</code>, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <important> <p>Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.</p> </important> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html\">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p> <code>alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p> <code>12345678-1234-1234-1234-123456789012</code> </p> </li> </ul>
            start_ingestion: <p>Specifies whether the event data store should start ingesting live events. The default is true.</p>
            billing_mode: <p>The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.</p> <p>The following are the possible values:</p> <ul> <li> <p> <code>EXTENDABLE_RETENTION_PRICING</code> - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.</p> </li> <li> <p> <code>FIXED_RETENTION_PRICING</code> - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.</p> </li> </ul> <p>The default value is <code>EXTENDABLE_RETENTION_PRICING</code>.</p> <p>For more information about CloudTrail pricing, see <a href=\"http://aws.amazon.com/cloudtrail/pricing/\">CloudTrail Pricing</a> and <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html\">Managing CloudTrail Lake costs</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.create_event_data_store_request.CreateEventDataStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.create_event_data_store_response.CreateEventDataStoreResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_event_data_store

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_event_data_store.create_event_data_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.create_event_data_store_request.CreateEventDataStoreRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if advanced_event_selectors is not None:
            input_["advanced_event_selectors"] = advanced_event_selectors
        if multi_region_enabled is not None:
            input_["multi_region_enabled"] = multi_region_enabled
        if organization_enabled is not None:
            input_["organization_enabled"] = organization_enabled
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if termination_protection_enabled is not None:
            input_["termination_protection_enabled"] = termination_protection_enabled
        if tags_list is not None:
            input_["tags_list"] = tags_list
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if start_ingestion is not None:
            input_["start_ingestion"] = start_ingestion
        if billing_mode is not None:
            input_["billing_mode"] = billing_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_trail(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        s3_bucket_name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        s3_key_prefix: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        sns_topic_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        include_global_service_events: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        is_multi_region_trail: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        enable_log_file_validation: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        cloud_watch_logs_log_group_arn: Optional[
            "aws_sdk_cloudtrail.types.string.String"
        ] = None,
        cloud_watch_logs_role_arn: Optional[
            "aws_sdk_cloudtrail.types.string.String"
        ] = None,
        kms_key_id: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        is_organization_trail: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        tags_list: Optional["aws_sdk_cloudtrail.types.tags_list.TagsList"] = None,
    ) -> "aws_sdk_cloudtrail.types.create_trail_response.CreateTrailResponse":
        r"""<p>Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. </p>

        Args:
            name: <p>Specifies the name of the trail. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul>
            s3_bucket_name: <p>Specifies the name of the Amazon S3 bucket designated for publishing log files. For information about bucket naming rules, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html\">Bucket naming rules</a> in the <i>Amazon Simple Storage Service User Guide</i>. </p>
            s3_key_prefix: <p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files\">Finding Your CloudTrail Log Files</a>. The maximum length is 200 characters.</p>
            sns_topic_name: <p>Specifies the name or ARN of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.</p>
            include_global_service_events: <p>Specifies whether the trail is publishing events from global services such as IAM to the log files.</p>
            is_multi_region_trail: <p>Specifies whether the trail is created in the current Region or in all Regions. The default is false, which creates a trail only in the Region where you are signed in. As a best practice, consider creating trails that log events in all Regions.</p>
            enable_log_file_validation: <p>Specifies whether log file integrity validation is enabled. The default is false.</p> <note> <p>When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.</p> </note>
            cloud_watch_logs_log_group_arn: <p>Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. You must use a log group that exists in your account.</p> <p>Not required unless you specify <code>CloudWatchLogsRoleArn</code>.</p>
            cloud_watch_logs_role_arn: <p>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. You must use a role that exists in your account.</p>
            kms_key_id: <p>Specifies the KMS key ID to use to encrypt the logs and digest files delivered by CloudTrail. The value can be an alias name prefixed by <code>alias/</code>, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html\">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p> <code>alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p> <code>12345678-1234-1234-1234-123456789012</code> </p> </li> </ul>
            is_organization_trail: <p>Specifies whether the trail is created for all accounts in an organization in Organizations, or only for the current Amazon Web Services account. The default is false, and cannot be true unless the call is made on behalf of an Amazon Web Services account that is the management account or delegated administrator account for an organization in Organizations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.create_trail_request.CreateTrailRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.create_trail_response.CreateTrailResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_trail

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.create_trail.create_trail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.create_trail_request.CreateTrailRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["s3_bucket_name"] = s3_bucket_name
        if s3_key_prefix is not None:
            input_["s3_key_prefix"] = s3_key_prefix
        if sns_topic_name is not None:
            input_["sns_topic_name"] = sns_topic_name
        if include_global_service_events is not None:
            input_["include_global_service_events"] = include_global_service_events
        if is_multi_region_trail is not None:
            input_["is_multi_region_trail"] = is_multi_region_trail
        if enable_log_file_validation is not None:
            input_["enable_log_file_validation"] = enable_log_file_validation
        if cloud_watch_logs_log_group_arn is not None:
            input_["cloud_watch_logs_log_group_arn"] = cloud_watch_logs_log_group_arn
        if cloud_watch_logs_role_arn is not None:
            input_["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if is_organization_trail is not None:
            input_["is_organization_trail"] = is_organization_trail
        if tags_list is not None:
            input_["tags_list"] = tags_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel(
        self,
        channel: "aws_sdk_cloudtrail.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.delete_channel_response.DeleteChannelResponse":
        """<p>Deletes a channel.</p>

        Args:
            channel: <p>The ARN or the <code>UUID</code> value of the channel that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_channel

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.delete_channel_request.DeleteChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel"] = channel

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_dashboard(
        self,
        dashboard_id: "aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.delete_dashboard_response.DeleteDashboardResponse":
        """<p> Deletes the specified dashboard. You cannot delete a dashboard that has termination protection enabled. </p>

        Args:
            dashboard_id: <p> The name or ARN for the dashboard. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.delete_dashboard_request.DeleteDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.delete_dashboard_response.DeleteDashboardResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_dashboard

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_dashboard.delete_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.delete_dashboard_request.DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_event_data_store(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.delete_event_data_store_response.DeleteEventDataStoreResponse":
        """<p>Disables the event data store specified by <code>EventDataStore</code>, which accepts an event data store ARN. After you run <code>DeleteEventDataStore</code>, the event data store enters a <code>PENDING_DELETION</code> state, and is automatically deleted after a wait period of seven days. <code>TerminationProtectionEnabled</code> must be set to <code>False</code> on the event data store and the <code>FederationStatus</code> must be <code>DISABLED</code>. You cannot delete an event data store if <code>TerminationProtectionEnabled</code> is <code>True</code> or the <code>FederationStatus</code> is <code>ENABLED</code>.</p> <p>After you run <code>DeleteEventDataStore</code> on an event data store, you cannot run <code>ListQueries</code>, <code>DescribeQuery</code>, or <code>GetQueryResults</code> on queries that are using an event data store in a <code>PENDING_DELETION</code> state. An event data store in the <code>PENDING_DELETION</code> state does not incur costs.</p>

        Args:
            event_data_store: <p>The ARN (or the ID suffix of the ARN) of the event data store to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.delete_event_data_store_request.DeleteEventDataStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.delete_event_data_store_response.DeleteEventDataStoreResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_event_data_store

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_event_data_store.delete_event_data_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.delete_event_data_store_request.DeleteEventDataStoreRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_cloudtrail.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p> Deletes the resource-based policy attached to the CloudTrail event data store, dashboard, or channel. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel you're deleting the resource-based policy from.</p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_resource_policy

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_trail(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.delete_trail_response.DeleteTrailResponse":
        r"""<p>Deletes a trail. This operation must be called from the Region in which the trail was created. <code>DeleteTrail</code> cannot be called on the shadow trails (replicated trails in other Regions) of a trail that is enabled in all Regions.</p> <important> <p> While deleting a CloudTrail trail is an irreversible action, CloudTrail does not delete log files in the Amazon S3 bucket for that trail, the Amazon S3 bucket itself, or the CloudWatchlog group to which the trail delivers events. Deleting a multi-Region trail will stop logging of events in all Amazon Web Services Regions enabled in your Amazon Web Services account. Deleting a single-Region trail will stop logging of events in that Region only. It will not stop logging of events in other Regions even if the trails in those other Regions have identical names to the deleted trail. </p> <p>For information about account closure and deletion of CloudTrail trails, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-account-closure.html\">https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-account-closure.html</a>.</p> </important>

        Args:
            name: <p>Specifies the name or the CloudTrail ARN of the trail to be deleted. The following is the format of a trail ARN. <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.delete_trail_request.DeleteTrailRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.delete_trail_response.DeleteTrailResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_trail

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.delete_trail.delete_trail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.delete_trail_request.DeleteTrailRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_organization_delegated_admin(
        self,
        delegated_admin_account_id: "aws_sdk_cloudtrail.types.account_id.AccountId",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.deregister_organization_delegated_admin_response.DeregisterOrganizationDelegatedAdminResponse":
        """<p>Removes CloudTrail delegated administrator permissions from a member account in an organization.</p>

        Args:
            delegated_admin_account_id: <p>A delegated administrator account ID. This is a member account in an organization that is currently designated as a delegated administrator.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.deregister_organization_delegated_admin_request.DeregisterOrganizationDelegatedAdminRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.deregister_organization_delegated_admin_response.DeregisterOrganizationDelegatedAdminResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.deregister_organization_delegated_admin

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.deregister_organization_delegated_admin.deregister_organization_delegated_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.deregister_organization_delegated_admin_request.DeregisterOrganizationDelegatedAdminRequest = {}  # type: ignore[typeddict-item]
        input_["delegated_admin_account_id"] = delegated_admin_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_query(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        event_data_store: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
        query_id: Optional["aws_sdk_cloudtrail.types.uuid.UUID"] = None,
        query_alias: Optional["aws_sdk_cloudtrail.types.query_alias.QueryAlias"] = None,
        refresh_id: Optional["aws_sdk_cloudtrail.types.refresh_id.RefreshId"] = None,
        event_data_store_owner_account_id: Optional[
            "aws_sdk_cloudtrail.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.describe_query_response.DescribeQueryResponse":
        """<p>Returns metadata about a query, including query run time in milliseconds, number of events scanned and matched, and query status. If the query results were delivered to an S3 bucket, the response also provides the S3 URI and the delivery status.</p> <p>You must specify either <code>QueryId</code> or <code>QueryAlias</code>. Specifying the <code>QueryAlias</code> parameter returns information about the last query run for the alias. You can provide <code>RefreshId</code> along with <code>QueryAlias</code> to view the query results of a dashboard query for the specified <code>RefreshId</code>.</p>

        Args:
            event_data_store: <p>The ARN (or the ID suffix of the ARN) of an event data store on which the specified query was run.</p>
            query_id: <p>The query ID.</p>
            query_alias: <p> The alias that identifies a query template. </p>
            refresh_id: <p> The ID of the dashboard refresh. </p>
            event_data_store_owner_account_id: <p> The account ID of the event data store owner. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.describe_query_request.DescribeQueryRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.describe_query_response.DescribeQueryResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.describe_query

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.describe_query.describe_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.describe_query_request.DescribeQueryRequest = {}  # type: ignore[typeddict-item]
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store
        if query_id is not None:
            input_["query_id"] = query_id
        if query_alias is not None:
            input_["query_alias"] = query_alias
        if refresh_id is not None:
            input_["refresh_id"] = refresh_id
        if event_data_store_owner_account_id is not None:
            input_["event_data_store_owner_account_id"] = (
                event_data_store_owner_account_id
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_trails(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        trail_name_list: Optional[
            "aws_sdk_cloudtrail.types.trail_name_list.TrailNameList"
        ] = None,
        include_shadow_trails: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.describe_trails_response.DescribeTrailsResponse":
        """<p>Retrieves settings for one or more trails associated with the current Region for your account.</p>

        Args:
            trail_name_list: <p>Specifies a list of trail names, trail ARNs, or both, of the trails to describe. The format of a trail ARN is:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>If an empty list is specified, information for the trail in the current Region is returned.</p> <ul> <li> <p>If an empty list is specified and <code>IncludeShadowTrails</code> is false, then information for all trails in the current Region is returned.</p> </li> <li> <p>If an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current Region and any associated shadow trails in other Regions is returned.</p> </li> </ul> <note> <p>If one or more trail names are specified, information is returned only if the names match the names of trails belonging only to the current Region and current account. To return information about a trail in another Region, you must specify its trail ARN.</p> </note>
            include_shadow_trails: <p>Specifies whether to include shadow trails in the response. A shadow trail is the replication in a Region of a trail that was created in a different Region, or in the case of an organization trail, the replication of an organization trail in member accounts. If you do not include shadow trails, organization trails in a member account and Region replication trails will not be returned. The default is true.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.describe_trails_request.DescribeTrailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.describe_trails_response.DescribeTrailsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.describe_trails

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.describe_trails.describe_trails(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.describe_trails_request.DescribeTrailsRequest = {}  # type: ignore[typeddict-item]
        if trail_name_list is not None:
            input_["trail_name_list"] = trail_name_list
        if include_shadow_trails is not None:
            input_["include_shadow_trails"] = include_shadow_trails

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_federation(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> (
        "aws_sdk_cloudtrail.types.disable_federation_response.DisableFederationResponse"
    ):
        """<p> Disables Lake query federation on the specified event data store. When you disable federation, CloudTrail disables the integration with Glue, Lake Formation, and Amazon Athena. After disabling Lake query federation, you can no longer query your event data in Amazon Athena.</p> <p>No CloudTrail Lake data is deleted when you disable federation and you can continue to run queries in CloudTrail Lake.</p>

        Args:
            event_data_store: <p> The ARN (or ID suffix of the ARN) of the event data store for which you want to disable Lake query federation. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.disable_federation_request.DisableFederationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.disable_federation_response.DisableFederationResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.disable_federation

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.disable_federation.disable_federation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.disable_federation_request.DisableFederationRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_federation(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        federation_role_arn: "aws_sdk_cloudtrail.types.federation_role_arn.FederationRoleArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.enable_federation_response.EnableFederationResponse":
        r"""<p> Enables Lake query federation on the specified event data store. Federating an event data store lets you view the metadata associated with the event data store in the Glue <a href=\"https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro\">Data Catalog</a> and run SQL queries against your event data using Amazon Athena. The table metadata stored in the Glue Data Catalog lets the Athena query engine know how to find, read, and process the data that you want to query.</p> <p>When you enable Lake query federation, CloudTrail creates a managed database named <code>aws:cloudtrail</code> (if the database doesn't already exist) and a managed federated table in the Glue Data Catalog. The event data store ID is used for the table name. CloudTrail registers the role ARN and event data store in <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation-lake-formation.html\">Lake Formation</a>, the service responsible for allowing fine-grained access control of the federated resources in the Glue Data Catalog.</p> <p>For more information about Lake query federation, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html\">Federate an event data store</a>.</p>

        Args:
            event_data_store: <p>The ARN (or ID suffix of the ARN) of the event data store for which you want to enable Lake query federation.</p>
            federation_role_arn: <p> The ARN of the federation role to use for the event data store. Amazon Web Services services like Lake Formation use this federation role to access data for the federated event data store. The federation role must exist in your account and provide the <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions-role\">required minimum permissions</a>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.enable_federation_request.EnableFederationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.enable_federation_response.EnableFederationResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.enable_federation

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.enable_federation.enable_federation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.enable_federation_request.EnableFederationRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store
        input_["federation_role_arn"] = federation_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def generate_query(
        self,
        event_data_stores: "aws_sdk_cloudtrail.types.event_data_store_list.EventDataStoreList",
        prompt: "aws_sdk_cloudtrail.types.prompt.Prompt",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.generate_query_response.GenerateQueryResponse":
        r"""<p> Generates a query from a natural language prompt. This operation uses generative artificial intelligence (generative AI) to produce a ready-to-use SQL query from the prompt. </p> <p>The prompt can be a question or a statement about the event data in your event data store. For example, you can enter prompts like \"What are my top errors in the past month?\" and “Give me a list of users that used SNS.”</p> <p>The prompt must be in English. For information about limitations, permissions, and supported Regions, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html\">Create CloudTrail Lake queries from natural language prompts</a> in the <i>CloudTrail </i> user guide.</p> <note> <p>Do not include any personally identifying, confidential, or sensitive information in your prompts.</p> <p>This feature uses generative AI large language models (LLMs); we recommend double-checking the LLM response.</p> </note>

        Args:
            event_data_stores: <p> The ARN (or ID suffix of the ARN) of the event data store that you want to query. You can only specify one event data store. </p>
            prompt: <p> The prompt that you want to use to generate the query. The prompt must be in English. For example prompts, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-query-generator.html#lake-query-generator-examples\">Example prompts</a> in the <i>CloudTrail </i> user guide. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.generate_query_request.GenerateQueryRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.generate_query_response.GenerateQueryResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.generate_query

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.generate_query.generate_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.generate_query_request.GenerateQueryRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_stores"] = event_data_stores
        input_["prompt"] = prompt

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_channel(
        self,
        channel: "aws_sdk_cloudtrail.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_channel_response.GetChannelResponse":
        """<p> Returns information about a specific channel. </p>

        Args:
            channel: <p>The ARN or <code>UUID</code> of a channel.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_channel_request.GetChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_channel_response.GetChannelResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_channel

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_channel.get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_channel_request.GetChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel"] = channel

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_dashboard(
        self,
        dashboard_id: "aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_dashboard_response.GetDashboardResponse":
        """<p> Returns the specified dashboard. </p>

        Args:
            dashboard_id: <p> The name or ARN for the dashboard. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_dashboard_request.GetDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_dashboard_response.GetDashboardResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_dashboard

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_dashboard.get_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_dashboard_request.GetDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_configuration(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        trail_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        event_data_store: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "aws_sdk_cloudtrail.types.get_event_configuration_response.GetEventConfigurationResponse":
        """<p>Retrieves the current event configuration settings for the specified event data store or trail. The response includes maximum event size configuration, the context key selectors configured for the event data store, and any aggregation settings configured for the trail.</p>

        Args:
            trail_name: <p>The name of the trail for which you want to retrieve event configuration settings.</p>
            event_data_store: <p>The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which you want to retrieve event configuration settings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_event_configuration_request.GetEventConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_event_configuration_response.GetEventConfigurationResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_event_configuration

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_event_configuration.get_event_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_event_configuration_request.GetEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        if trail_name is not None:
            input_["trail_name"] = trail_name
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_data_store(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_event_data_store_response.GetEventDataStoreResponse":
        """<p>Returns information about an event data store specified as either an ARN or the ID portion of the ARN.</p>

        Args:
            event_data_store: <p>The ARN (or ID suffix of the ARN) of the event data store about which you want information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_event_data_store_request.GetEventDataStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_event_data_store_response.GetEventDataStoreResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_event_data_store

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_event_data_store.get_event_data_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_event_data_store_request.GetEventDataStoreRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_event_selectors(
        self,
        trail_name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_event_selectors_response.GetEventSelectorsResponse":
        r"""<p>Describes the settings for the event selectors that you configured for your trail. The information returned for your event selectors includes the following:</p> <ul> <li> <p>If your event selector includes read-only events, write-only events, or all events. This applies to management events, data events, and network activity events.</p> </li> <li> <p>If your event selector includes management events.</p> </li> <li> <p>If your event selector includes network activity events, the event sources for which you are logging network activity events.</p> </li> <li> <p>If your event selector includes data events, the resources on which you are logging data events.</p> </li> </ul> <p>For more information about logging management, data, and network activity events, see the following topics in the <i>CloudTrail User Guide</i>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html\">Logging management events</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html\">Logging data events</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html\">Logging network activity events</a> </p> </li> </ul>

        Args:
            trail_name: <p>Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If you specify a trail ARN, it must be in the format:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_event_selectors_request.GetEventSelectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_event_selectors_response.GetEventSelectorsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_event_selectors

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_event_selectors.get_event_selectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_event_selectors_request.GetEventSelectorsRequest = {}  # type: ignore[typeddict-item]
        input_["trail_name"] = trail_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_import(
        self,
        import_id: "aws_sdk_cloudtrail.types.uuid.UUID",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_import_response.GetImportResponse":
        """<p> Returns information about a specific import. </p>

        Args:
            import_id: <p> The ID for the import. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_import_request.GetImportRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_import_response.GetImportResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_import

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_import.get_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_import_request.GetImportRequest = {}  # type: ignore[typeddict-item]
        input_["import_id"] = import_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_insight_selectors(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        trail_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        event_data_store: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.get_insight_selectors_response.GetInsightSelectorsResponse":
        r"""<p>Describes the settings for the Insights event selectors that you configured for your trail or event data store. <code>GetInsightSelectors</code> shows if CloudTrail Insights logging is enabled and which Insights types are configured with corresponding event categories. If you run <code>GetInsightSelectors</code> on a trail or event data store that does not have Insights events enabled, the operation throws the exception <code>InsightNotEnabledException</code> </p> <p>Specify either the <code>EventDataStore</code> parameter to get Insights event selectors for an event data store, or the <code>TrailName</code> parameter to the get Insights event selectors for a trail. You cannot specify these parameters together.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html\">Working with CloudTrail Insights</a> in the <i>CloudTrail User Guide</i>.</p>

        Args:
            trail_name: <p>Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If you specify a trail ARN, it must be in the format:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>You cannot use this parameter with the <code>EventDataStore</code> parameter.</p>
            event_data_store: <p> Specifies the ARN (or ID suffix of the ARN) of the event data store for which you want to get Insights selectors. </p> <p>You cannot use this parameter with the <code>TrailName</code> parameter.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_insight_selectors_request.GetInsightSelectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_insight_selectors_response.GetInsightSelectorsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_insight_selectors

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_insight_selectors.get_insight_selectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_insight_selectors_request.GetInsightSelectorsRequest = {}  # type: ignore[typeddict-item]
        if trail_name is not None:
            input_["trail_name"] = trail_name
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_query_results(
        self,
        query_id: "aws_sdk_cloudtrail.types.uuid.UUID",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        event_data_store: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
        max_query_results: Optional[
            "aws_sdk_cloudtrail.types.max_query_results.MaxQueryResults"
        ] = None,
        event_data_store_owner_account_id: Optional[
            "aws_sdk_cloudtrail.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.get_query_results_response.GetQueryResultsResponse":
        """<p>Gets event data results of a query. You must specify the <code>QueryID</code> value returned by the <code>StartQuery</code> operation.</p>

        Args:
            event_data_store: <p>The ARN (or ID suffix of the ARN) of the event data store against which the query was run.</p>
            query_id: <p>The ID of the query for which you want to get results.</p>
            next_token: <p>A token you can use to get the next page of query results.</p>
            max_query_results: <p>The maximum number of query results to display on a single page.</p>
            event_data_store_owner_account_id: <p> The account ID of the event data store owner. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_query_results_request.GetQueryResultsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_query_results_response.GetQueryResultsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_query_results

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_query_results.get_query_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_query_results_request.GetQueryResultsRequest = {}  # type: ignore[typeddict-item]
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store
        input_["query_id"] = query_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_query_results is not None:
            input_["max_query_results"] = max_query_results
        if event_data_store_owner_account_id is not None:
            input_["event_data_store_owner_account_id"] = (
                event_data_store_owner_account_id
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_cloudtrail.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p> Retrieves the JSON text of the resource-based policy document attached to the CloudTrail event data store, dashboard, or channel. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel attached to the resource-based policy.</p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_resource_policy

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_trail(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_trail_response.GetTrailResponse":
        """<p>Returns settings information for a specified trail.</p>

        Args:
            name: <p>The name or the Amazon Resource Name (ARN) of the trail for which you want to retrieve settings information.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_trail_request.GetTrailRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_trail_response.GetTrailResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_trail

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_trail.get_trail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_trail_request.GetTrailRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_trail_status(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.get_trail_status_response.GetTrailStatusResponse":
        """<p>Returns a JSON-formatted list of information about the specified trail. Fields include information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for each trail. This operation returns trail status from a single Region. To return trail status from all Regions, you must call the operation on each Region.</p>

        Args:
            name: <p>Specifies the name or the CloudTrail ARN of the trail for which you are requesting status. To get the status of a shadow trail (a replication of the trail in another Region), you must specify its ARN.</p> <p> The following is the format of a trail ARN: <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <note> <p>If the trail is an organization trail and you are a member account in the organization in Organizations, you must provide the full ARN of that trail, and not just the name.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.get_trail_status_request.GetTrailStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.get_trail_status_response.GetTrailStatusResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_trail_status

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.get_trail_status.get_trail_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.get_trail_status_request.GetTrailStatusRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channels(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_channels_max_results_count.ListChannelsMaxResultsCount"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_channels_response.ListChannelsResponse":
        """<p> Lists the channels in the current account, and their source names. </p>

        Args:
            max_results: <p> The maximum number of CloudTrail channels to display on a single page. </p>
            next_token: <p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_channels_response.ListChannelsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_channels

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_channels_request.ListChannelsRequest = {}  # type: ignore[typeddict-item]
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

    def list_dashboards(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_cloudtrail.types.dashboard_name.DashboardName"
        ] = None,
        type: Optional["aws_sdk_cloudtrail.types.dashboard_type.DashboardType"] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_dashboards_max_results_count.ListDashboardsMaxResultsCount"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_dashboards_response.ListDashboardsResponse":
        """<p> Returns information about all dashboards in the account, in the current Region. </p>

        Args:
            name_prefix: <p> Specify a name prefix to filter on. </p>
            type: <p> Specify a dashboard type to filter on: <code>CUSTOM</code> or <code>MANAGED</code>. </p>
            next_token: <p> A token you can use to get the next page of dashboard results. </p>
            max_results: <p> The maximum number of dashboards to display on a single page. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_dashboards_request.ListDashboardsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_dashboards_response.ListDashboardsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_dashboards

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_dashboards.list_dashboards(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_dashboards_request.ListDashboardsRequest = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if type is not None:
            input_["type"] = type
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

    def list_event_data_stores(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_event_data_stores_max_results_count.ListEventDataStoresMaxResultsCount"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_event_data_stores_response.ListEventDataStoresResponse":
        """<p>Returns information about all event data stores in the account, in the current Region.</p>

        Args:
            next_token: <p>A token you can use to get the next page of event data store results.</p>
            max_results: <p>The maximum number of event data stores to display on a single page.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_event_data_stores_request.ListEventDataStoresRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_event_data_stores_response.ListEventDataStoresResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_event_data_stores

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_event_data_stores.list_event_data_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_event_data_stores_request.ListEventDataStoresRequest = {}  # type: ignore[typeddict-item]
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

    def list_import_failures(
        self,
        import_id: "aws_sdk_cloudtrail.types.uuid.UUID",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_import_failures_max_results_count.ListImportFailuresMaxResultsCount"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_import_failures_response.ListImportFailuresResponse":
        """<p> Returns a list of failures for the specified import. </p>

        Args:
            import_id: <p> The ID of the import. </p>
            max_results: <p> The maximum number of failures to display on a single page. </p>
            next_token: <p> A token you can use to get the next page of import failures. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_import_failures_request.ListImportFailuresRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_import_failures_response.ListImportFailuresResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_import_failures

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_import_failures.list_import_failures(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_import_failures_request.ListImportFailuresRequest = {}  # type: ignore[typeddict-item]
        input_["import_id"] = import_id
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

    def iter_list_import_failures(
        self,
        import_id: "aws_sdk_cloudtrail.types.uuid.UUID",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_import_failures_max_results_count.ListImportFailuresMaxResultsCount"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.import_failure_list_item.ImportFailureListItem]":
        _token = next_token
        while True:
            _response = self.list_import_failures(
                import_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("failures",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_imports(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_imports_max_results_count.ListImportsMaxResultsCount"
        ] = None,
        destination: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
        import_status: Optional[
            "aws_sdk_cloudtrail.types.import_status.ImportStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_imports_response.ListImportsResponse":
        """<p> Returns information on all imports, or a select set of imports by <code>ImportStatus</code> or <code>Destination</code>. </p>

        Args:
            max_results: <p> The maximum number of imports to display on a single page. </p>
            destination: <p> The ARN of the destination event data store. </p>
            import_status: <p> The status of the import. </p>
            next_token: <p> A token you can use to get the next page of import results. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_imports_request.ListImportsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_imports_response.ListImportsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_imports

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_imports.list_imports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_imports_request.ListImportsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if destination is not None:
            input_["destination"] = destination
        if import_status is not None:
            input_["import_status"] = import_status
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_imports(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_imports_max_results_count.ListImportsMaxResultsCount"
        ] = None,
        destination: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
        import_status: Optional[
            "aws_sdk_cloudtrail.types.import_status.ImportStatus"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.imports_list_item.ImportsListItem]":
        _token = next_token
        while True:
            _response = self.list_imports(
                config_overrides=config_overrides,
                max_results=max_results,
                destination=destination,
                import_status=import_status,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("imports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_insights_data(
        self,
        insight_source: "aws_sdk_cloudtrail.types.resource_arn.ResourceArn",
        data_type: "aws_sdk_cloudtrail.types.list_insights_data_type.ListInsightsDataType",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        dimensions: Optional[
            "aws_sdk_cloudtrail.types.list_insights_data_dimensions.ListInsightsDataDimensions"
        ] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_insights_data_max_results_count.ListInsightsDataMaxResultsCount"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "aws_sdk_cloudtrail.types.list_insights_data_response.ListInsightsDataResponse"
    ):
        """<p>Returns Insights events generated on a trail that logs data events. You can list Insights events that occurred in a Region within the last 90 days.</p> <p>ListInsightsData supports the following Dimensions for Insights events:</p> <ul> <li> <p>Event ID</p> </li> <li> <p>Event name</p> </li> <li> <p>Event source</p> </li> </ul> <p>All dimensions are optional. The default number of results returned is 50, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.</p> <p>The rate of ListInsightsData requests is limited to two per second, per account, per Region. If this limit is exceeded, a throttling error occurs.</p>

        Args:
            insight_source: <p>The Amazon Resource Name(ARN) of the trail for which you want to retrieve Insights events.</p>
            data_type: <p>Specifies the category of events returned. To fetch Insights events, specify <code>InsightsEvents</code> as the value of <code>DataType</code> </p>
            dimensions: <p>Contains a map of dimensions. Currently the map can contain only one item.</p>
            start_time: <p>Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.</p>
            end_time: <p>Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.</p>
            max_results: <p>The number of events to return. Possible values are 1 through 50. The default is 50.</p>
            next_token: <p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified a EventName as a dimension with <code>PutObject</code> as a value, the call with NextToken should include those same parameters. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_insights_data_request.ListInsightsDataRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_insights_data_response.ListInsightsDataResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_insights_data

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_insights_data.list_insights_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_insights_data_request.ListInsightsDataRequest = {}  # type: ignore[typeddict-item]
        input_["insight_source"] = insight_source
        input_["data_type"] = data_type
        if dimensions is not None:
            input_["dimensions"] = dimensions
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    def iter_list_insights_data(
        self,
        insight_source: "aws_sdk_cloudtrail.types.resource_arn.ResourceArn",
        data_type: "aws_sdk_cloudtrail.types.list_insights_data_type.ListInsightsDataType",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        dimensions: Optional[
            "aws_sdk_cloudtrail.types.list_insights_data_dimensions.ListInsightsDataDimensions"
        ] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_insights_data_max_results_count.ListInsightsDataMaxResultsCount"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.event.Event]":
        _token = next_token
        while True:
            _response = self.list_insights_data(
                insight_source,
                data_type,
                config_overrides=config_overrides,
                dimensions=dimensions,
                start_time=start_time,
                end_time=end_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_insights_metric_data(
        self,
        event_source: "aws_sdk_cloudtrail.types.event_source.EventSource",
        event_name: "aws_sdk_cloudtrail.types.event_name.EventName",
        insight_type: "aws_sdk_cloudtrail.types.insight_type.InsightType",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        trail_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        error_code: Optional["aws_sdk_cloudtrail.types.error_code.ErrorCode"] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        period: Optional[
            "aws_sdk_cloudtrail.types.insights_metric_period.InsightsMetricPeriod"
        ] = None,
        data_type: Optional[
            "aws_sdk_cloudtrail.types.insights_metric_data_type.InsightsMetricDataType"
        ] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.insights_metric_max_results.InsightsMetricMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.insights_metric_next_token.InsightsMetricNextToken"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_insights_metric_data_response.ListInsightsMetricDataResponse":
        """<p>Returns Insights metrics data for trails that have enabled Insights. The request must include the <code>EventSource</code>, <code>EventName</code>, and <code>InsightType</code> parameters.</p> <p>If the <code>InsightType</code> is set to <code>ApiErrorRateInsight</code>, the request must also include the <code>ErrorCode</code> parameter.</p> <p>The following are the available time periods for <code>ListInsightsMetricData</code>. Each cutoff is inclusive.</p> <ul> <li> <p>Data points with a period of 60 seconds (1-minute) are available for 15 days.</p> </li> <li> <p>Data points with a period of 300 seconds (5-minute) are available for 63 days.</p> </li> <li> <p>Data points with a period of 3600 seconds (1 hour) are available for 90 days.</p> </li> </ul> <p>To use <code>ListInsightsMetricData</code> operation, you must have the following permissions:</p> <ul> <li> <p>If <code>ListInsightsMetricData</code> is invoked with <code>TrailName</code> parameter, access to the <code>ListInsightsMetricData</code> API operation is linked to the <code>cloudtrail:LookupEvents</code> action and <code>cloudtrail:ListInsightsData</code>. To use this operation, you must have permissions to perform the <code>cloudtrail:LookupEvents</code> and <code>cloudtrail:ListInsightsData</code> action on the specific trail.</p> </li> <li> <p>If <code>ListInsightsMetricData</code> is invoked without <code>TrailName</code> parameter, access to the <code>ListInsightsMetricData</code> API operation is linked to the <code>cloudtrail:LookupEvents</code> action only. To use this operation, you must have permissions to perform the <code>cloudtrail:LookupEvents</code> action.</p> </li> </ul>

        Args:
            trail_name: <p>The Amazon Resource Name(ARN) or name of the trail for which you want to retrieve Insights metrics data. This parameter should only be provided to fetch Insights metrics data generated on trails logging data events. This parameter is not required for Insights metric data generated on trails logging management events.</p>
            event_source: <p>The Amazon Web Services service to which the request was made, such as <code>iam.amazonaws.com</code> or <code>s3.amazonaws.com</code>.</p>
            event_name: <p>The name of the event, typically the Amazon Web Services API on which unusual levels of activity were recorded.</p>
            insight_type: <p>The type of CloudTrail Insights event, which is either <code>ApiCallRateInsight</code> or <code>ApiErrorRateInsight</code>. The <code>ApiCallRateInsight</code> Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The <code>ApiErrorRateInsight</code> Insights type analyzes management API calls that result in error codes.</p>
            error_code: <p>Conditionally required if the <code>InsightType</code> parameter is set to <code>ApiErrorRateInsight</code>.</p> <p>If returning metrics for the <code>ApiErrorRateInsight</code> Insights type, this is the error to retrieve data for. For example, <code>AccessDenied</code>.</p>
            start_time: <p>Specifies, in UTC, the start time for time-series data. The value specified is inclusive; results include data points with the specified time stamp.</p> <p>The default is 90 days before the time of request.</p>
            end_time: <p>Specifies, in UTC, the end time for time-series data. The value specified is exclusive; results include data points up to the specified time stamp.</p> <p>The default is the time of request.</p>
            period: <p>Granularity of data to retrieve, in seconds. Valid values are <code>60</code>, <code>300</code>, and <code>3600</code>. If you specify any other value, you will get an error. The default is 3600 seconds.</p>
            data_type: <p>Type of data points to return. Valid values are <code>NonZeroData</code> and <code>FillWithZeros</code>. The default is <code>NonZeroData</code>.</p>
            max_results: <p>The maximum number of data points to return. Valid values are integers from 1 to 21600. The default value is 21600.</p>
            next_token: <p>Returned if all datapoints can't be returned in a single call. For example, due to reaching <code>MaxResults</code>.</p> <p>Add this parameter to the request to continue retrieving results starting from the last evaluated point.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_insights_metric_data_request.ListInsightsMetricDataRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_insights_metric_data_response.ListInsightsMetricDataResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_insights_metric_data

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_insights_metric_data.list_insights_metric_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_insights_metric_data_request.ListInsightsMetricDataRequest = {}  # type: ignore[typeddict-item]
        if trail_name is not None:
            input_["trail_name"] = trail_name
        input_["event_source"] = event_source
        input_["event_name"] = event_name
        input_["insight_type"] = insight_type
        if error_code is not None:
            input_["error_code"] = error_code
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if period is not None:
            input_["period"] = period
        if data_type is not None:
            input_["data_type"] = data_type
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

    def list_public_keys(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "aws_sdk_cloudtrail.types.list_public_keys_response.ListPublicKeysResponse":
        """<p>Returns all public keys whose private keys were used to sign the digest files within the specified time range. The public key is needed to validate digest files that were signed with its corresponding private key.</p> <note> <p>CloudTrail uses different private and public key pairs per Region. Each digest file is signed with a private key unique to its Region. When you validate a digest file from a specific Region, you must look in the same Region for its corresponding public key.</p> </note>

        Args:
            start_time: <p>Optionally specifies, in UTC, the start of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used, and the current public key is returned.</p>
            end_time: <p>Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used.</p>
            next_token: <p>Reserved for future use.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_public_keys_request.ListPublicKeysRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_public_keys_response.ListPublicKeysResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_public_keys

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_public_keys.list_public_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_public_keys_request.ListPublicKeysRequest = {}  # type: ignore[typeddict-item]
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_public_keys(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.public_key.PublicKey]":
        _token = next_token
        while True:
            _response = self.list_public_keys(
                config_overrides=config_overrides,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("public_key_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queries(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.list_queries_max_results_count.ListQueriesMaxResultsCount"
        ] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        query_status: Optional[
            "aws_sdk_cloudtrail.types.query_status.QueryStatus"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.list_queries_response.ListQueriesResponse":
        """<p>Returns a list of queries and query statuses for the past seven days. You must specify an ARN value for <code>EventDataStore</code>. Optionally, to shorten the list of results, you can specify a time range, formatted as timestamps, by adding <code>StartTime</code> and <code>EndTime</code> parameters, and a <code>QueryStatus</code> value. Valid values for <code>QueryStatus</code> include <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code>.</p>

        Args:
            event_data_store: <p>The ARN (or the ID suffix of the ARN) of an event data store on which queries were run.</p>
            next_token: <p>A token you can use to get the next page of results.</p>
            max_results: <p>The maximum number of queries to show on a page.</p>
            start_time: <p>Use with <code>EndTime</code> to bound a <code>ListQueries</code> request, and limit its results to only those queries run within a specified time period.</p>
            end_time: <p>Use with <code>StartTime</code> to bound a <code>ListQueries</code> request, and limit its results to only those queries run within a specified time period.</p>
            query_status: <p>The status of queries that you want to return in results. Valid values for <code>QueryStatus</code> include <code>QUEUED</code>, <code>RUNNING</code>, <code>FINISHED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>CANCELLED</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_queries_request.ListQueriesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_queries_response.ListQueriesResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_queries

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_queries.list_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_queries_request.ListQueriesRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if query_status is not None:
            input_["query_status"] = query_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags(
        self,
        resource_id_list: "aws_sdk_cloudtrail.types.resource_id_list.ResourceIdList",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "aws_sdk_cloudtrail.types.list_tags_response.ListTagsResponse":
        """<p>Lists the tags for the specified trails, event data stores, dashboards, or channels in the current Region.</p>

        Args:
            resource_id_list: <p>Specifies a list of trail, event data store, dashboard, or channel ARNs whose tags will be listed. The list has a limit of 20 ARNs.</p> <p> Example trail ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>
            next_token: <p>Reserved for future use.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_tags_request.ListTagsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_tags_response.ListTagsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_tags

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_tags.list_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_tags_request.ListTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id_list"] = resource_id_list
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_tags(
        self,
        resource_id_list: "aws_sdk_cloudtrail.types.resource_id_list.ResourceIdList",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.resource_tag.ResourceTag]":
        _token = next_token
        while True:
            _response = self.list_tags(
                resource_id_list,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_tag_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_trails(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "aws_sdk_cloudtrail.types.list_trails_response.ListTrailsResponse":
        """<p>Lists trails that are in the current account.</p>

        Args:
            next_token: <p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.list_trails_request.ListTrailsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.list_trails_response.ListTrailsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_trails

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.list_trails.list_trails(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.list_trails_request.ListTrailsRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_trails(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.trail_info.TrailInfo]":
        _token = next_token
        while True:
            _response = self.list_trails(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("trails",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def lookup_events(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        lookup_attributes: Optional[
            "aws_sdk_cloudtrail.types.lookup_attributes_list.LookupAttributesList"
        ] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        event_category: Optional[
            "aws_sdk_cloudtrail.types.event_category.EventCategory"
        ] = None,
        max_results: Optional["aws_sdk_cloudtrail.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_cloudtrail.types.lookup_events_response.LookupEventsResponse":
        r"""<p>Looks up <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events\">management events</a> or <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-insights-events\">CloudTrail Insights events</a> that are captured by CloudTrail. You can look up events that occurred in a Region within the last 90 days.</p> <note> <p> <code>LookupEvents</code> returns recent Insights events for trails that enable Insights. To view Insights events for an event data store, you can run queries on your Insights event data store, and you can also view the Lake dashboard for Insights.</p> </note> <p>Lookup supports the following attributes for management events:</p> <ul> <li> <p>Amazon Web Services access key</p> </li> <li> <p>Event ID</p> </li> <li> <p>Event name</p> </li> <li> <p>Event source</p> </li> <li> <p>Read only</p> </li> <li> <p>Resource name</p> </li> <li> <p>Resource type</p> </li> <li> <p>User name</p> </li> </ul> <p>Lookup supports the following attributes for Insights events:</p> <ul> <li> <p>Event ID</p> </li> <li> <p>Event name</p> </li> <li> <p>Event source</p> </li> </ul> <p>All attributes are optional. The default number of results returned is 50, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.</p> <important> <p>The rate of lookup requests is limited to two per second, per account, per Region. If this limit is exceeded, a throttling error occurs.</p> </important>

        Args:
            lookup_attributes: <p>Contains a list of lookup attributes. Currently the list can contain only one item.</p>
            start_time: <p>Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.</p>
            end_time: <p>Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.</p>
            event_category: <p>Specifies the event category. If you do not specify an event category, events of the category are not returned in the response. For example, if you do not specify <code>insight</code> as the value of <code>EventCategory</code>, no Insights events are returned.</p>
            max_results: <p>The number of events to return. Possible values are 1 through 50. The default is 50.</p>
            next_token: <p>The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.lookup_events_request.LookupEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.lookup_events_response.LookupEventsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.lookup_events

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.lookup_events.lookup_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.lookup_events_request.LookupEventsRequest = {}  # type: ignore[typeddict-item]
        if lookup_attributes is not None:
            input_["lookup_attributes"] = lookup_attributes
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if event_category is not None:
            input_["event_category"] = event_category
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

    def iter_lookup_events(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        lookup_attributes: Optional[
            "aws_sdk_cloudtrail.types.lookup_attributes_list.LookupAttributesList"
        ] = None,
        start_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        event_category: Optional[
            "aws_sdk_cloudtrail.types.event_category.EventCategory"
        ] = None,
        max_results: Optional["aws_sdk_cloudtrail.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_cloudtrail.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_cloudtrail.types.event.Event]":
        _token = next_token
        while True:
            _response = self.lookup_events(
                config_overrides=config_overrides,
                lookup_attributes=lookup_attributes,
                start_time=start_time,
                end_time=end_time,
                event_category=event_category,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_event_configuration(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        trail_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        event_data_store: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        max_event_size: Optional[
            "aws_sdk_cloudtrail.types.max_event_size.MaxEventSize"
        ] = None,
        context_key_selectors: Optional[
            "aws_sdk_cloudtrail.types.context_key_selectors.ContextKeySelectors"
        ] = None,
        aggregation_configurations: Optional[
            "aws_sdk_cloudtrail.types.aggregation_configurations.AggregationConfigurations"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.put_event_configuration_response.PutEventConfigurationResponse":
        """<p>Updates the event configuration settings for the specified event data store or trail. This operation supports updating the maximum event size, adding or modifying context key selectors for event data store, and configuring aggregation settings for the trail.</p>

        Args:
            trail_name: <p>The name of the trail for which you want to update event configuration settings.</p>
            event_data_store: <p>The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which event configuration settings are updated.</p>
            max_event_size: <p>The maximum allowed size for events to be stored in the specified event data store. If you are using context key selectors, MaxEventSize must be set to Large.</p>
            context_key_selectors: <p>A list of context key selectors that will be included to provide enriched event data.</p>
            aggregation_configurations: <p>The list of aggregation configurations that you want to configure for the trail.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.put_event_configuration_request.PutEventConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.put_event_configuration_response.PutEventConfigurationResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_event_configuration

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_event_configuration.put_event_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.put_event_configuration_request.PutEventConfigurationRequest = {}  # type: ignore[typeddict-item]
        if trail_name is not None:
            input_["trail_name"] = trail_name
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store
        if max_event_size is not None:
            input_["max_event_size"] = max_event_size
        if context_key_selectors is not None:
            input_["context_key_selectors"] = context_key_selectors
        if aggregation_configurations is not None:
            input_["aggregation_configurations"] = aggregation_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_event_selectors(
        self,
        trail_name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        event_selectors: Optional[
            "aws_sdk_cloudtrail.types.event_selectors.EventSelectors"
        ] = None,
        advanced_event_selectors: Optional[
            "aws_sdk_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.put_event_selectors_response.PutEventSelectorsResponse":
        r"""<p>Configures event selectors (also referred to as <i>basic event selectors</i>) or advanced event selectors for your trail. You can use either <code>AdvancedEventSelectors</code> or <code>EventSelectors</code>, but not both. If you apply <code>AdvancedEventSelectors</code> to a trail, any existing <code>EventSelectors</code> are overwritten.</p> <p>You can use <code>AdvancedEventSelectors</code> to log management events, data events for all resource types, and network activity events.</p> <p>You can use <code>EventSelectors</code> to log management events and data events for the following resource types:</p> <ul> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::S3::Object</code> </p> </li> </ul> <p>You can't use <code>EventSelectors</code> to log network activity events.</p> <p>If you want your trail to log Insights events, be sure the event selector or advanced event selector enables logging of the Insights event types you want configured for your trail. For more information about logging Insights events, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html\">Working with CloudTrail Insights</a> in the <i>CloudTrail User Guide</i>. By default, trails created without specific event selectors are configured to log all read and write management events, and no data events or network activity events.</p> <p>When an event occurs in your account, CloudTrail evaluates the event selectors or advanced event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.</p> <p>Example</p> <ol> <li> <p>You create an event selector for a trail and specify that you want to log write-only events.</p> </li> <li> <p>The EC2 <code>GetConsoleOutput</code> and <code>RunInstances</code> API operations occur in your account.</p> </li> <li> <p>CloudTrail evaluates whether the events match your event selectors.</p> </li> <li> <p>The <code>RunInstances</code> is a write-only event and it matches your event selector. The trail logs the event.</p> </li> <li> <p>The <code>GetConsoleOutput</code> is a read-only event that doesn't match your event selector. The trail doesn't log the event. </p> </li> </ol> <p>The <code>PutEventSelectors</code> operation must be called from the Region in which the trail was created; otherwise, an <code>InvalidHomeRegionException</code> exception is thrown.</p> <p>You can configure up to five event selectors for each trail.</p> <p>You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html\">Logging management events</a>, <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html\">Logging data events</a>, <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html\">Logging network activity events</a>, and <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html\">Quotas in CloudTrail</a> in the <i>CloudTrail User Guide</i>.</p>

        Args:
            trail_name: <p>Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If you specify a trail ARN, it must be in the following format.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>
            event_selectors: <p>Specifies the settings for your event selectors. You can use event selectors to log management events and data events for the following resource types:</p> <ul> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::S3::Object</code> </p> </li> </ul> <p>You can't use event selectors to log network activity events.</p> <p>You can configure up to five event selectors for a trail. You can use either <code>EventSelectors</code> or <code>AdvancedEventSelectors</code> in a <code>PutEventSelectors</code> request, but not both. If you apply <code>EventSelectors</code> to a trail, any existing <code>AdvancedEventSelectors</code> are overwritten.</p>
            advanced_event_selectors: <p> Specifies the settings for advanced event selectors. You can use advanced event selectors to log management events, data events for all resource types, and network activity events.</p> <p>You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use either <code>AdvancedEventSelectors</code> or <code>EventSelectors</code>, but not both. If you apply <code>AdvancedEventSelectors</code> to a trail, any existing <code>EventSelectors</code> are overwritten. For more information about advanced event selectors, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html\">Logging data events</a> and <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.html\">Logging network activity events</a> in the <i>CloudTrail User Guide</i>. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.put_event_selectors_request.PutEventSelectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.put_event_selectors_response.PutEventSelectorsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_event_selectors

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_event_selectors.put_event_selectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.put_event_selectors_request.PutEventSelectorsRequest = {}  # type: ignore[typeddict-item]
        input_["trail_name"] = trail_name
        if event_selectors is not None:
            input_["event_selectors"] = event_selectors
        if advanced_event_selectors is not None:
            input_["advanced_event_selectors"] = advanced_event_selectors

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_insight_selectors(
        self,
        insight_selectors: "aws_sdk_cloudtrail.types.insight_selectors.InsightSelectors",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        trail_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        event_data_store: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
        insights_destination: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse":
        r"""<p>Lets you enable Insights event logging on specific event categories by specifying the Insights selectors that you want to enable on an existing trail or event data store. You also use <code>PutInsightSelectors</code> to turn off Insights event logging, by passing an empty list of Insights types. The valid Insights event types are <code>ApiErrorRateInsight</code> and <code>ApiCallRateInsight</code>, and valid EventCategories are <code>Management</code> and <code>Data</code>.</p> <note> <p> Insights on data events are not supported on event data stores. For event data stores, you can only enable Insights on management events. </p> </note> <p>To enable Insights on an event data store, you must specify the ARNs (or ID suffix of the ARNs) for the source event data store (<code>EventDataStore</code>) and the destination event data store (<code>InsightsDestination</code>). The source event data store logs management events and enables Insights. The destination event data store logs Insights events based upon the management event activity of the source event data store. The source and destination event data stores must belong to the same Amazon Web Services account.</p> <p>To log Insights events for a trail, you must specify the name (<code>TrailName</code>) of the CloudTrail trail for which you want to change or add Insights selectors.</p> <ul> <li> <p> For Management events Insights: To log CloudTrail Insights on the API call rate, the trail or event data store must log <code>write</code> management events. To log CloudTrail Insights on the API error rate, the trail or event data store must log <code>read</code> or <code>write</code> management events. </p> </li> <li> <p> For Data events Insights: To log CloudTrail Insights on the API call rate or API error rate, the trail must log <code>read</code> or <code>write</code> data events. Data events Insights are not supported on event data store. </p> </li> </ul> <p>To log CloudTrail Insights events on API call volume, the trail or event data store must log <code>write</code> management events. To log CloudTrail Insights events on API error rate, the trail or event data store must log <code>read</code> or <code>write</code> management events. You can call <code>GetEventSelectors</code> on a trail to check whether the trail logs management events. You can call <code>GetEventDataStore</code> on an event data store to check whether the event data store logs management events.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html\">Working with CloudTrail Insights</a> in the <i>CloudTrail User Guide</i>.</p>

        Args:
            trail_name: <p>The name of the CloudTrail trail for which you want to change or add Insights selectors.</p> <p>You cannot use this parameter with the <code>EventDataStore</code> and <code>InsightsDestination</code> parameters.</p>
            insight_selectors: <p>Contains the Insights types you want to log on a specific category of events on a trail or event data store. <code>ApiCallRateInsight</code> and <code>ApiErrorRateInsight</code> are valid Insight types.The EventCategory field can specify <code>Management</code> or <code>Data</code> events or both. For event data store, you can log Insights for management events only.</p> <p>The <code>ApiCallRateInsight</code> Insights type analyzes write-only management API calls or read and write data API calls that are aggregated per minute against a baseline API call volume.</p> <p>The <code>ApiErrorRateInsight</code> Insights type analyzes management and data API calls that result in error codes. The error is shown if the API call is unsuccessful.</p>
            event_data_store: <p>The ARN (or ID suffix of the ARN) of the source event data store for which you want to change or add Insights selectors. To enable Insights on an event data store, you must provide both the <code>EventDataStore</code> and <code>InsightsDestination</code> parameters.</p> <p>You cannot use this parameter with the <code>TrailName</code> parameter.</p>
            insights_destination: <p> The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events. To enable Insights on an event data store, you must provide both the <code>EventDataStore</code> and <code>InsightsDestination</code> parameters. </p> <p>You cannot use this parameter with the <code>TrailName</code> parameter.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.put_insight_selectors_request.PutInsightSelectorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.put_insight_selectors_response.PutInsightSelectorsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_insight_selectors

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_insight_selectors.put_insight_selectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.put_insight_selectors_request.PutInsightSelectorsRequest = {}  # type: ignore[typeddict-item]
        if trail_name is not None:
            input_["trail_name"] = trail_name
        input_["insight_selectors"] = insight_selectors
        if event_data_store is not None:
            input_["event_data_store"] = event_data_store
        if insights_destination is not None:
            input_["insights_destination"] = insights_destination

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "aws_sdk_cloudtrail.types.resource_arn.ResourceArn",
        resource_policy: "aws_sdk_cloudtrail.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.put_resource_policy_response.PutResourcePolicyResponse":
        r"""<p> Attaches a resource-based permission policy to a CloudTrail event data store, dashboard, or channel. For more information about resource-based policies, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html\">CloudTrail resource-based policy examples</a> in the <i>CloudTrail User Guide</i>. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel attached to the resource-based policy.</p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>
            resource_policy: <p> A JSON-formatted string for an Amazon Web Services resource-based policy. </p> <p> For example resource-based policies, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html\">CloudTrail resource-based policy examples</a> in the <i>CloudTrail User Guide</i>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_resource_policy

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_policy"] = resource_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_organization_delegated_admin(
        self,
        member_account_id: "aws_sdk_cloudtrail.types.account_id.AccountId",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.register_organization_delegated_admin_response.RegisterOrganizationDelegatedAdminResponse":
        r"""<p>Registers an organization’s member account as the CloudTrail <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-delegated-administrator.html\">delegated administrator</a>.</p>

        Args:
            member_account_id: <p>An organization member account ID that you want to designate as a delegated administrator.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.register_organization_delegated_admin_request.RegisterOrganizationDelegatedAdminRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.register_organization_delegated_admin_response.RegisterOrganizationDelegatedAdminResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.register_organization_delegated_admin

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.register_organization_delegated_admin.register_organization_delegated_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.register_organization_delegated_admin_request.RegisterOrganizationDelegatedAdminRequest = {}  # type: ignore[typeddict-item]
        input_["member_account_id"] = member_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_tags(
        self,
        resource_id: "aws_sdk_cloudtrail.types.string.String",
        tags_list: "aws_sdk_cloudtrail.types.tags_list.TagsList",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.remove_tags_response.RemoveTagsResponse":
        """<p>Removes the specified tags from a trail, event data store, dashboard, or channel.</p>

        Args:
            resource_id: <p>Specifies the ARN of the trail, event data store, dashboard, or channel from which tags should be removed.</p> <p> Example trail ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>
            tags_list: <p>Specifies a list of tags to be removed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.remove_tags_request.RemoveTagsRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.remove_tags_response.RemoveTagsResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.remove_tags

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.remove_tags.remove_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.remove_tags_request.RemoveTagsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_id"] = resource_id
        input_["tags_list"] = tags_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def restore_event_data_store(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.restore_event_data_store_response.RestoreEventDataStoreResponse":
        """<p>Restores a deleted event data store specified by <code>EventDataStore</code>, which accepts an event data store ARN. You can only restore a deleted event data store within the seven-day wait period after deletion. Restoring an event data store can take several minutes, depending on the size of the event data store.</p>

        Args:
            event_data_store: <p>The ARN (or the ID suffix of the ARN) of the event data store that you want to restore.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.restore_event_data_store_request.RestoreEventDataStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.restore_event_data_store_response.RestoreEventDataStoreResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.restore_event_data_store

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.restore_event_data_store.restore_event_data_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.restore_event_data_store_request.RestoreEventDataStoreRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_sample_queries(
        self,
        search_phrase: "aws_sdk_cloudtrail.types.search_sample_queries_search_phrase.SearchSampleQueriesSearchPhrase",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        max_results: Optional[
            "aws_sdk_cloudtrail.types.search_sample_queries_max_results.SearchSampleQueriesMaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_cloudtrail.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.search_sample_queries_response.SearchSampleQueriesResponse":
        """<p> Searches sample queries and returns a list of sample queries that are sorted by relevance. To search for sample queries, provide a natural language <code>SearchPhrase</code> in English. </p>

        Args:
            search_phrase: <p> The natural language phrase to use for the semantic search. The phrase must be in English. The length constraint is in characters, not words.</p>
            max_results: <p> The maximum number of results to return on a single page. The default value is 10. </p>
            next_token: <p> A token you can use to get the next page of results. The length constraint is in characters, not words. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.search_sample_queries_request.SearchSampleQueriesRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.search_sample_queries_response.SearchSampleQueriesResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.search_sample_queries

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.search_sample_queries.search_sample_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.search_sample_queries_request.SearchSampleQueriesRequest = {}  # type: ignore[typeddict-item]
        input_["search_phrase"] = search_phrase
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

    def start_dashboard_refresh(
        self,
        dashboard_id: "aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        query_parameter_values: Optional[
            "aws_sdk_cloudtrail.types.query_parameter_values.QueryParameterValues"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.start_dashboard_refresh_response.StartDashboardRefreshResponse":
        r"""<p> Starts a refresh of the specified dashboard. </p> <p> Each time a dashboard is refreshed, CloudTrail runs queries to populate the dashboard's widgets. CloudTrail must be granted permissions to run the <code>StartQuery</code> operation on your behalf. To provide permissions, run the <code>PutResourcePolicy</code> operation to attach a resource-based policy to each event data store. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard\">Example: Allow CloudTrail to run queries to populate a dashboard</a> in the <i>CloudTrail User Guide</i>. </p>

        Args:
            dashboard_id: <p> The name or ARN of the dashboard. </p>
            query_parameter_values: <p> The query parameter values for the dashboard </p> <p>For custom dashboards, the following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, and <code>$Period$</code>.</p> <p>For managed dashboards, the following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, <code>$Period$</code>, and <code>$EventDataStoreId$</code>. The <code>$EventDataStoreId$</code> query parameter is required.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.start_dashboard_refresh_request.StartDashboardRefreshRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.start_dashboard_refresh_response.StartDashboardRefreshResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_dashboard_refresh

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_dashboard_refresh.start_dashboard_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.start_dashboard_refresh_request.StartDashboardRefreshRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id
        if query_parameter_values is not None:
            input_["query_parameter_values"] = query_parameter_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_event_data_store_ingestion(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse":
        """<p>Starts the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN. To start ingestion, the event data store <code>Status</code> must be <code>STOPPED_INGESTION</code> and the <code>eventCategory</code> must be <code>Management</code>, <code>Data</code>, <code>NetworkActivity</code>, or <code>ConfigurationItem</code>.</p>

        Args:
            event_data_store: <p>The ARN (or ID suffix of the ARN) of the event data store for which you want to start ingestion.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.start_event_data_store_ingestion_request.StartEventDataStoreIngestionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.start_event_data_store_ingestion_response.StartEventDataStoreIngestionResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_event_data_store_ingestion

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_event_data_store_ingestion.start_event_data_store_ingestion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.start_event_data_store_ingestion_request.StartEventDataStoreIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_import(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        destinations: Optional[
            "aws_sdk_cloudtrail.types.import_destinations.ImportDestinations"
        ] = None,
        import_source: Optional[
            "aws_sdk_cloudtrail.types.import_source.ImportSource"
        ] = None,
        start_event_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        end_event_time: Optional["aws_sdk_cloudtrail.types.date.Date"] = None,
        import_id: Optional["aws_sdk_cloudtrail.types.uuid.UUID"] = None,
    ) -> "aws_sdk_cloudtrail.types.start_import_response.StartImportResponse":
        r"""<p> Starts an import of logged trail events from a source S3 bucket to a destination event data store. By default, CloudTrail only imports events contained in the S3 bucket's <code>CloudTrail</code> prefix and the prefixes inside the <code>CloudTrail</code> prefix, and does not check prefixes for other Amazon Web Services services. If you want to import CloudTrail events contained in another prefix, you must include the prefix in the <code>S3LocationUri</code>. For more considerations about importing trail events, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake.html#cloudtrail-trail-copy-considerations\">Considerations for copying trail events</a> in the <i>CloudTrail User Guide</i>. </p> <p> When you start a new import, the <code>Destinations</code> and <code>ImportSource</code> parameters are required. Before starting a new import, disable any access control lists (ACLs) attached to the source S3 bucket. For more information about disabling ACLs, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html\">Controlling ownership of objects and disabling ACLs for your bucket</a>. </p> <p> When you retry an import, the <code>ImportID</code> parameter is required. </p> <note> <p> If the destination event data store is for an organization, you must use the management account to import trail events. You cannot use the delegated administrator account for the organization. </p> </note>

        Args:
            destinations: <p> The ARN of the destination event data store. Use this parameter for a new import. </p>
            import_source: <p> The source S3 bucket for the import. Use this parameter for a new import. </p>
            start_event_time: <p> Use with <code>EndEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified <code>StartEventTime</code> and <code>EndEventTime</code> before attempting to import events. </p>
            end_event_time: <p> Use with <code>StartEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified <code>StartEventTime</code> and <code>EndEventTime</code> before attempting to import events. </p>
            import_id: <p> The ID of the import. Use this parameter when you are retrying an import. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.start_import_request.StartImportRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.start_import_response.StartImportResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_import

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_import.start_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.start_import_request.StartImportRequest = {}  # type: ignore[typeddict-item]
        if destinations is not None:
            input_["destinations"] = destinations
        if import_source is not None:
            input_["import_source"] = import_source
        if start_event_time is not None:
            input_["start_event_time"] = start_event_time
        if end_event_time is not None:
            input_["end_event_time"] = end_event_time
        if import_id is not None:
            input_["import_id"] = import_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_logging(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.start_logging_response.StartLoggingResponse":
        """<p>Starts the recording of Amazon Web Services API calls and log file delivery for a trail. For a trail that is enabled in all Regions, this operation must be called from the Region in which the trail was created. This operation cannot be called on the shadow trails (replicated trails in other Regions) of a trail that is enabled in all Regions.</p>

        Args:
            name: <p>Specifies the name or the CloudTrail ARN of the trail for which CloudTrail logs Amazon Web Services API calls. The following is the format of a trail ARN.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.start_logging_request.StartLoggingRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.start_logging_response.StartLoggingResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_logging

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_logging.start_logging(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.start_logging_request.StartLoggingRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_query(
        self,
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        query_statement: Optional[
            "aws_sdk_cloudtrail.types.query_statement.QueryStatement"
        ] = None,
        delivery_s3_uri: Optional[
            "aws_sdk_cloudtrail.types.delivery_s3_uri.DeliveryS3Uri"
        ] = None,
        query_alias: Optional["aws_sdk_cloudtrail.types.query_alias.QueryAlias"] = None,
        query_parameters: Optional[
            "aws_sdk_cloudtrail.types.query_parameters.QueryParameters"
        ] = None,
        event_data_store_owner_account_id: Optional[
            "aws_sdk_cloudtrail.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.start_query_response.StartQueryResponse":
        """<p>Starts a CloudTrail Lake query. Use the <code>QueryStatement</code> parameter to provide your SQL query, enclosed in single quotation marks. Use the optional <code>DeliveryS3Uri</code> parameter to deliver the query results to an S3 bucket.</p> <p> <code>StartQuery</code> requires you specify either the <code>QueryStatement</code> parameter, or a <code>QueryAlias</code> and any <code>QueryParameters</code>. In the current release, the <code>QueryAlias</code> and <code>QueryParameters</code> parameters are used only for the queries that populate the CloudTrail Lake dashboards.</p>

        Args:
            query_statement: <p>The SQL code of your query.</p>
            delivery_s3_uri: <p> The URI for the S3 bucket where CloudTrail delivers the query results. </p>
            query_alias: <p> The alias that identifies a query template. </p>
            query_parameters: <p> The query parameters for the specified <code>QueryAlias</code>. </p>
            event_data_store_owner_account_id: <p> The account ID of the event data store owner. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.start_query_request.StartQueryRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.start_query_response.StartQueryResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_query

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.start_query.start_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.start_query_request.StartQueryRequest = {}  # type: ignore[typeddict-item]
        if query_statement is not None:
            input_["query_statement"] = query_statement
        if delivery_s3_uri is not None:
            input_["delivery_s3_uri"] = delivery_s3_uri
        if query_alias is not None:
            input_["query_alias"] = query_alias
        if query_parameters is not None:
            input_["query_parameters"] = query_parameters
        if event_data_store_owner_account_id is not None:
            input_["event_data_store_owner_account_id"] = (
                event_data_store_owner_account_id
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_event_data_store_ingestion(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.stop_event_data_store_ingestion_response.StopEventDataStoreIngestionResponse":
        """<p>Stops the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN. To stop ingestion, the event data store <code>Status</code> must be <code>ENABLED</code> and the <code>eventCategory</code> must be <code>Management</code>, <code>Data</code>, <code>NetworkActivity</code>, or <code>ConfigurationItem</code>.</p>

        Args:
            event_data_store: <p>The ARN (or ID suffix of the ARN) of the event data store for which you want to stop ingestion.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.stop_event_data_store_ingestion_request.StopEventDataStoreIngestionRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.stop_event_data_store_ingestion_response.StopEventDataStoreIngestionResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.stop_event_data_store_ingestion

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.stop_event_data_store_ingestion.stop_event_data_store_ingestion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.stop_event_data_store_ingestion_request.StopEventDataStoreIngestionRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_import(
        self,
        import_id: "aws_sdk_cloudtrail.types.uuid.UUID",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.stop_import_response.StopImportResponse":
        """<p> Stops a specified import. </p>

        Args:
            import_id: <p> The ID of the import. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.stop_import_request.StopImportRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.stop_import_response.StopImportResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.stop_import

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.stop_import.stop_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.stop_import_request.StopImportRequest = {}  # type: ignore[typeddict-item]
        input_["import_id"] = import_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def stop_logging(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
    ) -> "aws_sdk_cloudtrail.types.stop_logging_response.StopLoggingResponse":
        """<p>Suspends the recording of Amazon Web Services API calls and log file delivery for the specified trail. Under most circumstances, there is no need to use this action. You can update a trail without stopping it first. This action is the only way to stop recording. For a trail enabled in all Regions, this operation must be called from the Region in which the trail was created, or an <code>InvalidHomeRegionException</code> will occur. This operation cannot be called on the shadow trails (replicated trails in other Regions) of a trail enabled in all Regions.</p>

        Args:
            name: <p>Specifies the name or the CloudTrail ARN of the trail for which CloudTrail will stop logging Amazon Web Services API calls. The following is the format of a trail ARN.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.stop_logging_request.StopLoggingRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.stop_logging_response.StopLoggingResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.stop_logging

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.stop_logging.stop_logging(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.stop_logging_request.StopLoggingRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel(
        self,
        channel: "aws_sdk_cloudtrail.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        destinations: Optional[
            "aws_sdk_cloudtrail.types.destinations.Destinations"
        ] = None,
        name: Optional["aws_sdk_cloudtrail.types.channel_name.ChannelName"] = None,
    ) -> "aws_sdk_cloudtrail.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates a channel specified by a required channel ARN or UUID.</p>

        Args:
            channel: <p>The ARN or ID (the ARN suffix) of the channel that you want to update.</p>
            destinations: <p>The ARNs of event data stores that you want to log events arriving through the channel.</p>
            name: <p> Changes the name of the channel. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.update_channel_response.UpdateChannelResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_channel

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.update_channel_request.UpdateChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel"] = channel
        if destinations is not None:
            input_["destinations"] = destinations
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_dashboard(
        self,
        dashboard_id: "aws_sdk_cloudtrail.types.dashboard_arn.DashboardArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        widgets: Optional[
            "aws_sdk_cloudtrail.types.request_widget_list.RequestWidgetList"
        ] = None,
        refresh_schedule: Optional[
            "aws_sdk_cloudtrail.types.refresh_schedule.RefreshSchedule"
        ] = None,
        termination_protection_enabled: Optional[
            "aws_sdk_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.update_dashboard_response.UpdateDashboardResponse":
        r"""<p> Updates the specified dashboard. </p> <p> To set a refresh schedule, CloudTrail must be granted permissions to run the <code>StartDashboardRefresh</code> operation to refresh the dashboard on your behalf. To provide permissions, run the <code>PutResourcePolicy</code> operation to attach a resource-based policy to the dashboard. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards\"> Resource-based policy example for a dashboard</a> in the <i>CloudTrail User Guide</i>. </p> <p> CloudTrail runs queries to populate the dashboard's widgets during a manual or scheduled refresh. CloudTrail must be granted permissions to run the <code>StartQuery</code> operation on your behalf. To provide permissions, run the <code>PutResourcePolicy</code> operation to attach a resource-based policy to each event data store. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard\">Example: Allow CloudTrail to run queries to populate a dashboard</a> in the <i>CloudTrail User Guide</i>. </p>

        Args:
            dashboard_id: <p> The name or ARN of the dashboard. </p>
            widgets: <p> An array of widgets for the dashboard. A custom dashboard can have a maximum of 10 widgets. </p> <p>To add new widgets, pass in an array that includes the existing widgets along with any new widgets. Run the <code>GetDashboard</code> operation to get the list of widgets for the dashboard.</p> <p>To remove widgets, pass in an array that includes the existing widgets minus the widgets you want removed.</p>
            refresh_schedule: <p> The refresh schedule configuration for the dashboard. </p>
            termination_protection_enabled: <p> Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.update_dashboard_request.UpdateDashboardRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.update_dashboard_response.UpdateDashboardResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_dashboard

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_dashboard.update_dashboard(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.update_dashboard_request.UpdateDashboardRequest = {}  # type: ignore[typeddict-item]
        input_["dashboard_id"] = dashboard_id
        if widgets is not None:
            input_["widgets"] = widgets
        if refresh_schedule is not None:
            input_["refresh_schedule"] = refresh_schedule
        if termination_protection_enabled is not None:
            input_["termination_protection_enabled"] = termination_protection_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_event_data_store(
        self,
        event_data_store: "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        name: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_name.EventDataStoreName"
        ] = None,
        advanced_event_selectors: Optional[
            "aws_sdk_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
        ] = None,
        multi_region_enabled: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        organization_enabled: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        retention_period: Optional[
            "aws_sdk_cloudtrail.types.retention_period.RetentionPeriod"
        ] = None,
        termination_protection_enabled: Optional[
            "aws_sdk_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
        ] = None,
        kms_key_id: Optional[
            "aws_sdk_cloudtrail.types.event_data_store_kms_key_id.EventDataStoreKmsKeyId"
        ] = None,
        billing_mode: Optional[
            "aws_sdk_cloudtrail.types.billing_mode.BillingMode"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.update_event_data_store_response.UpdateEventDataStoreResponse":
        r"""<p>Updates an event data store. The required <code>EventDataStore</code> value is an ARN or the ID portion of the ARN. Other parameters are optional, but at least one optional parameter must be specified, or CloudTrail throws an error. <code>RetentionPeriod</code> is in days, and valid values are integers between 7 and 3653 if the <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code>, or between 7 and 2557 if <code>BillingMode</code> is set to <code>FIXED_RETENTION_PRICING</code>. By default, <code>TerminationProtection</code> is enabled.</p> <p>For event data stores for CloudTrail events, <code>AdvancedEventSelectors</code> includes or excludes management, data, or network activity events in your event data store. For more information about <code>AdvancedEventSelectors</code>, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html\">AdvancedEventSelectors</a>.</p> <p> For event data stores for CloudTrail Insights events, Config configuration items, Audit Manager evidence, or non-Amazon Web Services events, <code>AdvancedEventSelectors</code> includes events of that type in your event data store.</p>

        Args:
            event_data_store: <p>The ARN (or the ID suffix of the ARN) of the event data store that you want to update.</p>
            name: <p>The event data store name.</p>
            advanced_event_selectors: <p>The advanced event selectors used to select events for the event data store. You can configure up to five advanced event selectors for each event data store.</p>
            multi_region_enabled: <p>Specifies whether an event data store collects events from all Regions, or only from the Region in which it was created.</p>
            organization_enabled: <p>Specifies whether an event data store collects events logged for an organization in Organizations.</p> <note> <p>Only the management account for the organization can convert an organization event data store to a non-organization event data store, or convert a non-organization event data store to an organization event data store.</p> </note>
            retention_period: <p>The retention period of the event data store, in days. If <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code>, you can set a retention period of up to 3653 days, the equivalent of 10 years. If <code>BillingMode</code> is set to <code>FIXED_RETENTION_PRICING</code>, you can set a retention period of up to 2557 days, the equivalent of seven years.</p> <p>CloudTrail Lake determines whether to retain an event by checking if the <code>eventTime</code> of the event is within the specified retention period. For example, if you set a retention period of 90 days, CloudTrail will remove events when the <code>eventTime</code> is older than 90 days.</p> <note> <p>If you decrease the retention period of an event data store, CloudTrail will remove any events with an <code>eventTime</code> older than the new retention period. For example, if the previous retention period was 365 days and you decrease it to 100 days, CloudTrail will remove events with an <code>eventTime</code> older than 100 days.</p> </note>
            termination_protection_enabled: <p>Indicates that termination protection is enabled and the event data store cannot be automatically deleted.</p>
            kms_key_id: <p>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by <code>alias/</code>, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <important> <p>Disabling or deleting the KMS key, or removing CloudTrail permissions on the key, prevents CloudTrail from logging events to the event data store, and prevents users from querying the data in the event data store that was encrypted with the key. After you associate an event data store with a KMS key, the KMS key cannot be removed or changed. Before you disable or delete a KMS key that you are using with an event data store, delete or back up your event data store.</p> </important> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html\">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p> <code>alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p> <code>12345678-1234-1234-1234-123456789012</code> </p> </li> </ul>
            billing_mode: <note> <p>You can't change the billing mode from <code>EXTENDABLE_RETENTION_PRICING</code> to <code>FIXED_RETENTION_PRICING</code>. If <code>BillingMode</code> is set to <code>EXTENDABLE_RETENTION_PRICING</code> and you want to use <code>FIXED_RETENTION_PRICING</code> instead, you'll need to stop ingestion on the event data store and create a new event data store that uses <code>FIXED_RETENTION_PRICING</code>.</p> </note> <p>The billing mode for the event data store determines the cost for ingesting events and the default and maximum retention period for the event data store.</p> <p>The following are the possible values:</p> <ul> <li> <p> <code>EXTENDABLE_RETENTION_PRICING</code> - This billing mode is generally recommended if you want a flexible retention period of up to 3653 days (about 10 years). The default retention period for this billing mode is 366 days.</p> </li> <li> <p> <code>FIXED_RETENTION_PRICING</code> - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years). The default retention period for this billing mode is 2557 days.</p> </li> </ul> <p>For more information about CloudTrail pricing, see <a href=\"http://aws.amazon.com/cloudtrail/pricing/\">CloudTrail Pricing</a> and <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html\">Managing CloudTrail Lake costs</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.update_event_data_store_request.UpdateEventDataStoreRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.update_event_data_store_response.UpdateEventDataStoreResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_event_data_store

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_event_data_store.update_event_data_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.update_event_data_store_request.UpdateEventDataStoreRequest = {}  # type: ignore[typeddict-item]
        input_["event_data_store"] = event_data_store
        if name is not None:
            input_["name"] = name
        if advanced_event_selectors is not None:
            input_["advanced_event_selectors"] = advanced_event_selectors
        if multi_region_enabled is not None:
            input_["multi_region_enabled"] = multi_region_enabled
        if organization_enabled is not None:
            input_["organization_enabled"] = organization_enabled
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if termination_protection_enabled is not None:
            input_["termination_protection_enabled"] = termination_protection_enabled
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if billing_mode is not None:
            input_["billing_mode"] = billing_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_trail(
        self,
        name: "aws_sdk_cloudtrail.types.string.String",
        *,
        config_overrides: Optional[CloudTrailClientConfig] = None,
        s3_bucket_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        s3_key_prefix: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        sns_topic_name: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        include_global_service_events: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        is_multi_region_trail: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        enable_log_file_validation: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
        cloud_watch_logs_log_group_arn: Optional[
            "aws_sdk_cloudtrail.types.string.String"
        ] = None,
        cloud_watch_logs_role_arn: Optional[
            "aws_sdk_cloudtrail.types.string.String"
        ] = None,
        kms_key_id: Optional["aws_sdk_cloudtrail.types.string.String"] = None,
        is_organization_trail: Optional[
            "aws_sdk_cloudtrail.types.boolean.Boolean"
        ] = None,
    ) -> "aws_sdk_cloudtrail.types.update_trail_response.UpdateTrailResponse":
        r"""<p>Updates trail settings that control what events you are logging, and how to handle log files. Changes to a trail do not require stopping the CloudTrail service. Use this action to designate an existing bucket for log delivery. If the existing bucket has previously been a target for CloudTrail log files, an IAM policy exists for the bucket. <code>UpdateTrail</code> must be called from the Region in which the trail was created; otherwise, an <code>InvalidHomeRegionException</code> is thrown.</p>

        Args:
            name: <p>Specifies the name of the trail or trail ARN. If <code>Name</code> is a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If <code>Name</code> is a trail ARN, it must be in the following format.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>
            s3_bucket_name: <p>Specifies the name of the Amazon S3 bucket designated for publishing log files. See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html\">Amazon S3 Bucket naming rules</a>.</p>
            s3_key_prefix: <p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files\">Finding Your CloudTrail Log Files</a>. The maximum length is 200 characters.</p>
            sns_topic_name: <p>Specifies the name or ARN of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.</p>
            include_global_service_events: <p>Specifies whether the trail is publishing events from global services such as IAM to the log files.</p>
            is_multi_region_trail: <p>Specifies whether the trail applies only to the current Region or to all Regions. The default is false. If the trail exists only in the current Region and this value is set to true, shadow trails (replications of the trail) will be created in the other Regions. If the trail exists in all Regions and this value is set to false, the trail will remain in the Region where it was created, and its shadow trails in other Regions will be deleted. As a best practice, consider using trails that log events in all Regions.</p>
            enable_log_file_validation: <p>Specifies whether log file validation is enabled. The default is false.</p> <note> <p>When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.</p> </note>
            cloud_watch_logs_log_group_arn: <p>Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs are delivered. You must use a log group that exists in your account.</p> <p>Not required unless you specify <code>CloudWatchLogsRoleArn</code>.</p>
            cloud_watch_logs_role_arn: <p>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. You must use a role that exists in your account.</p>
            kms_key_id: <p>Specifies the KMS key ID to use to encrypt the logs and digest files delivered by CloudTrail. The value can be an alias name prefixed by \"alias/\", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html\">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p>alias/MyAliasName</p> </li> <li> <p>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</p> </li> <li> <p>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</p> </li> <li> <p>12345678-1234-1234-1234-123456789012</p> </li> </ul>
            is_organization_trail: <p>Specifies whether the trail is applied to all accounts in an organization in Organizations, or only for the current Amazon Web Services account. The default is false, and cannot be true unless the call is made on behalf of an Amazon Web Services account that is the management account for an organization in Organizations. If the trail is not an organization trail and this is set to <code>true</code>, the trail will be created in all Amazon Web Services accounts that belong to the organization. If the trail is an organization trail and this is set to <code>false</code>, the trail will remain in the current Amazon Web Services account but be deleted from all member accounts in the organization.</p> <note> <p>Only the management account for the organization can convert an organization trail to a non-organization trail, or convert a non-organization trail to an organization trail.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_cloudtrail.types.update_trail_request.UpdateTrailRequest]",
        ) -> OperationResponse[
            "aws_sdk_cloudtrail.types.update_trail_response.UpdateTrailResponse"
        ]:
            import aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_trail

            output, http_response = (
                aws_sdk_cloudtrail._operations.cloud_trail_20131101.update_trail.update_trail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_cloudtrail.types.update_trail_request.UpdateTrailRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if s3_bucket_name is not None:
            input_["s3_bucket_name"] = s3_bucket_name
        if s3_key_prefix is not None:
            input_["s3_key_prefix"] = s3_key_prefix
        if sns_topic_name is not None:
            input_["sns_topic_name"] = sns_topic_name
        if include_global_service_events is not None:
            input_["include_global_service_events"] = include_global_service_events
        if is_multi_region_trail is not None:
            input_["is_multi_region_trail"] = is_multi_region_trail
        if enable_log_file_validation is not None:
            input_["enable_log_file_validation"] = enable_log_file_validation
        if cloud_watch_logs_log_group_arn is not None:
            input_["cloud_watch_logs_log_group_arn"] = cloud_watch_logs_log_group_arn
        if cloud_watch_logs_role_arn is not None:
            input_["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if is_organization_trail is not None:
            input_["is_organization_trail"] = is_organization_trail

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
