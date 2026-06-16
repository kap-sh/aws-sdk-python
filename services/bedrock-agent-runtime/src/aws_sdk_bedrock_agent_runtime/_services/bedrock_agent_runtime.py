"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AmazonBedrockAgentRunTimeService``."""

import warnings
from typing import Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

from aws_sdk_bedrock_agent_runtime._auth._identity import Credentials
from aws_sdk_bedrock_agent_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_bedrock_agent_runtime._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.flow_execution_resource import (
    FlowExecutionResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.flow_resource import (
    FlowResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.generate_query_resource import (
    GenerateQueryResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.inference_resource import (
    InferenceResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.inline_agent_resource import (
    InlineAgentResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.memory_resource import (
    MemoryResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.optimize_prompt_resource import (
    OptimizePromptResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.rerank_resource import (
    RerankResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.retrieve_and_generate_resource import (
    RetrieveAndGenerateResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream_resource import (
    RetrieveAndGenerateStreamResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.retrieve_resource import (
    RetrieveResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.session_resource import (
    SessionResource,
)
from aws_sdk_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.tagging_resource import (
    TaggingResource,
)
from aws_sdk_bedrock_agent_runtime._services._aws_config import aws_config
from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    Interceptor,
    OperationOptions,
    retry,
)


class BedrockAgentRuntimeClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BedrockAgentRuntimeClient:
    """A client for the ``BedrockAgentRuntime`` service.

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
        self._config = BedrockAgentRuntimeClientConfig(
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
        self.flow_execution_resource = FlowExecutionResource(self)
        self.flow_resource = FlowResource(self)
        self.generate_query_resource = GenerateQueryResource(self)
        self.inference_resource = InferenceResource(self)
        self.inline_agent_resource = InlineAgentResource(self)
        self.memory_resource = MemoryResource(self)
        self.optimize_prompt_resource = OptimizePromptResource(self)
        self.rerank_resource = RerankResource(self)
        self.retrieve_and_generate_resource = RetrieveAndGenerateResource(self)
        self.retrieve_and_generate_stream_resource = RetrieveAndGenerateStreamResource(
            self
        )
        self.retrieve_resource = RetrieveResource(self)
        self.session_resource = SessionResource(self)
        self.tagging_resource = TaggingResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentRuntimeClientConfig = config_overrides or {}
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
