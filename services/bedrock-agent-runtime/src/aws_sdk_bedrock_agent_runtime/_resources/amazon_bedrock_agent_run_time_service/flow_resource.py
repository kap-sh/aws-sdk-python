from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_id
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_inputs
    import aws_sdk_bedrock_agent_runtime.types.invoke_flow_request
    import aws_sdk_bedrock_agent_runtime.types.invoke_flow_response
    import aws_sdk_bedrock_agent_runtime.types.model_performance_configuration
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class FlowResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def invoke_flow(
        self,
        flow_identifier: "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "aws_sdk_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        enable_trace: Optional[bool] = None,
        model_performance_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
        execution_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse":
        """<p>Invokes an alias of a flow to run the inputs that you specify and return the output of each node as a stream. If there's an error, the error is returned. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html\">Test a flow in Amazon Bedrock</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeFlow</code>.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias.</p>
            inputs: <p>A list of objects, each containing information about an input into the flow.</p>
            enable_trace: <p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html\">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>
            model_performance_configuration: <p>Model performance settings for the request.</p>
            execution_id: <p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow.invoke_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_identifier"] = flow_identifier
        input["flow_alias_identifier"] = flow_alias_identifier
        input["inputs"] = inputs
        if enable_trace is not None:
            input["enable_trace"] = enable_trace
        if model_performance_configuration is not None:
            input["model_performance_configuration"] = model_performance_configuration
        if execution_id is not None:
            input["execution_id"] = execution_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFlowResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def invoke_flow(
        self,
        flow_identifier: "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "aws_sdk_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        enable_trace: Optional[bool] = None,
        model_performance_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
        execution_id: Optional[
            "aws_sdk_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse":
        """<p>Invokes an alias of a flow to run the inputs that you specify and return the output of each node as a stream. If there's an error, the error is returned. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html\">Test a flow in Amazon Bedrock</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeFlow</code>.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias.</p>
            inputs: <p>A list of objects, each containing information about an input into the flow.</p>
            enable_trace: <p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html\">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>
            model_performance_configuration: <p>Model performance settings for the request.</p>
            execution_id: <p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow.async_invoke_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest = {}  # type: ignore[typeddict-item]
        input["flow_identifier"] = flow_identifier
        input["flow_alias_identifier"] = flow_alias_identifier
        input["inputs"] = inputs
        if enable_trace is not None:
            input["enable_trace"] = enable_trace
        if model_performance_configuration is not None:
            input["model_performance_configuration"] = model_performance_configuration
        if execution_id is not None:
            input["execution_id"] = execution_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
