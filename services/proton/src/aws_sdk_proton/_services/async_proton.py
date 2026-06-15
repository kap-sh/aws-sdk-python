"""Generated from Smithy shape ``com.amazonaws.proton#AwsProton20200720``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_proton._auth._signers
import aws_sdk_proton._auth._sigv4
from aws_sdk_proton._auth._identity import Credentials
from aws_sdk_proton._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_proton._auth._zapros_handler import AuthMiddleware
from aws_sdk_proton._pagination import resolve_path as _resolve_path
from aws_sdk_proton._resources.aws_proton20200720.account_settings_resource import (
    AsyncAccountSettingsResource,
)
from aws_sdk_proton._resources.aws_proton20200720.component_output_resource import (
    AsyncComponentOutputResource,
)
from aws_sdk_proton._resources.aws_proton20200720.component_provisioned_resource_resource import (
    AsyncComponentProvisionedResourceResource,
)
from aws_sdk_proton._resources.aws_proton20200720.component_resource import (
    AsyncComponentResource,
)
from aws_sdk_proton._resources.aws_proton20200720.deployment_resource import (
    AsyncDeploymentResource,
)
from aws_sdk_proton._resources.aws_proton20200720.environment_account_connection_resource import (
    AsyncEnvironmentAccountConnectionResource,
)
from aws_sdk_proton._resources.aws_proton20200720.environment_output_resource import (
    AsyncEnvironmentOutputResource,
)
from aws_sdk_proton._resources.aws_proton20200720.environment_provisioned_resource_resource import (
    AsyncEnvironmentProvisionedResourceResource,
)
from aws_sdk_proton._resources.aws_proton20200720.environment_resource import (
    AsyncEnvironmentResource,
)
from aws_sdk_proton._resources.aws_proton20200720.environment_template_resource import (
    AsyncEnvironmentTemplateResource,
)
from aws_sdk_proton._resources.aws_proton20200720.environment_template_version_resource import (
    AsyncEnvironmentTemplateVersionResource,
)
from aws_sdk_proton._resources.aws_proton20200720.repository_resource import (
    AsyncRepositoryResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_instance_output_resource import (
    AsyncServiceInstanceOutputResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_instance_provisioned_resource_resource import (
    AsyncServiceInstanceProvisionedResourceResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_instance_resource import (
    AsyncServiceInstanceResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_pipeline_output_resource import (
    AsyncServicePipelineOutputResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_pipeline_provisioned_resource_resource import (
    AsyncServicePipelineProvisionedResourceResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_pipeline_resource import (
    AsyncServicePipelineResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_resource import (
    AsyncServiceResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_sync_blocker_resource import (
    AsyncServiceSyncBlockerResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_sync_config_resource import (
    AsyncServiceSyncConfigResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_template_resource import (
    AsyncServiceTemplateResource,
)
from aws_sdk_proton._resources.aws_proton20200720.service_template_version_resource import (
    AsyncServiceTemplateVersionResource,
)
from aws_sdk_proton._resources.aws_proton20200720.template_sync_config_resource import (
    AsyncTemplateSyncConfigResource,
)
from aws_sdk_proton._services._aws_config import aaws_config
from aws_sdk_proton._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.cancel_component_deployment_input
    import aws_sdk_proton.types.cancel_component_deployment_output
    import aws_sdk_proton.types.cancel_environment_deployment_input
    import aws_sdk_proton.types.cancel_environment_deployment_output
    import aws_sdk_proton.types.cancel_service_instance_deployment_input
    import aws_sdk_proton.types.cancel_service_instance_deployment_output
    import aws_sdk_proton.types.cancel_service_pipeline_deployment_input
    import aws_sdk_proton.types.cancel_service_pipeline_deployment_output
    import aws_sdk_proton.types.deployment_id
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.get_repository_sync_status_input
    import aws_sdk_proton.types.get_repository_sync_status_output
    import aws_sdk_proton.types.get_resources_summary_input
    import aws_sdk_proton.types.get_resources_summary_output
    import aws_sdk_proton.types.get_service_instance_sync_status_input
    import aws_sdk_proton.types.get_service_instance_sync_status_output
    import aws_sdk_proton.types.get_template_sync_status_input
    import aws_sdk_proton.types.get_template_sync_status_output
    import aws_sdk_proton.types.git_branch_name
    import aws_sdk_proton.types.list_repository_sync_definitions_input
    import aws_sdk_proton.types.list_repository_sync_definitions_output
    import aws_sdk_proton.types.list_tags_for_resource_input
    import aws_sdk_proton.types.list_tags_for_resource_output
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.notify_resource_deployment_status_change_input
    import aws_sdk_proton.types.notify_resource_deployment_status_change_output
    import aws_sdk_proton.types.outputs_list
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider
    import aws_sdk_proton.types.repository_sync_definition
    import aws_sdk_proton.types.resource_deployment_status
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.status_message
    import aws_sdk_proton.types.sync_type
    import aws_sdk_proton.types.tag
    import aws_sdk_proton.types.tag_key_list
    import aws_sdk_proton.types.tag_list
    import aws_sdk_proton.types.tag_resource_input
    import aws_sdk_proton.types.tag_resource_output
    import aws_sdk_proton.types.template_type
    import aws_sdk_proton.types.template_version_part
    import aws_sdk_proton.types.untag_resource_input
    import aws_sdk_proton.types.untag_resource_output


class AsyncProtonClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncProtonClient:
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
        self._config = AsyncProtonClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.account_settings_resource = AsyncAccountSettingsResource(self)
        self.component_output_resource = AsyncComponentOutputResource(self)
        self.component_provisioned_resource_resource = (
            AsyncComponentProvisionedResourceResource(self)
        )
        self.component_resource = AsyncComponentResource(self)
        self.deployment_resource = AsyncDeploymentResource(self)
        self.environment_account_connection_resource = (
            AsyncEnvironmentAccountConnectionResource(self)
        )
        self.environment_output_resource = AsyncEnvironmentOutputResource(self)
        self.environment_provisioned_resource_resource = (
            AsyncEnvironmentProvisionedResourceResource(self)
        )
        self.environment_resource = AsyncEnvironmentResource(self)
        self.environment_template_resource = AsyncEnvironmentTemplateResource(self)
        self.environment_template_version_resource = (
            AsyncEnvironmentTemplateVersionResource(self)
        )
        self.repository_resource = AsyncRepositoryResource(self)
        self.service_instance_output_resource = AsyncServiceInstanceOutputResource(self)
        self.service_instance_provisioned_resource_resource = (
            AsyncServiceInstanceProvisionedResourceResource(self)
        )
        self.service_instance_resource = AsyncServiceInstanceResource(self)
        self.service_pipeline_output_resource = AsyncServicePipelineOutputResource(self)
        self.service_pipeline_provisioned_resource_resource = (
            AsyncServicePipelineProvisionedResourceResource(self)
        )
        self.service_pipeline_resource = AsyncServicePipelineResource(self)
        self.service_resource = AsyncServiceResource(self)
        self.service_sync_blocker_resource = AsyncServiceSyncBlockerResource(self)
        self.service_sync_config_resource = AsyncServiceSyncConfigResource(self)
        self.service_template_resource = AsyncServiceTemplateResource(self)
        self.service_template_version_resource = AsyncServiceTemplateVersionResource(
            self
        )
        self.template_sync_config_resource = AsyncTemplateSyncConfigResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncProtonClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncProtonClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def cancel_component_deployment(
        self,
        component_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.cancel_component_deployment_output.CancelComponentDeploymentOutput":
        r"""<p>Attempts to cancel a component deployment (for a component that is in the <code>IN_PROGRESS</code> deployment status).</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component with the deployment to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.cancel_component_deployment_input.CancelComponentDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.cancel_component_deployment_output.CancelComponentDeploymentOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.cancel_component_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.cancel_component_deployment.async_cancel_component_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.cancel_component_deployment_input.CancelComponentDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["component_name"] = component_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_environment_deployment(
        self,
        environment_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.cancel_environment_deployment_output.CancelEnvironmentDeploymentOutput":
        r"""<p>Attempts to cancel an environment deployment on an <a>UpdateEnvironment</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-env-update.html\">Update an environment</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateEnvironment</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            environment_name: <p>The name of the environment with the deployment to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.cancel_environment_deployment_input.CancelEnvironmentDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.cancel_environment_deployment_output.CancelEnvironmentDeploymentOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.cancel_environment_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.cancel_environment_deployment.async_cancel_environment_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.cancel_environment_deployment_input.CancelEnvironmentDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["environment_name"] = environment_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_service_instance_deployment(
        self,
        service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName",
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.cancel_service_instance_deployment_output.CancelServiceInstanceDeploymentOutput":
        r"""<p>Attempts to cancel a service instance deployment on an <a>UpdateServiceInstance</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html\">Update a service instance</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServiceInstance</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            service_instance_name: <p>The name of the service instance with the deployment to cancel.</p>
            service_name: <p>The name of the service with the service instance deployment to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.cancel_service_instance_deployment_input.CancelServiceInstanceDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.cancel_service_instance_deployment_output.CancelServiceInstanceDeploymentOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.cancel_service_instance_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.cancel_service_instance_deployment.async_cancel_service_instance_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.cancel_service_instance_deployment_input.CancelServiceInstanceDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["service_instance_name"] = service_instance_name
        input_["service_name"] = service_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_service_pipeline_deployment(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.cancel_service_pipeline_deployment_output.CancelServicePipelineDeploymentOutput":
        r"""<p>Attempts to cancel a service pipeline deployment on an <a>UpdateServicePipeline</a> action, if the deployment is <code>IN_PROGRESS</code>. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html\">Update a service pipeline</a> in the <i>Proton User guide</i>.</p> <p>The following list includes potential cancellation scenarios.</p> <ul> <li> <p>If the cancellation attempt succeeds, the resulting deployment state is <code>CANCELLED</code>.</p> </li> <li> <p>If the cancellation attempt fails, the resulting deployment state is <code>FAILED</code>.</p> </li> <li> <p>If the current <a>UpdateServicePipeline</a> action succeeds before the cancellation attempt starts, the resulting deployment state is <code>SUCCEEDED</code> and the cancellation attempt has no effect.</p> </li> </ul>

        Args:
            service_name: <p>The name of the service with the service pipeline deployment to cancel.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.cancel_service_pipeline_deployment_input.CancelServicePipelineDeploymentInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.cancel_service_pipeline_deployment_output.CancelServicePipelineDeploymentOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.cancel_service_pipeline_deployment

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.cancel_service_pipeline_deployment.async_cancel_service_pipeline_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.cancel_service_pipeline_deployment_input.CancelServicePipelineDeploymentInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_repository_sync_status(
        self,
        repository_name: "aws_sdk_proton.types.repository_name.RepositoryName",
        repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        branch: "aws_sdk_proton.types.git_branch_name.GitBranchName",
        sync_type: "aws_sdk_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput":
        r"""<p>Get the sync status of a repository used for Proton template sync. For more information about template sync, see .</p> <note> <p>A repository sync status isn't tied to the Proton Repository resource (or any other Proton resource). Therefore, tags on an Proton Repository resource have no effect on this action. Specifically, you can't use these tags to control access to this action using Attribute-based access control (ABAC).</p> <p>For more information about ABAC, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags\">ABAC</a> in the <i>Proton User Guide</i>.</p> </note>

        Args:
            repository_name: <p>The repository name.</p>
            repository_provider: <p>The repository provider.</p>
            branch: <p>The repository branch.</p>
            sync_type: <p>The repository sync type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_repository_sync_status_input.GetRepositorySyncStatusInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_repository_sync_status_output.GetRepositorySyncStatusOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_repository_sync_status

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_repository_sync_status.async_get_repository_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_repository_sync_status_input.GetRepositorySyncStatusInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["repository_provider"] = repository_provider
        input_["branch"] = branch
        input_["sync_type"] = sync_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resources_summary(
        self, *, config_overrides: Optional[AsyncProtonClientConfig] = None
    ) -> "aws_sdk_proton.types.get_resources_summary_output.GetResourcesSummaryOutput":
        r"""<p>Get counts of Proton resources.</p> <p>For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when it's behind the recommended version of the Proton template that it uses and it needs an update to become current.</p> <p>The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the <code>components</code>, <code>environments</code>, and <code>serviceTemplates</code> field descriptions.</p> <p>For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html\">Proton dashboard</a> in the <i>Proton User Guide</i>.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_resources_summary_input.GetResourcesSummaryInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_resources_summary_output.GetResourcesSummaryOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_resources_summary

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_resources_summary.async_get_resources_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_resources_summary_input.GetResourcesSummaryInput = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_service_instance_sync_status(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_service_instance_sync_status_output.GetServiceInstanceSyncStatusOutput":
        """<p>Get the status of the synced service instance.</p>

        Args:
            service_name: <p>The name of the service that the service instance belongs to.</p>
            service_instance_name: <p>The name of the service instance that you want the sync status input for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_service_instance_sync_status_input.GetServiceInstanceSyncStatusInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_service_instance_sync_status_output.GetServiceInstanceSyncStatusOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_service_instance_sync_status

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_service_instance_sync_status.async_get_service_instance_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_service_instance_sync_status_input.GetServiceInstanceSyncStatusInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name
        input_["service_instance_name"] = service_instance_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_template_sync_status(
        self,
        template_name: "aws_sdk_proton.types.resource_name.ResourceName",
        template_type: "aws_sdk_proton.types.template_type.TemplateType",
        template_version: "aws_sdk_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.get_template_sync_status_output.GetTemplateSyncStatusOutput":
        """<p>Get the status of a template sync.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>
            template_version: <p>The template major version.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.get_template_sync_status_input.GetTemplateSyncStatusInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.get_template_sync_status_output.GetTemplateSyncStatusOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.get_template_sync_status

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.get_template_sync_status.async_get_template_sync_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.get_template_sync_status_input.GetTemplateSyncStatusInput = {}  # type: ignore[typeddict-item]
        input_["template_name"] = template_name
        input_["template_type"] = template_type
        input_["template_version"] = template_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_repository_sync_definitions(
        self,
        repository_name: "aws_sdk_proton.types.repository_name.RepositoryName",
        repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        sync_type: "aws_sdk_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput":
        """<p>List repository sync definitions with detail data.</p>

        Args:
            repository_name: <p>The repository name.</p>
            repository_provider: <p>The repository provider.</p>
            sync_type: <p>The sync type. The only supported value is <code>TEMPLATE_SYNC</code>.</p>
            next_token: <p>A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the list of repository sync definitions previously requested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_repository_sync_definitions_output.ListRepositorySyncDefinitionsOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_repository_sync_definitions

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_repository_sync_definitions.async_list_repository_sync_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_repository_sync_definitions_input.ListRepositorySyncDefinitionsInput = {}  # type: ignore[typeddict-item]
        input_["repository_name"] = repository_name
        input_["repository_provider"] = repository_provider
        input_["sync_type"] = sync_type
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_repository_sync_definitions(
        self,
        repository_name: "aws_sdk_proton.types.repository_name.RepositoryName",
        repository_provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider",
        sync_type: "aws_sdk_proton.types.sync_type.SyncType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_proton.types.repository_sync_definition.RepositorySyncDefinition]":
        _token = next_token
        while True:
            _response = await self.list_repository_sync_definitions(
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

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "aws_sdk_proton.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>List tags for a resource. For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for the listed tags.</p>
            next_token: <p>A token that indicates the location of the next resource tag in the array of resource tags, after the list of resource tags that was previously requested.</p>
            max_results: <p>The maximum number of tags to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_proton.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
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

    async def notify_resource_deployment_status_change(
        self,
        resource_arn: "aws_sdk_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        status: Optional[
            "aws_sdk_proton.types.resource_deployment_status.ResourceDeploymentStatus"
        ] = None,
        outputs: Optional["aws_sdk_proton.types.outputs_list.OutputsList"] = None,
        deployment_id: Optional[
            "aws_sdk_proton.types.deployment_id.DeploymentId"
        ] = None,
        status_message: Optional[
            "aws_sdk_proton.types.status_message.StatusMessage"
        ] = None,
    ) -> "aws_sdk_proton.types.notify_resource_deployment_status_change_output.NotifyResourceDeploymentStatusChangeOutput":
        r"""<p>Notify Proton of status changes to a provisioned resource when you use self-managed provisioning.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self\">Self-managed provisioning</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The provisioned resource Amazon Resource Name (ARN).</p>
            status: <p>The status of your provisioned resource.</p>
            outputs: <p>The provisioned resource state change detail data that's returned by Proton.</p>
            deployment_id: <p>The deployment ID for your provisioned resource.</p>
            status_message: <p>The deployment status message for your provisioned resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.notify_resource_deployment_status_change_input.NotifyResourceDeploymentStatusChangeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.notify_resource_deployment_status_change_output.NotifyResourceDeploymentStatusChangeOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.notify_resource_deployment_status_change

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.notify_resource_deployment_status_change.async_notify_resource_deployment_status_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.notify_resource_deployment_status_change_input.NotifyResourceDeploymentStatusChangeInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        if status is not None:
            input_["status"] = status
        if outputs is not None:
            input_["outputs"] = outputs
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if status_message is not None:
            input_["status_message"] = status_message

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_proton.types.arn.Arn",
        tags: "aws_sdk_proton.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.tag_resource_output.TagResourceOutput":
        r"""<p>Tag a resource. A tag is a key-value pair of metadata that you associate with an Proton resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Proton resource to apply customer tags to.</p>
            tags: <p>A list of customer tags to apply to the Proton resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_proton.types.arn.Arn",
        tag_keys: "aws_sdk_proton.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "aws_sdk_proton.types.untag_resource_output.UntagResourceOutput":
        r"""<p>Remove a customer tag from a resource. A tag is a key-value pair of metadata associated with an Proton resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove customer tags from.</p>
            tag_keys: <p>A list of customer tag keys that indicate the customer tags to be removed from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_proton.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

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
