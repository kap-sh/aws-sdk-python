from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agentcore_control._auth._signers
import aws_sdk_bedrock_agentcore_control._auth._sigv4
from aws_sdk_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type
    import aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request
    import aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response
    import aws_sdk_bedrock_agentcore_control.types.oauth2_credential_provider_item
    import aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class Oauth2CredentialProvider:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.create_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["credential_provider_vendor"] = credential_provider_vendor
        input_["oauth2_provider_config_input"] = oauth2_provider_config_input
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.get_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.update_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["credential_provider_vendor"] = credential_provider_vendor
        input_["oauth2_provider_config_input"] = oauth2_provider_config_input

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.delete_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_oauth2_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.list_oauth2_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncOauth2CredentialProvider:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.async_create_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["credential_provider_vendor"] = credential_provider_vendor
        input_["oauth2_provider_config_input"] = oauth2_provider_config_input
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.async_get_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "aws_sdk_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "aws_sdk_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.async_update_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["credential_provider_vendor"] = credential_provider_vendor
        input_["oauth2_provider_config_input"] = oauth2_provider_config_input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>

        Raises:
            aws_sdk_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            aws_sdk_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            aws_sdk_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            aws_sdk_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            aws_sdk_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            aws_sdk_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            aws_sdk_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            aws_sdk_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.async_delete_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_oauth2_credential_providers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

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
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.async_list_oauth2_credential_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
