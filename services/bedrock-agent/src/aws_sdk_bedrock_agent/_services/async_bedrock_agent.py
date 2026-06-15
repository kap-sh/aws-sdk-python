"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AmazonBedrockAgentBuildTimeLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._auth._identity import Credentials
from aws_sdk_bedrock_agent._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bedrock_agent._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.action_group_resource import (
    AsyncActionGroupResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.agent_collaborator_resource import (
    AsyncAgentCollaboratorResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.agent_resource import (
    AsyncAgentResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.alias_resource import (
    AsyncAliasResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.data_source_resource import (
    AsyncDataSourceResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.flow_resource import (
    AsyncFlowResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.ingestion_job_resource import (
    AsyncIngestionJobResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.knowledge_base_document_resource import (
    AsyncKnowledgeBaseDocumentResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.knowledge_base_resource import (
    AsyncKnowledgeBaseResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.prompt_resource import (
    AsyncPromptResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.tagging_resource import (
    AsyncTaggingResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.version_resource import (
    AsyncVersionResource,
)
from aws_sdk_bedrock_agent._services._aws_config import aaws_config
from aws_sdk_bedrock_agent._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_definition
    import aws_sdk_bedrock_agent.types.validate_flow_definition_request
    import aws_sdk_bedrock_agent.types.validate_flow_definition_response


class AsyncBedrockAgentClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class AsyncBedrockAgentClient:
    """A client for the ``BedrockAgent`` service.

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
        self._config = AsyncBedrockAgentClientConfig(
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
        self.action_group_resource = AsyncActionGroupResource(self)
        self.agent_collaborator_resource = AsyncAgentCollaboratorResource(self)
        self.agent_resource = AsyncAgentResource(self)
        self.alias_resource = AsyncAliasResource(self)
        self.data_source_resource = AsyncDataSourceResource(self)
        self.flow_resource = AsyncFlowResource(self)
        self.ingestion_job_resource = AsyncIngestionJobResource(self)
        self.knowledge_base_document_resource = AsyncKnowledgeBaseDocumentResource(self)
        self.knowledge_base_resource = AsyncKnowledgeBaseResource(self)
        self.prompt_resource = AsyncPromptResource(self)
        self.tagging_resource = AsyncTaggingResource(self)
        self.version_resource = AsyncVersionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockAgentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockAgentClientConfig = config_overrides or {}
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

    async def validate_flow_definition(
        self,
        definition: "aws_sdk_bedrock_agent.types.flow_definition.FlowDefinition",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.validate_flow_definition_response.ValidateFlowDefinitionResponse":
        """<p>Validates the definition of a flow.</p>

        Args:
            definition: <p>The definition of a flow to validate.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.validate_flow_definition_request.ValidateFlowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.validate_flow_definition_response.ValidateFlowDefinitionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.validate_flow_definition

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.validate_flow_definition.async_validate_flow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.validate_flow_definition_request.ValidateFlowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["definition"] = definition

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
