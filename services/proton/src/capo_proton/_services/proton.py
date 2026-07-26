"""Generated from Smithy shape ``com.amazonaws.proton#AwsProton20200720``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_proton._auth._signers
import capo_proton._auth._sigv4
from capo_proton._auth._identity import Credentials
from capo_proton._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_proton._auth._zapros_handler import AuthMiddleware
from capo_proton._pagination import resolve_path as _resolve_path
from capo_proton._resources.aws_proton20200720.account_settings_resource import (
    AccountSettingsResource,
)
from capo_proton._resources.aws_proton20200720.component_output_resource import (
    ComponentOutputResource,
)
from capo_proton._resources.aws_proton20200720.component_provisioned_resource_resource import (
    ComponentProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.component_resource import (
    ComponentResource,
)
from capo_proton._resources.aws_proton20200720.deployment_resource import (
    DeploymentResource,
)
from capo_proton._resources.aws_proton20200720.environment_account_connection_resource import (
    EnvironmentAccountConnectionResource,
)
from capo_proton._resources.aws_proton20200720.environment_output_resource import (
    EnvironmentOutputResource,
)
from capo_proton._resources.aws_proton20200720.environment_provisioned_resource_resource import (
    EnvironmentProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.environment_resource import (
    EnvironmentResource,
)
from capo_proton._resources.aws_proton20200720.environment_template_resource import (
    EnvironmentTemplateResource,
)
from capo_proton._resources.aws_proton20200720.environment_template_version_resource import (
    EnvironmentTemplateVersionResource,
)
from capo_proton._resources.aws_proton20200720.repository_resource import (
    RepositoryResource,
)
from capo_proton._resources.aws_proton20200720.service_instance_output_resource import (
    ServiceInstanceOutputResource,
)
from capo_proton._resources.aws_proton20200720.service_instance_provisioned_resource_resource import (
    ServiceInstanceProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.service_instance_resource import (
    ServiceInstanceResource,
)
from capo_proton._resources.aws_proton20200720.service_pipeline_output_resource import (
    ServicePipelineOutputResource,
)
from capo_proton._resources.aws_proton20200720.service_pipeline_provisioned_resource_resource import (
    ServicePipelineProvisionedResourceResource,
)
from capo_proton._resources.aws_proton20200720.service_pipeline_resource import (
    ServicePipelineResource,
)
from capo_proton._resources.aws_proton20200720.service_resource import ServiceResource
from capo_proton._resources.aws_proton20200720.service_sync_blocker_resource import (
    ServiceSyncBlockerResource,
)
from capo_proton._resources.aws_proton20200720.service_sync_config_resource import (
    ServiceSyncConfigResource,
)
from capo_proton._resources.aws_proton20200720.service_template_resource import (
    ServiceTemplateResource,
)
from capo_proton._resources.aws_proton20200720.service_template_version_resource import (
    ServiceTemplateVersionResource,
)
from capo_proton._resources.aws_proton20200720.template_sync_config_resource import (
    TemplateSyncConfigResource,
)
from capo_proton._services._aws_config import aws_config
from capo_proton._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.cancel_component_deployment_input
    import capo_proton.types.cancel_component_deployment_output
    import capo_proton.types.cancel_environment_deployment_input
    import capo_proton.types.cancel_environment_deployment_output
    import capo_proton.types.cancel_service_instance_deployment_input
    import capo_proton.types.cancel_service_instance_deployment_output
    import capo_proton.types.cancel_service_pipeline_deployment_input
    import capo_proton.types.cancel_service_pipeline_deployment_output
    import capo_proton.types.deployment_id
    import capo_proton.types.empty_next_token
    import capo_proton.types.get_repository_sync_status_input
    import capo_proton.types.get_repository_sync_status_output
    import capo_proton.types.get_resources_summary_input
    import capo_proton.types.get_resources_summary_output
    import capo_proton.types.get_service_instance_sync_status_input
    import capo_proton.types.get_service_instance_sync_status_output
    import capo_proton.types.get_template_sync_status_input
    import capo_proton.types.get_template_sync_status_output
    import capo_proton.types.git_branch_name
    import capo_proton.types.list_repository_sync_definitions_input
    import capo_proton.types.list_repository_sync_definitions_output
    import capo_proton.types.list_tags_for_resource_input
    import capo_proton.types.list_tags_for_resource_output
    import capo_proton.types.max_page_results
    import capo_proton.types.notify_resource_deployment_status_change_input
    import capo_proton.types.notify_resource_deployment_status_change_output
    import capo_proton.types.outputs_list
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.repository_sync_definition
    import capo_proton.types.resource_deployment_status
    import capo_proton.types.resource_name
    import capo_proton.types.status_message
    import capo_proton.types.sync_type
    import capo_proton.types.tag
    import capo_proton.types.tag_key_list
    import capo_proton.types.tag_list
    import capo_proton.types.tag_resource_input
    import capo_proton.types.tag_resource_output
    import capo_proton.types.template_type
    import capo_proton.types.template_version_part
    import capo_proton.types.untag_resource_input
    import capo_proton.types.untag_resource_output


class ProtonClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ProtonClient:
    """A client for the ``Proton`` service.

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
        self._config = ProtonClientConfig(
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
        self.account_settings_resource = AccountSettingsResource(self)
        self.component_output_resource = ComponentOutputResource(self)
        self.component_provisioned_resource_resource = (
            ComponentProvisionedResourceResource(self)
        )
        self.component_resource = ComponentResource(self)
        self.deployment_resource = DeploymentResource(self)
        self.environment_account_connection_resource = (
            EnvironmentAccountConnectionResource(self)
        )
        self.environment_output_resource = EnvironmentOutputResource(self)
        self.environment_provisioned_resource_resource = (
            EnvironmentProvisionedResourceResource(self)
        )
        self.environment_resource = EnvironmentResource(self)
        self.environment_template_resource = EnvironmentTemplateResource(self)
        self.environment_template_version_resource = EnvironmentTemplateVersionResource(
            self
        )
        self.repository_resource = RepositoryResource(self)
        self.service_instance_output_resource = ServiceInstanceOutputResource(self)
        self.service_instance_provisioned_resource_resource = (
            ServiceInstanceProvisionedResourceResource(self)
        )
        self.service_instance_resource = ServiceInstanceResource(self)
        self.service_pipeline_output_resource = ServicePipelineOutputResource(self)
        self.service_pipeline_provisioned_resource_resource = (
            ServicePipelineProvisionedResourceResource(self)
        )
        self.service_pipeline_resource = ServicePipelineResource(self)
        self.service_resource = ServiceResource(self)
        self.service_sync_blocker_resource = ServiceSyncBlockerResource(self)
        self.service_sync_config_resource = ServiceSyncConfigResource(self)
        self.service_template_resource = ServiceTemplateResource(self)
        self.service_template_version_resource = ServiceTemplateVersionResource(self)
        self.template_sync_config_resource = TemplateSyncConfigResource(self)

    def operation_options(
        self, config_overrides: Optional[ProtonClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ProtonClientConfig = config_overrides or {}
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

    def cancel_component_deployment(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_component_deployment_output.CancelComponentDeploymentOutput":
        r"""<p>Attempts to cancel a component deployment (for a component that is in the <code>IN_PROGRESS</code> deployment status).</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component with the deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.cancel_component_deployment_input.CancelComponentDeploymentInput]",
        ) -> OperationResponse[
            "capo_proton.types.cancel_component_deployment_output.CancelComponentDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_component_deployment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.cancel_component_deployment.cancel_component_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_component_deployment_input.CancelComponentDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["component_name"] = component_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_environment_deployment(
        self,
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_environment_deployment_output.CancelEnvironmentDeploymentOutput":
        r"""<p>Attempts to cancel an environment deployment on an <a>UpdateEnvironment</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html\">Update an environment</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateEnvironment</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            environment_name: <p>The name of the environment with the deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.cancel_environment_deployment_input.CancelEnvironmentDeploymentInput]",
        ) -> OperationResponse[
            "capo_proton.types.cancel_environment_deployment_output.CancelEnvironmentDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_environment_deployment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.cancel_environment_deployment.cancel_environment_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_environment_deployment_input.CancelEnvironmentDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["environment_name"] = environment_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_service_instance_deployment(
        self,
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_service_instance_deployment_output.CancelServiceInstanceDeploymentOutput":
        r"""<p>Attempts to cancel a service instance deployment on an <a>UpdateServiceInstance</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html\">Update a service instance</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServiceInstance</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            service_instance_name: <p>The name of the service instance with the deployment to cancel.</p>
            service_name: <p>The name of the service with the service instance deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.cancel_service_instance_deployment_input.CancelServiceInstanceDeploymentInput]",
        ) -> OperationResponse[
            "capo_proton.types.cancel_service_instance_deployment_output.CancelServiceInstanceDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_service_instance_deployment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.cancel_service_instance_deployment.cancel_service_instance_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_service_instance_deployment_input.CancelServiceInstanceDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["service_instance_name"] = service_instance_name
        input_["service_name"] = service_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_service_pipeline_deployment(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.cancel_service_pipeline_deployment_output.CancelServicePipelineDeploymentOutput":
        r"""<p>Attempts to cancel a service pipeline deployment on an <a>UpdateServicePipeline</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html\">Update a service pipeline</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServicePipeline</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            service_name: <p>The name of the service with the service pipeline deployment to cancel.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.cancel_service_pipeline_deployment_input.CancelServicePipelineDeploymentInput]",
        ) -> OperationResponse[
            "capo_proton.types.cancel_service_pipeline_deployment_output.CancelServicePipelineDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.cancel_service_pipeline_deployment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.cancel_service_pipeline_deployment.cancel_service_pipeline_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.cancel_service_pipeline_deployment_input.CancelServicePipelineDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_repository_sync_status(
        self,
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        sync_type: "capo_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput":
        r"""<p>Get the sync status of a repository used for Proton template sync. For more information about template sync, see .</p> <note> <p>A repository sync status isn't tied to the Proton Repository resource (or any other Proton resource). Therefore, tags on an Proton Repository resource have no effect on this action. Specifically, you can't use these tags to control access to this action using Attribute-based access control (ABAC).</p> <p>For more information about ABAC, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags\">ABAC</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            repository_name: <p>The repository name.</p>
            repository_provider: <p>The repository provider.</p>
            branch: <p>The repository branch.</p>
            sync_type: <p>The repository sync type.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_repository_sync_status_input.GetRepositorySyncStatusInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_repository_sync_status

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_repository_sync_status.get_repository_sync_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_repository_sync_status_input.GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["repository_provider"] = repository_provider
        input_["branch"] = branch
        input_["sync_type"] = sync_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resources_summary(
        self, *, config_overrides: Optional[ProtonClientConfig] = None
    ) -> "capo_proton.types.get_resources_summary_output.GetResourcesSummaryOutput":
        r"""<p>Get counts of Proton resources.</p> <p>For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it's behind the recommended version of the Proton template that it uses and it needs an update to become current.</p> <p>The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the <code>components</code>, <code>environments</code>, and <code>serviceTemplates</code> field descriptions.</p> <p>For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html\">Proton dashboard</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_resources_summary_input.GetResourcesSummaryInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_resources_summary_output.GetResourcesSummaryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_resources_summary

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_resources_summary.get_resources_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_resources_summary_input.GetResourcesSummaryInput = {}  # type: ignore[typeddict-item]

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_service_instance_sync_status(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_instance_sync_status_output.GetServiceInstanceSyncStatusOutput":
        """<p>Get the status of the synced service instance.</p>

        Args:
            service_name: <p>The name of the service that the service instance belongs to.</p>
            service_instance_name: <p>The name of the service instance that you want the sync status input for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_service_instance_sync_status_input.GetServiceInstanceSyncStatusInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_service_instance_sync_status_output.GetServiceInstanceSyncStatusOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_instance_sync_status

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_service_instance_sync_status.get_service_instance_sync_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_service_instance_sync_status_input.GetServiceInstanceSyncStatusInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name
        input_["service_instance_name"] = service_instance_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_template_sync_status(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        template_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> (
        "capo_proton.types.get_template_sync_status_output.GetTemplateSyncStatusOutput"
    ):
        """<p>Get the status of a template sync.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>
            template_version: <p>The template major version.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_template_sync_status_input.GetTemplateSyncStatusInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_template_sync_status_output.GetTemplateSyncStatusOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_template_sync_status

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_template_sync_status.get_template_sync_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.get_template_sync_status_input.GetTemplateSyncStatusInput = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        input_["template_type"] = template_type
        input_["template_version"] = template_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_repository_sync_definitions(
        self,
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        sync_type: "capo_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput":
        """<p>List repository sync definitions with detail data.</p>

        Args:
            repository_name: <p>The repository name.</p>
            repository_provider: <p>The repository provider.</p>
            sync_type: <p>The sync type. The only supported value is <code>TEMPLATE_SYNC</code>.</p>
            next_token: <p>A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the list of repository sync definitions previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_repository_sync_definitions

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_repository_sync_definitions.list_repository_sync_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["repository_provider"] = repository_provider
        input_["sync_type"] = sync_type
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def iter_list_repository_sync_definitions(
        self,
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        sync_type: "capo_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "Iterator[capo_proton.types.repository_sync_definition.RepositorySyncDefinition]":
        _token = next_token
        while True:
            _response = self.list_repository_sync_definitions(
                repository_name,
                repository_provider,
                sync_type,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sync_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>List tags for a resource. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for the listed tags.</p>
            next_token: <p>A token that indicates the location of the next resource tag in the array of resource tags, after the list of resource tags that was previously requested.</p>
            max_results: <p>The maximum number of tags to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_tags_for_resource

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
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

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "Iterator[capo_proton.types.tag.Tag]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def notify_resource_deployment_status_change(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        status: Optional[
            "capo_proton.types.resource_deployment_status.ResourceDeploymentStatus"
        ] = None,
        outputs: Optional["capo_proton.types.outputs_list.OutputsList"] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
        status_message: Optional[
            "capo_proton.types.status_message.StatusMessage"
        ] = None,
    ) -> "capo_proton.types.notify_resource_deployment_status_change_output.NotifyResourceDeploymentStatusChangeOutput":
        r"""<p>Notify Proton of status changes to a provisioned resource when you use self-managed provisioning.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The provisioned resource Amazon Resource Name (ARN).</p>
            status: <p>The status of your provisioned resource.</p>
            outputs: <p>The provisioned resource state change detail data that's returned by Proton.</p>
            deployment_id: <p>The deployment ID for your provisioned resource.</p>
            status_message: <p>The deployment status message for your provisioned resource.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html\">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.notify_resource_deployment_status_change_input.NotifyResourceDeploymentStatusChangeInput]",
        ) -> OperationResponse[
            "capo_proton.types.notify_resource_deployment_status_change_output.NotifyResourceDeploymentStatusChangeOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.notify_resource_deployment_status_change

            output, http_response = (
                capo_proton._operations.aws_proton20200720.notify_resource_deployment_status_change.notify_resource_deployment_status_change(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.notify_resource_deployment_status_change_input.NotifyResourceDeploymentStatusChangeInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if status is not None:
            input_["status"] = status
        if outputs is not None:
            input_["outputs"] = outputs
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if status_message is not None:
            input_["status_message"] = status_message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_proton.types.arn.Arn",
        tags: "capo_proton.types.tag_list.TagList",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.tag_resource_output.TagResourceOutput":
        r"""<p>Tag a resource. A tag is a key-value pair of metadata that you associate with an Proton resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Proton resource to apply customer tags to.</p>
            tags: <p>A list of customer tags to apply to the Proton resource.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_proton.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.tag_resource

            output, http_response = (
                capo_proton._operations.aws_proton20200720.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_proton.types.arn.Arn",
        tag_keys: "capo_proton.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.untag_resource_output.UntagResourceOutput":
        r"""<p>Remove a customer tag from a resource. A tag is a key-value pair of metadata associated with an Proton resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove customer tags from.</p>
            tag_keys: <p>A list of customer tag keys that indicate the customer tags to be removed from the resource.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_proton.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.untag_resource

            output, http_response = (
                capo_proton._operations.aws_proton20200720.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_proton.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
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
