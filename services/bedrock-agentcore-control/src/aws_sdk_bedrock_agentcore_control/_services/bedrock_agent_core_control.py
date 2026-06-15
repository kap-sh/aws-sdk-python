"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AmazonBedrockAgentCoreControl``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
from aws_sdk_bedrock_agentcore_control._auth._identity import Credentials
from aws_sdk_bedrock_agentcore_control._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bedrock_agentcore_control._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.agent_endpoint_resource import (
    AgentEndpointResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.agent_resource import (
    AgentResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.api_key_credential_provider import (
    ApiKeyCredentialProvider,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.browser_profile_resource import (
    BrowserProfileResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.browser_resource import (
    BrowserResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.code_interpreter_resource import (
    CodeInterpreterResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.configuration_bundle import (
    ConfigurationBundle,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.dataset import (
    Dataset,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.evaluator import (
    Evaluator,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_resource import (
    GatewayResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_rule_resource import (
    GatewayRuleResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_target_resource import (
    GatewayTargetResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.harness_resource import (
    HarnessResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.memory_resource import (
    MemoryResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.oauth2_credential_provider import (
    Oauth2CredentialProvider,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.online_evaluation_config import (
    OnlineEvaluationConfig,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_credential_provider import (
    PaymentCredentialProvider,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_manager_resource import (
    PaymentManagerResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_engine_resource import (
    PolicyEngineResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_generation_resource import (
    PolicyGenerationResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_resource import (
    PolicyResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.registry_record_resource import (
    RegistryRecordResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.registry_resource import (
    RegistryResource,
)
from aws_sdk_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.workload_identity import (
    WorkloadIdentity,
)
from aws_sdk_bedrock_agentcore_control._services._aws_config import aws_config
from aws_sdk_bedrock_agentcore_control._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class BedrockAgentCoreControlClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


class BedrockAgentCoreControlClient:
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
        self._config = BedrockAgentCoreControlClientConfig(
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
        self.agent_endpoint_resource = AgentEndpointResource(self)
        self.agent_resource = AgentResource(self)
        self.api_key_credential_provider = ApiKeyCredentialProvider(self)
        self.browser_profile_resource = BrowserProfileResource(self)
        self.browser_resource = BrowserResource(self)
        self.code_interpreter_resource = CodeInterpreterResource(self)
        self.configuration_bundle = ConfigurationBundle(self)
        self.dataset = Dataset(self)
        self.evaluator = Evaluator(self)
        self.gateway_resource = GatewayResource(self)
        self.gateway_rule_resource = GatewayRuleResource(self)
        self.gateway_target_resource = GatewayTargetResource(self)
        self.harness_resource = HarnessResource(self)
        self.memory_resource = MemoryResource(self)
        self.oauth2_credential_provider = Oauth2CredentialProvider(self)
        self.online_evaluation_config = OnlineEvaluationConfig(self)
        self.payment_credential_provider = PaymentCredentialProvider(self)
        self.payment_manager_resource = PaymentManagerResource(self)
        self.policy_engine_resource = PolicyEngineResource(self)
        self.policy_generation_resource = PolicyGenerationResource(self)
        self.policy_resource = PolicyResource(self)
        self.registry_record_resource = RegistryRecordResource(self)
        self.registry_resource = RegistryResource(self)
        self.workload_identity = WorkloadIdentity(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentCoreControlClientConfig = config_overrides or {}
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

    def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the resource-based policy for a specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to delete the resource policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_resource_policy

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy for a specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to retrieve the resource policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_resource_policy

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_token_vault(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        token_vault_id: Optional[
            "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_token_vault_response.GetTokenVaultResponse":
        """<p>Retrieves information about a token vault.</p>

        Args:
            token_vault_id: <p>The unique identifier of the token vault to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_token_vault_request.GetTokenVaultRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_token_vault_response.GetTokenVaultResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_token_vault

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_token_vault.get_token_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_token_vault_request.GetTokenVaultRequest = {}  # type: ignore[typeddict-item]
        if token_vault_id is not None:
            input_["token_vault_id"] = token_vault_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with the specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to list tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_tags_for_resource

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        policy: "aws_sdk_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a resource-based policy for a resource with the specified resourceArn.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to create or update the resource policy.</p>
            policy: <p>The resource policy to create or update.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.put_resource_policy

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["policy"] = policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def set_token_vault_cmk(
        self,
        kms_configuration: "aws_sdk_bedrock_agentcore_control.types.kms_configuration.KmsConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        token_vault_id: Optional[
            "aws_sdk_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_response.SetTokenVaultCMKResponse":
        """<p>Sets the customer master key (CMK) for a token vault.</p>

        Args:
            token_vault_id: <p>The unique identifier of the token vault to update.</p>
            kms_configuration: <p>The KMS configuration for the token vault, including the key type and KMS key ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_request.SetTokenVaultCMKRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_response.SetTokenVaultCMKResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.set_token_vault_cmk

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.set_token_vault_cmk.set_token_vault_cmk(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.set_token_vault_cmk_request.SetTokenVaultCMKRequest = {}  # type: ignore[typeddict-item]
        if token_vault_id is not None:
            input_["token_vault_id"] = token_vault_id
        input_["kms_configuration"] = kms_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.tag_resource_response.TagResourceResponse":
        """<p>Associates the specified tags to a resource with the specified resourceArn. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>The tags to add to the resource. A tag is a key-value pair.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.tag_resource

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "aws_sdk_bedrock_agentcore_control.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The tag keys of the tags to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.untag_resource

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
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
