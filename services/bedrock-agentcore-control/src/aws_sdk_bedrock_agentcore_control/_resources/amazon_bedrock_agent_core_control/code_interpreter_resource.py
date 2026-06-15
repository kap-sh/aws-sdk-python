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
    import aws_sdk_bedrock_agentcore_control.types.certificates
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_id
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary
    import aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_request
    import aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_response
    import aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_request
    import aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_response
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_request
    import aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_response
    import aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_request
    import aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_response
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.resource_type
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.sandbox_name
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    from aws_sdk_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from aws_sdk_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class CodeInterpreterResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        certificates: Optional[
            "aws_sdk_bedrock_agentcore_control.types.certificates.Certificates"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse":
        """<p>Creates a custom code interpreter.</p>

        Args:
            name: <p>The name of the code interpreter. The name must be unique within your account.</p>
            description: <p>The description of the code interpreter.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.</p>
            certificates: <p>A list of certificates to install in the code interpreter.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter.create_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        input_["network_configuration"] = network_configuration
        if certificates is not None:
            input_["certificates"] = certificates
        if client_token is not None:
            input_["client_token"] = client_token
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
        code_interpreter_id: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse":
        """<p>Gets information about a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter.get_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["code_interpreter_id"] = code_interpreter_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        code_interpreter_id: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse":
        """<p>Deletes a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter.delete_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["code_interpreter_id"] = code_interpreter_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse":
        """<p>Lists all custom code interpreters in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
            type: <p>The type of code interpreters to list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters

            output, http_response = (
                aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters.list_code_interpreters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCodeInterpreterResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "aws_sdk_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        certificates: Optional[
            "aws_sdk_bedrock_agentcore_control.types.certificates.Certificates"
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse":
        """<p>Creates a custom code interpreter.</p>

        Args:
            name: <p>The name of the code interpreter. The name must be unique within your account.</p>
            description: <p>The description of the code interpreter.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.</p>
            certificates: <p>A list of certificates to install in the code interpreter.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter.async_create_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        input_["network_configuration"] = network_configuration
        if certificates is not None:
            input_["certificates"] = certificates
        if client_token is not None:
            input_["client_token"] = client_token
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
        code_interpreter_id: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse":
        """<p>Gets information about a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter.async_get_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["code_interpreter_id"] = code_interpreter_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        code_interpreter_id: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse":
        """<p>Deletes a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter.async_delete_code_interpreter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest = {}  # type: ignore[typeddict-item]
        input_["code_interpreter_id"] = code_interpreter_id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "aws_sdk_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse":
        """<p>Lists all custom code interpreters in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
            type: <p>The type of code interpreters to list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse"
        ]:
            import aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters.async_list_code_interpreters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
