"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AmazonBedrockAgentCore``."""

import warnings
from collections.abc import Generator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._auth._identity import Credentials
from capo_bedrock_agentcore._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_agentcore._auth._zapros_handler import AuthMiddleware
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.agentic_resource import (
    AgenticResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.browser_profile_resource import (
    BrowserProfileResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.browser_session_resource import (
    BrowserSessionResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.code_interpreter_session_resource import (
    CodeInterpreterSessionResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.evaluation_resource import (
    EvaluationResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.memory_resource import (
    MemoryResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.payment_instrument_resource import (
    PaymentInstrumentResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.payment_session_resource import (
    PaymentSessionResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.process_payment_resource import (
    ProcessPaymentResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.registry_record_resource import (
    RegistryRecordResource,
)
from capo_bedrock_agentcore._services._aws_config import aws_config
from capo_bedrock_agentcore._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.audiences_list_type
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.complete_resource_token_auth_request
    import capo_bedrock_agentcore.types.complete_resource_token_auth_response
    import capo_bedrock_agentcore.types.credential_provider_name
    import capo_bedrock_agentcore.types.custom_request_parameters_type
    import capo_bedrock_agentcore.types.get_resource_api_key_request
    import capo_bedrock_agentcore.types.get_resource_api_key_response
    import capo_bedrock_agentcore.types.get_resource_oauth2_token_request
    import capo_bedrock_agentcore.types.get_resource_oauth2_token_response
    import capo_bedrock_agentcore.types.get_resource_payment_token_request
    import capo_bedrock_agentcore.types.get_resource_payment_token_response
    import capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_request
    import capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_response
    import capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_request
    import capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_response
    import capo_bedrock_agentcore.types.get_workload_access_token_request
    import capo_bedrock_agentcore.types.get_workload_access_token_response
    import capo_bedrock_agentcore.types.harness_allowed_tools
    import capo_bedrock_agentcore.types.harness_arn
    import capo_bedrock_agentcore.types.harness_messages
    import capo_bedrock_agentcore.types.harness_model_configuration
    import capo_bedrock_agentcore.types.harness_skills
    import capo_bedrock_agentcore.types.harness_system_prompt
    import capo_bedrock_agentcore.types.harness_tools
    import capo_bedrock_agentcore.types.invoke_code_interpreter_request
    import capo_bedrock_agentcore.types.invoke_code_interpreter_response
    import capo_bedrock_agentcore.types.invoke_harness_request
    import capo_bedrock_agentcore.types.invoke_harness_response
    import capo_bedrock_agentcore.types.oauth2_flow_type
    import capo_bedrock_agentcore.types.payment_token_request_input
    import capo_bedrock_agentcore.types.request_uri
    import capo_bedrock_agentcore.types.resource_oauth2_return_url_type
    import capo_bedrock_agentcore.types.resources_list_type
    import capo_bedrock_agentcore.types.scopes_list_type
    import capo_bedrock_agentcore.types.session_id
    import capo_bedrock_agentcore.types.state
    import capo_bedrock_agentcore.types.tool_arguments
    import capo_bedrock_agentcore.types.tool_name
    import capo_bedrock_agentcore.types.user_id_type
    import capo_bedrock_agentcore.types.user_identifier
    import capo_bedrock_agentcore.types.user_token_type
    import capo_bedrock_agentcore.types.workload_identity_name_type
    import capo_bedrock_agentcore.types.workload_identity_token_type


class BedrockAgentCoreClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class BedrockAgentCoreClient:
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
        self._config = BedrockAgentCoreClientConfig(
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
        self.agentic_resource = AgenticResource(self)
        self.browser_profile_resource = BrowserProfileResource(self)
        self.browser_session_resource = BrowserSessionResource(self)
        self.code_interpreter_session_resource = CodeInterpreterSessionResource(self)
        self.evaluation_resource = EvaluationResource(self)
        self.memory_resource = MemoryResource(self)
        self.payment_instrument_resource = PaymentInstrumentResource(self)
        self.payment_session_resource = PaymentSessionResource(self)
        self.process_payment_resource = ProcessPaymentResource(self)
        self.registry_record_resource = RegistryRecordResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentCoreClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentCoreClientConfig = config_overrides or {}
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

    def complete_resource_token_auth(
        self,
        user_identifier: "capo_bedrock_agentcore.types.user_identifier.UserIdentifier",
        session_uri: "capo_bedrock_agentcore.types.request_uri.RequestUri",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.complete_resource_token_auth_response.CompleteResourceTokenAuthResponse":
        """<p>Confirms the user authentication session for obtaining OAuth2.0 tokens for a resource.</p>

        Args:
            user_identifier: <p>The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.</p>
            session_uri: <p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.complete_resource_token_auth_request.CompleteResourceTokenAuthRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.complete_resource_token_auth_response.CompleteResourceTokenAuthResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.complete_resource_token_auth

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.complete_resource_token_auth.complete_resource_token_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.complete_resource_token_auth_request.CompleteResourceTokenAuthRequest = {
            "user_identifier": user_identifier,
            "session_uri": session_uri,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_api_key(
        self,
        workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_resource_api_key_response.GetResourceApiKeyResponse":
        """<p>Retrieves the API key associated with an API key credential provider.</p>

        Args:
            workload_identity_token: <p>The identity token of the workload from which you want to retrieve the API key.</p>
            resource_credential_provider_name: <p>The credential provider name for the resource from which you are retrieving the API key.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_resource_api_key_request.GetResourceApiKeyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_resource_api_key_response.GetResourceApiKeyResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_api_key

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_api_key.get_resource_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_resource_api_key_request.GetResourceApiKeyRequest = {
            "workload_identity_token": workload_identity_token,
            "resource_credential_provider_name": resource_credential_provider_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_oauth2_token(
        self,
        workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        scopes: "capo_bedrock_agentcore.types.scopes_list_type.ScopesListType",
        oauth2_flow: "capo_bedrock_agentcore.types.oauth2_flow_type.Oauth2FlowType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_uri: Optional[
            "capo_bedrock_agentcore.types.request_uri.RequestUri"
        ] = None,
        resource_oauth2_return_url: Optional[
            "capo_bedrock_agentcore.types.resource_oauth2_return_url_type.ResourceOauth2ReturnUrlType"
        ] = None,
        force_authentication: Optional[bool] = None,
        custom_parameters: Optional[
            "capo_bedrock_agentcore.types.custom_request_parameters_type.CustomRequestParametersType"
        ] = None,
        custom_state: Optional["capo_bedrock_agentcore.types.state.State"] = None,
        resources: Optional[
            "capo_bedrock_agentcore.types.resources_list_type.ResourcesListType"
        ] = None,
        audiences: Optional[
            "capo_bedrock_agentcore.types.audiences_list_type.AudiencesListType"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_resource_oauth2_token_response.GetResourceOauth2TokenResponse":
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

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_resource_oauth2_token_request.GetResourceOauth2TokenRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_resource_oauth2_token_response.GetResourceOauth2TokenResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_oauth2_token

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_oauth2_token.get_resource_oauth2_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_resource_oauth2_token_request.GetResourceOauth2TokenRequest = {
            "workload_identity_token": workload_identity_token,
            "resource_credential_provider_name": resource_credential_provider_name,
            "scopes": scopes,
            "oauth2_flow": oauth2_flow,
        }
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_payment_token(
        self,
        workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        payment_token_request: "capo_bedrock_agentcore.types.payment_token_request_input.PaymentTokenRequestInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_resource_payment_token_response.GetResourcePaymentTokenResponse":
        """<p>Generates authentication tokens for payment providers that use vendor-specific authentication mechanisms.</p>

        Args:
            workload_identity_token: <p>Workload access token for authorization.</p>
            resource_credential_provider_name: <p>Name of the payment credential provider to use.</p>
            payment_token_request: <p>Vendor-specific token request input. Contains all request parameters in a type-safe, vendor-specific structure.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_resource_payment_token_request.GetResourcePaymentTokenRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_resource_payment_token_response.GetResourcePaymentTokenResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_payment_token

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_payment_token.get_resource_payment_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_resource_payment_token_request.GetResourcePaymentTokenRequest = {
            "workload_identity_token": workload_identity_token,
            "resource_credential_provider_name": resource_credential_provider_name,
            "payment_token_request": payment_token_request,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_access_token(
        self,
        workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_workload_access_token_response.GetWorkloadAccessTokenResponse":
        """<p>Obtains a workload access token for agentic workloads not acting on behalf of a user.</p>

        Args:
            workload_name: <p>The unique identifier for the registered workload.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_workload_access_token_request.GetWorkloadAccessTokenRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_workload_access_token_response.GetWorkloadAccessTokenResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token.get_workload_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_workload_access_token_request.GetWorkloadAccessTokenRequest = {
            "workload_name": workload_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_access_token_for_jwt(
        self,
        workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        user_token: "capo_bedrock_agentcore.types.user_token_type.UserTokenType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_response.GetWorkloadAccessTokenForJWTResponse":
        """<p>Obtains a workload access token for agentic workloads acting on behalf of a user, using a JWT token.</p>

        Args:
            workload_name: <p>The unique identifier for the registered workload.</p>
            user_token: <p>The OAuth 2.0 token issued by the user's identity provider.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_request.GetWorkloadAccessTokenForJWTRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_response.GetWorkloadAccessTokenForJWTResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_jwt

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_jwt.get_workload_access_token_for_jwt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_request.GetWorkloadAccessTokenForJWTRequest = {
            "workload_name": workload_name,
            "user_token": user_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_access_token_for_user_id(
        self,
        workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        user_id: "capo_bedrock_agentcore.types.user_id_type.UserIdType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_response.GetWorkloadAccessTokenForUserIdResponse":
        """<p>Obtains a workload access token for agentic workloads acting on behalf of a user, using the user's ID.</p>

        Args:
            workload_name: <p>The name of the workload from which you want to retrieve the access token.</p>
            user_id: <p>The ID of the user for whom you are retrieving the access token.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_request.GetWorkloadAccessTokenForUserIdRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_response.GetWorkloadAccessTokenForUserIdResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_user_id

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_user_id.get_workload_access_token_for_user_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_request.GetWorkloadAccessTokenForUserIdRequest = {
            "workload_name": workload_name,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_code_interpreter(
        self,
        code_interpreter_identifier: str,
        name: "capo_bedrock_agentcore.types.tool_name.ToolName",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        arguments: Optional[
            "capo_bedrock_agentcore.types.tool_arguments.ToolArguments"
        ] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse]":
        r"""<p>Executes code within an active code interpreter session in Amazon Bedrock AgentCore. This operation processes the provided code, runs it in a secure environment, and returns the execution results including output, errors, and generated visualizations.</p> <p>To execute code, you must specify the code interpreter identifier, session ID, and the code to run in the arguments parameter. The operation returns a stream containing the execution results, which can include text output, error messages, and data visualizations.</p> <p>This operation is subject to request rate limiting based on your account's service quotas.</p> <p>The following operations are related to <code>InvokeCodeInterpreter</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html\">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html\">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with <code>StartCodeInterpreterSession</code>.</p>
            session_id: <p>The unique identifier of the code interpreter session to use. This must be an active session created with <code>StartCodeInterpreterSession</code>. If the session has expired or been stopped, the request will fail.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            name: <p>The name of the code interpreter to invoke.</p>
            arguments: <p>The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_code_interpreter.invoke_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "name": name,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if arguments is not None:
            input_["arguments"] = arguments

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def invoke_harness(
        self,
        harness_arn: "capo_bedrock_agentcore.types.harness_arn.HarnessArn",
        runtime_session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        messages: "capo_bedrock_agentcore.types.harness_messages.HarnessMessages",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        runtime_user_id: Optional[str] = None,
        model: Optional[
            "capo_bedrock_agentcore.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
        actor_id: Optional[str] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse]":
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

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_harness

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_harness.invoke_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest = {
            "harness_arn": harness_arn,
            "runtime_session_id": runtime_session_id,
            "messages": messages,
        }
        if runtime_user_id is not None:
            input_["runtime_user_id"] = runtime_user_id
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
