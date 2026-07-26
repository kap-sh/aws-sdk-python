"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ApplicationSignals``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_application_signals._auth._signers
import capo_application_signals._auth._sigv4
from capo_application_signals._auth._identity import Credentials
from capo_application_signals._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_application_signals._auth._zapros_handler import AuthMiddleware
from capo_application_signals._pagination import resolve_path as _resolve_path
from capo_application_signals._resources.application_signals.service_level_objective_resource import (
    ServiceLevelObjectiveResource,
)
from capo_application_signals._services._aws_config import aws_config
from capo_application_signals._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_application_signals.types.amazon_resource_name
    import capo_application_signals.types.attribute_filters
    import capo_application_signals.types.attributes
    import capo_application_signals.types.audit_targets
    import capo_application_signals.types.auditors
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.batch_get_service_level_objective_budget_report_input
    import capo_application_signals.types.batch_get_service_level_objective_budget_report_output
    import capo_application_signals.types.batch_update_exclusion_windows_input
    import capo_application_signals.types.batch_update_exclusion_windows_output
    import capo_application_signals.types.change_event
    import capo_application_signals.types.delete_grouping_configuration_output
    import capo_application_signals.types.detail_level
    import capo_application_signals.types.exclusion_window
    import capo_application_signals.types.exclusion_windows
    import capo_application_signals.types.get_service_input
    import capo_application_signals.types.get_service_output
    import capo_application_signals.types.grouping_attribute_definitions
    import capo_application_signals.types.list_audit_finding_max_results
    import capo_application_signals.types.list_audit_findings_input
    import capo_application_signals.types.list_audit_findings_output
    import capo_application_signals.types.list_entity_events_input
    import capo_application_signals.types.list_entity_events_max_results
    import capo_application_signals.types.list_entity_events_output
    import capo_application_signals.types.list_grouping_attribute_definitions_input
    import capo_application_signals.types.list_grouping_attribute_definitions_output
    import capo_application_signals.types.list_service_dependencies_input
    import capo_application_signals.types.list_service_dependencies_max_results
    import capo_application_signals.types.list_service_dependencies_output
    import capo_application_signals.types.list_service_dependents_input
    import capo_application_signals.types.list_service_dependents_max_results
    import capo_application_signals.types.list_service_dependents_output
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_input
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_output
    import capo_application_signals.types.list_service_operation_max_results
    import capo_application_signals.types.list_service_operations_input
    import capo_application_signals.types.list_service_operations_output
    import capo_application_signals.types.list_service_states_input
    import capo_application_signals.types.list_service_states_max_results
    import capo_application_signals.types.list_service_states_output
    import capo_application_signals.types.list_services_input
    import capo_application_signals.types.list_services_max_results
    import capo_application_signals.types.list_services_output
    import capo_application_signals.types.list_tags_for_resource_request
    import capo_application_signals.types.list_tags_for_resource_response
    import capo_application_signals.types.next_token
    import capo_application_signals.types.put_grouping_configuration_input
    import capo_application_signals.types.put_grouping_configuration_output
    import capo_application_signals.types.service_dependency
    import capo_application_signals.types.service_dependent
    import capo_application_signals.types.service_level_objective_id
    import capo_application_signals.types.service_level_objective_ids
    import capo_application_signals.types.service_operation
    import capo_application_signals.types.service_state
    import capo_application_signals.types.service_summary
    import capo_application_signals.types.start_discovery_input
    import capo_application_signals.types.start_discovery_output
    import capo_application_signals.types.tag_key_list
    import capo_application_signals.types.tag_list
    import capo_application_signals.types.tag_resource_request
    import capo_application_signals.types.tag_resource_response
    import capo_application_signals.types.untag_resource_request
    import capo_application_signals.types.untag_resource_response


class ApplicationSignalsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ApplicationSignalsClient:
    """A client for the ``ApplicationSignals`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = ApplicationSignalsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.service_level_objective_resource = ServiceLevelObjectiveResource(self)

    def operation_options(
        self, config_overrides: Optional[ApplicationSignalsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApplicationSignalsClientConfig = config_overrides or {}
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

    def batch_get_service_level_objective_budget_report(
        self,
        timestamp: datetime.datetime,
        slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.batch_get_service_level_objective_budget_report_output.BatchGetServiceLevelObjectiveBudgetReportOutput":
        r"""<p>Use this operation to retrieve one or more <i>service level objective (SLO) budget reports</i>.</p> <p>An <i>error budget</i> is the amount of time or requests in an unhealthy state that your service can accumulate during an interval before your overall SLO budget health is breached and the SLO is considered to be unmet. For example, an SLO with a threshold of 99.95% and a monthly interval translates to an error budget of 21.9 minutes of downtime in a 30-day month.</p> <p>Budget reports include a health indicator, the attainment value, and remaining budget.</p> <p>For more information about SLO error budgets, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-concepts\"> SLO concepts</a>.</p>

        Args:
            timestamp: <p>The date and time that you want the report to be for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>
            slo_ids: <p>An array containing the IDs of the service level objectives that you want to include in the report.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.batch_get_service_level_objective_budget_report_input.BatchGetServiceLevelObjectiveBudgetReportInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.batch_get_service_level_objective_budget_report_output.BatchGetServiceLevelObjectiveBudgetReportOutput"
        ]:
            import capo_application_signals._operations.application_signals.batch_get_service_level_objective_budget_report

            output, http_response = (
                capo_application_signals._operations.application_signals.batch_get_service_level_objective_budget_report.batch_get_service_level_objective_budget_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.batch_get_service_level_objective_budget_report_input.BatchGetServiceLevelObjectiveBudgetReportInput = {}  # type: ignore[typeddict-item]
        input_["timestamp"] = timestamp
        input_["slo_ids"] = slo_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_exclusion_windows(
        self,
        slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        add_exclusion_windows: Optional[
            "capo_application_signals.types.exclusion_windows.ExclusionWindows"
        ] = None,
        remove_exclusion_windows: Optional[
            "capo_application_signals.types.exclusion_windows.ExclusionWindows"
        ] = None,
    ) -> "capo_application_signals.types.batch_update_exclusion_windows_output.BatchUpdateExclusionWindowsOutput":
        """<p>Add or remove time window exclusions for one or more Service Level Objectives (SLOs).</p>

        Args:
            slo_ids: <p>The list of SLO IDs to add or remove exclusion windows from.</p>
            add_exclusion_windows: <p>A list of exclusion windows to add to the specified SLOs. You can add up to 10 exclusion windows per SLO.</p>
            remove_exclusion_windows: <p>A list of exclusion windows to remove from the specified SLOs. The window configuration must match an existing exclusion window.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.batch_update_exclusion_windows_input.BatchUpdateExclusionWindowsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.batch_update_exclusion_windows_output.BatchUpdateExclusionWindowsOutput"
        ]:
            import capo_application_signals._operations.application_signals.batch_update_exclusion_windows

            output, http_response = (
                capo_application_signals._operations.application_signals.batch_update_exclusion_windows.batch_update_exclusion_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.batch_update_exclusion_windows_input.BatchUpdateExclusionWindowsInput = {}  # type: ignore[typeddict-item]
        input_["slo_ids"] = slo_ids
        if add_exclusion_windows is not None:
            input_["add_exclusion_windows"] = add_exclusion_windows
        if remove_exclusion_windows is not None:
            input_["remove_exclusion_windows"] = remove_exclusion_windows

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_grouping_configuration(
        self, *, config_overrides: Optional[ApplicationSignalsClientConfig] = None
    ) -> "capo_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput":
        """<p>Deletes the grouping configuration for this account. This removes all custom grouping attribute definitions that were previously configured.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput"
        ]:
            import capo_application_signals._operations.application_signals.delete_grouping_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.delete_grouping_configuration.delete_grouping_configuration(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_service(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.get_service_output.GetServiceOutput":
        """<p>Returns information about a service discovered by Application Signals.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.get_service_input.GetServiceInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.get_service_output.GetServiceOutput"
        ]:
            import capo_application_signals._operations.application_signals.get_service

            output, http_response = (
                capo_application_signals._operations.application_signals.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.get_service_input.GetServiceInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["key_attributes"] = key_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_audit_findings(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        audit_targets: "capo_application_signals.types.audit_targets.AuditTargets",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        auditors: Optional["capo_application_signals.types.auditors.Auditors"] = None,
        detail_level: Optional[
            "capo_application_signals.types.detail_level.DetailLevel"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_application_signals.types.list_audit_finding_max_results.ListAuditFindingMaxResults"
        ] = None,
    ) -> "capo_application_signals.types.list_audit_findings_output.ListAuditFindingsOutput":
        """<p>Returns a list of audit findings that provide automated analysis of service behavior and root cause analysis. These findings help identify the most significant observations about your services, including performance issues, anomalies, and potential problems. The findings are generated using heuristic algorithms based on established troubleshooting patterns.</p>

        Args:
            start_time: <p>The start of the time period to retrieve audit findings for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>
            end_time: <p>The end of the time period to retrieve audit findings for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>
            auditors: <p>A list of auditor names to filter the findings by. Only findings generated by the specified auditors will be returned.</p> <p>The following auditors are available for configuration:</p> <ul> <li> <p> <code>slo</code> - SloAuditor: Identifies SLO violations and detects breached thresholds during the Assessment phase.</p> </li> <li> <p> <code>operation_metric</code> - OperationMetricAuditor: Detects anomalies in service operation metrics from Application Signals RED metrics during the Assessment phase</p> <note> <p>Anomaly detection is not supported for sparse metrics (those missing more than 80% of datapoints within the given time period).</p> </note> </li> <li> <p> <code>service_quota</code> - ServiceQuotaAuditor: Monitors resource utilization against service quotas during the Assessment phase</p> </li> <li> <p> <code>trace</code> - TraceAuditor: Performs deep-dive analysis of distributed traces, correlating traces with breached SLOs or abnormal RED metrics during the Analysis phase</p> </li> <li> <p> <code>dependency_metric</code> - CriticalPathAuditor: Analyzes service dependency impacts and maps dependency relationships from Application Signals RED metrics during the Analysis phase</p> </li> <li> <p> <code>top_contributor</code> - TopContributorAuditor: Identifies infrastructure-level contributors to issues by analyzing EMF logs of Application Signals RED metrics during the Analysis phase</p> </li> <li> <p> <code>log</code> - LogAuditor: Extracts insights from application logs, categorizing error types and ranking severity by frequency during the Analysis phase</p> </li> <li> <p> <code>change_indicator</code> - ChangeIndicatorAuditor: Detects change events (deployments, configuration changes) that occurred within 10 minutes before and during a detected anomaly, and surfaces them as findings with deployment timestamps in the Analysis phase. When changes are detected, the <code>top_contributor</code> auditor skips its analysis to avoid redundancy.</p> </li> </ul> <note> <p> <code>InitAuditor</code> and <code>Summarizer</code> auditors are not configurable as they are automatically triggered during the audit process.</p> </note>
            audit_targets: <p>A list of audit targets to filter the findings by. You can specify services, SLOs, or service operations to limit the audit findings to specific entities.</p>
            detail_level: <p>The level of details of the audit findings. Supported values: <code>BRIEF</code>, <code>DETAILED</code>.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of audit findings.</p>
            max_results: <p>The maximum number of audit findings to return in one operation. If you omit this parameter, the default of 10 is used.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_audit_findings_input.ListAuditFindingsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_audit_findings_output.ListAuditFindingsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_audit_findings

            output, http_response = (
                capo_application_signals._operations.application_signals.list_audit_findings.list_audit_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_audit_findings_input.ListAuditFindingsInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if auditors is not None:
            input_["auditors"] = auditors
        input_["audit_targets"] = audit_targets
        if detail_level is not None:
            input_["detail_level"] = detail_level
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

    def list_entity_events(
        self,
        entity: "capo_application_signals.types.attributes.Attributes",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_entity_events_max_results.ListEntityEventsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_entity_events_output.ListEntityEventsOutput":
        r"""<p>Returns a list of change events for a specific entity, such as deployments, configuration changes, or other state-changing activities. This operation helps track the history of changes that may have affected service performance.</p>

        Args:
            entity: <p>The entity for which to retrieve change events. This specifies the service, resource, or other entity whose event history you want to examine.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> <li> <p> <code>AwsAccountId</code> specifies the account where this object is in.</p> </li> </ul> <p>Below is an example of a service.</p> <p> <code>{ \"Type\": \"Service\", \"Name\": \"visits-service\", \"Environment\": \"petclinic-test\" }</code> </p> <p>Below is an example of a resource.</p> <p> <code>{ \"Type\": \"AWS::Resource\", \"ResourceType\": \"AWS::DynamoDB::Table\", \"Identifier\": \"Customers\" }</code> </p>
            start_time: <p>The start of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>
            end_time: <p>The end of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>
            max_results: <p>The maximum number of change events to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of change events.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_entity_events_input.ListEntityEventsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_entity_events_output.ListEntityEventsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_entity_events

            output, http_response = (
                capo_application_signals._operations.application_signals.list_entity_events.list_entity_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_entity_events_input.ListEntityEventsInput = {}  # type: ignore[typeddict-item]
        input_["entity"] = entity
        input_["start_time"] = start_time
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

    def iter_list_entity_events(
        self,
        entity: "capo_application_signals.types.attributes.Attributes",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_entity_events_max_results.ListEntityEventsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.change_event.ChangeEvent]":
        _token = next_token
        while True:
            _response = self.list_entity_events(
                entity,
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("change_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_grouping_attribute_definitions(
        self,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
    ) -> "capo_application_signals.types.list_grouping_attribute_definitions_output.ListGroupingAttributeDefinitionsOutput":
        """<p>Returns the current grouping configuration for this account, including all custom grouping attribute definitions that have been configured. These definitions determine how services are logically grouped based on telemetry attributes, Amazon Web Services tags, or predefined mappings.</p>

        Args:
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of grouping attribute definitions.</p>
            aws_account_id: <p>The Amazon Web Services account ID to retrieve grouping attribute definitions for. Use this when accessing grouping configurations from a different account in cross-account monitoring scenarios.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include grouping attributes from source accounts in the returned data.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_grouping_attribute_definitions_input.ListGroupingAttributeDefinitionsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_grouping_attribute_definitions_output.ListGroupingAttributeDefinitionsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_grouping_attribute_definitions

            output, http_response = (
                capo_application_signals._operations.application_signals.list_grouping_attribute_definitions.list_grouping_attribute_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_grouping_attribute_definitions_input.ListGroupingAttributeDefinitionsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_service_dependencies(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependencies_max_results.ListServiceDependenciesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_dependencies_output.ListServiceDependenciesOutput":
        """<p>Returns a list of service dependencies of the service that you specify. A dependency is an infrastructure component that an operation of this service connects with. Dependencies can include Amazon Web Services services, Amazon Web Services resources, and third-party services. </p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested end time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service dependencies.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_dependencies_input.ListServiceDependenciesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_dependencies_output.ListServiceDependenciesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_dependencies

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_dependencies.list_service_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_dependencies_input.ListServiceDependenciesInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["key_attributes"] = key_attributes
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

    def iter_list_service_dependencies(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependencies_max_results.ListServiceDependenciesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> (
        "Iterator[capo_application_signals.types.service_dependency.ServiceDependency]"
    ):
        _token = next_token
        while True:
            _response = self.list_service_dependencies(
                start_time,
                end_time,
                key_attributes,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_dependencies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_dependents(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependents_max_results.ListServiceDependentsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_dependents_output.ListServiceDependentsOutput":
        """<p>Returns the list of dependents that invoked the specified service during the provided time range. Dependents include other services, CloudWatch Synthetics canaries, and clients that are instrumented with CloudWatch RUM app monitors.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service dependents.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_dependents_input.ListServiceDependentsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_dependents_output.ListServiceDependentsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_dependents

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_dependents.list_service_dependents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_dependents_input.ListServiceDependentsInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["key_attributes"] = key_attributes
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

    def iter_list_service_dependents(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependents_max_results.ListServiceDependentsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_dependent.ServiceDependent]":
        _token = next_token
        while True:
            _response = self.list_service_dependents(
                start_time,
                end_time,
                key_attributes,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_dependents",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_level_objective_exclusion_windows(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results.ListServiceLevelObjectiveExclusionWindowsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_level_objective_exclusion_windows_output.ListServiceLevelObjectiveExclusionWindowsOutput":
        """<p>Retrieves all exclusion windows configured for a specific SLO.</p>

        Args:
            id: <p>The ID of the SLO to list exclusion windows for.</p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used. </p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives. </p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_level_objective_exclusion_windows_input.ListServiceLevelObjectiveExclusionWindowsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_level_objective_exclusion_windows_output.ListServiceLevelObjectiveExclusionWindowsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_level_objective_exclusion_windows

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_level_objective_exclusion_windows.list_service_level_objective_exclusion_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_level_objective_exclusion_windows_input.ListServiceLevelObjectiveExclusionWindowsInput = {}  # type: ignore[typeddict-item]
        input_["id"] = id
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

    def iter_list_service_level_objective_exclusion_windows(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results.ListServiceLevelObjectiveExclusionWindowsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.exclusion_window.ExclusionWindow]":
        _token = next_token
        while True:
            _response = self.list_service_level_objective_exclusion_windows(
                id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exclusion_windows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_operations(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_operation_max_results.ListServiceOperationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_operations_output.ListServiceOperationsOutput":
        """<p>Returns a list of the <i>operations</i> of this service that have been discovered by Application Signals. Only the operations that were invoked during the specified time range are returned.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested end time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service operations.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_operations_input.ListServiceOperationsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_operations_output.ListServiceOperationsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_operations

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_operations.list_service_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_operations_input.ListServiceOperationsInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        input_["key_attributes"] = key_attributes
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

    def iter_list_service_operations(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_operation_max_results.ListServiceOperationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_operation.ServiceOperation]":
        _token = next_token
        while True:
            _response = self.list_service_operations(
                start_time,
                end_time,
                key_attributes,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_services_max_results.ListServicesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "capo_application_signals.types.list_services_output.ListServicesOutput":
        """<p>Returns a list of services that have been discovered by Application Signals. A service represents a minimum logical and transactional unit that completes a business function. Services are discovered through Application Signals instrumentation.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            max_results: <p> The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used. </p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of services.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include services from source accounts in the returned data. </p>
            aws_account_id: <p>Amazon Web Services Account ID.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_services_input.ListServicesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_services_output.ListServicesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_services

            output, http_response = (
                capo_application_signals._operations.application_signals.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_services_input.ListServicesInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_services(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_services_max_results.ListServicesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_services(
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_linked_accounts=include_linked_accounts,
                aws_account_id=aws_account_id,
            )
            _page = _resolve_path(_response, ("service_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_states(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_states_max_results.ListServiceStatesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        attribute_filters: Optional[
            "capo_application_signals.types.attribute_filters.AttributeFilters"
        ] = None,
    ) -> "capo_application_signals.types.list_service_states_output.ListServiceStatesOutput":
        """<p>Returns information about the last deployment and other change states of services. This API provides visibility into recent changes that may have affected service performance, helping with troubleshooting and change correlation.</p>

        Args:
            start_time: <p>The start of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>
            end_time: <p>The end of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>
            max_results: <p>The maximum number of service states to return in one operation. If you omit this parameter, the default of 20 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service states.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include service states from source accounts in the returned data.</p>
            aws_account_id: <p>The Amazon Web Services account ID to filter service states by. Use this to limit results to services from a specific account.</p>
            attribute_filters: <p>A list of attribute filters to narrow down the services. You can filter by platform, environment, or other service attributes.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_states_input.ListServiceStatesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_states_output.ListServiceStatesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_states

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_states.list_service_states(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_states_input.ListServiceStatesInput = {}  # type: ignore[typeddict-item]
        input_["start_time"] = start_time
        input_["end_time"] = end_time
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if attribute_filters is not None:
            input_["attribute_filters"] = attribute_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_service_states(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_states_max_results.ListServiceStatesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        attribute_filters: Optional[
            "capo_application_signals.types.attribute_filters.AttributeFilters"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_state.ServiceState]":
        _token = next_token
        while True:
            _response = self.list_service_states(
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_linked_accounts=include_linked_accounts,
                aws_account_id=aws_account_id,
                attribute_filters=attribute_filters,
            )
            _page = _resolve_path(_response, ("service_states",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_application_signals.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Displays the tags associated with a CloudWatch resource. Tags can be assigned to service level objectives.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to view tags for.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_application_signals._operations.application_signals.list_tags_for_resource

            output, http_response = (
                capo_application_signals._operations.application_signals.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_grouping_configuration(
        self,
        grouping_attribute_definitions: "capo_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.put_grouping_configuration_output.PutGroupingConfigurationOutput":
        """<p>Creates or updates the grouping configuration for this account. This operation allows you to define custom grouping attributes that determine how services are logically grouped based on telemetry attributes, Amazon Web Services tags, or predefined mappings. These grouping attributes can then be used to organize and filter services in the Application Signals console and APIs.</p>

        Args:
            grouping_attribute_definitions: <p>An array of grouping attribute definitions that specify how services should be grouped. Each definition includes a friendly name, source keys to derive the grouping value from, and an optional default value.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.put_grouping_configuration_input.PutGroupingConfigurationInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.put_grouping_configuration_output.PutGroupingConfigurationOutput"
        ]:
            import capo_application_signals._operations.application_signals.put_grouping_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.put_grouping_configuration.put_grouping_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.put_grouping_configuration_input.PutGroupingConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["grouping_attribute_definitions"] = grouping_attribute_definitions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_discovery(
        self, *, config_overrides: Optional[ApplicationSignalsClientConfig] = None
    ) -> "capo_application_signals.types.start_discovery_output.StartDiscoveryOutput":
        r"""<p>Enables this Amazon Web Services account to be able to use CloudWatch Application Signals by creating the <i>AWSServiceRoleForCloudWatchApplicationSignals</i> service-linked role. This service- linked role has the following permissions:</p> <ul> <li> <p> <code>xray:GetServiceGraph</code> </p> </li> <li> <p> <code>logs:StartQuery</code> </p> </li> <li> <p> <code>logs:GetQueryResults</code> </p> </li> <li> <p> <code>cloudwatch:GetMetricData</code> </p> </li> <li> <p> <code>cloudwatch:ListMetrics</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>autoscaling:DescribeAutoScalingGroups</code> </p> </li> </ul> <p>A service-linked CloudTrail event channel is created to process CloudTrail events and return change event information. This includes last deployment time, userName, eventName, and other event metadata.</p> <p>After completing this step, you still need to instrument your Java and Python applications to send data to Application Signals. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html\"> Enabling Application Signals</a>.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.start_discovery_input.StartDiscoveryInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.start_discovery_output.StartDiscoveryOutput"
        ]:
            import capo_application_signals._operations.application_signals.start_discovery

            output, http_response = (
                capo_application_signals._operations.application_signals.start_discovery.start_discovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.start_discovery_input.StartDiscoveryInput = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_application_signals.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_application_signals.types.tag_list.TagList",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.tag_resource_response.TagResourceResponse":
        r"""<p>Assigns one or more tags (key-value pairs) to the specified CloudWatch resource, such as a service level objective.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with an alarm that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a CloudWatch resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to set tags for.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>The list of key-value pairs to associate with the alarm.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_application_signals._operations.application_signals.tag_resource

            output, http_response = (
                capo_application_signals._operations.application_signals.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_application_signals.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_application_signals.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to delete tags from.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_application_signals._operations.application_signals.untag_resource

            output, http_response = (
                capo_application_signals._operations.application_signals.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
