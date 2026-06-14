from typing import TYPE_CHECKING, Optional

import aws_sdk_securityagent._auth._signers
import aws_sdk_securityagent._auth._sigv4
from aws_sdk_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.create_integration_input
    import aws_sdk_securityagent.types.create_integration_output
    import aws_sdk_securityagent.types.delete_integration_input
    import aws_sdk_securityagent.types.delete_integration_output
    import aws_sdk_securityagent.types.get_integration_input
    import aws_sdk_securityagent.types.get_integration_output
    import aws_sdk_securityagent.types.integration_filter
    import aws_sdk_securityagent.types.integration_id
    import aws_sdk_securityagent.types.integration_summary
    import aws_sdk_securityagent.types.kms_key_id
    import aws_sdk_securityagent.types.list_integrations_input
    import aws_sdk_securityagent.types.list_integrations_output
    import aws_sdk_securityagent.types.max_results
    import aws_sdk_securityagent.types.next_token
    import aws_sdk_securityagent.types.provider
    import aws_sdk_securityagent.types.provider_input
    import aws_sdk_securityagent.types.tag_map
    from aws_sdk_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from aws_sdk_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class IntegrationResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def create(
        self,
        provider: "aws_sdk_securityagent.types.provider.Provider",
        input: "aws_sdk_securityagent.types.provider_input.ProviderInput",
        integration_display_name: str,
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        kms_key_id: Optional["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["aws_sdk_securityagent.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_securityagent.types.create_integration_output.CreateIntegrationOutput"
    ):
        """<p>Creates a new integration with a third-party provider, such as GitHub, for code review and remediation.</p>

        Args:
            provider: <p>The integration provider. Currently, only GITHUB is supported.</p>
            input: <p>The provider-specific input required to create the integration.</p>
            integration_display_name: <p>The display name for the integration.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>
            tags: <p>The tags to associate with the integration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.create_integration_input.CreateIntegrationInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_integration

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.create_integration.create_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_integration_input.CreateIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["input"] = input
        input_["integration_display_name"] = integration_display_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.get_integration_output.GetIntegrationOutput":
        """<p>Retrieves information about an integration.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.get_integration_input.GetIntegrationInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.get_integration_output.GetIntegrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.get_integration

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.get_integration_input.GetIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["integration_id"] = integration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> (
        "aws_sdk_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
    ):
        """<p>Deletes an integration with a third-party provider.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_integration

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_integration_input.DeleteIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["integration_id"] = integration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        filter: Optional[
            "aws_sdk_securityagent.types.integration_filter.IntegrationFilter"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityagent.types.list_integrations_output.ListIntegrationsOutput":
        """<p>Lists the integrations in your account, optionally filtered by provider or provider type.</p>

        Args:
            filter: <p>A filter to apply to the list of integrations.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_securityagent.types.list_integrations_input.ListIntegrationsInput]",
        ) -> OperationResponse[
            "aws_sdk_securityagent.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_integrations

            output, http_response = (
                aws_sdk_securityagent._operations.security_agent.list_integrations.list_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_integrations_input.ListIntegrationsInput = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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


class AsyncIntegrationResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def create(
        self,
        provider: "aws_sdk_securityagent.types.provider.Provider",
        input: "aws_sdk_securityagent.types.provider_input.ProviderInput",
        integration_display_name: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        kms_key_id: Optional["aws_sdk_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["aws_sdk_securityagent.types.tag_map.TagMap"] = None,
    ) -> (
        "aws_sdk_securityagent.types.create_integration_output.CreateIntegrationOutput"
    ):
        """<p>Creates a new integration with a third-party provider, such as GitHub, for code review and remediation.</p>

        Args:
            provider: <p>The integration provider. Currently, only GITHUB is supported.</p>
            input: <p>The provider-specific input required to create the integration.</p>
            integration_display_name: <p>The display name for the integration.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>
            tags: <p>The tags to associate with the integration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.create_integration_input.CreateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.create_integration

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.create_integration_input.CreateIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["provider"] = provider
        input_["input"] = input
        input_["integration_display_name"] = integration_display_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "aws_sdk_securityagent.types.get_integration_output.GetIntegrationOutput":
        """<p>Retrieves information about an integration.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.get_integration_input.GetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.get_integration_output.GetIntegrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.get_integration

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.get_integration.async_get_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.get_integration_input.GetIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["integration_id"] = integration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        integration_id: "aws_sdk_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> (
        "aws_sdk_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
    ):
        """<p>Deletes an integration with a third-party provider.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.delete_integration

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.delete_integration_input.DeleteIntegrationInput = {}  # type: ignore[typeddict-item]
        input_["integration_id"] = integration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "aws_sdk_securityagent.types.integration_filter.IntegrationFilter"
        ] = None,
        next_token: Optional["aws_sdk_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional[
            "aws_sdk_securityagent.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_securityagent.types.list_integrations_output.ListIntegrationsOutput":
        """<p>Lists the integrations in your account, optionally filtered by provider or provider type.</p>

        Args:
            filter: <p>A filter to apply to the list of integrations.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_securityagent.types.list_integrations_input.ListIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_securityagent.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import aws_sdk_securityagent._operations.security_agent.list_integrations

            (
                output,
                http_response,
            ) = await aws_sdk_securityagent._operations.security_agent.list_integrations.async_list_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_securityagent.types.list_integrations_input.ListIntegrationsInput = {}  # type: ignore[typeddict-item]
        if filter is not None:
            input_["filter"] = filter
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
