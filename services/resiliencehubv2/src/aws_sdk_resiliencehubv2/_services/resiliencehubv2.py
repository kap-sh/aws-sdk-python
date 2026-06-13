"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#NGRHServiceCore``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_resiliencehubv2._auth._signers
import aws_sdk_resiliencehubv2._auth._sigv4
from aws_sdk_resiliencehubv2._auth._identity import Credentials
from aws_sdk_resiliencehubv2._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_resiliencehubv2._auth._zapros_handler import AuthMiddleware
from aws_sdk_resiliencehubv2._pagination import resolve_path as _resolve_path
from aws_sdk_resiliencehubv2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.account_id
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.assertion
    import aws_sdk_resiliencehubv2.types.assertion_source
    import aws_sdk_resiliencehubv2.types.assertion_text
    import aws_sdk_resiliencehubv2.types.assessment_status
    import aws_sdk_resiliencehubv2.types.assessment_summary
    import aws_sdk_resiliencehubv2.types.associated_system_list
    import aws_sdk_resiliencehubv2.types.availability_slo
    import aws_sdk_resiliencehubv2.types.aws_region
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.create_assertion_request
    import aws_sdk_resiliencehubv2.types.create_assertion_response
    import aws_sdk_resiliencehubv2.types.create_input_source_request
    import aws_sdk_resiliencehubv2.types.create_input_source_response
    import aws_sdk_resiliencehubv2.types.create_policy_request
    import aws_sdk_resiliencehubv2.types.create_policy_response
    import aws_sdk_resiliencehubv2.types.create_report_request
    import aws_sdk_resiliencehubv2.types.create_report_response
    import aws_sdk_resiliencehubv2.types.create_service_function_request
    import aws_sdk_resiliencehubv2.types.create_service_function_resources_request
    import aws_sdk_resiliencehubv2.types.create_service_function_resources_response
    import aws_sdk_resiliencehubv2.types.create_service_function_response
    import aws_sdk_resiliencehubv2.types.create_service_request
    import aws_sdk_resiliencehubv2.types.create_service_response
    import aws_sdk_resiliencehubv2.types.create_system_request
    import aws_sdk_resiliencehubv2.types.create_system_response
    import aws_sdk_resiliencehubv2.types.create_user_journey_request
    import aws_sdk_resiliencehubv2.types.create_user_journey_response
    import aws_sdk_resiliencehubv2.types.data_recovery_targets
    import aws_sdk_resiliencehubv2.types.delete_assertion_request
    import aws_sdk_resiliencehubv2.types.delete_assertion_response
    import aws_sdk_resiliencehubv2.types.delete_input_source_request
    import aws_sdk_resiliencehubv2.types.delete_input_source_response
    import aws_sdk_resiliencehubv2.types.delete_policy_request
    import aws_sdk_resiliencehubv2.types.delete_policy_response
    import aws_sdk_resiliencehubv2.types.delete_service_function_request
    import aws_sdk_resiliencehubv2.types.delete_service_function_resources_request
    import aws_sdk_resiliencehubv2.types.delete_service_function_resources_response
    import aws_sdk_resiliencehubv2.types.delete_service_function_response
    import aws_sdk_resiliencehubv2.types.delete_service_request
    import aws_sdk_resiliencehubv2.types.delete_service_response
    import aws_sdk_resiliencehubv2.types.delete_system_request
    import aws_sdk_resiliencehubv2.types.delete_system_response
    import aws_sdk_resiliencehubv2.types.delete_user_journey_request
    import aws_sdk_resiliencehubv2.types.delete_user_journey_response
    import aws_sdk_resiliencehubv2.types.dependency_criticality
    import aws_sdk_resiliencehubv2.types.dependency_discovery_input
    import aws_sdk_resiliencehubv2.types.dependency_summary
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.entity_id
    import aws_sdk_resiliencehubv2.types.entity_label
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.failure_category
    import aws_sdk_resiliencehubv2.types.finding_severity
    import aws_sdk_resiliencehubv2.types.finding_status
    import aws_sdk_resiliencehubv2.types.finding_summary
    import aws_sdk_resiliencehubv2.types.get_failure_mode_finding_request
    import aws_sdk_resiliencehubv2.types.get_failure_mode_finding_response
    import aws_sdk_resiliencehubv2.types.get_policy_request
    import aws_sdk_resiliencehubv2.types.get_policy_response
    import aws_sdk_resiliencehubv2.types.get_service_request
    import aws_sdk_resiliencehubv2.types.get_service_response
    import aws_sdk_resiliencehubv2.types.get_system_request
    import aws_sdk_resiliencehubv2.types.get_system_response
    import aws_sdk_resiliencehubv2.types.get_user_journey_request
    import aws_sdk_resiliencehubv2.types.get_user_journey_response
    import aws_sdk_resiliencehubv2.types.import_app_request
    import aws_sdk_resiliencehubv2.types.import_app_response
    import aws_sdk_resiliencehubv2.types.import_policy_request
    import aws_sdk_resiliencehubv2.types.import_policy_response
    import aws_sdk_resiliencehubv2.types.input_source_id
    import aws_sdk_resiliencehubv2.types.input_source_summary
    import aws_sdk_resiliencehubv2.types.input_source_type
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.list_assertions_request
    import aws_sdk_resiliencehubv2.types.list_assertions_response
    import aws_sdk_resiliencehubv2.types.list_dependencies_request
    import aws_sdk_resiliencehubv2.types.list_dependencies_response
    import aws_sdk_resiliencehubv2.types.list_failure_mode_assessments_request
    import aws_sdk_resiliencehubv2.types.list_failure_mode_assessments_response
    import aws_sdk_resiliencehubv2.types.list_failure_mode_findings_request
    import aws_sdk_resiliencehubv2.types.list_failure_mode_findings_response
    import aws_sdk_resiliencehubv2.types.list_input_sources_request
    import aws_sdk_resiliencehubv2.types.list_input_sources_response
    import aws_sdk_resiliencehubv2.types.list_policies_request
    import aws_sdk_resiliencehubv2.types.list_policies_response
    import aws_sdk_resiliencehubv2.types.list_reports_request
    import aws_sdk_resiliencehubv2.types.list_reports_response
    import aws_sdk_resiliencehubv2.types.list_resources_request
    import aws_sdk_resiliencehubv2.types.list_resources_response
    import aws_sdk_resiliencehubv2.types.list_service_events_request
    import aws_sdk_resiliencehubv2.types.list_service_events_response
    import aws_sdk_resiliencehubv2.types.list_service_functions_request
    import aws_sdk_resiliencehubv2.types.list_service_functions_response
    import aws_sdk_resiliencehubv2.types.list_service_topology_edges_request
    import aws_sdk_resiliencehubv2.types.list_service_topology_edges_response
    import aws_sdk_resiliencehubv2.types.list_services_request
    import aws_sdk_resiliencehubv2.types.list_services_response
    import aws_sdk_resiliencehubv2.types.list_system_events_request
    import aws_sdk_resiliencehubv2.types.list_system_events_response
    import aws_sdk_resiliencehubv2.types.list_systems_request
    import aws_sdk_resiliencehubv2.types.list_systems_response
    import aws_sdk_resiliencehubv2.types.list_tags_for_resource_request
    import aws_sdk_resiliencehubv2.types.list_tags_for_resource_response
    import aws_sdk_resiliencehubv2.types.list_user_journeys_request
    import aws_sdk_resiliencehubv2.types.list_user_journeys_response
    import aws_sdk_resiliencehubv2.types.long_description
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach
    import aws_sdk_resiliencehubv2.types.multi_az_targets
    import aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach
    import aws_sdk_resiliencehubv2.types.multi_region_targets
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.ou_id
    import aws_sdk_resiliencehubv2.types.permission_model
    import aws_sdk_resiliencehubv2.types.policy_summary
    import aws_sdk_resiliencehubv2.types.query_granularity
    import aws_sdk_resiliencehubv2.types.region_list
    import aws_sdk_resiliencehubv2.types.report_generation_result
    import aws_sdk_resiliencehubv2.types.report_type
    import aws_sdk_resiliencehubv2.types.resource_configuration
    import aws_sdk_resiliencehubv2.types.resource_list
    import aws_sdk_resiliencehubv2.types.service_event
    import aws_sdk_resiliencehubv2.types.service_event_type_list
    import aws_sdk_resiliencehubv2.types.service_function
    import aws_sdk_resiliencehubv2.types.service_function_criticality
    import aws_sdk_resiliencehubv2.types.service_report_configuration
    import aws_sdk_resiliencehubv2.types.service_resource
    import aws_sdk_resiliencehubv2.types.service_summary
    import aws_sdk_resiliencehubv2.types.service_topology_edge_summary
    import aws_sdk_resiliencehubv2.types.start_failure_mode_assessment_request
    import aws_sdk_resiliencehubv2.types.start_failure_mode_assessment_response
    import aws_sdk_resiliencehubv2.types.system_event
    import aws_sdk_resiliencehubv2.types.system_event_type_list
    import aws_sdk_resiliencehubv2.types.system_summary
    import aws_sdk_resiliencehubv2.types.tag_key_list
    import aws_sdk_resiliencehubv2.types.tag_map
    import aws_sdk_resiliencehubv2.types.tag_resource_request
    import aws_sdk_resiliencehubv2.types.tag_resource_response
    import aws_sdk_resiliencehubv2.types.untag_resource_request
    import aws_sdk_resiliencehubv2.types.untag_resource_response
    import aws_sdk_resiliencehubv2.types.update_assertion_request
    import aws_sdk_resiliencehubv2.types.update_assertion_response
    import aws_sdk_resiliencehubv2.types.update_dependency_request
    import aws_sdk_resiliencehubv2.types.update_dependency_response
    import aws_sdk_resiliencehubv2.types.update_failure_mode_finding_request
    import aws_sdk_resiliencehubv2.types.update_failure_mode_finding_response
    import aws_sdk_resiliencehubv2.types.update_policy_request
    import aws_sdk_resiliencehubv2.types.update_policy_response
    import aws_sdk_resiliencehubv2.types.update_service_function_request
    import aws_sdk_resiliencehubv2.types.update_service_function_response
    import aws_sdk_resiliencehubv2.types.update_service_request
    import aws_sdk_resiliencehubv2.types.update_service_response
    import aws_sdk_resiliencehubv2.types.update_system_request
    import aws_sdk_resiliencehubv2.types.update_system_response
    import aws_sdk_resiliencehubv2.types.update_user_journey_request
    import aws_sdk_resiliencehubv2.types.update_user_journey_response
    import aws_sdk_resiliencehubv2.types.user_journey_id
    import aws_sdk_resiliencehubv2.types.user_journey_summary
    import aws_sdk_resiliencehubv2.types.uuid


class resiliencehubv2ClientConfig(TypedDict, total=False):
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


class resiliencehubv2Client:
    """A client for the ``resiliencehubv2`` service.

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
        self.config = resiliencehubv2ClientConfig(
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
        self, config_overrides: Optional[resiliencehubv2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: resiliencehubv2ClientConfig = config_overrides or {}
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

    def create_assertion(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        text: "aws_sdk_resiliencehubv2.types.assertion_text.AssertionText",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_assertion_response.CreateAssertionResponse":
        """<p>Creates a resilience assertion for a service.</p>

        Args:
            text: <p>The text content of the assertion.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_assertion_request.CreateAssertionRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_assertion_response.CreateAssertionResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_assertion

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_assertion.create_assertion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_assertion_request.CreateAssertionRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["text"] = text
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_input_source(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        resource_configuration: "aws_sdk_resiliencehubv2.types.resource_configuration.ResourceConfiguration",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_input_source_response.CreateInputSourceResponse":
        """<p>Creates an input source for a service.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_input_source_request.CreateInputSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_input_source_response.CreateInputSourceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_input_source

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_input_source.create_input_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_input_source_request.CreateInputSourceRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["resource_configuration"] = resource_configuration
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_policy(
        self,
        name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        availability_slo: Optional[
            "aws_sdk_resiliencehubv2.types.availability_slo.AvailabilitySlo"
        ] = None,
        multi_az: Optional[
            "aws_sdk_resiliencehubv2.types.multi_az_targets.MultiAzTargets"
        ] = None,
        multi_region: Optional[
            "aws_sdk_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
        ] = None,
        data_recovery: Optional[
            "aws_sdk_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
        ] = None,
        kms_key_id: Optional[
            "aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"
        ] = None,
        tags: Optional["aws_sdk_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_policy_response.CreatePolicyResponse":
        """<p>Creates a resilience policy that defines availability and disaster recovery requirements.</p>

        Args:
            availability_slo: <p>The availability SLO for the resilience policy.</p>
            multi_az: <p>The multi-AZ disaster recovery targets for the resilience policy.</p>
            multi_region: <p>The multi-Region disaster recovery targets for the resilience policy.</p>
            data_recovery: <p>The data recovery targets for the resilience policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_policy_request.CreatePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_policy_response.CreatePolicyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_policy

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_policy.create_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_policy_request.CreatePolicyRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if availability_slo is not None:
            input["availability_slo"] = availability_slo
        if multi_az is not None:
            input["multi_az"] = multi_az
        if multi_region is not None:
            input["multi_region"] = multi_region
        if data_recovery is not None:
            input["data_recovery"] = data_recovery
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_report(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        report_type: "aws_sdk_resiliencehubv2.types.report_type.ReportType",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_report_response.CreateReportResponse":
        """<p>On-demand report creation. Idempotent — duplicate requests with same clientToken return existing result.</p>

        Args:
            report_type: <p>The type of report to generate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_report_request.CreateReportRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_report_response.CreateReportResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_report

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_report.create_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_report_request.CreateReportRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["report_type"] = report_type
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_service(
        self,
        name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName",
        regions: "aws_sdk_resiliencehubv2.types.region_list.RegionList",
        permission_model: "aws_sdk_resiliencehubv2.types.permission_model.PermissionModel",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        associated_systems: Optional[
            "aws_sdk_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
        ] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        dependency_discovery: Optional[
            "aws_sdk_resiliencehubv2.types.dependency_discovery_input.DependencyDiscoveryInput"
        ] = None,
        report_configuration: Optional[
            "aws_sdk_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
        ] = None,
        kms_key_id: Optional[
            "aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"
        ] = None,
        tags: Optional["aws_sdk_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_service_response.CreateServiceResponse":
        """<p>Creates a service.</p>

        Args:
            associated_systems: <p>The systems to associate with the service.</p>
            regions: <p>The AWS Regions where the service operates.</p>
            permission_model: <p>The permission model for the service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_service_response.CreateServiceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_service

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_service_request.CreateServiceRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if associated_systems is not None:
            input["associated_systems"] = associated_systems
        if policy_arn is not None:
            input["policy_arn"] = policy_arn
        input["regions"] = regions
        input["permission_model"] = permission_model
        if dependency_discovery is not None:
            input["dependency_discovery"] = dependency_discovery
        if report_configuration is not None:
            input["report_configuration"] = report_configuration
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_service_function(
        self,
        name: "aws_sdk_resiliencehubv2.types.entity_label.EntityLabel",
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        criticality: "aws_sdk_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_service_function_response.CreateServiceFunctionResponse":
        """<p>Creates a service function within a service.</p>

        Args:
            criticality: <p>The criticality level of the service function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_service_function_request.CreateServiceFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_service_function_response.CreateServiceFunctionResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_service_function

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_service_function.create_service_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_service_function_request.CreateServiceFunctionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["service_arn"] = service_arn
        if description is not None:
            input["description"] = description
        input["criticality"] = criticality
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_service_function_resources(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId",
        resources: "aws_sdk_resiliencehubv2.types.resource_list.ResourceList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_service_function_resources_response.CreateServiceFunctionResourcesResponse":
        """<p>Associates resources with a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to associate resources with.</p>
            resources: <p>The list of resources to associate with the service function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_service_function_resources_request.CreateServiceFunctionResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_service_function_resources_response.CreateServiceFunctionResourcesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_service_function_resources

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_service_function_resources.create_service_function_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_service_function_resources_request.CreateServiceFunctionResourcesRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["service_function_id"] = service_function_id
        input["resources"] = resources

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_system(
        self,
        name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        sharing_enabled: Optional[bool] = None,
        kms_key_id: Optional[
            "aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"
        ] = None,
        tags: Optional["aws_sdk_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_system_response.CreateSystemResponse":
        """<p>Creates a system that represents a logical grouping of services.</p>

        Args:
            sharing_enabled: <p>Indicates whether cross-account sharing is enabled for the system.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_system_request.CreateSystemRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_system_response.CreateSystemResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_system

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_system.create_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_system_request.CreateSystemRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if description is not None:
            input["description"] = description
        if sharing_enabled is not None:
            input["sharing_enabled"] = sharing_enabled
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_user_journey(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        name: "aws_sdk_resiliencehubv2.types.entity_label.EntityLabel",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.create_user_journey_response.CreateUserJourneyResponse":
        """<p>Creates a user journey within a system.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.create_user_journey_request.CreateUserJourneyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.create_user_journey_response.CreateUserJourneyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_user_journey

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.create_user_journey.create_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.create_user_journey_request.CreateUserJourneyRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
        input["name"] = name
        if description is not None:
            input["description"] = description
        if policy_arn is not None:
            input["policy_arn"] = policy_arn
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_assertion(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        assertion_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_assertion_response.DeleteAssertionResponse":
        """<p>Deletes a resilience assertion from a service.</p>

        Args:
            assertion_id: <p>The unique identifier of the assertion to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_assertion_request.DeleteAssertionRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_assertion_response.DeleteAssertionResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_assertion

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_assertion.delete_assertion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_assertion_request.DeleteAssertionRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["assertion_id"] = assertion_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_input_source(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        input_source_id: "aws_sdk_resiliencehubv2.types.input_source_id.InputSourceId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_input_source_response.DeleteInputSourceResponse":
        """<p>Deletes an input source.</p>

        Args:
            input_source_id: <p>The identifier of the input source to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_input_source_request.DeleteInputSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_input_source_response.DeleteInputSourceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_input_source

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_input_source.delete_input_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_input_source_request.DeleteInputSourceRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["input_source_id"] = input_source_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_policy(
        self,
        policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_policy_response.DeletePolicyResponse":
        """<p>Deletes a resilience policy.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_policy_request.DeletePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_policy_response.DeletePolicyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_policy

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_policy_request.DeletePolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_arn"] = policy_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_service(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a service.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_service_response.DeleteServiceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_service

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_service_request.DeleteServiceRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_service_function(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_service_function_response.DeleteServiceFunctionResponse":
        """<p>Deletes a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_service_function_request.DeleteServiceFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_service_function_response.DeleteServiceFunctionResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_service_function

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_service_function.delete_service_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_service_function_request.DeleteServiceFunctionRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["service_function_id"] = service_function_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_service_function_resources(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId",
        resources: "aws_sdk_resiliencehubv2.types.resource_list.ResourceList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_service_function_resources_response.DeleteServiceFunctionResourcesResponse":
        """<p>Removes resources from a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to remove resources from.</p>
            resources: <p>The list of resources to remove from the service function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_service_function_resources_request.DeleteServiceFunctionResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_service_function_resources_response.DeleteServiceFunctionResourcesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_service_function_resources

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_service_function_resources.delete_service_function_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_service_function_resources_request.DeleteServiceFunctionResourcesRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["service_function_id"] = service_function_id
        input["resources"] = resources

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_system(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_system_response.DeleteSystemResponse":
        """<p>Deletes a system.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_system_request.DeleteSystemRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_system_response.DeleteSystemResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_system

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_system.delete_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_system_request.DeleteSystemRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_user_journey(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        user_journey_id: "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.delete_user_journey_response.DeleteUserJourneyResponse":
        """<p>Deletes a user journey.</p>

        Args:
            user_journey_id: <p>The identifier of the user journey to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.delete_user_journey_request.DeleteUserJourneyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.delete_user_journey_response.DeleteUserJourneyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_user_journey

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.delete_user_journey.delete_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.delete_user_journey_request.DeleteUserJourneyRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
        input["user_journey_id"] = user_journey_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_failure_mode_finding(
        self,
        finding_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid",
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.get_failure_mode_finding_response.GetFailureModeFindingResponse":
        """<p>Retrieves a finding by findingId.</p>

        Args:
            finding_id: <p>The unique identifier of the finding to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.get_failure_mode_finding_request.GetFailureModeFindingRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.get_failure_mode_finding_response.GetFailureModeFindingResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_failure_mode_finding

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_failure_mode_finding.get_failure_mode_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.get_failure_mode_finding_request.GetFailureModeFindingRequest = {}  # type: ignore[typeddict-item]
        input["finding_id"] = finding_id
        input["service_arn"] = service_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_policy(
        self,
        policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves a resilience policy by ARN.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.get_policy_response.GetPolicyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_policy

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.get_policy_request.GetPolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_arn"] = policy_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_service(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.get_service_response.GetServiceResponse":
        """<p>Retrieves a service by ARN.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.get_service_response.GetServiceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_service

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.get_service_request.GetServiceRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_system(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.get_system_response.GetSystemResponse":
        """<p>Retrieves a system by ARN.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.get_system_request.GetSystemRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.get_system_response.GetSystemResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_system

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_system.get_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.get_system_request.GetSystemRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_user_journey(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        user_journey_id: "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> (
        "aws_sdk_resiliencehubv2.types.get_user_journey_response.GetUserJourneyResponse"
    ):
        """<p>Retrieves a user journey.</p>

        Args:
            user_journey_id: <p>The identifier of the user journey to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.get_user_journey_request.GetUserJourneyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.get_user_journey_response.GetUserJourneyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_user_journey

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.get_user_journey.get_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.get_user_journey_request.GetUserJourneyRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
        input["user_journey_id"] = user_journey_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_app(
        self,
        v1_app_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        kms_key_id: Optional[
            "aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"
        ] = None,
        skip_manually_added_resources: Optional[bool] = None,
        associated_systems: Optional[
            "aws_sdk_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
        ] = None,
        tags: Optional["aws_sdk_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.import_app_response.ImportAppResponse":
        """<p>Imports a V1 app into the V2 resource model, creating a service with the same name.</p>

        Args:
            skip_manually_added_resources: <p>Whether to skip manually added resources during import.</p>
            associated_systems: <p>The systems to associate with the imported service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.import_app_request.ImportAppRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.import_app_response.ImportAppResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.import_app

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.import_app.import_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.import_app_request.ImportAppRequest = {}  # type: ignore[typeddict-item]
        input["v1_app_arn"] = v1_app_arn
        if policy_arn is not None:
            input["policy_arn"] = policy_arn
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if skip_manually_added_resources is not None:
            input["skip_manually_added_resources"] = skip_manually_added_resources
        if associated_systems is not None:
            input["associated_systems"] = associated_systems
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_policy(
        self,
        v1_policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        kms_key_id: Optional[
            "aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"
        ] = None,
        availability_slo: Optional[
            "aws_sdk_resiliencehubv2.types.availability_slo.AvailabilitySlo"
        ] = None,
        multi_az_disaster_recovery_approach: Optional[
            "aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.MultiAzDisasterRecoveryApproach"
        ] = None,
        multi_region_disaster_recovery_approach: Optional[
            "aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach.MultiRegionDisasterRecoveryApproach"
        ] = None,
        tags: Optional["aws_sdk_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.import_policy_response.ImportPolicyResponse":
        """<p>Imports a V1 policy into V2, mapping RTO/RPO values from V1 scenarios.</p>

        Args:
            availability_slo: <p>The availability SLO to set on the imported policy.</p>
            multi_az_disaster_recovery_approach: <p>The multi-AZ disaster recovery approach for the imported policy.</p>
            multi_region_disaster_recovery_approach: <p>The multi-Region disaster recovery approach for the imported policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.import_policy_request.ImportPolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.import_policy_response.ImportPolicyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.import_policy

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.import_policy.import_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.import_policy_request.ImportPolicyRequest = {}  # type: ignore[typeddict-item]
        input["v1_policy_arn"] = v1_policy_arn
        if kms_key_id is not None:
            input["kms_key_id"] = kms_key_id
        if availability_slo is not None:
            input["availability_slo"] = availability_slo
        if multi_az_disaster_recovery_approach is not None:
            input["multi_az_disaster_recovery_approach"] = (
                multi_az_disaster_recovery_approach
            )
        if multi_region_disaster_recovery_approach is not None:
            input["multi_region_disaster_recovery_approach"] = (
                multi_region_disaster_recovery_approach
            )
        if tags is not None:
            input["tags"] = tags
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_assertions(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        source: Optional[
            "aws_sdk_resiliencehubv2.types.assertion_source.AssertionSource"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> (
        "aws_sdk_resiliencehubv2.types.list_assertions_response.ListAssertionsResponse"
    ):
        """<p>Lists resilience assertions for a service.</p>

        Args:
            source: <p>Filter assertions by source type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_assertions_request.ListAssertionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_assertions_response.ListAssertionsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_assertions

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_assertions.list_assertions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_assertions_request.ListAssertionsRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if source is not None:
            input["source"] = source
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

    def iter_list_assertions(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        source: Optional[
            "aws_sdk_resiliencehubv2.types.assertion_source.AssertionSource"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.assertion.Assertion]":
        _token = next_token
        while True:
            _response = self.list_assertions(
                service_arn,
                config_overrides=config_overrides,
                source=source,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assertions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dependencies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        query_range_start_time: Optional[datetime.datetime] = None,
        query_range_end_time: Optional[datetime.datetime] = None,
        query_range_granularity: Optional[
            "aws_sdk_resiliencehubv2.types.query_granularity.QueryGranularity"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_dependencies_response.ListDependenciesResponse":
        """<p>Lists dependencies discovered for services.</p>

        Args:
            query_range_start_time: <p>The start time for the dependency query range.</p>
            query_range_end_time: <p>The end time for the dependency query range.</p>
            query_range_granularity: <p>The granularity for the dependency query range.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_dependencies_request.ListDependenciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_dependencies_response.ListDependenciesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_dependencies

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_dependencies.list_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_dependencies_request.ListDependenciesRequest = {}  # type: ignore[typeddict-item]
        if service_arn is not None:
            input["service_arn"] = service_arn
        if query_range_start_time is not None:
            input["query_range_start_time"] = query_range_start_time
        if query_range_end_time is not None:
            input["query_range_end_time"] = query_range_end_time
        if query_range_granularity is not None:
            input["query_range_granularity"] = query_range_granularity
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

    def iter_list_dependencies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        query_range_start_time: Optional[datetime.datetime] = None,
        query_range_end_time: Optional[datetime.datetime] = None,
        query_range_granularity: Optional[
            "aws_sdk_resiliencehubv2.types.query_granularity.QueryGranularity"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.dependency_summary.DependencySummary]":
        _token = next_token
        while True:
            _response = self.list_dependencies(
                config_overrides=config_overrides,
                service_arn=service_arn,
                query_range_start_time=query_range_start_time,
                query_range_end_time=query_range_end_time,
                query_range_granularity=query_range_granularity,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dependency_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_failure_mode_assessments(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_failure_mode_assessments_response.ListFailureModeAssessmentsResponse":
        """<p>Lists failure mode assessments.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_failure_mode_assessments_request.ListFailureModeAssessmentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_failure_mode_assessments_response.ListFailureModeAssessmentsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_assessments

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_assessments.list_failure_mode_assessments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_failure_mode_assessments_request.ListFailureModeAssessmentsRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
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

    def iter_list_failure_mode_assessments(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.assessment_summary.AssessmentSummary]":
        _token = next_token
        while True:
            _response = self.list_failure_mode_assessments(
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assessment_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_failure_mode_findings(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        severity: Optional[
            "aws_sdk_resiliencehubv2.types.finding_severity.FindingSeverity"
        ] = None,
        failure_category: Optional[
            "aws_sdk_resiliencehubv2.types.failure_category.FailureCategory"
        ] = None,
        status: Optional[
            "aws_sdk_resiliencehubv2.types.finding_status.FindingStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_failure_mode_findings_response.ListFailureModeFindingsResponse":
        """<p>List findings.</p>

        Args:
            severity: <p>Filter findings by severity.</p>
            failure_category: <p>Filter findings by failure category.</p>
            status: <p>Filter findings by status.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_failure_mode_findings_request.ListFailureModeFindingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_failure_mode_findings_response.ListFailureModeFindingsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_findings

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_findings.list_failure_mode_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_failure_mode_findings_request.ListFailureModeFindingsRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if severity is not None:
            input["severity"] = severity
        if failure_category is not None:
            input["failure_category"] = failure_category
        if status is not None:
            input["status"] = status
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

    def iter_list_failure_mode_findings(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        severity: Optional[
            "aws_sdk_resiliencehubv2.types.finding_severity.FindingSeverity"
        ] = None,
        failure_category: Optional[
            "aws_sdk_resiliencehubv2.types.failure_category.FailureCategory"
        ] = None,
        status: Optional[
            "aws_sdk_resiliencehubv2.types.finding_status.FindingStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.finding_summary.FindingSummary]":
        _token = next_token
        while True:
            _response = self.list_failure_mode_findings(
                service_arn,
                config_overrides=config_overrides,
                severity=severity,
                failure_category=failure_category,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("findings_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_sources(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "aws_sdk_resiliencehubv2.types.input_source_type.InputSourceType"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_input_sources_response.ListInputSourcesResponse":
        """<p>Lists input sources for a service.</p>

        Args:
            type: <p>Filter input sources by type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_input_sources_request.ListInputSourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_input_sources_response.ListInputSourcesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_input_sources

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_input_sources.list_input_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_input_sources_request.ListInputSourcesRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if type is not None:
            input["type"] = type
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

    def iter_list_input_sources(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "aws_sdk_resiliencehubv2.types.input_source_type.InputSourceType"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.input_source_summary.InputSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_input_sources(
                service_arn,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_source_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_policies_response.ListPoliciesResponse":
        """<p>Lists resilience policies.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_policies_request.ListPoliciesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_policies_response.ListPoliciesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_policies

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_policies_request.ListPoliciesRequest = {}  # type: ignore[typeddict-item]
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

    def iter_list_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.policy_summary.PolicySummary]":
        _token = next_token
        while True:
            _response = self.list_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_reports(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        report_type: Optional[
            "aws_sdk_resiliencehubv2.types.report_type.ReportType"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_reports_response.ListReportsResponse":
        """<p>List reports for a service, or all reports owned by the account if serviceArn is not provided.</p>

        Args:
            service_arn: <p>Optional. If not provided, lists all reports owned by the account.</p>
            report_type: <p>Filter reports by type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_reports_request.ListReportsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_reports_response.ListReportsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_reports

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_reports.list_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_reports_request.ListReportsRequest = {}  # type: ignore[typeddict-item]
        if service_arn is not None:
            input["service_arn"] = service_arn
        if report_type is not None:
            input["report_type"] = report_type
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

    def iter_list_reports(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        report_type: Optional[
            "aws_sdk_resiliencehubv2.types.report_type.ReportType"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.report_generation_result.ReportGenerationResult]":
        _token = next_token
        while True:
            _response = self.list_reports(
                config_overrides=config_overrides,
                service_arn=service_arn,
                report_type=report_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("report_generation_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resources(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_function_id: Optional[
            "aws_sdk_resiliencehubv2.types.entity_id.EntityId"
        ] = None,
        aws_region: Optional[
            "aws_sdk_resiliencehubv2.types.aws_region.AwsRegion"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_resources_response.ListResourcesResponse":
        """<p>List resources.</p>

        Args:
            service_function_id: <p>Filter resources by service function identifier.</p>
            aws_region: <p>Filter resources by AWS Region.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_resources_request.ListResourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_resources_response.ListResourcesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_resources

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_resources.list_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_resources_request.ListResourcesRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if service_function_id is not None:
            input["service_function_id"] = service_function_id
        if aws_region is not None:
            input["aws_region"] = aws_region
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

    def iter_list_resources(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_function_id: Optional[
            "aws_sdk_resiliencehubv2.types.entity_id.EntityId"
        ] = None,
        aws_region: Optional[
            "aws_sdk_resiliencehubv2.types.aws_region.AwsRegion"
        ] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.service_resource.ServiceResource]":
        _token = next_token
        while True:
            _response = self.list_resources(
                service_arn,
                config_overrides=config_overrides,
                service_function_id=service_function_id,
                aws_region=aws_region,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_events(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "aws_sdk_resiliencehubv2.types.service_event_type_list.ServiceEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_service_events_response.ListServiceEventsResponse":
        """<p>Lists events for a service.</p>

        Args:
            event_types: <p>Filter events by type.</p>
            start_time: <p>The start time for filtering events.</p>
            end_time: <p>The end time for filtering events.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_service_events_request.ListServiceEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_service_events_response.ListServiceEventsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_service_events

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_service_events.list_service_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_service_events_request.ListServiceEventsRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if event_types is not None:
            input["event_types"] = event_types
        if start_time is not None:
            input["start_time"] = start_time
        if end_time is not None:
            input["end_time"] = end_time
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

    def iter_list_service_events(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "aws_sdk_resiliencehubv2.types.service_event_type_list.ServiceEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.service_event.ServiceEvent]":
        _token = next_token
        while True:
            _response = self.list_service_events(
                service_arn,
                config_overrides=config_overrides,
                event_types=event_types,
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

    def list_service_functions(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_service_functions_response.ListServiceFunctionsResponse":
        """<p>Lists service functions for a service.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_service_functions_request.ListServiceFunctionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_service_functions_response.ListServiceFunctionsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_service_functions

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_service_functions.list_service_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_service_functions_request.ListServiceFunctionsRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
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

    def iter_list_service_functions(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.service_function.ServiceFunction]":
        _token = next_token
        while True:
            _response = self.list_service_functions(
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        system_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        user_journey_id: Optional[
            "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId"
        ] = None,
        ou_id: Optional["aws_sdk_resiliencehubv2.types.ou_id.OuId"] = None,
        account_id: Optional[
            "aws_sdk_resiliencehubv2.types.account_id.AccountId"
        ] = None,
        assessment_status: Optional[
            "aws_sdk_resiliencehubv2.types.assessment_status.AssessmentStatus"
        ] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_services_response.ListServicesResponse":
        """<p>Lists services.</p>

        Args:
            user_journey_id: <p>Filter services by user journey identifier.</p>
            ou_id: <p>Filter services by organizational unit (OU) identifier.</p>
            account_id: <p>Filter services by AWS account ID.</p>
            assessment_status: <p>Filter services by assessment status.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_services_response.ListServicesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_services

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_services_request.ListServicesRequest = {}  # type: ignore[typeddict-item]
        if system_arn is not None:
            input["system_arn"] = system_arn
        if user_journey_id is not None:
            input["user_journey_id"] = user_journey_id
        if ou_id is not None:
            input["ou_id"] = ou_id
        if account_id is not None:
            input["account_id"] = account_id
        if assessment_status is not None:
            input["assessment_status"] = assessment_status
        if policy_arn is not None:
            input["policy_arn"] = policy_arn
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

    def iter_list_services(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        system_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        user_journey_id: Optional[
            "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId"
        ] = None,
        ou_id: Optional["aws_sdk_resiliencehubv2.types.ou_id.OuId"] = None,
        account_id: Optional[
            "aws_sdk_resiliencehubv2.types.account_id.AccountId"
        ] = None,
        assessment_status: Optional[
            "aws_sdk_resiliencehubv2.types.assessment_status.AssessmentStatus"
        ] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_services(
                config_overrides=config_overrides,
                system_arn=system_arn,
                user_journey_id=user_journey_id,
                ou_id=ou_id,
                account_id=account_id,
                assessment_status=assessment_status,
                policy_arn=policy_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_topology_edges(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_service_topology_edges_response.ListServiceTopologyEdgesResponse":
        """<p>Lists topology edges for a service.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_service_topology_edges_request.ListServiceTopologyEdgesRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_service_topology_edges_response.ListServiceTopologyEdgesResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_service_topology_edges

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_service_topology_edges.list_service_topology_edges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_service_topology_edges_request.ListServiceTopologyEdgesRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
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

    def iter_list_service_topology_edges(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.service_topology_edge_summary.ServiceTopologyEdgeSummary]":
        _token = next_token
        while True:
            _response = self.list_service_topology_edges(
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_topology_edge_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_system_events(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "aws_sdk_resiliencehubv2.types.system_event_type_list.SystemEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_system_events_response.ListSystemEventsResponse":
        """<p>Lists events for a system.</p>

        Args:
            event_types: <p>Filter events by type.</p>
            start_time: <p>The start time for filtering events.</p>
            end_time: <p>The end time for filtering events.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_system_events_request.ListSystemEventsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_system_events_response.ListSystemEventsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_system_events

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_system_events.list_system_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_system_events_request.ListSystemEventsRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
        if event_types is not None:
            input["event_types"] = event_types
        if start_time is not None:
            input["start_time"] = start_time
        if end_time is not None:
            input["end_time"] = end_time
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

    def iter_list_system_events(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "aws_sdk_resiliencehubv2.types.system_event_type_list.SystemEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.system_event.SystemEvent]":
        _token = next_token
        while True:
            _response = self.list_system_events(
                system_arn,
                config_overrides=config_overrides,
                event_types=event_types,
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

    def list_systems(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        ou_id: Optional["aws_sdk_resiliencehubv2.types.ou_id.OuId"] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_systems_response.ListSystemsResponse":
        """<p>Lists systems.</p>

        Args:
            ou_id: <p>Filter systems by organizational unit (OU) identifier.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_systems_request.ListSystemsRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_systems_response.ListSystemsResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_systems

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_systems.list_systems(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_systems_request.ListSystemsRequest = {}  # type: ignore[typeddict-item]
        if ou_id is not None:
            input["ou_id"] = ou_id
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

    def iter_list_systems(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        ou_id: Optional["aws_sdk_resiliencehubv2.types.ou_id.OuId"] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.system_summary.SystemSummary]":
        _token = next_token
        while True:
            _response = self.list_systems(
                config_overrides=config_overrides,
                ou_id=ou_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("system_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a resource.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_tags_for_resource

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_user_journeys(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.list_user_journeys_response.ListUserJourneysResponse":
        """<p>Lists user journeys for a system.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.list_user_journeys_request.ListUserJourneysRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.list_user_journeys_response.ListUserJourneysResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_user_journeys

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.list_user_journeys.list_user_journeys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.list_user_journeys_request.ListUserJourneysRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
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

    def iter_list_user_journeys(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_resiliencehubv2.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[aws_sdk_resiliencehubv2.types.user_journey_summary.UserJourneySummary]":
        _token = next_token
        while True:
            _response = self.list_user_journeys(
                system_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("user_journey_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_failure_mode_assessment(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "aws_sdk_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.start_failure_mode_assessment_response.StartFailureModeAssessmentResponse":
        """<p>Start a failure mode assessment.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.start_failure_mode_assessment_request.StartFailureModeAssessmentRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.start_failure_mode_assessment_response.StartFailureModeAssessmentResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.start_failure_mode_assessment

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.start_failure_mode_assessment.start_failure_mode_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.start_failure_mode_assessment_request.StartFailureModeAssessmentRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        tags: "aws_sdk_resiliencehubv2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>"""

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.tag_resource

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        tag_keys: "aws_sdk_resiliencehubv2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "aws_sdk_resiliencehubv2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            tag_keys: <p>The tag keys to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.untag_resource

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_assertion(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        assertion_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        text: Optional[
            "aws_sdk_resiliencehubv2.types.assertion_text.AssertionText"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_assertion_response.UpdateAssertionResponse":
        """<p>Updates a resilience assertion.</p>

        Args:
            assertion_id: <p>The unique identifier of the assertion to update.</p>
            text: <p>The updated text content of the assertion.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_assertion_request.UpdateAssertionRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_assertion_response.UpdateAssertionResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_assertion

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_assertion.update_assertion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_assertion_request.UpdateAssertionRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["assertion_id"] = assertion_id
        if text is not None:
            input["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_dependency(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        dependency_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        criticality: Optional[
            "aws_sdk_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
        ] = None,
        comment: Optional[str] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_dependency_response.UpdateDependencyResponse":
        """<p>Updates a dependency classification.</p>

        Args:
            dependency_id: <p>The identifier of the dependency to update.</p>
            criticality: <p>The updated criticality level of the dependency.</p>
            comment: <p>A comment about the dependency.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_dependency_request.UpdateDependencyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_dependency_response.UpdateDependencyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_dependency

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_dependency.update_dependency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_dependency_request.UpdateDependencyRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["dependency_id"] = dependency_id
        if criticality is not None:
            input["criticality"] = criticality
        if comment is not None:
            input["comment"] = comment

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_failure_mode_finding(
        self,
        finding_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid",
        status: "aws_sdk_resiliencehubv2.types.finding_status.FindingStatus",
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        comment: Optional[str] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_failure_mode_finding_response.UpdateFailureModeFindingResponse":
        """<p>Updates an existing finding.</p>

        Args:
            finding_id: <p>The identifier of the finding to update.</p>
            status: <p>The new status for the finding.</p>
            comment: <p>A comment about the finding update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_failure_mode_finding_request.UpdateFailureModeFindingRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_failure_mode_finding_response.UpdateFailureModeFindingResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_failure_mode_finding

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_failure_mode_finding.update_failure_mode_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_failure_mode_finding_request.UpdateFailureModeFindingRequest = {}  # type: ignore[typeddict-item]
        input["finding_id"] = finding_id
        input["status"] = status
        input["service_arn"] = service_arn
        if comment is not None:
            input["comment"] = comment

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_policy(
        self,
        policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        availability_slo: Optional[
            "aws_sdk_resiliencehubv2.types.availability_slo.AvailabilitySlo"
        ] = None,
        multi_az: Optional[
            "aws_sdk_resiliencehubv2.types.multi_az_targets.MultiAzTargets"
        ] = None,
        multi_region: Optional[
            "aws_sdk_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
        ] = None,
        data_recovery: Optional[
            "aws_sdk_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_policy_response.UpdatePolicyResponse":
        """<p>Updates an existing resilience policy.</p>

        Args:
            availability_slo: <p>The updated availability SLO for the policy.</p>
            multi_az: <p>The updated multi-AZ disaster recovery targets for the policy.</p>
            multi_region: <p>The updated multi-Region disaster recovery targets for the policy.</p>
            data_recovery: <p>The updated data recovery targets for the policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_policy_request.UpdatePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_policy_response.UpdatePolicyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_policy

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_policy.update_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_policy_request.UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
        input["policy_arn"] = policy_arn
        if description is not None:
            input["description"] = description
        if availability_slo is not None:
            input["availability_slo"] = availability_slo
        if multi_az is not None:
            input["multi_az"] = multi_az
        if multi_region is not None:
            input["multi_region"] = multi_region
        if data_recovery is not None:
            input["data_recovery"] = data_recovery

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_service(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        associated_systems: Optional[
            "aws_sdk_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
        ] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
        regions: Optional[
            "aws_sdk_resiliencehubv2.types.region_list.RegionList"
        ] = None,
        permission_model: Optional[
            "aws_sdk_resiliencehubv2.types.permission_model.PermissionModel"
        ] = None,
        dependency_discovery: Optional[
            "aws_sdk_resiliencehubv2.types.dependency_discovery_input.DependencyDiscoveryInput"
        ] = None,
        report_configuration: Optional[
            "aws_sdk_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_service_response.UpdateServiceResponse":
        """<p>Updates an existing service.</p>

        Args:
            associated_systems: <p>The updated systems to associate with the service.</p>
            regions: <p>The updated AWS Regions where the service operates.</p>
            permission_model: <p>The updated permission model for the service.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_service_response.UpdateServiceResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_service

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_service_request.UpdateServiceRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        if description is not None:
            input["description"] = description
        if associated_systems is not None:
            input["associated_systems"] = associated_systems
        if policy_arn is not None:
            input["policy_arn"] = policy_arn
        if regions is not None:
            input["regions"] = regions
        if permission_model is not None:
            input["permission_model"] = permission_model
        if dependency_discovery is not None:
            input["dependency_discovery"] = dependency_discovery
        if report_configuration is not None:
            input["report_configuration"] = report_configuration

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_service_function(
        self,
        service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        service_function_id: "aws_sdk_resiliencehubv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        name: Optional["aws_sdk_resiliencehubv2.types.entity_label.EntityLabel"] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        criticality: Optional[
            "aws_sdk_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
        ] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_service_function_response.UpdateServiceFunctionResponse":
        """<p>Updates a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to update.</p>
            criticality: <p>The updated criticality level of the service function.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_service_function_request.UpdateServiceFunctionRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_service_function_response.UpdateServiceFunctionResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_service_function

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_service_function.update_service_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_service_function_request.UpdateServiceFunctionRequest = {}  # type: ignore[typeddict-item]
        input["service_arn"] = service_arn
        input["service_function_id"] = service_function_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if criticality is not None:
            input["criticality"] = criticality

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_system(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        sharing_enabled: Optional[bool] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_system_response.UpdateSystemResponse":
        """<p>Updates an existing system.</p>

        Args:
            sharing_enabled: <p>Whether cross-account sharing is enabled for the system.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_system_request.UpdateSystemRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_system_response.UpdateSystemResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_system

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_system.update_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_system_request.UpdateSystemRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
        if description is not None:
            input["description"] = description
        if sharing_enabled is not None:
            input["sharing_enabled"] = sharing_enabled

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_user_journey(
        self,
        system_arn: "aws_sdk_resiliencehubv2.types.arn.Arn",
        user_journey_id: "aws_sdk_resiliencehubv2.types.user_journey_id.UserJourneyId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        name: Optional["aws_sdk_resiliencehubv2.types.entity_label.EntityLabel"] = None,
        description: Optional[
            "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        policy_arn: Optional["aws_sdk_resiliencehubv2.types.arn.Arn"] = None,
    ) -> "aws_sdk_resiliencehubv2.types.update_user_journey_response.UpdateUserJourneyResponse":
        """<p>Updates an existing user journey.</p>

        Args:
            user_journey_id: <p>The identifier of the user journey to update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_resiliencehubv2.types.update_user_journey_request.UpdateUserJourneyRequest]",
        ) -> OperationResponse[
            "aws_sdk_resiliencehubv2.types.update_user_journey_response.UpdateUserJourneyResponse"
        ]:
            import aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_user_journey

            output, http_response = (
                aws_sdk_resiliencehubv2._operations.ngrh_service_core.update_user_journey.update_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_resiliencehubv2.types.update_user_journey_request.UpdateUserJourneyRequest = {}  # type: ignore[typeddict-item]
        input["system_arn"] = system_arn
        input["user_journey_id"] = user_journey_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if policy_arn is not None:
            input["policy_arn"] = policy_arn

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
