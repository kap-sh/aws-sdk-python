"""Generated from Smithy shape ``com.amazonaws.bedrock#AmazonBedrockControlPlaneService``."""

import warnings
from typing import Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

from aws_sdk_bedrock._auth._identity import Credentials
from aws_sdk_bedrock._auth._providers import (
    BearerTokenProvider,
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    StaticBearerTokenProvider,
    default_aws_credentials_chain,
)
from aws_sdk_bedrock._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.advanced_prompt_optimization_job_resource import (
    AdvancedPromptOptimizationJobResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.allowlist_resource import (
    AllowlistResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.automated_reasoning_policy_resource import (
    AutomatedReasoningPolicyResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.bedrock_marketplace_resource import (
    BedrockMarketplaceResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.custom_model_deployment_resource import (
    CustomModelDeploymentResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.custom_model_resource import (
    CustomModelResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.data_retention_resource import (
    DataRetentionResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.enforced_guardrail_configuration_resource import (
    EnforcedGuardrailConfigurationResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.evaluation_job_resource import (
    EvaluationJobResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.guardrails_resource import (
    GuardrailsResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.inference_profile_resource import (
    InferenceProfileResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.logging_resource import (
    LoggingResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_copy_resource import (
    ModelCopyResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_import_resource import (
    ModelImportResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_invocation_job_resource import (
    ModelInvocationJobResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.model_resource import (
    ModelResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.prompt_router_resource import (
    PromptRouterResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.provisioned_model_throughput_resource import (
    ProvisionedModelThroughputResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.resource_policy_resource import (
    ResourcePolicyResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.subscription_resource import (
    SubscriptionResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.tagging_resource import (
    TaggingResource,
)
from aws_sdk_bedrock._resources.amazon_bedrock_control_plane_service.training_resource import (
    TrainingResource,
)
from aws_sdk_bedrock._services._aws_config import aws_config
from aws_sdk_bedrock._services._pipeline import (
    Interceptor,
    OperationOptions,
    retry,
)


class BedrockClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    bearer_provider: BearerTokenProvider | None


class BedrockClient:
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
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
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self._config = BedrockClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "bearer_provider": bearer_provider,
            }
        )

        # resources
        self.advanced_prompt_optimization_job_resource = (
            AdvancedPromptOptimizationJobResource(self)
        )
        self.allowlist_resource = AllowlistResource(self)
        self.automated_reasoning_policy_resource = AutomatedReasoningPolicyResource(
            self
        )
        self.bedrock_marketplace_resource = BedrockMarketplaceResource(self)
        self.custom_model_deployment_resource = CustomModelDeploymentResource(self)
        self.custom_model_resource = CustomModelResource(self)
        self.data_retention_resource = DataRetentionResource(self)
        self.enforced_guardrail_configuration_resource = (
            EnforcedGuardrailConfigurationResource(self)
        )
        self.evaluation_job_resource = EvaluationJobResource(self)
        self.guardrails_resource = GuardrailsResource(self)
        self.inference_profile_resource = InferenceProfileResource(self)
        self.logging_resource = LoggingResource(self)
        self.model_copy_resource = ModelCopyResource(self)
        self.model_import_resource = ModelImportResource(self)
        self.model_invocation_job_resource = ModelInvocationJobResource(self)
        self.model_resource = ModelResource(self)
        self.prompt_router_resource = PromptRouterResource(self)
        self.provisioned_model_throughput_resource = ProvisionedModelThroughputResource(
            self
        )
        self.resource_policy_resource = ResourcePolicyResource(self)
        self.subscription_resource = SubscriptionResource(self)
        self.tagging_resource = TaggingResource(self)
        self.training_resource = TrainingResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockClientConfig = config_overrides or {}
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
            bearer_provider=overrides.get(
                "bearer_provider", self._config.get("bearer_provider")
            ),
        )
        return interceptors_, options_

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
