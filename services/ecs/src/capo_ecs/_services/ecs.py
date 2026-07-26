"""Generated from Smithy shape ``com.amazonaws.ecs#AmazonEC2ContainerServiceV20141113``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ecs._auth._signers
import capo_ecs._auth._sigv4
from capo_ecs._auth._identity import Credentials
from capo_ecs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ecs._auth._zapros_handler import AuthMiddleware
from capo_ecs._pagination import resolve_path as _resolve_path
from capo_ecs._resources.amazon_ec2_container_service_v20141113.capacity_provider_resource import (
    CapacityProviderResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.cluster_resource import (
    ClusterResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.container_instance_resource import (
    ContainerInstanceResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_deployment_resource import (
    DaemonDeploymentResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_resource import (
    DaemonResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_revision_resource import (
    DaemonRevisionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.daemon_task_definition_resource import (
    DaemonTaskDefinitionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.service_deployment_resource import (
    ServiceDeploymentResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.service_resource import (
    ServiceResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.service_revision_resource import (
    ServiceRevisionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.task_definition_resource import (
    TaskDefinitionResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.task_resource import (
    TaskResource,
)
from capo_ecs._resources.amazon_ec2_container_service_v20141113.task_set_resource import (
    TaskSetResource,
)
from capo_ecs._services._aws_config import aws_config
from capo_ecs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.continue_service_deployment_request
    import capo_ecs.types.continue_service_deployment_response
    import capo_ecs.types.delete_account_setting_request
    import capo_ecs.types.delete_account_setting_response
    import capo_ecs.types.deployment_lifecycle_hook_action
    import capo_ecs.types.deregister_task_definition_request
    import capo_ecs.types.deregister_task_definition_response
    import capo_ecs.types.describe_task_definition_request
    import capo_ecs.types.describe_task_definition_response
    import capo_ecs.types.discover_poll_endpoint_request
    import capo_ecs.types.discover_poll_endpoint_response
    import capo_ecs.types.integer
    import capo_ecs.types.list_account_settings_request
    import capo_ecs.types.list_account_settings_response
    import capo_ecs.types.list_services_by_namespace_request
    import capo_ecs.types.list_services_by_namespace_response
    import capo_ecs.types.list_tags_for_resource_request
    import capo_ecs.types.list_tags_for_resource_response
    import capo_ecs.types.list_task_definition_families_request
    import capo_ecs.types.list_task_definition_families_response
    import capo_ecs.types.put_account_setting_default_request
    import capo_ecs.types.put_account_setting_default_response
    import capo_ecs.types.put_account_setting_request
    import capo_ecs.types.put_account_setting_response
    import capo_ecs.types.setting
    import capo_ecs.types.setting_name
    import capo_ecs.types.string
    import capo_ecs.types.tag_keys
    import capo_ecs.types.tag_resource_request
    import capo_ecs.types.tag_resource_response
    import capo_ecs.types.tags
    import capo_ecs.types.task_definition_family_status
    import capo_ecs.types.task_definition_field_list
    import capo_ecs.types.untag_resource_request
    import capo_ecs.types.untag_resource_response


class ECSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ECSClient:
    """A client for the ``ECS`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = ECSClientConfig(
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

        # resources
        self.capacity_provider_resource = CapacityProviderResource(self)
        self.cluster_resource = ClusterResource(self)
        self.container_instance_resource = ContainerInstanceResource(self)
        self.daemon_deployment_resource = DaemonDeploymentResource(self)
        self.daemon_resource = DaemonResource(self)
        self.daemon_revision_resource = DaemonRevisionResource(self)
        self.daemon_task_definition_resource = DaemonTaskDefinitionResource(self)
        self.service_deployment_resource = ServiceDeploymentResource(self)
        self.service_resource = ServiceResource(self)
        self.service_revision_resource = ServiceRevisionResource(self)
        self.task_definition_resource = TaskDefinitionResource(self)
        self.task_resource = TaskResource(self)
        self.task_set_resource = TaskSetResource(self)

    def operation_options(
        self, config_overrides: Optional[ECSClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ECSClientConfig = config_overrides or {}
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

    def continue_service_deployment(
        self,
        service_deployment_arn: "capo_ecs.types.string.String",
        hook_id: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        action: Optional[
            "capo_ecs.types.deployment_lifecycle_hook_action.DeploymentLifecycleHookAction"
        ] = None,
    ) -> "capo_ecs.types.continue_service_deployment_response.ContinueServiceDeploymentResponse":
        r"""<p>Continues or rolls back an Amazon ECS service deployment that is paused at a lifecycle hook.</p> <p>When a service deployment reaches a lifecycle stage that has a <code>PAUSE</code> hook configured, the deployment pauses and waits for an explicit action. Use this API to either continue the deployment to the next stage or roll back to the previous service revision.</p> <p>To find the <code>hookId</code> of the paused hook, call <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html\">DescribeServiceDeployments</a> and inspect the <code>lifecycleHookDetails</code> field.</p>

        Args:
            service_deployment_arn: <p>The ARN of the service deployment to continue or roll back.</p>
            hook_id: <p>The ID of the paused lifecycle hook to act on. You can find the <code>hookId</code> by calling <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html\">DescribeServiceDeployments</a> and inspecting the <code>lifecycleHookDetails</code> field of the service deployment.</p>
            action: <p>The action to take on the paused lifecycle hook. Valid values are:</p> <ul> <li> <p> <code>CONTINUE</code> - Proceeds the deployment to the next lifecycle stage.</p> </li> <li> <p> <code>ROLLBACK</code> - Rolls back the deployment to the previous service revision.</p> </li> </ul> <p>If no value is specified, the default action is <code>CONTINUE</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_deployment_not_found_exception.ServiceDeploymentNotFoundException: <p>The service deploy ARN that you specified in the <code>StopServiceDeployment</code> doesn't exist. You can use <code>ListServiceDeployments</code> to retrieve the service deployment ARNs.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To continue a paused service deployment
            This example continues a service deployment that is paused at a lifecycle hook, using the CONTINUE action to proceed to the next deployment stage.

            >>> client.continue_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', hook_id='ABCDEFGHIJKLMNOPQRSTUVWXYZ234567', action='CONTINUE')
            To roll back a paused service deployment
            This example rolls back a service deployment that is paused at a lifecycle hook, using the ROLLBACK action to revert to the previous service revision.

            >>> client.continue_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', hook_id='ABCDEFGHIJKLMNOPQRSTUVWXYZ234567', action='ROLLBACK')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.continue_service_deployment_request.ContinueServiceDeploymentRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.continue_service_deployment_response.ContinueServiceDeploymentResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.continue_service_deployment

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.continue_service_deployment.continue_service_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.continue_service_deployment_request.ContinueServiceDeploymentRequest = {}  # type: ignore[typeddict-item]
        input_["service_deployment_arn"] = service_deployment_arn
        input_["hook_id"] = hook_id
        if action is not None:
            input_["action"] = action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_account_setting(
        self,
        name: "capo_ecs.types.setting_name.SettingName",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.delete_account_setting_response.DeleteAccountSettingResponse":
        """<p>Disables an account setting for a specified user, role, or the root user for an account.</p>

        Args:
            name: <p>The resource name to disable the account setting for. If <code>serviceLongArnFormat</code> is specified, the ARN for your Amazon ECS services is affected. If <code>taskLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If <code>containerInstanceLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS container instances is affected. If <code>awsvpcTrunking</code> is specified, the ENI limit for your Amazon ECS container instances is affected.</p>
            principal_arn: <p>The Amazon Resource Name (ARN) of the principal. It can be a user, role, or the root user. If you specify the root user, it disables the account setting for all users, roles, and the root user of the account unless a user or role explicitly overrides these settings. If this field is omitted, the setting is changed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete your account setting
            This example deletes the account setting for your user for the specified resource type.

            >>> client.delete_account_setting(name='serviceLongArnFormat')
            To delete the account settings for a specific IAM user or IAM role
            This example deletes the account setting for a specific IAM user or IAM role for the specified resource type. Only the root user can view or modify the account settings for another user.

            >>> client.delete_account_setting(name='containerInstanceLongArnFormat', principal_arn='arn:aws:iam::<aws_account_id>:user/principalName')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_account_setting_request.DeleteAccountSettingRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_account_setting_response.DeleteAccountSettingResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_account_setting

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_account_setting.delete_account_setting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.delete_account_setting_request.DeleteAccountSettingRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_task_definition(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.deregister_task_definition_response.DeregisterTaskDefinitionResponse":
        r"""<p>Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as <code>INACTIVE</code>. Existing tasks and services that reference an <code>INACTIVE</code> task definition continue to run without disruption. Existing services that reference an <code>INACTIVE</code> task definition can still scale up or down by modifying the service's desired count. If you want to delete a task definition revision, you must first deregister the task definition revision.</p> <p>You can't use an <code>INACTIVE</code> task definition to run new tasks or create new services, and you can't update an existing service to reference an <code>INACTIVE</code> task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.</p> <note> <p>At this time, <code>INACTIVE</code> task definitions remain discoverable in your account indefinitely. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> task definitions persisting beyond the lifecycle of any associated tasks and services.</p> </note> <p>You must deregister a task definition revision before you delete it. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskDefinitions.html\">DeleteTaskDefinitions</a>.</p>

        Args:
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a <code>revision</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a revision of a task definition
            This example deregisters the first revision of the fargate-task task definition

            >>> client.deregister_task_definition(task_definition='fargate-task:1')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.deregister_task_definition_request.DeregisterTaskDefinitionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.deregister_task_definition_response.DeregisterTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_task_definition

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_task_definition.deregister_task_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.deregister_task_definition_request.DeregisterTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["task_definition"] = task_definition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_task_definition(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        include: Optional[
            "capo_ecs.types.task_definition_field_list.TaskDefinitionFieldList"
        ] = None,
    ) -> "capo_ecs.types.describe_task_definition_response.DescribeTaskDefinitionResponse":
        """<p>Describes a task definition. You can specify a <code>family</code> and <code>revision</code> to find information about a specific task definition, or you can simply specify the family to find the latest <code>ACTIVE</code> revision in that family.</p> <note> <p>You can only describe <code>INACTIVE</code> task definitions while an active task or service references them.</p> </note>

        Args:
            task_definition: <p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.</p>
            include: <p>Determines whether to see the resource tags for the task definition. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a task definition
            This example provides a description of the specified task definition.

            >>> client.describe_task_definition(task_definition='hello_world:8')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_task_definition_request.DescribeTaskDefinitionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_task_definition_response.DescribeTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_definition

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_task_definition.describe_task_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.describe_task_definition_request.DescribeTaskDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["task_definition"] = task_definition
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def discover_poll_endpoint(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        container_instance: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.discover_poll_endpoint_response.DiscoverPollEndpointResponse":
        r"""<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Returns an endpoint for the Amazon ECS agent to poll for updates.</p>

        Args:
            container_instance: <p>The container instance ID or full ARN of the container instance. For more information about the ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids\">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.discover_poll_endpoint_request.DiscoverPollEndpointRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.discover_poll_endpoint_response.DiscoverPollEndpointResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.discover_poll_endpoint

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.discover_poll_endpoint.discover_poll_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.discover_poll_endpoint_request.DiscoverPollEndpointRequest = {}  # type: ignore[typeddict-item]
        if container_instance is not None:
            input_["container_instance"] = container_instance
        if cluster is not None:
            input_["cluster"] = cluster

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_account_settings(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        name: Optional["capo_ecs.types.setting_name.SettingName"] = None,
        value: Optional["capo_ecs.types.string.String"] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
        effective_settings: Optional["capo_ecs.types.boolean.Boolean"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.integer.Integer"] = None,
    ) -> "capo_ecs.types.list_account_settings_response.ListAccountSettingsResponse":
        """<p>Lists the account settings for a specified principal.</p>

        Args:
            name: <p>The name of the account setting you want to list the settings for.</p>
            value: <p>The value of the account settings to filter results with. You must also specify an account setting name to use this parameter.</p>
            principal_arn: <p>The ARN of the principal, which can be a user, role, or the root user. If this field is omitted, the account settings are listed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p> <note> <p>Federated users assume the account setting of the root user and can't have explicit account settings set for them.</p> </note>
            effective_settings: <p>Determines whether to return the effective settings. If <code>true</code>, the account settings for the root user or the default setting for the <code>principalArn</code> are returned. If <code>false</code>, the account settings for the <code>principalArn</code> are returned if they're set. Otherwise, no account settings are returned.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListAccountSettings</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of account setting results returned by <code>ListAccountSettings</code> in paginated output. When this parameter is used, <code>ListAccountSettings</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAccountSettings</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 10. If this parameter isn't used, then <code>ListAccountSettings</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view your effective account settings
            This example displays the effective account settings for your account.

            >>> client.list_account_settings(effective_settings=True)
            To view the effective account settings for a specific IAM user or IAM role
            This example displays the effective account settings for the specified user or role.

            >>> client.list_account_settings(effective_settings=True, principal_arn='arn:aws:iam::<aws_account_id>:user/principalName')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_account_settings_request.ListAccountSettingsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_account_settings_response.ListAccountSettingsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_account_settings

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_account_settings.list_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_account_settings_request.ListAccountSettingsRequest = {}  # type: ignore[typeddict-item]
        if name is not None:
            input_["name"] = name
        if value is not None:
            input_["value"] = value
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn
        if effective_settings is not None:
            input_["effective_settings"] = effective_settings
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

    def iter_list_account_settings(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        name: Optional["capo_ecs.types.setting_name.SettingName"] = None,
        value: Optional["capo_ecs.types.string.String"] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
        effective_settings: Optional["capo_ecs.types.boolean.Boolean"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.integer.Integer"] = None,
    ) -> "Iterator[capo_ecs.types.setting.Setting]":
        _token = next_token
        while True:
            _response = self.list_account_settings(
                config_overrides=config_overrides,
                name=name,
                value=value,
                principal_arn=principal_arn,
                effective_settings=effective_settings,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("settings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services_by_namespace(
        self,
        namespace: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_services_by_namespace_response.ListServicesByNamespaceResponse":
        r"""<p>This operation lists all of the services that are associated with a Cloud Map namespace. This list might include services in different clusters. In contrast, <code>ListServices</code> can only list services in one cluster at a time. If you need to filter the list of services in a single cluster by various parameters, use <code>ListServices</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            namespace: <p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace to list the services in.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            next_token: <p>The <code>nextToken</code> value that's returned from a <code>ListServicesByNamespace</code> request. It indicates that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> is returned, it is possible the number of results is less than <code>maxResults</code>.</p>
            max_results: <p>The maximum number of service results that <code>ListServicesByNamespace</code> returns in paginated output. When this parameter is used, <code>ListServicesByNamespace</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServicesByNamespace</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServicesByNamespace</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_services_by_namespace_request.ListServicesByNamespaceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_services_by_namespace_response.ListServicesByNamespaceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services_by_namespace

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services_by_namespace.list_services_by_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_services_by_namespace_request.ListServicesByNamespaceRequest = {}  # type: ignore[typeddict-item]
        input_["namespace"] = namespace
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

    def iter_list_services_by_namespace(
        self,
        namespace: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "Iterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_services_by_namespace(
                namespace,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("service_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags for an Amazon ECS resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon ECS tasks, services, task definitions, clusters, and container instances.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html\">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the tags for a cluster.
            This example lists the tags for the 'dev' cluster.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:ecs:region:aws_account_id:cluster/dev')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_tags_for_resource

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_task_definition_families(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_family_status.TaskDefinitionFamilyStatus"
        ] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_task_definition_families_response.ListTaskDefinitionFamiliesResponse":
        """<p>Returns a list of task definition families that are registered to your account. This list includes task definition families that no longer have any <code>ACTIVE</code> task definition revisions.</p> <p>You can filter out task definition families that don't contain any <code>ACTIVE</code> task definition revisions by setting the <code>status</code> parameter to <code>ACTIVE</code>. You can also filter the results with the <code>familyPrefix</code> parameter.</p>

        Args:
            family_prefix: <p>The <code>familyPrefix</code> is a string that's used to filter the results of <code>ListTaskDefinitionFamilies</code>. If you specify a <code>familyPrefix</code>, only task definition family names that begin with the <code>familyPrefix</code> string are returned.</p>
            status: <p>The task definition family status to filter the <code>ListTaskDefinitionFamilies</code> results with. By default, both <code>ACTIVE</code> and <code>INACTIVE</code> task definition families are listed. If this parameter is set to <code>ACTIVE</code>, only task definition families that have an <code>ACTIVE</code> task definition revision are returned. If this parameter is set to <code>INACTIVE</code>, only task definition families that do not have any <code>ACTIVE</code> task definition revisions are returned. If you paginate the resulting output, be sure to keep the <code>status</code> value constant in each subsequent request.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTaskDefinitionFamilies</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task definition family results that <code>ListTaskDefinitionFamilies</code> returned in paginated output. When this parameter is used, <code>ListTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTaskDefinitionFamilies</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTaskDefinitionFamilies</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your registered task definition families
            This example lists all of your registered task definition families.

            >>> client.list_task_definition_families()
            To filter your registered task definition families
            This example lists the task definition revisions that start with "hpcc".

            >>> client.list_task_definition_families(family_prefix='hpcc')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_task_definition_families_request.ListTaskDefinitionFamiliesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_task_definition_families_response.ListTaskDefinitionFamiliesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definition_families

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definition_families.list_task_definition_families(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.list_task_definition_families_request.ListTaskDefinitionFamiliesRequest = {}  # type: ignore[typeddict-item]
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if status is not None:
            input_["status"] = status
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

    def iter_list_task_definition_families(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_family_status.TaskDefinitionFamilyStatus"
        ] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "Iterator[capo_ecs.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_task_definition_families(
                config_overrides=config_overrides,
                family_prefix=family_prefix,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("families",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_account_setting(
        self,
        name: "capo_ecs.types.setting_name.SettingName",
        value: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        principal_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.put_account_setting_response.PutAccountSettingResponse":
        r"""<p>Modifies an account setting. Account settings are set on a per-Region basis.</p> <p>If you change the root user account setting, the default settings are reset for users and roles that do not have specified individual account settings. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html\">Account Settings</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            name: <p>The Amazon ECS account setting name to modify.</p> <p>The following are the valid values for the account setting name.</p> <ul> <li> <p> <code>serviceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>taskLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>containerInstanceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>awsvpcTrunking</code> - When modified, the elastic network interface (ENI) limit for any new container instances that support the feature is changed. If <code>awsvpcTrunking</code> is turned on, any new container instances that support the feature are launched have the increased ENI limits available to them. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html\">Elastic Network Interface Trunking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>containerInsights</code> - Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up. </p> <p>To use Container Insights with enhanced observability, set the <code>containerInsights</code> account setting to <code>enhanced</code>.</p> <p>To use Container Insights, set the <code>containerInsights</code> account setting to <code>enabled</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html\">Monitor Amazon ECS containers using Container Insights with enhanced observability</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>dualStackIPv6</code> - When turned on, when using a VPC in dual stack mode, your tasks using the <code>awsvpc</code> network mode can have an IPv6 address assigned. For more information on using IPv6 with tasks launched on Amazon EC2 instances, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html#task-networking-vpc-dual-stack\">Using a VPC in dual-stack mode</a>. For more information on using IPv6 with tasks launched on Fargate, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html#fargate-task-networking-vpc-dual-stack\">Using a VPC in dual-stack mode</a>.</p> </li> <li> <p> <code>fargateTaskRetirementWaitPeriod</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateTaskRetirementWaitPeriod</code> to configure the wait time to retire a Fargate task. For information about the Fargate tasks maintenance, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html\">Amazon Web Services Fargate task maintenance</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>fargateEventWindows</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateEventWindows</code> to use EC2 Event Windows associated with Fargate tasks to configure time windows for task retirement.</p> </li> <li> <p> <code>tagResourceAuthorization</code> - Amazon ECS is introducing tagging authorization for resource creation. Users must have permissions for actions that create the resource, such as <code>ecsCreateCluster</code>. If tags are specified when you create a resource, Amazon Web Services performs additional authorization to verify if users or roles have permissions to create tags. Therefore, you must grant explicit permissions to use the <code>ecs:TagResource</code> action. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html\">Grant permission to tag resources on creation</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>defaultLogDriverMode</code> - Amazon ECS supports setting a default delivery mode of log messages from a container to the <code>logDriver</code> that you specify in the container's <code>logConfiguration</code>. The delivery mode affects application stability when the flow of logs from the container to the log driver is interrupted. The <code>defaultLogDriverMode</code> setting supports two values: <code>blocking</code> and <code>non-blocking</code>. If you don't specify a delivery mode in your container definition's <code>logConfiguration</code>, the mode you specify using this account setting will be used as the default. For more information about log delivery modes, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html\">LogConfiguration</a>. </p> <note> <p>On June 25, 2025, Amazon ECS changed the default log driver mode from <code>blocking</code> to <code>non-blocking</code> to prioritize task availability over logging. To continue using the <code>blocking</code> mode after this change, do one of the following:</p> <ul> <li> <p>Set the <code>mode</code> option in your container definition's <code>logConfiguration</code> as <code>blocking</code>.</p> </li> <li> <p>Set the <code>defaultLogDriverMode</code> account setting to <code>blocking</code>.</p> </li> </ul> </note> </li> <li> <p> <code>guardDutyActivate</code> - The <code>guardDutyActivate</code> parameter is read-only in Amazon ECS and indicates whether Amazon ECS Runtime Monitoring is enabled or disabled by your security administrator in your Amazon ECS account. Amazon GuardDuty controls this account setting on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-integration.html\">Protecting Amazon ECS workloads with Amazon ECS Runtime Monitoring</a>.</p> </li> </ul>
            value: <p>The account setting value for the specified principal ARN. Accepted values are <code>enabled</code>, <code>disabled</code>, <code>enhanced</code>, <code>on</code>, and <code>off</code>.</p> <p>When you specify <code>fargateTaskRetirementWaitPeriod</code> for the <code>name</code>, the following are the valid values:</p> <ul> <li> <p> <code>0</code> - Amazon Web Services sends the notification, and immediately retires the affected tasks.</p> </li> <li> <p> <code>7</code> - Amazon Web Services sends the notification, and waits 7 calendar days to retire the tasks.</p> </li> <li> <p> <code>14</code> - Amazon Web Services sends the notification, and waits 14 calendar days to retire the tasks.</p> </li> </ul>
            principal_arn: <p>The ARN of the principal, which can be a user, role, or the root user. If you specify the root user, it modifies the account setting for all users, roles, and the root user of the account unless a user or role explicitly overrides these settings. If this field is omitted, the setting is changed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p> <note> <p>You must use the root user when you set the Fargate wait time (<code>fargateTaskRetirementWaitPeriod</code>). </p> <p>Federated users assume the account setting of the root user and can't have explicit account settings set for them.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify your account settings
            This example modifies your account settings to opt in to the new ARN and resource ID format for Amazon ECS services. If you’re using this command as the root user, then changes apply to the entire AWS account, unless an IAM user or role explicitly overrides these settings for themselves.

            >>> client.put_account_setting(name='serviceLongArnFormat', value='enabled')
            To modify the account settings for a specific IAM user or IAM role
            This example modifies the account setting for a specific IAM user or IAM role to opt in to the new ARN and resource ID format for Amazon ECS container instances. If you’re using this command as the root user, then changes apply to the entire AWS account, unless an IAM user or role explicitly overrides these settings for themselves.

            >>> client.put_account_setting(name='containerInstanceLongArnFormat', value='enabled', principal_arn='arn:aws:iam::<aws_account_id>:user/principalName')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.put_account_setting_request.PutAccountSettingRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.put_account_setting_response.PutAccountSettingResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting.put_account_setting(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.put_account_setting_request.PutAccountSettingRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["value"] = value
        if principal_arn is not None:
            input_["principal_arn"] = principal_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_account_setting_default(
        self,
        name: "capo_ecs.types.setting_name.SettingName",
        value: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.put_account_setting_default_response.PutAccountSettingDefaultResponse":
        r"""<p>Modifies an account setting for all users on an account for whom no individual account setting has been specified. Account settings are set on a per-Region basis.</p>

        Args:
            name: <p>The resource name for which to modify the account setting.</p> <p>The following are the valid values for the account setting name.</p> <ul> <li> <p> <code>serviceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>taskLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>containerInstanceLongArnFormat</code> - When modified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.</p> </li> <li> <p> <code>awsvpcTrunking</code> - When modified, the elastic network interface (ENI) limit for any new container instances that support the feature is changed. If <code>awsvpcTrunking</code> is turned on, any new container instances that support the feature are launched have the increased ENI limits available to them. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html\">Elastic Network Interface Trunking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>containerInsights</code> - Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up. </p> <p>To use Container Insights with enhanced observability, set the <code>containerInsights</code> account setting to <code>enhanced</code>.</p> <p>To use Container Insights, set the <code>containerInsights</code> account setting to <code>enabled</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html\">Monitor Amazon ECS containers using Container Insights with enhanced observability</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>dualStackIPv6</code> - When turned on, when using a VPC in dual stack mode, your tasks using the <code>awsvpc</code> network mode can have an IPv6 address assigned. For more information on using IPv6 with tasks launched on Amazon EC2 instances, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html#task-networking-vpc-dual-stack\">Using a VPC in dual-stack mode</a>. For more information on using IPv6 with tasks launched on Fargate, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html#fargate-task-networking-vpc-dual-stack\">Using a VPC in dual-stack mode</a>.</p> </li> <li> <p> <code>fargateFIPSMode</code> - If you specify <code>fargateFIPSMode</code>, Fargate FIPS 140 compliance is affected.</p> </li> <li> <p> <code>fargateTaskRetirementWaitPeriod</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateTaskRetirementWaitPeriod</code> to configure the wait time to retire a Fargate task. For information about the Fargate tasks maintenance, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html\">Amazon Web Services Fargate task maintenance</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>fargateEventWindows</code> - When Amazon Web Services determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched to replace them. Use <code>fargateEventWindows</code> to use EC2 Event Windows associated with Fargate tasks to configure time windows for task retirement.</p> </li> <li> <p> <code>tagResourceAuthorization</code> - Amazon ECS is introducing tagging authorization for resource creation. Users must have permissions for actions that create the resource, such as <code>ecsCreateCluster</code>. If tags are specified when you create a resource, Amazon Web Services performs additional authorization to verify if users or roles have permissions to create tags. Therefore, you must grant explicit permissions to use the <code>ecs:TagResource</code> action. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html\">Grant permission to tag resources on creation</a> in the <i>Amazon ECS Developer Guide</i>.</p> </li> <li> <p> <code>defaultLogDriverMode</code> -Amazon ECS supports setting a default delivery mode of log messages from a container to the <code>logDriver</code> that you specify in the container's <code>logConfiguration</code>. The delivery mode affects application stability when the flow of logs from the container to the log driver is interrupted. The <code>defaultLogDriverMode</code> setting supports two values: <code>blocking</code> and <code>non-blocking</code>. If you don't specify a delivery mode in your container definition's <code>logConfiguration</code>, the mode you specify using this account setting will be used as the default. For more information about log delivery modes, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html\">LogConfiguration</a>.</p> <note> <p>On June 25, 2025, Amazon ECS changed the default log driver mode from <code>blocking</code> to <code>non-blocking</code> to prioritize task availability over logging. To continue using the <code>blocking</code> mode after this change, do one of the following:</p> <ul> <li> <p>Set the <code>mode</code> option in your container definition's <code>logConfiguration</code> as <code>blocking</code>.</p> </li> <li> <p>Set the <code>defaultLogDriverMode</code> account setting to <code>blocking</code>.</p> </li> </ul> </note> </li> <li> <p> <code>guardDutyActivate</code> - The <code>guardDutyActivate</code> parameter is read-only in Amazon ECS and indicates whether Amazon ECS Runtime Monitoring is enabled or disabled by your security administrator in your Amazon ECS account. Amazon GuardDuty controls this account setting on your behalf. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-integration.html\">Protecting Amazon ECS workloads with Amazon ECS Runtime Monitoring</a>.</p> </li> </ul>
            value: <p>The account setting value for the specified principal ARN. Accepted values are <code>enabled</code>, <code>disabled</code>, <code>on</code>, <code>enhanced</code>, and <code>off</code>.</p> <p>When you specify <code>fargateTaskRetirementWaitPeriod</code> for the <code>name</code>, the following are the valid values:</p> <ul> <li> <p> <code>0</code> - Amazon Web Services sends the notification, and immediately retires the affected tasks.</p> </li> <li> <p> <code>7</code> - Amazon Web Services sends the notification, and waits 7 calendar days to retire the tasks.</p> </li> <li> <p> <code>14</code> - Amazon Web Services sends the notification, and waits 14 calendar days to retire the tasks.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To modify the default account settings for all IAM users or roles on an account
            This example modifies the default account setting for the specified resource for all IAM users or roles on an account. These changes apply to the entire AWS account, unless an IAM user or role explicitly overrides these settings for themselves.

            >>> client.put_account_setting_default(name='serviceLongArnFormat', value='enabled')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.put_account_setting_default_request.PutAccountSettingDefaultRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.put_account_setting_default_response.PutAccountSettingDefaultResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting_default

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.put_account_setting_default.put_account_setting_default(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.put_account_setting_default_request.PutAccountSettingDefaultRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["value"] = value

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_ecs.types.string.String",
        tags: "capo_ecs.types.tags.Tags",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.tag_resource_response.TagResourceResponse":
        r"""<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags that are associated with that resource are deleted as well.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p> <p>In order to tag a service that has the following ARN format, you need to migrate the service to the long ARN. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-arn-migration.html\">Migrate an Amazon ECS short service ARN to a long ARN</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p> <code>arn:aws:ecs:region:aws_account_id:service/service-name</code> </p> <p>After the migration is complete, the service has the long ARN format, as shown below. Use this ARN to tag the service.</p> <p> <code>arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name</code> </p> <p>If you try to tag a service with a short ARN, you receive an <code>InvalidParameterException</code> error.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html\">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To tag a cluster.
            This example tags the 'dev' cluster with key 'team' and value 'dev'.

            >>> client.tag_resource(resource_arn='arn:aws:ecs:region:aws_account_id:cluster/dev', tags=[{'key': 'team', 'value': 'dev'}])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.tag_resource

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_ecs.types.string.String",
        tag_keys: "capo_ecs.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html\">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html\">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To untag a cluster.
            This example deletes the 'team' tag from the 'dev' cluster.

            >>> client.untag_resource(resource_arn='arn:aws:ecs:region:aws_account_id:cluster/dev', tag_keys=['team'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.untag_resource

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ecs.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
