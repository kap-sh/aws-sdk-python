"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AmazonBedrockAgentCoreControl``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
from aws_sdk_bedrock_agentcore_control._auth._identity import Credentials
from aws_sdk_bedrock_agentcore_control._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_bedrock_agentcore_control._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.agent_endpoint_resource import (
    AsyncAgentEndpointResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.agent_resource import (
    AsyncAgentResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.api_key_credential_provider import (
    AsyncApiKeyCredentialProvider,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.browser_profile_resource import (
    AsyncBrowserProfileResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.browser_resource import (
    AsyncBrowserResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.code_interpreter_resource import (
    AsyncCodeInterpreterResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.configuration_bundle import (
    AsyncConfigurationBundle,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.dataset import (
    AsyncDataset,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.evaluator import (
    AsyncEvaluator,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_resource import (
    AsyncGatewayResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_rule_resource import (
    AsyncGatewayRuleResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_target_resource import (
    AsyncGatewayTargetResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.harness_resource import (
    AsyncHarnessResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.memory_resource import (
    AsyncMemoryResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.oauth2_credential_provider import (
    AsyncOauth2CredentialProvider,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.online_evaluation_config import (
    AsyncOnlineEvaluationConfig,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_credential_provider import (
    AsyncPaymentCredentialProvider,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_manager_resource import (
    AsyncPaymentManagerResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_engine_resource import (
    AsyncPolicyEngineResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_generation_resource import (
    AsyncPolicyGenerationResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_resource import (
    AsyncPolicyResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.registry_record_resource import (
    AsyncRegistryRecordResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.registry_resource import (
    AsyncRegistryResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.workload_identity import (
    AsyncWorkloadIdentity,
)
from aws_sdk_bedrock_agentcore_control._services._aws_config import aaws_config
from aws_sdk_bedrock_agentcore_control._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_request
    import aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_response
    import aws_sdk_bedrock_agentcore_control.types.get_resource_policy_request
    import aws_sdk_bedrock_agentcore_control.types.get_resource_policy_response
    import aws_sdk_bedrock_agentcore_control.types.get_token_vault_request
    import aws_sdk_bedrock_agentcore_control.types.get_token_vault_response
    import aws_sdk_bedrock_agentcore_control.types.kms_configuration
    import aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_request
    import aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_response
    import aws_sdk_bedrock_agentcore_control.types.put_resource_policy_request
    import aws_sdk_bedrock_agentcore_control.types.put_resource_policy_response
    import aws_sdk_bedrock_agentcore_control.types.resource_policy_body
    import aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_request
    import aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_response
    import aws_sdk_bedrock_agentcore_control.types.tag_key_list
    import aws_sdk_bedrock_agentcore_control.types.tag_resource_request
    import aws_sdk_bedrock_agentcore_control.types.tag_resource_response
    import aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.token_vault_id_type
    import aws_sdk_bedrock_agentcore_control.types.untag_resource_request
    import aws_sdk_bedrock_agentcore_control.types.untag_resource_response


class AsyncBedrockAgentCoreControlClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBedrockAgentCoreControlClient:
    """A client for the ``BedrockAgentCoreControl`` service.

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
        self._config = AsyncBedrockAgentCoreControlClientConfig(
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
        self.agent_endpoint_resource = AsyncAgentEndpointResource(self)
        self.agent_resource = AsyncAgentResource(self)
        self.api_key_credential_provider = AsyncApiKeyCredentialProvider(self)
        self.browser_profile_resource = AsyncBrowserProfileResource(self)
        self.browser_resource = AsyncBrowserResource(self)
        self.code_interpreter_resource = AsyncCodeInterpreterResource(self)
        self.configuration_bundle = AsyncConfigurationBundle(self)
        self.dataset = AsyncDataset(self)
        self.evaluator = AsyncEvaluator(self)
        self.gateway_resource = AsyncGatewayResource(self)
        self.gateway_rule_resource = AsyncGatewayRuleResource(self)
        self.gateway_target_resource = AsyncGatewayTargetResource(self)
        self.harness_resource = AsyncHarnessResource(self)
        self.memory_resource = AsyncMemoryResource(self)
        self.oauth2_credential_provider = AsyncOauth2CredentialProvider(self)
        self.online_evaluation_config = AsyncOnlineEvaluationConfig(self)
        self.payment_credential_provider = AsyncPaymentCredentialProvider(self)
        self.payment_manager_resource = AsyncPaymentManagerResource(self)
        self.policy_engine_resource = AsyncPolicyEngineResource(self)
        self.policy_generation_resource = AsyncPolicyGenerationResource(self)
        self.policy_resource = AsyncPolicyResource(self)
        self.registry_record_resource = AsyncRegistryRecordResource(self)
        self.registry_resource = AsyncRegistryResource(self)
        self.workload_identity = AsyncWorkloadIdentity(self)

    def operation_options(
        self,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockAgentCoreControlClientConfig = config_overrides or {}
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

    async def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the resource-based policy for a specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to delete the resource policy.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy for a specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to retrieve the resource policy.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_token_vault(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        token_vault_id: Optional[
            "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_token_vault_response.GetTokenVaultResponse":
        """<p>Retrieves information about a token vault.</p>

        Args:
            token_vault_id: <p>The unique identifier of the token vault to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_token_vault_request.GetTokenVaultRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_token_vault_response.GetTokenVaultResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_token_vault

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_token_vault.async_get_token_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_token_vault_request.GetTokenVaultRequest = {}  # type: ignore[typeddict-item]
        if token_vault_id is not None:
            input_["token_vault_id"] = token_vault_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with the specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to list tags.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        policy: "aws_sdk_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a resource-based policy for a resource with the specified resourceArn.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to create or update the resource policy.</p>
            policy: <p>The resource policy to create or update.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def set_token_vault_cmk(
        self,
        kms_configuration: "aws_sdk_bedrock_agentcore_control.types.kms_configuration.KmsConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        token_vault_id: Optional[
            "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_response.SetTokenVaultCMKResponse":
        """<p>Sets the customer master key (CMK) for a token vault.</p>

        Args:
            token_vault_id: <p>The unique identifier of the token vault to update.</p>
            kms_configuration: <p>The KMS configuration for the token vault, including the key type and KMS key ARN.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown when a resource is modified concurrently by multiple requests.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_request.SetTokenVaultCMKRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_response.SetTokenVaultCMKResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.set_token_vault_cmk

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.set_token_vault_cmk.async_set_token_vault_cmk(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_request.SetTokenVaultCMKRequest = {}  # type: ignore[typeddict-item]
        if token_vault_id is not None:
            input_["token_vault_id"] = token_vault_id
        input_["kms_configuration"] = kms_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified resourceArn. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>The tags to add to the resource. A tag is a key-value pair.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "aws_sdk_bedrock_agentcore_control.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The tag keys of the tags to remove from the resource.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
