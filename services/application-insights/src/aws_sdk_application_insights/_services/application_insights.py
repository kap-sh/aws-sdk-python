"""Generated from Smithy shape ``com.amazonaws.applicationinsights#EC2WindowsBarleyService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_application_insights._auth._signers
import aws_sdk_application_insights._auth._sigv4
from aws_sdk_application_insights._auth._identity import Credentials
from aws_sdk_application_insights._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_application_insights._auth._zapros_handler import AuthMiddleware
from aws_sdk_application_insights._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.add_workload_request
    import aws_sdk_application_insights.types.add_workload_response
    import aws_sdk_application_insights.types.amazon_resource_name
    import aws_sdk_application_insights.types.attach_missing_permission
    import aws_sdk_application_insights.types.auto_config_enabled
    import aws_sdk_application_insights.types.auto_create
    import aws_sdk_application_insights.types.component_configuration
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.configuration_event_status
    import aws_sdk_application_insights.types.create_application_request
    import aws_sdk_application_insights.types.create_application_response
    import aws_sdk_application_insights.types.create_component_request
    import aws_sdk_application_insights.types.create_component_response
    import aws_sdk_application_insights.types.create_log_pattern_request
    import aws_sdk_application_insights.types.create_log_pattern_response
    import aws_sdk_application_insights.types.custom_component_name
    import aws_sdk_application_insights.types.cwe_monitor_enabled
    import aws_sdk_application_insights.types.delete_application_request
    import aws_sdk_application_insights.types.delete_application_response
    import aws_sdk_application_insights.types.delete_component_request
    import aws_sdk_application_insights.types.delete_component_response
    import aws_sdk_application_insights.types.delete_log_pattern_request
    import aws_sdk_application_insights.types.delete_log_pattern_response
    import aws_sdk_application_insights.types.describe_application_request
    import aws_sdk_application_insights.types.describe_application_response
    import aws_sdk_application_insights.types.describe_component_configuration_recommendation_request
    import aws_sdk_application_insights.types.describe_component_configuration_recommendation_response
    import aws_sdk_application_insights.types.describe_component_configuration_request
    import aws_sdk_application_insights.types.describe_component_configuration_response
    import aws_sdk_application_insights.types.describe_component_request
    import aws_sdk_application_insights.types.describe_component_response
    import aws_sdk_application_insights.types.describe_log_pattern_request
    import aws_sdk_application_insights.types.describe_log_pattern_response
    import aws_sdk_application_insights.types.describe_observation_request
    import aws_sdk_application_insights.types.describe_observation_response
    import aws_sdk_application_insights.types.describe_problem_observations_request
    import aws_sdk_application_insights.types.describe_problem_observations_response
    import aws_sdk_application_insights.types.describe_problem_request
    import aws_sdk_application_insights.types.describe_problem_response
    import aws_sdk_application_insights.types.describe_workload_request
    import aws_sdk_application_insights.types.describe_workload_response
    import aws_sdk_application_insights.types.end_time
    import aws_sdk_application_insights.types.grouping_type
    import aws_sdk_application_insights.types.list_applications_request
    import aws_sdk_application_insights.types.list_applications_response
    import aws_sdk_application_insights.types.list_components_request
    import aws_sdk_application_insights.types.list_components_response
    import aws_sdk_application_insights.types.list_configuration_history_request
    import aws_sdk_application_insights.types.list_configuration_history_response
    import aws_sdk_application_insights.types.list_log_pattern_sets_request
    import aws_sdk_application_insights.types.list_log_pattern_sets_response
    import aws_sdk_application_insights.types.list_log_patterns_request
    import aws_sdk_application_insights.types.list_log_patterns_response
    import aws_sdk_application_insights.types.list_problems_request
    import aws_sdk_application_insights.types.list_problems_response
    import aws_sdk_application_insights.types.list_tags_for_resource_request
    import aws_sdk_application_insights.types.list_tags_for_resource_response
    import aws_sdk_application_insights.types.list_workloads_request
    import aws_sdk_application_insights.types.list_workloads_response
    import aws_sdk_application_insights.types.log_pattern_name
    import aws_sdk_application_insights.types.log_pattern_rank
    import aws_sdk_application_insights.types.log_pattern_regex
    import aws_sdk_application_insights.types.log_pattern_set_name
    import aws_sdk_application_insights.types.max_entities
    import aws_sdk_application_insights.types.monitor
    import aws_sdk_application_insights.types.observation_id
    import aws_sdk_application_insights.types.ops_center_enabled
    import aws_sdk_application_insights.types.ops_item_sns_topic_arn
    import aws_sdk_application_insights.types.pagination_token
    import aws_sdk_application_insights.types.problem_id
    import aws_sdk_application_insights.types.recommendation_type
    import aws_sdk_application_insights.types.remove_sns_topic
    import aws_sdk_application_insights.types.remove_workload_request
    import aws_sdk_application_insights.types.remove_workload_response
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.resource_list
    import aws_sdk_application_insights.types.sns_notification_arn
    import aws_sdk_application_insights.types.start_time
    import aws_sdk_application_insights.types.tag_key_list
    import aws_sdk_application_insights.types.tag_list
    import aws_sdk_application_insights.types.tag_resource_request
    import aws_sdk_application_insights.types.tag_resource_response
    import aws_sdk_application_insights.types.tier
    import aws_sdk_application_insights.types.untag_resource_request
    import aws_sdk_application_insights.types.untag_resource_response
    import aws_sdk_application_insights.types.update_application_request
    import aws_sdk_application_insights.types.update_application_response
    import aws_sdk_application_insights.types.update_component_configuration_request
    import aws_sdk_application_insights.types.update_component_configuration_response
    import aws_sdk_application_insights.types.update_component_request
    import aws_sdk_application_insights.types.update_component_response
    import aws_sdk_application_insights.types.update_log_pattern_request
    import aws_sdk_application_insights.types.update_log_pattern_response
    import aws_sdk_application_insights.types.update_problem_request
    import aws_sdk_application_insights.types.update_problem_response
    import aws_sdk_application_insights.types.update_status
    import aws_sdk_application_insights.types.update_workload_request
    import aws_sdk_application_insights.types.update_workload_response
    import aws_sdk_application_insights.types.visibility
    import aws_sdk_application_insights.types.workload_configuration
    import aws_sdk_application_insights.types.workload_id
    import aws_sdk_application_insights.types.workload_name


class ApplicationInsightsClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class ApplicationInsightsClient:
    """A client for the ``ApplicationInsights`` service.

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
        self._config = ApplicationInsightsClientConfig(
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
        self, config_overrides: Optional[ApplicationInsightsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApplicationInsightsClientConfig = config_overrides or {}
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

    def add_workload(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        workload_configuration: "aws_sdk_application_insights.types.workload_configuration.WorkloadConfiguration",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.add_workload_response.AddWorkloadResponse":
        """<p>Adds a workload to a component. Each component can have at most five workloads.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            workload_configuration: <p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.add_workload_request.AddWorkloadRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.add_workload_response.AddWorkloadResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.add_workload

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.add_workload.add_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.add_workload_request.AddWorkloadRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        input_["workload_configuration"] = workload_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_application(
        self,
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        resource_group_name: Optional[
            "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        ops_center_enabled: Optional[
            "aws_sdk_application_insights.types.ops_center_enabled.OpsCenterEnabled"
        ] = None,
        cwe_monitor_enabled: Optional[
            "aws_sdk_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
        ] = None,
        ops_item_sns_topic_arn: Optional[
            "aws_sdk_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
        ] = None,
        sns_notification_arn: Optional[
            "aws_sdk_application_insights.types.sns_notification_arn.SNSNotificationArn"
        ] = None,
        tags: Optional["aws_sdk_application_insights.types.tag_list.TagList"] = None,
        auto_config_enabled: Optional[
            "aws_sdk_application_insights.types.auto_config_enabled.AutoConfigEnabled"
        ] = None,
        auto_create: Optional[
            "aws_sdk_application_insights.types.auto_create.AutoCreate"
        ] = None,
        grouping_type: Optional[
            "aws_sdk_application_insights.types.grouping_type.GroupingType"
        ] = None,
        attach_missing_permission: Optional[
            "aws_sdk_application_insights.types.attach_missing_permission.AttachMissingPermission"
        ] = None,
    ) -> "aws_sdk_application_insights.types.create_application_response.CreateApplicationResponse":
        """<p>Adds an application that is created from a resource group.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            ops_center_enabled: <p> When set to <code>true</code>, creates opsItems for any problems detected on an application. </p>
            cwe_monitor_enabled: <p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>
            ops_item_sns_topic_arn: <p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem. </p>
            sns_notification_arn: <p> The SNS notification topic ARN. </p>
            tags: <p>List of tags to add to the application. tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
            auto_config_enabled: <p> Indicates whether Application Insights automatically configures unmonitored resources in the resource group. </p>
            auto_create: <p> Configures all of the resources in the resource group by applying the recommended configurations. </p>
            grouping_type: <p>Application Insights can create applications based on a resource group or on an account. To create an account-based application using all of the resources in the account, set this parameter to <code>ACCOUNT_BASED</code>. </p>
            attach_missing_permission: <p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.create_application_response.CreateApplicationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.create_application

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.create_application_request.CreateApplicationRequest = {}  # type: ignore[typeddict-item]
        if resource_group_name is not None:
            input_["resource_group_name"] = resource_group_name
        if ops_center_enabled is not None:
            input_["ops_center_enabled"] = ops_center_enabled
        if cwe_monitor_enabled is not None:
            input_["cwe_monitor_enabled"] = cwe_monitor_enabled
        if ops_item_sns_topic_arn is not None:
            input_["ops_item_sns_topic_arn"] = ops_item_sns_topic_arn
        if sns_notification_arn is not None:
            input_["sns_notification_arn"] = sns_notification_arn
        if tags is not None:
            input_["tags"] = tags
        if auto_config_enabled is not None:
            input_["auto_config_enabled"] = auto_config_enabled
        if auto_create is not None:
            input_["auto_create"] = auto_create
        if grouping_type is not None:
            input_["grouping_type"] = grouping_type
        if attach_missing_permission is not None:
            input_["attach_missing_permission"] = attach_missing_permission

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_component(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.custom_component_name.CustomComponentName",
        resource_list: "aws_sdk_application_insights.types.resource_list.ResourceList",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.create_component_response.CreateComponentResponse":
        """<p>Creates a custom component by grouping similar standalone instances to monitor.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            resource_list: <p>The list of resource ARNs that belong to the component.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.create_component_request.CreateComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.create_component_response.CreateComponentResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.create_component

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.create_component.create_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.create_component_request.CreateComponentRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        input_["resource_list"] = resource_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_log_pattern(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "aws_sdk_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "aws_sdk_application_insights.types.log_pattern_name.LogPatternName",
        pattern: "aws_sdk_application_insights.types.log_pattern_regex.LogPatternRegex",
        rank: "aws_sdk_application_insights.types.log_pattern_rank.LogPatternRank",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.create_log_pattern_response.CreateLogPatternResponse":
        """<p>Adds an log pattern to a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
            pattern: <p>The log pattern. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.</p>
            rank: <p>Rank of the log pattern. Must be a value between <code>1</code> and <code>1,000,000</code>. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank <code>1</code> will be the first to get matched to a log line. A pattern of rank <code>1,000,000</code> will be last to get matched. When you configure custom log patterns from the console, a <code>Low</code> severity pattern translates to a <code>750,000</code> rank. A <code>Medium</code> severity pattern translates to a <code>500,000</code> rank. And a <code>High</code> severity pattern translates to a <code>250,000</code> rank. Rank values less than <code>1</code> or greater than <code>1,000,000</code> are reserved for Amazon Web Services provided patterns. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.create_log_pattern_request.CreateLogPatternRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.create_log_pattern_response.CreateLogPatternResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.create_log_pattern

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.create_log_pattern.create_log_pattern(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.create_log_pattern_request.CreateLogPatternRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["pattern_set_name"] = pattern_set_name
        input_["pattern_name"] = pattern_name
        input_["pattern"] = pattern
        input_["rank"] = rank

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_application(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.delete_application_response.DeleteApplicationResponse":
        """<p>Removes the specified application from monitoring. Does not delete the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.delete_application

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.delete_application_request.DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_component(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.custom_component_name.CustomComponentName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.delete_component_response.DeleteComponentResponse":
        """<p>Ungroups a custom component. When you ungroup custom components, all applicable monitors that are set up for the component are removed and the instances revert to their standalone status.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.delete_component_request.DeleteComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.delete_component_response.DeleteComponentResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.delete_component

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.delete_component.delete_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.delete_component_request.DeleteComponentRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_log_pattern(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "aws_sdk_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "aws_sdk_application_insights.types.log_pattern_name.LogPatternName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.delete_log_pattern_response.DeleteLogPatternResponse":
        """<p>Removes the specified log pattern from a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.delete_log_pattern_request.DeleteLogPatternRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.delete_log_pattern_response.DeleteLogPatternResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.delete_log_pattern

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.delete_log_pattern.delete_log_pattern(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.delete_log_pattern_request.DeleteLogPatternRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["pattern_set_name"] = pattern_set_name
        input_["pattern_name"] = pattern_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_application(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_application_response.DescribeApplicationResponse":
        """<p>Describes the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_application_request.DescribeApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_application_response.DescribeApplicationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_application

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_application.describe_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_application_request.DescribeApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_component(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_component_response.DescribeComponentResponse":
        """<p>Describes a component and lists the resources that are grouped together in a component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_component_request.DescribeComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_component_response.DescribeComponentResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_component

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_component.describe_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_component_request.DescribeComponentRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_component_configuration(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_component_configuration_response.DescribeComponentConfigurationResponse":
        """<p>Describes the monitoring configuration of the component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_component_configuration_request.DescribeComponentConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_component_configuration_response.DescribeComponentConfigurationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_component_configuration

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_component_configuration.describe_component_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_component_configuration_request.DescribeComponentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_component_configuration_recommendation(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        tier: "aws_sdk_application_insights.types.tier.Tier",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        workload_name: Optional[
            "aws_sdk_application_insights.types.workload_name.WorkloadName"
        ] = None,
        recommendation_type: Optional[
            "aws_sdk_application_insights.types.recommendation_type.RecommendationType"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_component_configuration_recommendation_response.DescribeComponentConfigurationRecommendationResponse":
        """<p>Describes the recommended monitoring configuration of the component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            tier: <p>The tier of the application component.</p>
            workload_name: <p>The name of the workload. The name of the workload is required when the tier of the application component is <code>SAP_ASE_SINGLE_NODE</code> or <code>SAP_ASE_HIGH_AVAILABILITY</code>.</p>
            recommendation_type: <p>The recommended configuration type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_component_configuration_recommendation_request.DescribeComponentConfigurationRecommendationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_component_configuration_recommendation_response.DescribeComponentConfigurationRecommendationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_component_configuration_recommendation

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_component_configuration_recommendation.describe_component_configuration_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_component_configuration_recommendation_request.DescribeComponentConfigurationRecommendationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        input_["tier"] = tier
        if workload_name is not None:
            input_["workload_name"] = workload_name
        if recommendation_type is not None:
            input_["recommendation_type"] = recommendation_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_log_pattern(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "aws_sdk_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "aws_sdk_application_insights.types.log_pattern_name.LogPatternName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_log_pattern_response.DescribeLogPatternResponse":
        """<p>Describe a specific log pattern from a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_log_pattern_request.DescribeLogPatternRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_log_pattern_response.DescribeLogPatternResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_log_pattern

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_log_pattern.describe_log_pattern(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_log_pattern_request.DescribeLogPatternRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["pattern_set_name"] = pattern_set_name
        input_["pattern_name"] = pattern_name
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_observation(
        self,
        observation_id: "aws_sdk_application_insights.types.observation_id.ObservationId",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_observation_response.DescribeObservationResponse":
        """<p>Describes an anomaly or error with the application.</p>

        Args:
            observation_id: <p>The ID of the observation.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_observation_request.DescribeObservationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_observation_response.DescribeObservationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_observation

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_observation.describe_observation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_observation_request.DescribeObservationRequest = {}  # type: ignore[typeddict-item]
        input_["observation_id"] = observation_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_problem(
        self,
        problem_id: "aws_sdk_application_insights.types.problem_id.ProblemId",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_problem_response.DescribeProblemResponse":
        """<p>Describes an application problem.</p>

        Args:
            problem_id: <p>The ID of the problem.</p>
            account_id: <p>The Amazon Web Services account ID for the owner of the resource group affected by the problem.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_problem_request.DescribeProblemRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_problem_response.DescribeProblemResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_problem

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_problem.describe_problem(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_problem_request.DescribeProblemRequest = {}  # type: ignore[typeddict-item]
        input_["problem_id"] = problem_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_problem_observations(
        self,
        problem_id: "aws_sdk_application_insights.types.problem_id.ProblemId",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_problem_observations_response.DescribeProblemObservationsResponse":
        """<p>Describes the anomalies or errors associated with the problem.</p>

        Args:
            problem_id: <p>The ID of the problem.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_problem_observations_request.DescribeProblemObservationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_problem_observations_response.DescribeProblemObservationsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_problem_observations

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_problem_observations.describe_problem_observations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_problem_observations_request.DescribeProblemObservationsRequest = {}  # type: ignore[typeddict-item]
        input_["problem_id"] = problem_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_workload(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        workload_id: "aws_sdk_application_insights.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.describe_workload_response.DescribeWorkloadResponse":
        """<p>Describes a workload and its configuration.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            workload_id: <p>The ID of the workload.</p>
            account_id: <p>The Amazon Web Services account ID for the workload owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.describe_workload_request.DescribeWorkloadRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.describe_workload_response.DescribeWorkloadResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_workload

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.describe_workload.describe_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.describe_workload_request.DescribeWorkloadRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        input_["workload_id"] = workload_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_applications(
        self,
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists the IDs of the applications that you are monitoring. </p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_applications_response.ListApplicationsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_applications

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_applications_request.ListApplicationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_components(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.list_components_response.ListComponentsResponse":
        """<p>Lists the auto-grouped, standalone, and custom components of the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_components_request.ListComponentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_components_response.ListComponentsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_components

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_components.list_components(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_components_request.ListComponentsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_configuration_history(
        self,
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        resource_group_name: Optional[
            "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        start_time: Optional[
            "aws_sdk_application_insights.types.start_time.StartTime"
        ] = None,
        end_time: Optional[
            "aws_sdk_application_insights.types.end_time.EndTime"
        ] = None,
        event_status: Optional[
            "aws_sdk_application_insights.types.configuration_event_status.ConfigurationEventStatus"
        ] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.list_configuration_history_response.ListConfigurationHistoryResponse":
        """<p> Lists the INFO, WARN, and ERROR events for periodic configuration updates performed by Application Insights. Examples of events represented are: </p> <ul> <li> <p>INFO: creating a new alarm or updating an alarm threshold.</p> </li> <li> <p>WARN: alarm not created due to insufficient data points used to predict thresholds.</p> </li> <li> <p>ERROR: alarm not created due to permission errors or exceeding quotas. </p> </li> </ul>

        Args:
            resource_group_name: <p>Resource group to which the application belongs. </p>
            start_time: <p>The start time of the event. </p>
            end_time: <p>The end time of the event.</p>
            event_status: <p>The status of the configuration update event. Possible values include INFO, WARN, and ERROR.</p>
            max_results: <p> The maximum number of results returned by <code>ListConfigurationHistory</code> in paginated output. When this parameter is used, <code>ListConfigurationHistory</code> returns only <code>MaxResults</code> in a single page along with a <code>NextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListConfigurationHistory</code> request with the returned <code>NextToken</code> value. If this parameter is not used, then <code>ListConfigurationHistory</code> returns all results. </p>
            next_token: <p>The <code>NextToken</code> value returned from a previous paginated <code>ListConfigurationHistory</code> request where <code>MaxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_configuration_history_request.ListConfigurationHistoryRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_configuration_history_response.ListConfigurationHistoryResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_configuration_history

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_configuration_history.list_configuration_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_configuration_history_request.ListConfigurationHistoryRequest = {}  # type: ignore[typeddict-item]
        if resource_group_name is not None:
            input_["resource_group_name"] = resource_group_name
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if event_status is not None:
            input_["event_status"] = event_status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_log_patterns(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        pattern_set_name: Optional[
            "aws_sdk_application_insights.types.log_pattern_set_name.LogPatternSetName"
        ] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.list_log_patterns_response.ListLogPatternsResponse":
        """<p>Lists the log patterns in the specific log <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_log_patterns_request.ListLogPatternsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_log_patterns_response.ListLogPatternsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_log_patterns

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_log_patterns.list_log_patterns(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_log_patterns_request.ListLogPatternsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        if pattern_set_name is not None:
            input_["pattern_set_name"] = pattern_set_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_log_pattern_sets(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.list_log_pattern_sets_response.ListLogPatternSetsResponse":
        """<p>Lists the log pattern sets in the specific application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_log_pattern_sets_request.ListLogPatternSetsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_log_pattern_sets_response.ListLogPatternSetsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_log_pattern_sets

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_log_pattern_sets.list_log_pattern_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_log_pattern_sets_request.ListLogPatternSetsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_problems(
        self,
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
        resource_group_name: Optional[
            "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        start_time: Optional[
            "aws_sdk_application_insights.types.start_time.StartTime"
        ] = None,
        end_time: Optional[
            "aws_sdk_application_insights.types.end_time.EndTime"
        ] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        component_name: Optional[
            "aws_sdk_application_insights.types.component_name.ComponentName"
        ] = None,
        visibility: Optional[
            "aws_sdk_application_insights.types.visibility.Visibility"
        ] = None,
    ) -> (
        "aws_sdk_application_insights.types.list_problems_response.ListProblemsResponse"
    ):
        """<p>Lists the problems with your application.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
            resource_group_name: <p>The name of the resource group.</p>
            start_time: <p>The time when the problem was detected, in epoch seconds. If you don't specify a time frame for the request, problems within the past seven days are returned.</p>
            end_time: <p>The time when the problem ended, in epoch seconds. If not specified, problems within the past seven days are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            component_name: <p> The name of the component. </p>
            visibility: <p>Specifies whether or not you can view the problem. If not specified, visible and ignored problems are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_problems_request.ListProblemsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_problems_response.ListProblemsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_problems

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_problems.list_problems(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_problems_request.ListProblemsRequest = {}  # type: ignore[typeddict-item]
        if account_id is not None:
            input_["account_id"] = account_id
        if resource_group_name is not None:
            input_["resource_group_name"] = resource_group_name
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if component_name is not None:
            input_["component_name"] = component_name
        if visibility is not None:
            input_["visibility"] = visibility

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_application_insights.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieve a list of the tags (keys and values) that are associated with a specified application. A <i>tag</i> is a label that you optionally define and associate with an application. Each tag consists of a required <i>tag key</i> and an optional associated <i>tag value</i>. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the application that you want to retrieve tag information for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_workloads(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "aws_sdk_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "aws_sdk_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "aws_sdk_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.list_workloads_response.ListWorkloadsResponse":
        """<p>Lists the workloads that are configured on a given component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID of the owner of the workload.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.list_workloads_request.ListWorkloadsRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.list_workloads_response.ListWorkloadsResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.list_workloads

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.list_workloads.list_workloads(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.list_workloads_request.ListWorkloadsRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def remove_workload(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        workload_id: "aws_sdk_application_insights.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.remove_workload_response.RemoveWorkloadResponse":
        """<p>Remove workload from a component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            workload_id: <p>The ID of the workload.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.remove_workload_request.RemoveWorkloadRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.remove_workload_response.RemoveWorkloadResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.remove_workload

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.remove_workload.remove_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.remove_workload_request.RemoveWorkloadRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        input_["workload_id"] = workload_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_application_insights.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_application_insights.types.tag_list.TagList",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.tag_resource_response.TagResourceResponse":
        """<p>Add one or more tags (keys and values) to a specified application. A <i>tag</i> is a label that you optionally define and associate with an application. Tags can help you categorize and manage application in different ways, such as by purpose, owner, environment, or other criteria. </p> <p>Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the application that you want to add one or more tags to.</p>
            tags: <p>A list of tags that to add to the application. A tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.tag_resource

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_application_insights.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_application_insights.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
    ) -> "aws_sdk_application_insights.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove one or more tags (keys and values) from a specified application.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the application that you want to remove one or more tags from.</p>
            tag_keys: <p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the application, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.untag_resource

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_application(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        ops_center_enabled: Optional[
            "aws_sdk_application_insights.types.ops_center_enabled.OpsCenterEnabled"
        ] = None,
        cwe_monitor_enabled: Optional[
            "aws_sdk_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
        ] = None,
        ops_item_sns_topic_arn: Optional[
            "aws_sdk_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
        ] = None,
        sns_notification_arn: Optional[
            "aws_sdk_application_insights.types.sns_notification_arn.SNSNotificationArn"
        ] = None,
        remove_sns_topic: Optional[
            "aws_sdk_application_insights.types.remove_sns_topic.RemoveSNSTopic"
        ] = None,
        auto_config_enabled: Optional[
            "aws_sdk_application_insights.types.auto_config_enabled.AutoConfigEnabled"
        ] = None,
        attach_missing_permission: Optional[
            "aws_sdk_application_insights.types.attach_missing_permission.AttachMissingPermission"
        ] = None,
    ) -> "aws_sdk_application_insights.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            ops_center_enabled: <p> When set to <code>true</code>, creates opsItems for any problems detected on an application. </p>
            cwe_monitor_enabled: <p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>
            ops_item_sns_topic_arn: <p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.</p>
            sns_notification_arn: <p> The SNS topic ARN. Allows you to receive SNS notifications for updates and issues with an application. </p>
            remove_sns_topic: <p> Disassociates the SNS topic from the opsItem created for detected problems.</p>
            auto_config_enabled: <p> Turns auto-configuration on or off. </p>
            attach_missing_permission: <p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.update_application_response.UpdateApplicationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.update_application

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.update_application_request.UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        if ops_center_enabled is not None:
            input_["ops_center_enabled"] = ops_center_enabled
        if cwe_monitor_enabled is not None:
            input_["cwe_monitor_enabled"] = cwe_monitor_enabled
        if ops_item_sns_topic_arn is not None:
            input_["ops_item_sns_topic_arn"] = ops_item_sns_topic_arn
        if sns_notification_arn is not None:
            input_["sns_notification_arn"] = sns_notification_arn
        if remove_sns_topic is not None:
            input_["remove_sns_topic"] = remove_sns_topic
        if auto_config_enabled is not None:
            input_["auto_config_enabled"] = auto_config_enabled
        if attach_missing_permission is not None:
            input_["attach_missing_permission"] = attach_missing_permission

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_component(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.custom_component_name.CustomComponentName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        new_component_name: Optional[
            "aws_sdk_application_insights.types.custom_component_name.CustomComponentName"
        ] = None,
        resource_list: Optional[
            "aws_sdk_application_insights.types.resource_list.ResourceList"
        ] = None,
    ) -> "aws_sdk_application_insights.types.update_component_response.UpdateComponentResponse":
        """<p>Updates the custom component name and/or the list of resources that make up the component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            new_component_name: <p>The new name of the component.</p>
            resource_list: <p>The list of resource ARNs that belong to the component.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.update_component_request.UpdateComponentRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.update_component_response.UpdateComponentResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.update_component

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.update_component.update_component(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.update_component_request.UpdateComponentRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        if new_component_name is not None:
            input_["new_component_name"] = new_component_name
        if resource_list is not None:
            input_["resource_list"] = resource_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_component_configuration(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        monitor: Optional["aws_sdk_application_insights.types.monitor.Monitor"] = None,
        tier: Optional["aws_sdk_application_insights.types.tier.Tier"] = None,
        component_configuration: Optional[
            "aws_sdk_application_insights.types.component_configuration.ComponentConfiguration"
        ] = None,
        auto_config_enabled: Optional[
            "aws_sdk_application_insights.types.auto_config_enabled.AutoConfigEnabled"
        ] = None,
    ) -> "aws_sdk_application_insights.types.update_component_configuration_response.UpdateComponentConfigurationResponse":
        r"""<p>Updates the monitoring configurations for the component. The configuration input parameter is an escaped JSON of the configuration and should match the schema of what is returned by <code>DescribeComponentConfigurationRecommendation</code>. </p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            monitor: <p>Indicates whether the application component is monitored.</p>
            tier: <p>The tier of the application component.</p>
            component_configuration: <p>The configuration settings of the component. The value is the escaped JSON of the configuration. For more information about the JSON format, see <a href=\"https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-json.html\">Working with JSON</a>. You can send a request to <code>DescribeComponentConfigurationRecommendation</code> to see the recommended configuration for a component. For the complete format of the component configuration file, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config.html\">Component Configuration</a>.</p>
            auto_config_enabled: <p> Automatically configures the component by applying the recommended configurations. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.update_component_configuration_request.UpdateComponentConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.update_component_configuration_response.UpdateComponentConfigurationResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.update_component_configuration

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.update_component_configuration.update_component_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.update_component_configuration_request.UpdateComponentConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        if monitor is not None:
            input_["monitor"] = monitor
        if tier is not None:
            input_["tier"] = tier
        if component_configuration is not None:
            input_["component_configuration"] = component_configuration
        if auto_config_enabled is not None:
            input_["auto_config_enabled"] = auto_config_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_log_pattern(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "aws_sdk_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "aws_sdk_application_insights.types.log_pattern_name.LogPatternName",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        pattern: Optional[
            "aws_sdk_application_insights.types.log_pattern_regex.LogPatternRegex"
        ] = None,
        rank: Optional[
            "aws_sdk_application_insights.types.log_pattern_rank.LogPatternRank"
        ] = None,
    ) -> "aws_sdk_application_insights.types.update_log_pattern_response.UpdateLogPatternResponse":
        """<p>Adds a log pattern to a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
            pattern: <p>The log pattern. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.</p>
            rank: <p>Rank of the log pattern. Must be a value between <code>1</code> and <code>1,000,000</code>. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank <code>1</code> will be the first to get matched to a log line. A pattern of rank <code>1,000,000</code> will be last to get matched. When you configure custom log patterns from the console, a <code>Low</code> severity pattern translates to a <code>750,000</code> rank. A <code>Medium</code> severity pattern translates to a <code>500,000</code> rank. And a <code>High</code> severity pattern translates to a <code>250,000</code> rank. Rank values less than <code>1</code> or greater than <code>1,000,000</code> are reserved for Amazon Web Services provided patterns. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.update_log_pattern_request.UpdateLogPatternRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.update_log_pattern_response.UpdateLogPatternResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.update_log_pattern

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.update_log_pattern.update_log_pattern(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.update_log_pattern_request.UpdateLogPatternRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["pattern_set_name"] = pattern_set_name
        input_["pattern_name"] = pattern_name
        if pattern is not None:
            input_["pattern"] = pattern
        if rank is not None:
            input_["rank"] = rank

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_problem(
        self,
        problem_id: "aws_sdk_application_insights.types.problem_id.ProblemId",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        update_status: Optional[
            "aws_sdk_application_insights.types.update_status.UpdateStatus"
        ] = None,
        visibility: Optional[
            "aws_sdk_application_insights.types.visibility.Visibility"
        ] = None,
    ) -> "aws_sdk_application_insights.types.update_problem_response.UpdateProblemResponse":
        """<p>Updates the visibility of the problem or specifies the problem as <code>RESOLVED</code>.</p>

        Args:
            problem_id: <p>The ID of the problem.</p>
            update_status: <p>The status of the problem. Arguments can be passed for only problems that show a status of <code>RECOVERING</code>.</p>
            visibility: <p>The visibility of a problem. When you pass a value of <code>IGNORED</code>, the problem is removed from the default view, and all notifications for the problem are suspended. When <code>VISIBLE</code> is passed, the <code>IGNORED</code> action is reversed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.update_problem_request.UpdateProblemRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.update_problem_response.UpdateProblemResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.update_problem

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.update_problem.update_problem(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.update_problem_request.UpdateProblemRequest = {}  # type: ignore[typeddict-item]
        input_["problem_id"] = problem_id
        if update_status is not None:
            input_["update_status"] = update_status
        if visibility is not None:
            input_["visibility"] = visibility

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_workload(
        self,
        resource_group_name: "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "aws_sdk_application_insights.types.component_name.ComponentName",
        workload_configuration: "aws_sdk_application_insights.types.workload_configuration.WorkloadConfiguration",
        *,
        config_overrides: Optional[ApplicationInsightsClientConfig] = None,
        workload_id: Optional[
            "aws_sdk_application_insights.types.workload_id.WorkloadId"
        ] = None,
    ) -> "aws_sdk_application_insights.types.update_workload_response.UpdateWorkloadResponse":
        """<p>Adds a workload to a component. Each component can have at most five workloads.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p> The name of the component. </p>
            workload_id: <p>The ID of the workload.</p>
            workload_configuration: <p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_application_insights.types.update_workload_request.UpdateWorkloadRequest]",
        ) -> OperationResponse[
            "aws_sdk_application_insights.types.update_workload_response.UpdateWorkloadResponse"
        ]:
            import aws_sdk_application_insights._operations.ec2_windows_barley_service.update_workload

            output, http_response = (
                aws_sdk_application_insights._operations.ec2_windows_barley_service.update_workload.update_workload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_application_insights.types.update_workload_request.UpdateWorkloadRequest = {}  # type: ignore[typeddict-item]
        input_["resource_group_name"] = resource_group_name
        input_["component_name"] = component_name
        if workload_id is not None:
            input_["workload_id"] = workload_id
        input_["workload_configuration"] = workload_configuration

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
