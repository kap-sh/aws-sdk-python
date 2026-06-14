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
    import aws_sdk_bedrock_agentcore_control.types.api_key_credential_provider_item
    import aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.credential_provider_name
    import aws_sdk_bedrock_agentcore_control.types.default_api_key_type
    import aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_response
    import aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_request
    import aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.secret_reference
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_request
    import aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_response
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class ApiKeyCredentialProvider:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "aws_sdk_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse":
        """<p>Creates a new API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider. The name must be unique within your account.</p>
            api_key: <p>The API key to use for authentication. This value is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>
            tags: <p>A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider.create_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source
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
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse":
        """<p>Retrieves information about an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider.get_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
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
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "aws_sdk_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse":
        """<p>Updates an existing API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to update.</p>
            api_key: <p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider.update_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source

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
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse":
        """<p>Deletes an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider.delete_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_api_key_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse":
        """<p>Lists all API key credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers.list_api_key_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest = {}  # type: ignore[typeddict-item]
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


class AsyncApiKeyCredentialProvider:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "aws_sdk_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse":
        """<p>Creates a new API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider. The name must be unique within your account.</p>
            api_key: <p>The API key to use for authentication. This value is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>
            tags: <p>A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider.async_create_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source
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
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse":
        """<p>Retrieves information about an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider.async_get_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
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
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "aws_sdk_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse":
        """<p>Updates an existing API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to update.</p>
            api_key: <p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the AWS Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider.async_update_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source

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
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse":
        """<p>Deletes an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider.async_delete_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_api_key_credential_providers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse":
        """<p>Lists all API key credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers.async_list_api_key_credential_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest = {}  # type: ignore[typeddict-item]
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
