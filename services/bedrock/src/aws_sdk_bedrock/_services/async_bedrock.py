"""Generated from Smithy shape ``com.amazonaws.bedrock#AmazonBedrockControlPlaneService``."""

import warnings
from collections.abc import AsyncIterator
from typing import Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

from aws_sdk_bedrock._auth._identity import Credentials
from aws_sdk_bedrock._auth._providers import (
    BearerTokenProvider,
    CredentialsProvider,
    StaticAwsCredentialsProvider,
    StaticBearerTokenProvider,
)
from aws_sdk_bedrock._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.advanced_prompt_optimization_job_resource import (
    AsyncAdvancedPromptOptimizationJobResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.allowlist_resource import (
    AsyncAllowlistResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.automated_reasoning_policy_resource import (
    AsyncAutomatedReasoningPolicyResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.bedrock_marketplace_resource import (
    AsyncBedrockMarketplaceResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.custom_model_deployment_resource import (
    AsyncCustomModelDeploymentResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.custom_model_resource import (
    AsyncCustomModelResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.data_retention_resource import (
    AsyncDataRetentionResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.enforced_guardrail_configuration_resource import (
    AsyncEnforcedGuardrailConfigurationResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.evaluation_job_resource import (
    AsyncEvaluationJobResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.guardrails_resource import (
    AsyncGuardrailsResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.inference_profile_resource import (
    AsyncInferenceProfileResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.logging_resource import (
    AsyncLoggingResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_copy_resource import (
    AsyncModelCopyResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_import_resource import (
    AsyncModelImportResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_invocation_job_resource import (
    AsyncModelInvocationJobResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_resource import (
    AsyncModelResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.prompt_router_resource import (
    AsyncPromptRouterResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.provisioned_model_throughput_resource import (
    AsyncProvisionedModelThroughputResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.resource_policy_resource import (
    AsyncResourcePolicyResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.subscription_resource import (
    AsyncSubscriptionResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.tagging_resource import (
    AsyncTaggingResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.training_resource import (
    AsyncTrainingResource,
)
from aws_sdk_bedrock._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    aretry,
)


class AsyncBedrockClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None
    bearer_provider: BearerTokenProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncBedrockClient:
    """A client for the ``Bedrock`` service.

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
        bearer: Bearer token for authentication.
        bearer_provider: Provider that resolves bearer tokens. Takes precedence over ``bearer``.
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
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
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
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self.config = AsyncBedrockClientConfig(
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
                "bearer_provider": bearer_provider,
            }
        )
        # resources
        self.advanced_prompt_optimization_job_resource = (
            AsyncAdvancedPromptOptimizationJobResource(self)
        )
        self.allowlist_resource = AsyncAllowlistResource(self)
        self.automated_reasoning_policy_resource = (
            AsyncAutomatedReasoningPolicyResource(self)
        )
        self.bedrock_marketplace_resource = AsyncBedrockMarketplaceResource(self)
        self.custom_model_deployment_resource = AsyncCustomModelDeploymentResource(self)
        self.custom_model_resource = AsyncCustomModelResource(self)
        self.data_retention_resource = AsyncDataRetentionResource(self)
        self.enforced_guardrail_configuration_resource = (
            AsyncEnforcedGuardrailConfigurationResource(self)
        )
        self.evaluation_job_resource = AsyncEvaluationJobResource(self)
        self.guardrails_resource = AsyncGuardrailsResource(self)
        self.inference_profile_resource = AsyncInferenceProfileResource(self)
        self.logging_resource = AsyncLoggingResource(self)
        self.model_copy_resource = AsyncModelCopyResource(self)
        self.model_import_resource = AsyncModelImportResource(self)
        self.model_invocation_job_resource = AsyncModelInvocationJobResource(self)
        self.model_resource = AsyncModelResource(self)
        self.prompt_router_resource = AsyncPromptRouterResource(self)
        self.provisioned_model_throughput_resource = (
            AsyncProvisionedModelThroughputResource(self)
        )
        self.resource_policy_resource = AsyncResourcePolicyResource(self)
        self.subscription_resource = AsyncSubscriptionResource(self)
        self.tagging_resource = AsyncTaggingResource(self)
        self.training_resource = AsyncTrainingResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
            bearer_provider=overrides.get(
                "bearer_provider", self.config.get("bearer_provider")
            ),
        )
        return interceptors_, options_

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
