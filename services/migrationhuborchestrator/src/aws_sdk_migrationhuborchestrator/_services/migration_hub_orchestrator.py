"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#AWSMigrationHubOrchestrator``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_migrationhuborchestrator._auth._signers
import aws_sdk_migrationhuborchestrator._auth._sigv4
from aws_sdk_migrationhuborchestrator._auth._identity import Credentials
from aws_sdk_migrationhuborchestrator._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_migrationhuborchestrator._auth._zapros_handler import AuthMiddleware
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.migration_workflow import (
    MigrationWorkflow,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.migration_workflow_template import (
    MigrationWorkflowTemplate,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.plugin import (
    Plugin,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step import (
    TemplateStep,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step_group import (
    TemplateStepGroup,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.template_step_groups import (
    TemplateStepGroups,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.workflow_step import (
    WorkflowStep,
)
from aws_sdk_migrationhuborchestrator._resources.aws_migration_hub_orchestrator.workflow_step_group import (
    WorkflowStepGroup,
)
from aws_sdk_migrationhuborchestrator._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.list_tags_for_resource_request
    import aws_sdk_migrationhuborchestrator.types.list_tags_for_resource_response
    import aws_sdk_migrationhuborchestrator.types.resource_arn
    import aws_sdk_migrationhuborchestrator.types.tag_key_list
    import aws_sdk_migrationhuborchestrator.types.tag_map
    import aws_sdk_migrationhuborchestrator.types.tag_resource_request
    import aws_sdk_migrationhuborchestrator.types.tag_resource_response
    import aws_sdk_migrationhuborchestrator.types.untag_resource_request
    import aws_sdk_migrationhuborchestrator.types.untag_resource_response


class MigrationHubOrchestratorClientConfig(TypedDict, total=False):
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


class MigrationHubOrchestratorClient:
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
        self.config = MigrationHubOrchestratorClientConfig(
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
        # resources
        self.migration_workflow = MigrationWorkflow(self)
        self.migration_workflow_template = MigrationWorkflowTemplate(self)
        self.plugin = Plugin(self)
        self.template_step = TemplateStep(self)
        self.template_step_group = TemplateStepGroup(self)
        self.template_step_groups = TemplateStepGroups(self)
        self.workflow_step = WorkflowStep(self)
        self.workflow_step_group = WorkflowStepGroup(self)

    def operation_options(
        self, config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MigrationHubOrchestratorClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_migrationhuborchestrator.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the tags added to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_tags_for_resource

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_migrationhuborchestrator.types.resource_arn.ResourceArn",
        tags: "aws_sdk_migrationhuborchestrator.types.tag_map.TagMap",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.tag_resource_response.TagResourceResponse":
        """<p>Tag a resource by specifying its Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add tags.</p>
            tags: <p>A collection of labels, in the form of key:value pairs, that apply to this resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.tag_resource

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_migrationhuborchestrator.types.resource_arn.ResourceArn",
        tag_keys: "aws_sdk_migrationhuborchestrator.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[MigrationHubOrchestratorClientConfig] = None,
    ) -> "aws_sdk_migrationhuborchestrator.types.untag_resource_response.UntagResourceResponse":
        """<p>Deletes the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p>
            tag_keys: <p>One or more tag keys. Specify only the tag keys, not the tag values.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_migrationhuborchestrator.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_migrationhuborchestrator.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.untag_resource

            output, http_response = (
                aws_sdk_migrationhuborchestrator._operations.aws_migration_hub_orchestrator.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_migrationhuborchestrator.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
