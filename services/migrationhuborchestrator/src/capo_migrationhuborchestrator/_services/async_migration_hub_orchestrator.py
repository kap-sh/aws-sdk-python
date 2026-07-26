"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#AWSMigrationHubOrchestrator``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_migrationhuborchestrator._auth._signers
import capo_migrationhuborchestrator._auth._sigv4
from capo_migrationhuborchestrator._auth._identity import Credentials
from capo_migrationhuborchestrator._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_migrationhuborchestrator._auth._zapros_handler import AuthMiddleware
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.migration_workflow import (
    AsyncMigrationWorkflow,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.migration_workflow_template import (
    AsyncMigrationWorkflowTemplate,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.plugin import (
    AsyncPlugin,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step import (
    AsyncTemplateStep,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step_group import (
    AsyncTemplateStepGroup,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step_groups import (
    AsyncTemplateStepGroups,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.workflow_step import (
    AsyncWorkflowStep,
)
from capo_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.workflow_step_group import (
    AsyncWorkflowStepGroup,
)
from capo_migrationhuborchestrator._services._aws_config import aaws_config
from capo_migrationhuborchestrator._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.list_tags_for_resource_request
    import capo_migrationhuborchestrator.types.list_tags_for_resource_response
    import capo_migrationhuborchestrator.types.resource_arn
    import capo_migrationhuborchestrator.types.tag_key_list
    import capo_migrationhuborchestrator.types.tag_map
    import capo_migrationhuborchestrator.types.tag_resource_request
    import capo_migrationhuborchestrator.types.tag_resource_response
    import capo_migrationhuborchestrator.types.untag_resource_request
    import capo_migrationhuborchestrator.types.untag_resource_response


class AsyncMigrationHubOrchestratorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncMigrationHubOrchestratorClient:
    """A client for the ``MigrationHubOrchestrator`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncMigrationHubOrchestratorClientConfig(
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
        self.migration_workflow = AsyncMigrationWorkflow(self)
        self.migration_workflow_template = AsyncMigrationWorkflowTemplate(self)
        self.plugin = AsyncPlugin(self)
        self.template_step = AsyncTemplateStep(self)
        self.template_step_group = AsyncTemplateStepGroup(self)
        self.template_step_groups = AsyncTemplateStepGroups(self)
        self.workflow_step = AsyncWorkflowStep(self)
        self.workflow_step_group = AsyncWorkflowStepGroup(self)

    def operation_options(
        self,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMigrationHubOrchestratorClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags added to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn",
        tags: "capo_migrationhuborchestrator.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> (
        "capo_migrationhuborchestrator.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Tag a resource by specifying its Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add tags.</p>
            tags: <p>A collection of labels, in the form of key:value pairs, that apply to this resource.</p>

        Raises:
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.tag_resource

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn",
        tag_keys: "capo_migrationhuborchestrator.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMigrationHubOrchestratorClientConfig] = None,
    ) -> "capo_migrationhuborchestrator.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>
            tag_keys: <p>One or more tag keys. Specify only the tag keys, not the tag values.</p>

        Raises:
            capo_migrationhuborchestrator.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource is not available.</p>
            capo_migrationhuborchestrator.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_migrationhuborchestrator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhuborchestrator.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhuborchestrator.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.untag_resource

            (
                output,
                http_response,
            ) = await capo_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhuborchestrator.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
