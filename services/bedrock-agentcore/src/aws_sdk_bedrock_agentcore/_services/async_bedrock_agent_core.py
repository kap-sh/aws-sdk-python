"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AmazonBedrockAgentCore``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
from aws_sdk_bedrock_agentcore._auth._identity import Credentials
from aws_sdk_bedrock_agentcore._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_bedrock_agentcore._auth._zapros_handler import AuthMiddleware
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.agentic_resource import (
    AsyncAgenticResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.browser_profile_resource import (
    AsyncBrowserProfileResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.browser_session_resource import (
    AsyncBrowserSessionResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.code_interpreter_session_resource import (
    AsyncCodeInterpreterSessionResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.evaluation_resource import (
    AsyncEvaluationResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.memory_resource import (
    AsyncMemoryResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.payment_instrument_resource import (
    AsyncPaymentInstrumentResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.payment_session_resource import (
    AsyncPaymentSessionResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.process_payment_resource import (
    AsyncProcessPaymentResource,
)
from aws_sdk_bedrock_agentcore._resources.amazon_bedrock_agent_core.registry_record_resource import (
    AsyncRegistryRecordResource,
)
from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.audiences_list_type
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_id
    import aws_sdk_bedrock_agentcore.types.complete_resource_token_auth_request
    import aws_sdk_bedrock_agentcore.types.complete_resource_token_auth_response
    import aws_sdk_bedrock_agentcore.types.credential_provider_name
    import aws_sdk_bedrock_agentcore.types.custom_request_parameters_type
    import aws_sdk_bedrock_agentcore.types.get_resource_api_key_request
    import aws_sdk_bedrock_agentcore.types.get_resource_api_key_response
    import aws_sdk_bedrock_agentcore.types.get_resource_oauth2_token_request
    import aws_sdk_bedrock_agentcore.types.get_resource_oauth2_token_response
    import aws_sdk_bedrock_agentcore.types.get_resource_payment_token_request
    import aws_sdk_bedrock_agentcore.types.get_resource_payment_token_response
    import aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_jwt_request
    import aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_jwt_response
    import aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_user_id_request
    import aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_user_id_response
    import aws_sdk_bedrock_agentcore.types.get_workload_access_token_request
    import aws_sdk_bedrock_agentcore.types.get_workload_access_token_response
    import aws_sdk_bedrock_agentcore.types.harness_allowed_tools
    import aws_sdk_bedrock_agentcore.types.harness_arn
    import aws_sdk_bedrock_agentcore.types.harness_messages
    import aws_sdk_bedrock_agentcore.types.harness_model_configuration
    import aws_sdk_bedrock_agentcore.types.harness_skills
    import aws_sdk_bedrock_agentcore.types.harness_system_prompt
    import aws_sdk_bedrock_agentcore.types.harness_tools
    import aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_request
    import aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_response
    import aws_sdk_bedrock_agentcore.types.invoke_harness_request
    import aws_sdk_bedrock_agentcore.types.invoke_harness_response
    import aws_sdk_bedrock_agentcore.types.oauth2_flow_type
    import aws_sdk_bedrock_agentcore.types.payment_token_request_input
    import aws_sdk_bedrock_agentcore.types.request_uri
    import aws_sdk_bedrock_agentcore.types.resource_oauth2_return_url_type
    import aws_sdk_bedrock_agentcore.types.resources_list_type
    import aws_sdk_bedrock_agentcore.types.scopes_list_type
    import aws_sdk_bedrock_agentcore.types.session_id
    import aws_sdk_bedrock_agentcore.types.state
    import aws_sdk_bedrock_agentcore.types.tool_arguments
    import aws_sdk_bedrock_agentcore.types.tool_name
    import aws_sdk_bedrock_agentcore.types.user_id_type
    import aws_sdk_bedrock_agentcore.types.user_identifier
    import aws_sdk_bedrock_agentcore.types.user_token_type
    import aws_sdk_bedrock_agentcore.types.workload_identity_name_type
    import aws_sdk_bedrock_agentcore.types.workload_identity_token_type


class AsyncBedrockAgentCoreClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


class AsyncBedrockAgentCoreClient:
    """A client for the ``BedrockAgentCore`` service.

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
        self._config = AsyncBedrockAgentCoreClientConfig(
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
        self.agentic_resource = AsyncAgenticResource(self)
        self.browser_profile_resource = AsyncBrowserProfileResource(self)
        self.browser_session_resource = AsyncBrowserSessionResource(self)
        self.code_interpreter_session_resource = AsyncCodeInterpreterSessionResource(
            self
        )
        self.evaluation_resource = AsyncEvaluationResource(self)
        self.memory_resource = AsyncMemoryResource(self)
        self.payment_instrument_resource = AsyncPaymentInstrumentResource(self)
        self.payment_session_resource = AsyncPaymentSessionResource(self)
        self.process_payment_resource = AsyncProcessPaymentResource(self)
        self.registry_record_resource = AsyncRegistryRecordResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockAgentCoreClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def complete_resource_token_auth(
        self,
        user_identifier: "aws_sdk_bedrock_agentcore.types.user_identifier.UserIdentifier",
        session_uri: "aws_sdk_bedrock_agentcore.types.request_uri.RequestUri",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.complete_resource_token_auth_response.CompleteResourceTokenAuthResponse":
        """<p>Confirms the user authentication session for obtaining OAuth2.0 tokens for a resource.</p>

        Args:
            user_identifier: <p>The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.</p>
            session_uri: <p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.complete_resource_token_auth_request.CompleteResourceTokenAuthRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.complete_resource_token_auth_response.CompleteResourceTokenAuthResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.complete_resource_token_auth

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.complete_resource_token_auth.async_complete_resource_token_auth(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.complete_resource_token_auth_request.CompleteResourceTokenAuthRequest = {}  # type: ignore[typeddict-item]
        input_["user_identifier"] = user_identifier
        input_["session_uri"] = session_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_api_key(
        self,
        workload_identity_token: "aws_sdk_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "aws_sdk_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_resource_api_key_response.GetResourceApiKeyResponse":
        """<p>Retrieves the API key associated with an API key credential provider.</p>

        Args:
            workload_identity_token: <p>The identity token of the workload from which you want to retrieve the API key.</p>
            resource_credential_provider_name: <p>The credential provider name for the resource from which you are retrieving the API key.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_resource_api_key_request.GetResourceApiKeyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_resource_api_key_response.GetResourceApiKeyResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_api_key

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_api_key.async_get_resource_api_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_resource_api_key_request.GetResourceApiKeyRequest = {}  # type: ignore[typeddict-item]
        input_["workload_identity_token"] = workload_identity_token
        input_["resource_credential_provider_name"] = resource_credential_provider_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_oauth2_token(
        self,
        workload_identity_token: "aws_sdk_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "aws_sdk_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        scopes: "aws_sdk_bedrock_agentcore.types.scopes_list_type.ScopesListType",
        oauth2_flow: "aws_sdk_bedrock_agentcore.types.oauth2_flow_type.Oauth2FlowType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        session_uri: Optional[
            "aws_sdk_bedrock_agentcore.types.request_uri.RequestUri"
        ] = None,
        resource_oauth2_return_url: Optional[
            "aws_sdk_bedrock_agentcore.types.resource_oauth2_return_url_type.ResourceOauth2ReturnUrlType"
        ] = None,
        force_authentication: Optional[bool] = None,
        custom_parameters: Optional[
            "aws_sdk_bedrock_agentcore.types.custom_request_parameters_type.CustomRequestParametersType"
        ] = None,
        custom_state: Optional["aws_sdk_bedrock_agentcore.types.state.State"] = None,
        resources: Optional[
            "aws_sdk_bedrock_agentcore.types.resources_list_type.ResourcesListType"
        ] = None,
        audiences: Optional[
            "aws_sdk_bedrock_agentcore.types.audiences_list_type.AudiencesListType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_resource_oauth2_token_response.GetResourceOauth2TokenResponse":
        """<p>Returns the OAuth 2.0 token of the provided resource.</p>

        Args:
            workload_identity_token: <p>The identity token of the workload from which you want to retrieve the OAuth2 token.</p>
            resource_credential_provider_name: <p>The name of the resource's credential provider.</p>
            scopes: <p>The OAuth scopes being requested.</p>
            oauth2_flow: <p>The type of flow to be performed.</p>
            session_uri: <p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>
            resource_oauth2_return_url: <p>The callback URL to redirect to after the OAuth 2.0 token retrieval is complete. This URL must be one of the provided URLs configured for the workload identity.</p>
            force_authentication: <p>Indicates whether to always initiate a new three-legged OAuth (3LO) flow, regardless of any existing session.</p>
            custom_parameters: <p>A map of custom parameters to include in the authorization request to the resource credential provider. These parameters are in addition to the standard OAuth 2.0 flow parameters, and will not override them.</p>
            custom_state: <p>An opaque string that will be sent back to the callback URL provided in resourceOauth2ReturnUrl. This state should be used to protect the callback URL of your application against CSRF attacks by ensuring the response corresponds to the original request.</p>
            resources: <p>The resources to include in the token request. These are used to specify the target resources for which the OAuth2 token is being requested.</p>
            audiences: <p>The audiences to include in the token request. These are used to specify the intended recipients of the OAuth2 token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_resource_oauth2_token_request.GetResourceOauth2TokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_resource_oauth2_token_response.GetResourceOauth2TokenResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_oauth2_token

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_oauth2_token.async_get_resource_oauth2_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_resource_oauth2_token_request.GetResourceOauth2TokenRequest = {}  # type: ignore[typeddict-item]
        input_["workload_identity_token"] = workload_identity_token
        input_["resource_credential_provider_name"] = resource_credential_provider_name
        input_["scopes"] = scopes
        input_["oauth2_flow"] = oauth2_flow
        if session_uri is not None:
            input_["session_uri"] = session_uri
        if resource_oauth2_return_url is not None:
            input_["resource_oauth2_return_url"] = resource_oauth2_return_url
        if force_authentication is not None:
            input_["force_authentication"] = force_authentication
        if custom_parameters is not None:
            input_["custom_parameters"] = custom_parameters
        if custom_state is not None:
            input_["custom_state"] = custom_state
        if resources is not None:
            input_["resources"] = resources
        if audiences is not None:
            input_["audiences"] = audiences

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_payment_token(
        self,
        workload_identity_token: "aws_sdk_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "aws_sdk_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        payment_token_request: "aws_sdk_bedrock_agentcore.types.payment_token_request_input.PaymentTokenRequestInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_resource_payment_token_response.GetResourcePaymentTokenResponse":
        """<p>Generates authentication tokens for payment providers that use vendor-specific authentication mechanisms.</p>

        Args:
            workload_identity_token: <p>Workload access token for authorization.</p>
            resource_credential_provider_name: <p>Name of the payment credential provider to use.</p>
            payment_token_request: <p>Vendor-specific token request input. Contains all request parameters in a type-safe, vendor-specific structure.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_resource_payment_token_request.GetResourcePaymentTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_resource_payment_token_response.GetResourcePaymentTokenResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_payment_token

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_payment_token.async_get_resource_payment_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_resource_payment_token_request.GetResourcePaymentTokenRequest = {}  # type: ignore[typeddict-item]
        input_["workload_identity_token"] = workload_identity_token
        input_["resource_credential_provider_name"] = resource_credential_provider_name
        input_["payment_token_request"] = payment_token_request

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workload_access_token(
        self,
        workload_name: "aws_sdk_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_workload_access_token_response.GetWorkloadAccessTokenResponse":
        """<p>Obtains a workload access token for agentic workloads not acting on behalf of a user.</p>

        Args:
            workload_name: <p>The unique identifier for the registered workload.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_workload_access_token_request.GetWorkloadAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_workload_access_token_response.GetWorkloadAccessTokenResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token.async_get_workload_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_workload_access_token_request.GetWorkloadAccessTokenRequest = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workload_access_token_for_jwt(
        self,
        workload_name: "aws_sdk_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        user_token: "aws_sdk_bedrock_agentcore.types.user_token_type.UserTokenType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_jwt_response.GetWorkloadAccessTokenForJWTResponse":
        """<p>Obtains a workload access token for agentic workloads acting on behalf of a user, using a JWT token.</p>

        Args:
            workload_name: <p>The unique identifier for the registered workload.</p>
            user_token: <p>The OAuth 2.0 token issued by the user's identity provider.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_jwt_request.GetWorkloadAccessTokenForJWTRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_jwt_response.GetWorkloadAccessTokenForJWTResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_jwt

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_jwt.async_get_workload_access_token_for_jwt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_jwt_request.GetWorkloadAccessTokenForJWTRequest = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name
        input_["user_token"] = user_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_workload_access_token_for_user_id(
        self,
        workload_name: "aws_sdk_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        user_id: "aws_sdk_bedrock_agentcore.types.user_id_type.UserIdType",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_user_id_response.GetWorkloadAccessTokenForUserIdResponse":
        """<p>Obtains a workload access token for agentic workloads acting on behalf of a user, using the user's ID.</p>

        Args:
            workload_name: <p>The name of the workload from which you want to retrieve the access token.</p>
            user_id: <p>The ID of the user for whom you are retrieving the access token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_user_id_request.GetWorkloadAccessTokenForUserIdRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_user_id_response.GetWorkloadAccessTokenForUserIdResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_user_id

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_user_id.async_get_workload_access_token_for_user_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.get_workload_access_token_for_user_id_request.GetWorkloadAccessTokenForUserIdRequest = {}  # type: ignore[typeddict-item]
        input_["workload_name"] = workload_name
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def invoke_code_interpreter(
        self,
        code_interpreter_identifier: str,
        name: "aws_sdk_bedrock_agentcore.types.tool_name.ToolName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "aws_sdk_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        arguments: Optional[
            "aws_sdk_bedrock_agentcore.types.tool_arguments.ToolArguments"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse":
        r"""<p>Executes code within an active code interpreter session in Amazon Bedrock AgentCore. This operation processes the provided code, runs it in a secure environment, and returns the execution results including output, errors, and generated visualizations.</p> <p>To execute code, you must specify the code interpreter identifier, session ID, and the code to run in the arguments parameter. The operation returns a stream containing the execution results, which can include text output, error messages, and data visualizations.</p> <p>This operation is subject to request rate limiting based on your account's service quotas.</p> <p>The following operations are related to <code>InvokeCodeInterpreter</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with <code>StartCodeInterpreterSession</code>.</p>
            session_id: <p>The unique identifier of the code interpreter session to use. This must be an active session created with <code>StartCodeInterpreterSession</code>. If the session has expired or been stopped, the request will fail.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            name: <p>The name of the code interpreter to invoke.</p>
            arguments: <p>The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_code_interpreter

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_code_interpreter.async_invoke_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["code_interpreter_identifier"] = code_interpreter_identifier
        if session_id is not None:
            input_["session_id"] = session_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        input_["name"] = name
        if arguments is not None:
            input_["arguments"] = arguments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def invoke_harness(
        self,
        harness_arn: "aws_sdk_bedrock_agentcore.types.harness_arn.HarnessArn",
        runtime_session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId",
        messages: "aws_sdk_bedrock_agentcore.types.harness_messages.HarnessMessages",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        runtime_user_id: Optional[str] = None,
        model: Optional[
            "aws_sdk_bedrock_agentcore.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "aws_sdk_bedrock_agentcore.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "aws_sdk_bedrock_agentcore.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "aws_sdk_bedrock_agentcore.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "aws_sdk_bedrock_agentcore.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
        actor_id: Optional[str] = None,
    ) -> (
        "aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse"
    ):
        """<p>Operation to invoke a Harness.</p>

        Args:
            harness_arn: <p>The ARN of the harness to invoke.</p>
            runtime_session_id: <p>The session ID for the invocation. Use the same session ID across requests to continue a conversation.</p>
            runtime_user_id: <p>An identifier for the end user making the request. This value is passed through to the runtime container.</p>
            messages: <p>The messages to send to the agent.</p>
            model: <p>The model configuration to use for this invocation. If specified, overrides the harness default.</p>
            system_prompt: <p>The system prompt to use for this invocation. If specified, overrides the harness default.</p>
            tools: <p>The tools available to the agent for this invocation. If specified, overrides the harness default.</p>
            skills: <p>The skills available to the agent for this invocation. If specified, overrides the harness default.</p>
            allowed_tools: <p>The tools that the agent is allowed to use for this invocation. If specified, overrides the harness default.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute. If specified, overrides the harness default.</p>
            max_tokens: <p>The maximum number of tokens the agent can generate per iteration. If specified, overrides the harness default.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution. If specified, overrides the harness default.</p>
            actor_id: <p>The actor ID for memory operations. Overrides the actor ID configured on the harness.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_harness

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_harness.async_invoke_harness(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest = {}  # type: ignore[typeddict-item]
        input_["harness_arn"] = harness_arn
        input_["runtime_session_id"] = runtime_session_id
        if runtime_user_id is not None:
            input_["runtime_user_id"] = runtime_user_id
        input_["messages"] = messages
        if model is not None:
            input_["model"] = model
        if system_prompt is not None:
            input_["system_prompt"] = system_prompt
        if tools is not None:
            input_["tools"] = tools
        if skills is not None:
            input_["skills"] = skills
        if allowed_tools is not None:
            input_["allowed_tools"] = allowed_tools
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if actor_id is not None:
            input_["actor_id"] = actor_id

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
