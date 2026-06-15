"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AmazonBedrockAgentBuildTimeLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._auth._identity import Credentials
from aws_sdk_bedrock_agent._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bedrock_agent._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.action_group_resource import (
    ActionGroupResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.agent_collaborator_resource import (
    AgentCollaboratorResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.agent_resource import (
    AgentResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.alias_resource import (
    AliasResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.data_source_resource import (
    DataSourceResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.flow_resource import (
    FlowResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.ingestion_job_resource import (
    IngestionJobResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.knowledge_base_document_resource import (
    KnowledgeBaseDocumentResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.knowledge_base_resource import (
    KnowledgeBaseResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.prompt_resource import (
    PromptResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.tagging_resource import (
    TaggingResource,
)
from aws_sdk_bedrock_agent._resources.amazon_bedrock_agent_build_time_lambda.version_resource import (
    VersionResource,
)
from aws_sdk_bedrock_agent._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_definition
    import aws_sdk_bedrock_agent.types.validate_flow_definition_request
    import aws_sdk_bedrock_agent.types.validate_flow_definition_response


class BedrockAgentClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class BedrockAgentClient:
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
        self._config = BedrockAgentClientConfig(
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
        self.action_group_resource = ActionGroupResource(self)
        self.agent_collaborator_resource = AgentCollaboratorResource(self)
        self.agent_resource = AgentResource(self)
        self.alias_resource = AliasResource(self)
        self.data_source_resource = DataSourceResource(self)
        self.flow_resource = FlowResource(self)
        self.ingestion_job_resource = IngestionJobResource(self)
        self.knowledge_base_document_resource = KnowledgeBaseDocumentResource(self)
        self.knowledge_base_resource = KnowledgeBaseResource(self)
        self.prompt_resource = PromptResource(self)
        self.tagging_resource = TaggingResource(self)
        self.version_resource = VersionResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentClientConfig = config_overrides or {}
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

    def validate_flow_definition(
        self,
        definition: "aws_sdk_bedrock_agent.types.flow_definition.FlowDefinition",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.validate_flow_definition_response.ValidateFlowDefinitionResponse":
        """<p>Validates the definition of a flow.</p>

        Args:
            definition: <p>The definition of a flow to validate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.validate_flow_definition_request.ValidateFlowDefinitionRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.validate_flow_definition_response.ValidateFlowDefinitionResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.validate_flow_definition

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.validate_flow_definition.validate_flow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.validate_flow_definition_request.ValidateFlowDefinitionRequest = {}  # type: ignore[typeddict-item]
        input_["definition"] = definition

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
